#Nouvelle partie

import webbrowser

from PyQt5 import QtWidgets
from pop_creation import Ui_pop_creation

def nouvellePartie(self, livre: int, chapitre: str):
    self.creation = QtWidgets.QWidget()
    self.pop_creation = Ui_pop_creation()
    self.pop_creation.setupUi(self.creation)
    self.Partie(livre, chapitre)
    self.menu.close()
    self.creation.show()
    self.ouvrirPDF()

def ouvrirPDF():
		path = 'Loup-solitaire-01-les-maitres-des-tenebres.pdf'
		webbrowser.open_new(path)