
import sys
#https://blog.finxter.com/how-to-open-a-pdf-file-in-python/#:~:text=Popen()%20%E2%80%94%20Without%20CMD,PDF%20directly%20in%20the%20viewer.
import webbrowser

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from get_livres import getLivres
from get_saves import getSaves
from get_chapitre import getChapitre
from get_armes import getArmes
from get_disciplines import getDisciplines
from get_liens import getLiens
from modifier_tables import insertInventaire, insertPersonnage, insertMaitrise, insertInventaireArme


from pop_up import Ui_pop_up
from pop_creation import Ui_pop_creation
from interface import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow, Ui_pop_up, Ui_pop_creation):
	def __init__(self, *args, obj=None, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.debuterPartie()
		self.setupUi(self)

	#https://www.youtube.com/watch?v=17xE-8UlV_Y (Sajanraj T D)
	def debuterPartie(self):
		self.menu = QtWidgets.QWidget()
		self.pop_up = Ui_pop_up()
		self.pop_up.setupUi(self.menu)
		tuple_livres = getLivres()
		tuple_saves = getSaves()
		for livre in tuple_livres:
			self.pop_up.comboBoxLivre.addItem(livre[1])
		for sauvegarde in tuple_saves:
			self.pop_up.comboBoxSave.addItems(sauvegarde)
		self.pop_up.boutonQuitter.clicked.connect(sys.exit)
		self.pop_up.boutonNouvellePartie.clicked.connect(self.popUpNouvellePartie)
		
		self.menu.show()


	def popUpNouvellePartie(self):
		livre = self.pop_up.comboBoxLivre.currentIndex() + 1
		chapitre = 'Avertir le roi'
		self.creation = QtWidgets.QWidget()
		self.pop_creation = Ui_pop_creation()
		self.pop_creation.setupUi(self.creation)
		self.menu.close()
		self.creation.show()
		#self.ouvrirPDF()

		for x in range(8):
			x = None
			self.pop_creation.comboBoxInventaire.addItem(x)
		self.pop_creation.pushButtonAjouterSac.clicked.connect(self.ajouterObjet)
		self.pop_creation.pushButtonEnleverSac.clicked.connect(self.enleverObjet)

		listeDisciplines = getDisciplines()
		for discipline in listeDisciplines:
			self.pop_creation.comboBoxDisciplines.addItem(discipline[1], discipline[0])
		for x in range(5):
			x = None
			self.pop_creation.comboBoxMaitrise.addItem(x)
		self.pop_creation.pushButtonAjouterDiscipline.clicked.connect(self.ajouterDiscipline)
		self.pop_creation.pushButtonEnleverDiscipline.clicked.connect(self.enleverDiscipline)

		listeArmes = getArmes()
		for arme in listeArmes:
			self.pop_creation.comboBoxArmes.addItem(arme[1])
		self.pop_creation.pushButtonAjouterArme.clicked.connect(self.ajouterArme)
		self.pop_creation.pushButtonEnleverArme.clicked.connect(self.enleverArme)

		nom = self.pop_creation.lineEditNomPersonnage.text()
		habilete = self.pop_creation.spinBoxHabilete.value()
		endurance_max = self.pop_creation.spinBoxEndurance.value()
		bourse = self.pop_creation.spinBoxBourse.value()

		self.comboBoxPagesSuivantes.addItem('1')

		self.pop_creation.pushButtonDemarrer.clicked.connect(lambda: self.demarrerNouvellePartie(livre))

		self.Partie(livre, chapitre)
		
	def ajouterArme(self):
		arme = self.pop_creation.comboBoxArmes.currentText()
		self.pop_creation.comboBoxInventaireArmes.addItem(arme)
	def enleverArme(self):
		arme = self.pop_creation.comboBoxInventaireArmes.current()
		self.pop_creation.comboBoxInventaireArmes.removeItem(arme)

	def ajouterDiscipline(self):
		discipline = self.pop_creation.comboBoxDisciplines.currentText()
		discipline_id = self.pop_creation.comboBoxDisciplines.currentData()
		for x in range(5):
			place = self.pop_creation.comboBoxMaitrise.itemText(x)
			if place == '':
				self.pop_creation.comboBoxMaitrise.insertItem(x, discipline, discipline_id)
				break

	def enleverDiscipline(self):
		maitrise = self.pop_creation.comboBoxMaitrise.currentIndex()
		self.pop_creation.comboBoxMaitrise.removeItem(maitrise)

	def ajouterObjet(self):
		
		nouvelObjet = self.pop_creation.lineEditObjet.text()
		for x in range(8):
			place = self.pop_creation.comboBoxInventaire.itemText(x)
			if place == '':
				self.pop_creation.comboBoxInventaire.insertItem(x, nouvelObjet)
				break
	def enleverObjet(self):
		objet = self.pop_creation.comboBoxInventaire.currentIndex()
		self.pop_creation.comboBoxInventaire.removeItem(objet)

	def ouvrirPDF(self):
		path = 'Loup-solitaire-01-les-maitres-des-tenebres.pdf'
		webbrowser.open_new(path)
	
	def demarrerNouvellePartie(self, livre):
		nom_personnage = self.pop_creation.lineEditNomPersonnage.text()
		habilete = self.pop_creation.spinBoxHabilete.value()
		endurance = self.pop_creation.spinBoxEndurance.value()
		endurance_max = endurance
		bourse = self.pop_creation.spinBoxBourse.value()
		objets_speciaux = self.pop_creation.plainTextEditObjetsSpeciaux.toPlainText()

		objet = {}
		for x in range(8):
			objet[x] = self.pop_creation.comboBoxInventaire.itemText(x)
		
		inventaire_id = insertInventaire(nom_personnage, objet[0], objet[1], objet[2], objet[3], objet[4], objet[5], objet[6], objet[7])
		personnage_id = insertPersonnage(nom_personnage, habilete, endurance, endurance_max, bourse, inventaire_id, objets_speciaux)

		for x in range(5):
			discipline_id = self.pop_creation.comboBoxMaitrise.currentData(x)
			insertMaitrise(discipline_id, personnage_id)




		#for maitre in 
		



	def Partie(self, livre, chapitre):
		page = getChapitre(livre, chapitre)
		no_chapitre, texte = page
		self.textBrowser.setText(texte)
		self.labelChapitre.setText("Chapitre " + no_chapitre)
		window.show()

		self.pushButtonTournerPage.clicked.connect(lambda: self.tournerPage(livre))
	
	def tournerPage(self, livre):
		
		pageDestination = self.comboBoxPagesSuivantes.currentText()
		self.comboBoxPagesSuivantes.clear()
		tupleLiens = getLiens(pageDestination)
		for lien in tupleLiens:
			page_lien = str(lien[1])
			self.comboBoxPagesSuivantes.addItem(page_lien)

		self.Partie(livre, pageDestination)

app = QApplication(sys.argv)

window = MainWindow()


app.exec()