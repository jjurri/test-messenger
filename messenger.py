import requests
from PyQt5 import QtWidgets
import design


class MessengerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.send)

	def send(self):
		username = self.lineEdit.text()
		password = self.lineEdit_2.text()
		text = self.plainTextEdit.toPlainText()

		if not username or not password or not text:
			return

		try:
			response = requests.post(
				'http://127.0.0.1:5000/send',
				json={'username': username, 'password': password, 'text': text}
			)
		except requests.exceptions.ConnectionError:
			print('Connection error')


if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MessengerApp()
	window.show()
	app.exec_()
