# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
from . import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 462)
        icon = QIcon()
        icon.addFile(u":/icons/icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 552, 437))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainImage = QLabel(self.frame_4)
        self.mainImage.setObjectName(u"mainImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainImage.sizePolicy().hasHeightForWidth())
        self.mainImage.setSizePolicy(sizePolicy1)
        self.mainImage.setStyleSheet(u"")
        self.mainImage.setPixmap(QPixmap(u"../img/uiframehires.png"))
        self.mainImage.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.mainImage)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadImgBtn = QPushButton(self.frame)
        self.loadImgBtn.setObjectName(u"loadImgBtn")

        self.verticalLayout.addWidget(self.loadImgBtn)

        self.bgColorBtn = QPushButton(self.frame)
        self.bgColorBtn.setObjectName(u"bgColorBtn")

        self.verticalLayout.addWidget(self.bgColorBtn)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.leftBox = QDoubleSpinBox(self.frame_7)
        self.leftBox.setObjectName(u"leftBox")
        self.leftBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.leftBox.setDecimals(9)
        self.leftBox.setMaximum(1.000000000000000)
        self.leftBox.setSingleStep(0.010000000000000)
        self.leftBox.setValue(0.001953000000000)

        self.gridLayout_2.addWidget(self.leftBox, 0, 1, 1, 1)

        self.topBox = QDoubleSpinBox(self.frame_7)
        self.topBox.setObjectName(u"topBox")
        self.topBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.topBox.setDecimals(9)
        self.topBox.setMaximum(1.000000000000000)
        self.topBox.setSingleStep(0.010000000000000)
        self.topBox.setValue(0.003906000000000)

        self.gridLayout_2.addWidget(self.topBox, 1, 1, 1, 1)

        self.bottomBox = QDoubleSpinBox(self.frame_7)
        self.bottomBox.setObjectName(u"bottomBox")
        self.bottomBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.bottomBox.setDecimals(9)
        self.bottomBox.setMaximum(1.000000000000000)
        self.bottomBox.setSingleStep(0.010000000000000)
        self.bottomBox.setValue(0.941406000000000)

        self.gridLayout_2.addWidget(self.bottomBox, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.rightBox = QDoubleSpinBox(self.frame_7)
        self.rightBox.setObjectName(u"rightBox")
        self.rightBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.rightBox.setDecimals(9)
        self.rightBox.setMaximum(1.000000000000000)
        self.rightBox.setSingleStep(0.010000000000000)
        self.rightBox.setValue(0.460937000000000)

        self.gridLayout_2.addWidget(self.rightBox, 0, 3, 1, 1)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.stepBox = QDoubleSpinBox(self.frame_7)
        self.stepBox.setObjectName(u"stepBox")
        self.stepBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.stepBox.setDecimals(9)
        self.stepBox.setMaximum(1.000000000000000)
        self.stepBox.setSingleStep(0.010000000000000)
        self.stepBox.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.stepBox, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_7)

        self.applyBtn = QPushButton(self.frame)
        self.applyBtn.setObjectName(u"applyBtn")

        self.verticalLayout.addWidget(self.applyBtn)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.texCordsBox = QPlainTextEdit(self.frame)
        self.texCordsBox.setObjectName(u"texCordsBox")
        self.texCordsBox.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.texCordsBox)

        self.applyTexBtn = QPushButton(self.frame)
        self.applyTexBtn.setObjectName(u"applyTexBtn")

        self.verticalLayout.addWidget(self.applyTexBtn)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Coordinator 1.0", None))
        self.mainImage.setText("")
        self.loadImgBtn.setText(QCoreApplication.translate("MainWindow", u"Load image", None))
        self.bgColorBtn.setText(QCoreApplication.translate("MainWindow", u"Background color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"right:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"bottom:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"left:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"top:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"step:", None))
        self.applyBtn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TexCoords:", None))
        self.texCordsBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<TexCoords left=\"0.001953125\" right=\"0.4609375\" top=\"0.00390625\" bottom=\"0.94140625\"/>", None))
        self.applyTexBtn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

