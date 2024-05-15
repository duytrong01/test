# Form implementation generated from reading ui file 'ShopApp.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 100, 671, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.name.setGeometry(QtCore.QRect(190, 40, 211, 22))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gender = QtWidgets.QComboBox(parent=self.groupBox)
        self.gender.setGeometry(QtCore.QRect(190, 110, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.gender.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 260, 671, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.coffee = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.coffee.setGeometry(QtCore.QRect(70, 60, 81, 20))
        self.coffee.setObjectName("coffee")
        self.snack = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.snack.setGeometry(QtCore.QRect(450, 60, 81, 20))
        self.snack.setObjectName("snack")
        self.adult = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.adult.setGeometry(QtCore.QRect(200, 110, 61, 22))
        self.adult.setObjectName("adult")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 81, 16))
        self.label_4.setObjectName("label_4")
        self.kid = QtWidgets.QSpinBox(parent=self.groupBox_2)
        self.kid.setGeometry(QtCore.QRect(200, 160, 61, 22))
        self.kid.setObjectName("kid")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 55, 16))
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QPushButton(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(150, 480, 93, 28))
        self.price.setObjectName("price")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 480, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 490, 55, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG BÁN VÉ"))
        self.groupBox.setTitle(_translate("MainWindow", "THÔNG TIN KHÁCH HÀNG"))
        self.label_2.setText(_translate("MainWindow", "HỌ TÊN"))
        self.label_3.setText(_translate("MainWindow", "GIỚI TÍNH"))
        self.gender.setItemText(0, _translate("MainWindow", "Nam"))
        self.gender.setItemText(1, _translate("MainWindow", "Nữ"))
        self.gender.setItemText(2, _translate("MainWindow", "Không chọn"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DỊCH VỤ"))
        self.coffee.setText(_translate("MainWindow", "COFFEE"))
        self.snack.setText(_translate("MainWindow", "BIM BIM"))
        self.label_4.setText(_translate("MainWindow", "NGƯỜI LỚN"))
        self.label_5.setText(_translate("MainWindow", "TRẺ EM"))
        self.price.setText(_translate("MainWindow", "TIỀN TRẢ"))
        self.label_6.setText(_translate("MainWindow", "VND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
