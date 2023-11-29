import re
import sys

from PIL import Image, ImageQt

from PySide6.QtCore import QPoint
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QColorDialog

from src.CropWidget import CropWidget
from src.UI.MainWindow import Ui_MainWindow


TEX_COORDS_TEMPLATE = (
    '<TexCoords left="{left}" right="{right}" top="{top}" bottom="{bottom}"/>'
)


class ImageCropper(QMainWindow, Ui_MainWindow):
    def __init__(self, file_name=""):
        super().__init__()
        self.setupUi(self)
        self.loadImgBtn.clicked.connect(self.open_image)
        self.applyBtn.clicked.connect(self.resize_crop)
        self.applyTexBtn.clicked.connect(self.parse_coords)
        self.bgColorBtn.clicked.connect(self.on_color_picker)
        self.bg_color = None
        self.mainImage.setMouseTracking(True)
        self.mainImage.mouseMoveEvent = self.show_mouse_position
        self.mainImage.hide()
        self.image_path = None
        self.pixmap = None
        self.crop_widget = CropWidget(self.mainImage, self)

        self.leftBox.editingFinished.connect(self.resize_crop)
        self.rightBox.editingFinished.connect(self.resize_crop)
        self.topBox.editingFinished.connect(self.resize_crop)
        self.bottomBox.editingFinished.connect(self.resize_crop)
        self.stepBox.editingFinished.connect(self.change_step)
        if file_name:
            self.load_image(file_name)

    def change_step(self):
        value = self.stepBox.value()
        self.leftBox.setSingleStep(value)
        self.rightBox.setSingleStep(value)
        self.topBox.setSingleStep(value)
        self.bottomBox.setSingleStep(value)

    def on_color_picker(self):
        dialog = QColorDialog(self)
        if self.bg_color:
            dialog.setCurrentColor(QColor(self.bg_color))
        if dialog.exec():
            self.bg_color = dialog.currentColor().name()
            self.mainImage.setStyleSheet("background-color: %s;" % self.bg_color)

    def parse_coords(self):
        line = self.texCordsBox.toPlainText()
        values = re.findall(r"\d+\.\d+|\d+", line)

        left, right, top, bottom = map(float, values)
        self.leftBox.setValue(left)
        self.rightBox.setValue(right)
        self.topBox.setValue(top)
        self.bottomBox.setValue(bottom)
        self.resize_crop()

    def resize_crop(self):
        left = self.leftBox.value()
        top = self.topBox.value()
        right = self.rightBox.value()
        bottom = self.bottomBox.value()
        self.texCordsBox.setPlainText(
            TEX_COORDS_TEMPLATE.format(left=left, right=right, top=top, bottom=bottom)
        )

        curr_w = self.mainImage.pixmap().width()
        curr_h = self.mainImage.pixmap().height()

        new_x = left * curr_w
        new_y = top * curr_h
        new_w = (right * curr_w) - new_x
        new_h = (bottom * curr_h) - new_y

        global_point = self.mainImage.mapToGlobal(QPoint(new_x, new_y))
        self.crop_widget.move(self.mainImage.mapFromGlobal(global_point))
        self.crop_widget.setFixedSize(new_w, new_h)

    def show_mouse_position(self, event):
        x = event.position().x() / self.mainImage.pixmap().width()
        y = event.position().y() / self.mainImage.pixmap().height()
        self.statusBar.showMessage(f"left: {x} top: {y}")

    def load_image(self, file_name):
        if file_name.upper().endswith(".BLP"):
            blp_image = Image.open(file_name)
            self.pixmap = QPixmap.fromImage(ImageQt.ImageQt(blp_image))
        else:
            self.image_path = file_name
            self.pixmap = QPixmap(file_name)
        self.mainImage.setPixmap(self.pixmap)
        self.crop_widget.setMainImage(self.mainImage)
        self.leftBox.setValue(0.0)
        self.topBox.setValue(0.0)
        self.rightBox.setValue(0.5)
        self.bottomBox.setValue(0.5)
        self.resize_crop()
        self.mainImage.show()

    def open_image(self):
        options = QFileDialog.Option()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image File",
            "",
            "Images (*.png *.jpg *.tga *.blp);;All Files (*)",
            options=options,
        )

        if file_name:
            self.load_image(file_name)


def main():
    app = QApplication()
    path = ""
    if len(sys.argv) == 2:
        path = sys.argv[1]
    window = ImageCropper(path)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
