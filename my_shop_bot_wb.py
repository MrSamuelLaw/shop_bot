#!/usr/bin/env python


from wb.shop_bot.gui.shob_bot_wb import Ui_shop_bot_wb
from wb.shop_bot.gui.rect_gen_dialog import Ui_Dialog
from wb.shop_bot.gui.feeds_n_speeds_dockWidget import Ui_DockWidget
from wb.shop_bot.bolt_pattern import bolt_pattern
from wb.shop_bot.feeds_n_speeds import MillFNS
from PySide2 import QtWidgets, QtCore
import pyperclip
import logging

class my_shop_bot_wb(Ui_shop_bot_wb):

    def __init__(self):
        self._logger = logging.getLogger('log')
        self._logger.info('shop_bot workbench instantiated')

    def __del__(self):
        self._logger.info('shop_bot_workbench deleted')
        self.dockWidget.deleteLater()

    def run_integrated(self, parent):
        self._logger.info('getting shop_bot workbench ready')
        self.load_parent_elements(parent)
        self.setupUi(self.wb_widget)

        # put functions here
        self.rect_macro_button.clicked.connect(self.rect_generator)
        self.FnS_calc_pushButton.clicked.connect(self.calc_feeds_n_speeds)

        # return self to keep instance alive
        return self

    def load_parent_elements(self, parent):
        self._logger.debug('shob_bot wb loading parent elements')
        self.open = parent.open
        self.get_current_plainTextEdit = parent.get_current_plainTextEdit
        self.wb_widget = parent.wb_widget
        self.parent = parent.parent  # get parents's proptery named parent

    def rect_generator(self):
        """
        implements bolt_pattern.py
        """

        self._logger.debug('generating bolt pattern')
        # set the form up
        bp = bolt_pattern()
        dialog = QtWidgets.QDialog()
        form = Ui_Dialog()
        form.setupUi(dialog)
        units = ['in', 'mm']
        for u in units:
            form.unit_combo_box.addItem(u)

        # add functions
        form.generate_button.clicked.connect(dialog.accept)

        # capture the return
        if dialog.exec_():
            try:
                unit = form.unit_combo_box.currentText()
                x = float(form.w_line_edit.text())
                y = float(form.h_line_edit.text())
                depth = float(form.d_line_edit.text())
                output = bp.get_rect_gcode(unit, x, y, depth)
            except Exception as e:
                output = e
            # pyperclip.copy(str(output))
            self.open()
            self.plainTextEdit = self.get_current_plainTextEdit()
            self.plainTextEdit.insertPlainText(str(output))

    def calc_feeds_n_speeds(self):
        # create MillFNS object
        mill = MillFNS(18_000, 300)

        # setup the tool options
        shapes = ['square nose', 'ball nose', 'other']
        params = mill.get_manufacture_parameter_defs()

        # setup the docked widget
        self.dockWidget = QtWidgets.QDockWidget(self.parent)
        form = Ui_DockWidget()
        form.setupUi(self.dockWidget)

        # create function to display help menu
        def show_help_screen():
            help_text = []
            for p in params:
                help_text.append(': '.join( [str(p), str(params[p])] ))
            help_text = '\n'.join(help_text)
            QtWidgets.QMessageBox.information(self.dockWidget, 'Help Menu', help_text)

        # load the shapes comboBox
        for s in shapes:
            form.shapes_comboBox.addItem(str(s))

        # load the parameter comboBoxes
        for p in params.keys():
            form.comboBox.addItem(str(p))
            form.comboBox_2.addItem(str(p))
            form.comboBox_3.addItem(str(p))
            form.comboBox_4.addItem(str(p))
        form.comboBox_2.setCurrentIndex(1)
        form.comboBox_3.setCurrentIndex(2)
        form.comboBox_4.setCurrentIndex(3)

        # define the solver function
        def calculate():
            mill.define_endmill(
                diameter=form.tool_diameter_lineEdit.text(),
                flute_number=form.flute_number_lineEdit.text(),
                shape=form.shapes_comboBox.currentText()
            )
            mill.define_manufacture_parameters(
                **{
                    str(form.comboBox.currentText()): float(form.lineEdit.text()),
                    str(form.comboBox_2.currentText()): float(form.lineEdit_2.text()),
                    str(form.comboBox_3.currentText()): float(form.lineEdit_3.text()),
                    str(form.comboBox_4.currentText()): float(form.lineEdit_4.text())
                }
            )
            warnings, results = mill.get_feeds_n_speeds(
                adoc=form.adoc_lineEdit.text(),
                rdoc=form.rdoc_lineEdit.text()
            )
            form.plainTextEdit.clear()
            if warnings:
                form.plainTextEdit.appendPlainText('\n'.join(warnings))
            # refactor this little bit here
            output = []
            for k in results.keys():
                output.append(': '.join([str(k), f'{results[k][0]:0.5f}', str(results[k][1]) ]))
            form.plainTextEdit.appendPlainText('\n'.join(output))

        # connect signals and slots
        form.pushButton.clicked.connect(calculate)
        form.help_pushButton.clicked.connect(show_help_screen)

        # show the dockwidget
        self.parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockWidget)
        self.dockWidget.show()
