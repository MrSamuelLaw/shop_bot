# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rect_gen_dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(272, 312)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.d_label = QLabel(Dialog)
        self.d_label.setObjectName(u"d_label")
        self.d_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.d_label, 2, 0, 1, 1)

        self.w_line_edit = QLineEdit(Dialog)
        self.w_line_edit.setObjectName(u"w_line_edit")

        self.gridLayout.addWidget(self.w_line_edit, 0, 1, 1, 1)

        self.h_label = QLabel(Dialog)
        self.h_label.setObjectName(u"h_label")
        self.h_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.h_label, 1, 0, 1, 1)

        self.w_label = QLabel(Dialog)
        self.w_label.setObjectName(u"w_label")
        self.w_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.w_label, 0, 0, 1, 1)

        self.unit_label = QLabel(Dialog)
        self.unit_label.setObjectName(u"unit_label")
        self.unit_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.unit_label, 3, 0, 1, 1)

        self.h_line_edit = QLineEdit(Dialog)
        self.h_line_edit.setObjectName(u"h_line_edit")

        self.gridLayout.addWidget(self.h_line_edit, 1, 1, 1, 1)

        self.unit_combo_box = QComboBox(Dialog)
        self.unit_combo_box.setObjectName(u"unit_combo_box")

        self.gridLayout.addWidget(self.unit_combo_box, 3, 1, 1, 1)

        self.generate_button = QPushButton(Dialog)
        self.generate_button.setObjectName(u"generate_button")

        self.gridLayout.addWidget(self.generate_button, 4, 1, 1, 1)

        self.d_line_edit = QLineEdit(Dialog)
        self.d_line_edit.setObjectName(u"d_line_edit")

        self.gridLayout.addWidget(self.d_line_edit, 2, 1, 1, 1)

        QWidget.setTabOrder(self.w_line_edit, self.h_line_edit)
        QWidget.setTabOrder(self.h_line_edit, self.d_line_edit)
        QWidget.setTabOrder(self.d_line_edit, self.unit_combo_box)
        QWidget.setTabOrder(self.unit_combo_box, self.generate_button)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.d_label.setText(QCoreApplication.translate("Dialog", u"Depth", None))
        self.h_label.setText(QCoreApplication.translate("Dialog", u"Height", None))
        self.w_label.setText(QCoreApplication.translate("Dialog", u"Width", None))
        self.unit_label.setText(QCoreApplication.translate("Dialog", u"Units", None))
        self.generate_button.setText(QCoreApplication.translate("Dialog", u"generate", None))
    # retranslateUi

