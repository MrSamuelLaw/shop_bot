# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feeds_n_speeds_dockWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(373, 815)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 0)
        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_5 = QLabel(self.dockWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.dockWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 11, 1, 1, 1)

        self.flute_number_lineEdit = QLineEdit(self.dockWidgetContents)
        self.flute_number_lineEdit.setObjectName(u"flute_number_lineEdit")

        self.gridLayout_3.addWidget(self.flute_number_lineEdit, 5, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.help_pushButton = QPushButton(self.dockWidgetContents)
        self.help_pushButton.setObjectName(u"help_pushButton")
        self.help_pushButton.setEnabled(True)
        self.help_pushButton.setMaximumSize(QSize(16, 16777215))
        self.help_pushButton.setFocusPolicy(Qt.ClickFocus)

        self.gridLayout_2.addWidget(self.help_pushButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 16, 0, 1, 1)

        self.label_8 = QLabel(self.dockWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 15, 0, 1, 1)

        self.rdoc_lineEdit = QLineEdit(self.dockWidgetContents)
        self.rdoc_lineEdit.setObjectName(u"rdoc_lineEdit")

        self.gridLayout_3.addWidget(self.rdoc_lineEdit, 15, 1, 1, 1)

        self.label_4 = QLabel(self.dockWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 8, 1, 1, 1)

        self.label_3 = QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.dockWidgetContents)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_2, 10, 0, 1, 1)

        self.lineEdit = QLineEdit(self.dockWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 9, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.dockWidgetContents)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_4, 12, 0, 1, 1)

        self.tool_diameter_lineEdit = QLineEdit(self.dockWidgetContents)
        self.tool_diameter_lineEdit.setObjectName(u"tool_diameter_lineEdit")

        self.gridLayout_3.addWidget(self.tool_diameter_lineEdit, 4, 1, 1, 1)

        self.adoc_lineEdit = QLineEdit(self.dockWidgetContents)
        self.adoc_lineEdit.setObjectName(u"adoc_lineEdit")

        self.gridLayout_3.addWidget(self.adoc_lineEdit, 14, 1, 1, 1)

        self.comboBox = QComboBox(self.dockWidgetContents)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.comboBox, 9, 0, 1, 1)

        self.label_7 = QLabel(self.dockWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 14, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.dockWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 10, 1, 1, 1)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 16, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.dockWidgetContents)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.comboBox_3, 11, 0, 1, 1)

        self.shapes_comboBox = QComboBox(self.dockWidgetContents)
        self.shapes_comboBox.setObjectName(u"shapes_comboBox")
        self.shapes_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.shapes_comboBox, 7, 1, 1, 1)

        self.label_6 = QLabel(self.dockWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 13, 1, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.dockWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 17, 0, 1, 2)

        self.lineEdit_4 = QLineEdit(self.dockWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 12, 1, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)
        QWidget.setTabOrder(self.tool_diameter_lineEdit, self.flute_number_lineEdit)
        QWidget.setTabOrder(self.flute_number_lineEdit, self.shapes_comboBox)
        QWidget.setTabOrder(self.shapes_comboBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.adoc_lineEdit)
        QWidget.setTabOrder(self.adoc_lineEdit, self.rdoc_lineEdit)
        QWidget.setTabOrder(self.rdoc_lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.plainTextEdit)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"Mill Feeds_n_Speeds Calculator", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"Tool Definition", None))
        self.label_5.setText(QCoreApplication.translate("DockWidget", u"Shape", None))
        self.help_pushButton.setText(QCoreApplication.translate("DockWidget", u"?", None))
        self.label_8.setText(QCoreApplication.translate("DockWidget", u"rdoc", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"Flute Count", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"Manufacture's Parameters", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"Diameter [in]", None))
        self.label_7.setText(QCoreApplication.translate("DockWidget", u"adoc", None))
        self.pushButton.setText(QCoreApplication.translate("DockWidget", u"calculate", None))
        self.label_6.setText(QCoreApplication.translate("DockWidget", u"Cut Settings", None))
    # retranslateUi

