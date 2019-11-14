#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =========== TEMPLATE FILE =====================
# Replace LROOT with ui_* filename (LROOT=media)
# Replace CROOT with wrapper class name (CROOT=MediaDialog)
# =========== TEMPLATE FILE =====================

from PyQt5 import QtCore, QtGui, QtWidgets
import locale

from ui_LROOT import Ui_CROOT

class CROOT(QtWidgets.QDialog, Ui_CROOT):

	# custom_signal=QtCore.pyqtSignal(int)

	def __init__(self, parent=None):
		super(QtWidgets.QDialog,self).__init__(parent)
		self.setupUi(self)

if __name__ == "__main__":
	import argparse
	import signal
	import sys

	signal.signal(signal.SIGINT,signal.SIG_DFL)
	
	app = QtWidgets.QApplication(sys.argv)
	win=CROOT()
	win.show()
	sys.exit(app.exec_())
