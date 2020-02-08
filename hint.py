# pip install PyQt5
# pyuic5 design.ui -o design.py

# import ...

class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = ExampleApp()
	window.show()
	app.exec_()