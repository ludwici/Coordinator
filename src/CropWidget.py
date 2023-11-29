from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QLabel, QFrame


TEX_COORDS_TEMPLATE = (
    '<TexCoords left="{left}" right="{right}" top="{top}" bottom="{bottom}"/>'
)


class CropWidget(QLabel):
    TopLeft, TopRight, BottomLeft, BottomRight = range(4)

    def __init__(self, parent, main_widget):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.setFixedSize(100, 100)
        self.offset = QPoint()
        self.main_image = None
        self.main_image_rect = None
        self.setStyleSheet(
            "border: 1px solid blue; background-color: rgba(0, 0, 255, 100);"
        )
        self.main_widget = main_widget

    def setMainImage(self, label: QLabel):
        self.main_image = label
        self.main_image_rect = label.geometry()

    def mousePressEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            self.offset = ev.pos()

    def mouseReleaseEvent(self, event):
        if not self.main_image:
            return

    def mouseMoveEvent(self, ev):
        if not self.main_image:
            return

        if ev.buttons() & Qt.MouseButton.LeftButton:
            new_pos = self.mapToParent(ev.pos() - self.offset)
            image_rect = self.main_image.geometry()
            widget_rect = self.geometry()

            max_right = image_rect.right() - widget_rect.width()
            max_bottom = image_rect.bottom() - widget_rect.height()
            if not (0 <= new_pos.x() <= max_right):
                new_pos.setX(max(min(new_pos.x(), max_right), 0))
            if not (0 <= new_pos.y() <= max_bottom):
                new_pos.setY(max(min(new_pos.y(), max_bottom), 0))
            self.move(new_pos)

            new_x = new_pos.x() / image_rect.width()
            new_w = (new_pos.x() + widget_rect.width()) / image_rect.width()
            new_y = new_pos.y() / image_rect.height()
            new_h = (new_pos.y() + widget_rect.height()) / image_rect.height()

            self.main_widget.texCordsBox.setPlainText(
                TEX_COORDS_TEMPLATE.format(
                    left=new_x, right=new_w, top=new_y, bottom=new_h
                )
            )

            self.main_widget.leftBox.setValue(new_x)
            self.main_widget.rightBox.setValue(new_w)
            self.main_widget.topBox.setValue(new_y)
            self.main_widget.bottomBox.setValue(new_h)
