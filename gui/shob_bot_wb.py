# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shob_bot_wb.ui'
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

class Ui_shop_bot_wb(object):
    def setupUi(self, shop_bot_wb):
        if shop_bot_wb.objectName():
            shop_bot_wb.setObjectName(u"shop_bot_wb")
        shop_bot_wb.resize(543, 117)
        self.gridLayout = QGridLayout(shop_bot_wb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rect_macro_button = QPushButton(shop_bot_wb)
        self.rect_macro_button.setObjectName(u"rect_macro_button")

        self.gridLayout.addWidget(self.rect_macro_button, 0, 2, 1, 1)

        self.FnS_calc_pushButton = QPushButton(shop_bot_wb)
        self.FnS_calc_pushButton.setObjectName(u"FnS_calc_pushButton")

        self.gridLayout.addWidget(self.FnS_calc_pushButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.retranslateUi(shop_bot_wb)

        QMetaObject.connectSlotsByName(shop_bot_wb)
    # setupUi

    def retranslateUi(self, shop_bot_wb):
        shop_bot_wb.setWindowTitle(QCoreApplication.translate("shop_bot_wb", u"Form", None))
        self.rect_macro_button.setText(QCoreApplication.translate("shop_bot_wb", u"rect_macro", None))
        self.FnS_calc_pushButton.setText(QCoreApplication.translate("shop_bot_wb", u"F and S calc", None))
    # retranslateUi

