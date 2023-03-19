# Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import time

# Base Structure
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 529)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(-60, 0, 851, 511))
        self.background_label.setText("")
        self.background_label.setPixmap(QtGui.QPixmap("download (1).jpg"))
        self.background_label.setObjectName("background_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 34))
        self.label.setStyleSheet("color: rgb(255, 104, 28);\n"
"font: 10pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"background-color: rgb(111, 157, 255);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 20, 321, 31))
        self.comboBox.setStyleSheet("background-color: rgb(111, 157, 255);\n"
"color: rgb(255, 104, 28);\n"
"font: 10pt \"Segoe Print\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(40, 70, 331, 51))
        self.price_label.setStyleSheet("color: rgb(67, 67, 67);\n"
"font: 10pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 101, 150);")
        self.price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.price_label.setObjectName("price_label")
        self.high24_label = QtWidgets.QLabel(self.centralwidget)
        self.high24_label.setGeometry(QtCore.QRect(570, 10, 91, 81))
        self.high24_label.setStyleSheet("color: rgb(67, 67, 67);\n"
"font: 9pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"background-color: rgb(245, 255, 126);")
        self.high24_label.setAlignment(QtCore.Qt.AlignCenter)
        self.high24_label.setObjectName("high24_label")
        self.low24_label = QtWidgets.QLabel(self.centralwidget)
        self.low24_label.setGeometry(QtCore.QRect(690, 10, 91, 81))
        self.low24_label.setStyleSheet("color: rgb(67, 67, 67);\n"
"font: 9pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"background-color: rgb(245, 255, 126);")
        self.low24_label.setAlignment(QtCore.Qt.AlignCenter)
        self.low24_label.setObjectName("low24_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 791, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.more_label = QtWidgets.QLabel(self.centralwidget)
        self.more_label.setGeometry(QtCore.QRect(290, 143, 191, 31))
        self.more_label.setStyleSheet("color: rgb(255, 100, 49);\n"
"font: 9pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"")
        self.more_label.setAlignment(QtCore.Qt.AlignCenter)
        self.more_label.setObjectName("more_label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(527, 1, 3, 170))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.market_label = QtWidgets.QLabel(self.centralwidget)
        self.market_label.setGeometry(QtCore.QRect(590, 110, 171, 51))
        self.market_label.setStyleSheet("color: rgb(67, 67, 67);\n"
"font: 10pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 101, 150);")
        self.market_label.setAlignment(QtCore.Qt.AlignCenter)
        self.market_label.setObjectName("market_label")
        self.price_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.price_listWidget.setGeometry(QtCore.QRect(0, 180, 261, 331))
        self.price_listWidget.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"font: 9pt \"Segoe Print\";\n"
"color: rgb(15, 15, 15);")
        self.price_listWidget.setObjectName("price_listWidget")
        self.historical_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.historical_listWidget.setGeometry(QtCore.QRect(264, 180, 261, 331))
        self.historical_listWidget.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"font: 9pt \"Segoe Print\";\n"
"color: rgb(15, 15, 15);")
        self.historical_listWidget.setObjectName("historical_listWidget")
        self.toplists_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.toplists_listWidget.setGeometry(QtCore.QRect(529, 180, 261, 331))
        self.toplists_listWidget.setStyleSheet("background-color: rgb(166, 166, 166);\n"
"font: 9pt \"Segoe Print\";\n"
"color: rgb(15, 15, 15);")
        self.toplists_listWidget.setObjectName("toplists_listWidget")
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear())
        self.clear_pushButton.setGeometry(QtCore.QRect(0, 146, 91, 23))
        self.clear_pushButton.setStyleSheet("color: rgb(255, 100, 49);\n"
"font: 9pt \"Segoe Print\";\n"
"border-radius: 10px;\n"
"")
        self.clear_pushButton.setObjectName("clear_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.comboBox.currentTextChanged.connect(self.get_cryptoinfo)

        #Add Scroll To listWidget
        #self.price_listWidget.setDragDropMode(3)
        self.price_listWidget.setVerticalScrollMode(True)
        # self.price_listWidget.setWordWrap(True)
        # self.historical_listWidget.setDragDropMode(3)
        # self.historical_listWidget.setWordWrap(True)
        # self.historical_listWidget.setAutoScroll(True)
        # self.toplists_listWidget.setDragDropMode(3)
        # self.toplists_listWidget.setWordWrap(True)
        # self.toplists_listWidget.setAutoScroll(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_cryptoinfo(self):
        intance = self.comboBox.currentText()
        if intance == 'BitCoin(BTC)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            print(res1)
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(f'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')

        elif intance == 'Ethereum(ETH)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=ETH&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(f'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')
            
        elif intance == 'XRP':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=XRP&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=XRP&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(f'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')

        elif intance == 'Tether(USDT)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=USDT&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=USDT&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(F'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')

        elif intance == 'Litecoin(LTC)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=LTC&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=LTC&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(F'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')

        elif intance == 'Polkadot(DOT)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=DOT&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=DOT&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(F'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')

        elif intance == 'Chainlink(LINK)':
            API = 'c589babe9400cdca240bb7e9b7aff9bac46126262186372a42af00678afcd6bf'
            average_URL = f'https://min-api.cryptocompare.com/data/generateAvg?fsym=LINK&tsym=USD&e=Kraken&api_key={API}'
            historical_URL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=LINK&tsym=USD&limit=10'
            
            r1 = requests.get(average_URL)
            r2 = requests.get(historical_URL)
            res1 = r1.json()
            res2 = r2.json()
            price = res1['RAW']['PRICE']
            high24hour = res1['RAW']['HIGH24HOUR']
            low24hour = res1['RAW']['LOW24HOUR']
            market = res1['RAW']['MARKET']

            self.price_label.setText(F'{price} $')
            self.high24_label.setText(f'{high24hour}')
            self.low24_label.setText(f'{low24hour}')
            self.market_label.setText(f'{market}')
            self.price_listWidget.addItem(f'{res1}')
            self.historical_listWidget.addItem(f'{res2}')


        toplist_URL = f'https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&tsym=USD'
        r3 = requests.get(toplist_URL)
        res3 = r3.json()
        self.toplists_listWidget.addItem(f'{res3}')

    def clear(self):
        self.price_listWidget.clear()
        self.historical_listWidget.clear()
        self.toplists_listWidget.clear()
        self.price_label.clear()
        self.high24_label.clear()
        self.low24_label.clear()
        self.market_label.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptoCurrency App"))
        self.label.setText(_translate("MainWindow", "Select Crypto :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "BitCoin(BTC)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ethereum(ETH)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "BUSD"))
        self.comboBox.setItemText(3, _translate("MainWindow", "XRP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Tether(USDT)"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Litecoin(LTC)"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Polkadot(DOT)"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Binance Coin(BNB)"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Chainlink(LINK)"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Polygon(MATIC)"))
        self.price_label.setText(_translate("MainWindow", "Crypto Price:"))
        self.high24_label.setText(_translate("MainWindow", "HIGH24HOUR"))
        self.low24_label.setText(_translate("MainWindow", "LOW24HOUR"))
        self.more_label.setText(_translate("MainWindow", "More Information"))
        self.market_label.setText(_translate("MainWindow", "MARKET"))
        self.clear_pushButton.setText(_translate("MainWindow", "Clear Lists"))


# Initialize the app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
