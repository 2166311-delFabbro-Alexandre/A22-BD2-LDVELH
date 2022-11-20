# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1357, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelChapitre = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelChapitre.setFont(font)
        self.labelChapitre.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelChapitre.setObjectName("labelChapitre")
        self.horizontalLayout_2.addWidget(self.labelChapitre)
        self.progressBarEndurance = QtWidgets.QProgressBar(self.frame)
        self.progressBarEndurance.setMaximumSize(QtCore.QSize(450, 16777215))
        self.progressBarEndurance.setProperty("value", 24)
        self.progressBarEndurance.setTextVisible(True)
        self.progressBarEndurance.setInvertedAppearance(True)
        self.progressBarEndurance.setFormat("")
        self.progressBarEndurance.setObjectName("progressBarEndurance")
        self.horizontalLayout_2.addWidget(self.progressBarEndurance)
        self.labelHabileteLivre = QtWidgets.QLabel(self.frame)
        self.labelHabileteLivre.setMaximumSize(QtCore.QSize(100, 16777215))
        self.labelHabileteLivre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelHabileteLivre.setObjectName("labelHabileteLivre")
        self.horizontalLayout_2.addWidget(self.labelHabileteLivre)
        self.spinBoxHabileteLivre = QtWidgets.QSpinBox(self.frame)
        self.spinBoxHabileteLivre.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spinBoxHabileteLivre.setObjectName("spinBoxHabileteLivre")
        self.horizontalLayout_2.addWidget(self.spinBoxHabileteLivre)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Canada))
        self.textBrowser.setMarkdown("")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTournerPage = QtWidgets.QPushButton(self.frame)
        self.pushButtonTournerPage.setObjectName("pushButtonTournerPage")
        self.horizontalLayout.addWidget(self.pushButtonTournerPage)
        self.comboBoxPagesSuivantes = QtWidgets.QComboBox(self.frame)
        self.comboBoxPagesSuivantes.setObjectName("comboBoxPagesSuivantes")
        self.horizontalLayout.addWidget(self.comboBoxPagesSuivantes)
        self.pushLienPDF = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushLienPDF.setFont(font)
        self.pushLienPDF.setObjectName("pushLienPDF")
        self.horizontalLayout.addWidget(self.pushLienPDF)
        self.pushSave = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushSave.setFont(font)
        self.pushSave.setObjectName("pushSave")
        self.horizontalLayout.addWidget(self.pushSave)
        self.pushQuitter = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushQuitter.setFont(font)
        self.pushQuitter.setObjectName("pushQuitter")
        self.horizontalLayout.addWidget(self.pushQuitter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.frame)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setStyleSheet("/*background-image: url(:./feuille_aventure/UIs/feuille_aventure.png)")
        self.tab_2.setObjectName("tab_2")
        self.labelBackground = QtWidgets.QLabel(self.tab_2)
        self.labelBackground.setGeometry(QtCore.QRect(-2, 9, 1331, 831))
        self.labelBackground.setText("")
        self.labelBackground.setPixmap(QtGui.QPixmap(":/tab/feuille_aventure.png"))
        self.labelBackground.setScaledContents(True)
        self.labelBackground.setObjectName("labelBackground")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 130, 491, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layoutDisciplines = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutDisciplines.setContentsMargins(0, 0, 0, 0)
        self.layoutDisciplines.setObjectName("layoutDisciplines")
        self.labelDiscipline1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDiscipline1.setObjectName("labelDiscipline1")
        self.layoutDisciplines.addWidget(self.labelDiscipline1)
        self.labelDiscipline2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDiscipline2.setObjectName("labelDiscipline2")
        self.layoutDisciplines.addWidget(self.labelDiscipline2)
        self.labelDiscipline5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDiscipline5.setObjectName("labelDiscipline5")
        self.layoutDisciplines.addWidget(self.labelDiscipline5)
        self.labelDiscipline3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDiscipline3.setObjectName("labelDiscipline3")
        self.layoutDisciplines.addWidget(self.labelDiscipline3)
        self.labelDiscipline4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelDiscipline4.setObjectName("labelDiscipline4")
        self.layoutDisciplines.addWidget(self.labelDiscipline4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(120, 380, 491, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layoutArmes = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutArmes.setContentsMargins(0, 0, 0, 0)
        self.layoutArmes.setObjectName("layoutArmes")
        self.labelArme1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelArme1.setObjectName("labelArme1")
        self.layoutArmes.addWidget(self.labelArme1)
        self.labelArme2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.labelArme2.setObjectName("labelArme2")
        self.layoutArmes.addWidget(self.labelArme2)
        self.spinBoxRepas = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxRepas.setGeometry(QtCore.QRect(420, 530, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(44)
        self.spinBoxRepas.setFont(font)
        self.spinBoxRepas.setMaximum(8)
        self.spinBoxRepas.setObjectName("spinBoxRepas")
        self.spinBoxBourse = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxBourse.setGeometry(QtCore.QRect(360, 710, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.spinBoxBourse.setFont(font)
        self.spinBoxBourse.setObjectName("spinBoxBourse")
        self.spinBoxHabilete = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxHabilete.setGeometry(QtCore.QRect(690, 140, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.spinBoxHabilete.setFont(font)
        self.spinBoxHabilete.setObjectName("spinBoxHabilete")
        self.spinBoxEndurance = QtWidgets.QSpinBox(self.tab_2)
        self.spinBoxEndurance.setGeometry(QtCore.QRect(970, 140, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.spinBoxEndurance.setFont(font)
        self.spinBoxEndurance.setObjectName("spinBoxEndurance")
        self.labelNomFeuille = QtWidgets.QLabel(self.tab_2)
        self.labelNomFeuille.setGeometry(QtCore.QRect(700, 40, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Parchment")
        font.setPointSize(80)
        font.setUnderline(True)
        self.labelNomFeuille.setFont(font)
        self.labelNomFeuille.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelNomFeuille.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelNomFeuille.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNomFeuille.setObjectName("labelNomFeuille")
        self.textBrowserObjetsSpeciaux = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserObjetsSpeciaux.setGeometry(QtCore.QRect(90, 680, 251, 91))
        self.textBrowserObjetsSpeciaux.setObjectName("textBrowserObjetsSpeciaux")
        self.listWidgetInventaire = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetInventaire.setGeometry(QtCore.QRect(90, 530, 321, 91))
        self.listWidgetInventaire.setObjectName("listWidgetInventaire")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelChapitre.setText(_translate("MainWindow", "Chapitre: x"))
        self.labelHabileteLivre.setText(_translate("MainWindow", "Habileté"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonTournerPage.setText(_translate("MainWindow", "Tourner page"))
        self.pushLienPDF.setText(_translate("MainWindow", "Lien vers pdf?"))
        self.pushSave.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushQuitter.setText(_translate("MainWindow", "Quitter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.labelDiscipline1.setText(_translate("MainWindow", "TextLabel"))
        self.labelDiscipline2.setText(_translate("MainWindow", "TextLabel"))
        self.labelDiscipline5.setText(_translate("MainWindow", "TextLabel"))
        self.labelDiscipline3.setText(_translate("MainWindow", "TextLabel"))
        self.labelDiscipline4.setText(_translate("MainWindow", "TextLabel"))
        self.labelArme1.setText(_translate("MainWindow", "TextLabel"))
        self.labelArme2.setText(_translate("MainWindow", "TextLabel"))
        self.labelNomFeuille.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
import background_rc
