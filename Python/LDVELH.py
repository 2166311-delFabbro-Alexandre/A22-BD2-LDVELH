import sys
#https://blog.finxter.com/how-to-open-a-pdf-file-in-python/#:~:text=Popen()%20%E2%80%94%20Without%20CMD,PDF%20directly%20in%20the%20viewer.
import webbrowser

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from select_init import getLivres, getSaves, getChapitre, getArmes, getDisciplines, getLiens
from modifier_tables import insertInventaire, insertPersonnage, insertMaitrise, insertInventaireArme, updateSauvegarde
from select_aventure import getFeuilleAventure, getInventaireArmes, getMaitrises, getInventaire


from pop_up import Ui_pop_up
from pop_creation import Ui_pop_creation
from interface import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow, Ui_pop_up, Ui_pop_creation):

	def __init__(self, *args, obj=None, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.debuterPartie()
		self.setupUi(self)
		self.dictionnaireNotes = {}

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
		nombreSaves = self.pop_up.comboBoxSave.count()
		self.pop_up.boutonNouvellePartie.clicked.connect(lambda: self.departJeu(nombreSaves))
		# if self.pop_up.comboBoxSave.count() < 4:
		# 	self.pop_up.boutonNouvellePartie.clicked.connect(self.departJeu)
		# if self.pop_up.comboBoxSave.count() == 4:
		# 	msg = QMessageBox()
		# 	msg.setIcon(QMessageBox.Information)
		# 	msg.setText("This is a message box")
		# 	msg.setInformativeText("This is additional information")
		# 	msg.setWindowTitle("MessageBox demo")
		# 	msg.setDetailedText("The details are as follows:")	
		# 	self.pop_up.boutonPartieSave.clicked.connect(self.remplirFeuilleAventure)
		
		self.menu.show()

	def departJeu(self, nombreSaves):
		if nombreSaves == 1:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("Déjà quatre parties sauvegardées.  Veuillez supprimer une partie.  Si vous débutez maintenant, vous ne pourrez pas sauvegarder.")
			msg.setInformativeText("Voulez-vous vous lancer tout de même à l'aventure?")
			msg.setWindowTitle("Loup Solitaire")
			msg.addButton("Revenir au menu", 2)
			msg.addButton("Débuter la partie", 1)
			reponse = msg.exec_()
			if reponse == 1:
				self.popUpNouvellePartie()
			else:
				return
		#self.popUpNouvellePartie
		#self.remplirFeuilleAventure

	def popUpNouvellePartie(self):
		livre = self.pop_up.comboBoxLivre.currentIndex() + 1
		chapitre = 'Avertir le roi'
		self.creation = QtWidgets.QWidget()
		self.pop_creation = Ui_pop_creation()
		self.pop_creation.setupUi(self.creation)
		self.comboBoxPagesSuivantes.addItem('1')
		self.menu.close()
		#self.creation.show()
		self.remplirFeuilleAventure(livre, chapitre, 1)
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
			self.pop_creation.comboBoxArmes.addItem(arme[1], arme[0])
		self.pop_creation.pushButtonAjouterArme.clicked.connect(self.ajouterArme)
		self.pop_creation.pushButtonEnleverArme.clicked.connect(self.enleverArme)

		self.pop_creation.pushButtonDemarrer.clicked.connect(lambda: self.enregistrerNouvellePartie(livre, chapitre, self.dictionnaireNotes))


	def ajouterArme(self):
		arme = self.pop_creation.comboBoxArmes.currentText()
		arme_id = self.pop_creation.comboBoxArmes.currentData()
		self.pop_creation.comboBoxInventaireArmes.addItem(arme, arme_id)
	def enleverArme(self):
		arme = self.pop_creation.comboBoxInventaireArmes.currentIndex()
		self.pop_creation.comboBoxInventaireArmes.removeItem(arme)


	def ajouterDiscipline(self):
		indexDiscipline = self.pop_creation.comboBoxDisciplines.currentIndex()
		discipline = self.pop_creation.comboBoxDisciplines.currentText()
		discipline_id = self.pop_creation.comboBoxDisciplines.currentData()
		for index in range(5):
			place = self.pop_creation.comboBoxMaitrise.itemText(index)
			if place == '':
				if indexDiscipline > -1:
					self.pop_creation.comboBoxDisciplines.model().item(indexDiscipline).setEnabled(False)
				self.pop_creation.comboBoxDisciplines.setCurrentIndex(-1)
				self.pop_creation.comboBoxMaitrise.setItemData(index, discipline_id)
				self.pop_creation.comboBoxMaitrise.setItemText(index, discipline)
				note= self.pop_creation.plainTextEditDiscipline.toPlainText()
				self.dictionnaireNotes[discipline_id] = note
				self.pop_creation.plainTextEditDiscipline.clear()
				if self.check():
					self.pop_creation.pushButtonDemarrer.setDisabled(True)
				else:
					self.pop_creation.pushButtonDemarrer.setDisabled(False)
				break
	def check(self)->bool:
		vide = 0
		for x in range(5):
			texte = self.pop_creation.comboBoxMaitrise.itemText(x)
			if texte == '':
				vide =+ 1
		if vide > 0:
			return True
	def enleverDiscipline(self):
		maitrise = self.pop_creation.comboBoxMaitrise.currentIndex()
		discipline_id = self.pop_creation.comboBoxMaitrise.currentData()
		indexDiscipline = self.pop_creation.comboBoxDisciplines.findData(discipline_id)
		if discipline_id is not None:
			self.pop_creation.comboBoxDisciplines.model().item(indexDiscipline).setEnabled(True)
			self.pop_creation.comboBoxMaitrise.setItemData(maitrise, None)
			self.pop_creation.comboBoxMaitrise.setItemText(maitrise, '')
			self.dictionnaireNotes.pop(discipline_id) 


	def ajouterObjet(self):
		nouvelObjet = self.pop_creation.lineEditObjet.text()
		for x in range(8):
			place = self.pop_creation.comboBoxInventaire.itemText(x)
			if place == '':
				self.pop_creation.comboBoxInventaire.insertItem(x, nouvelObjet)
				self.pop_creation.lineEditObjet.clear()
				break
	def enleverObjet(self):
		objet = self.pop_creation.comboBoxInventaire.currentIndex()
		self.pop_creation.comboBoxInventaire.removeItem(objet)


	def ouvrirPDF(self):
		path = 'Loup-solitaire-01-les-maitres-des-tenebres.pdf'
		webbrowser.open_new(path)
	

	def enregistrerNouvellePartie(self, livre, chapitre, dictionnaireNotes):
		self.creation.close()
		nom_personnage = self.pop_creation.lineEditNomPersonnage.text()
		habilete = self.pop_creation.spinBoxHabilete.value()
		endurance = self.pop_creation.spinBoxEndurance.value()
		endurance_max = endurance
		bourse = self.pop_creation.spinBoxBourse.value()
		objets_speciaux = self.pop_creation.plainTextEditObjetsSpeciaux.toPlainText()

		objet = {}
		for x in range(8):
			objet[x] = self.pop_creation.comboBoxInventaire.itemText(x)
		
		personnage_id = insertPersonnage(nom_personnage, habilete, endurance, endurance_max, bourse, objets_speciaux)
		insertInventaire(personnage_id, nom_personnage, objet[0], objet[1], objet[2], objet[3], objet[4], objet[5], objet[6], objet[7])

		for x in range(5):
			discipline_id = self.pop_creation.comboBoxMaitrise.itemData(x)
			notes = dictionnaireNotes[discipline_id]
			insertMaitrise(discipline_id, personnage_id, notes)
		
		for arme in range(self.pop_creation.comboBoxInventaireArmes.count()):
			arme_id = self.pop_creation.comboBoxInventaireArmes.itemData(arme)
			insertInventaireArme(arme_id, personnage_id)
		
		self.remplirFeuilleAventure(livre, chapitre, personnage_id)


	def remplirFeuilleAventure(self, livre, chapitre, personnage_id):

		self.spinBoxEndurance.valueChanged.connect(self.changerProgressBar)
		self.spinBoxHabilete.valueChanged.connect(lambda: self.changerSpinBoxHabilete('livre'))
		self.spinBoxHabileteLivre.valueChanged.connect(self.changerSpinBoxHabilete)
		self.pushButtonAjouterObjet.clicked.connect(self.ajouterObjetFeuille)
		self.pushButtonEnleverObjet.clicked.connect(self.enleverObjetFeuille)
		self.pushButtonTournerPage.clicked.connect(lambda: self.tournerPage(livre))
		self.pushLienPDF.clicked.connect(self.ouvrirPDF)
		self.pushQuitter.clicked.connect(sys.exit)
		self.pushSave.clicked.connect(lambda: self.sauvegarderPartie(livre, chapitre, personnage_id))


		self.listeLabelsDisciplines = [
			'self.labelDiscipline1',
			'self.labelDiscipline2',
			'self.labelDiscipline3',
			'self.labelDiscipline4',
			'self.labelDiscipline5',
		]

		self.listeLabelsArmes =  [
			'self.labelArme1',
			'self,labelArme2'
		]


		personnage = getFeuilleAventure(personnage_id)
		nom_personnage, habilete, endurance, endurance_max, bourse, objets_speciaux = personnage
		self.labelNomFeuille.setText(nom_personnage)
		self.spinBoxHabilete.setValue(habilete)
		self.spinBoxHabileteLivre.setValue(habilete)
		self.spinBoxEndurance.setValue(endurance)
		self.spinBoxEndurance.setMaximum(endurance_max)
		self.progressBarEndurance.setValue(endurance)
		self.progressBarEndurance.setMaximum(endurance_max)
		self.spinBoxBourse.setValue(bourse)
		self.plainTextEditObjetsSpeciaux.setPlainText(objets_speciaux)
	

		maitrises = getMaitrises(personnage_id)
		#https://www.youtube.com/watch?v=bkqjXE_NTbU ->  Jie Jenn "How to iterate child widgets | PyQt6 Tutorial"
		for x in range(self.layoutDisciplines.count()):
			discipline = maitrises[x]
			maitrise_id, nom_discipline, maitrise_notes = discipline
			self.layoutDisciplines.itemAt(x).widget().setText(nom_discipline)
			self.layoutDisciplines.itemAt(x).widget().setToolTip(maitrise_notes)
			

		inventaireArmes = getInventaireArmes(personnage_id)
		for x in range(len(inventaireArmes)):
			arme = inventaireArmes[x]
			id_arme, nom_arme = arme
			self.layoutArmes.itemAt(x).widget().setText(nom_arme)


		inventaireObjets = getInventaire(personnage_id)
		id, personnage_id, nom_personnage, objet1, objet2, objet3, objet4, objet5, objet6, objet7, objet8 = inventaireObjets
		for objet in range(8):
			if inventaireObjets[(objet + 3)].lower() == 'repas':
				value = self.spinBoxRepas.value()
				self.spinBoxRepas.setValue(value+1)
			elif inventaireObjets[(objet + 3)] != '': 
				self.listWidgetInventaire.addItem(inventaireObjets[(objet + 3)])
			self.changerMaxRepas()

		window.show()
		self.partie(livre, chapitre)


	def partie(self, livre, chapitre):

		page = getChapitre(livre, chapitre)
		chapitre_id, no_chapitre, texte = page
		self.textBrowser.setText(texte)
		self.labelChapitre.setText("Chapitre " + no_chapitre)


	def ajouterObjetFeuille(self):
		totalObjets = self.listWidgetInventaire.count() + self.spinBoxRepas.value()
		if totalObjets < 8:
			objet = self.lineEditObjetFeuille.text()
			if objet.lower() == 'repas':
				value = self.spinBoxRepas.value()
				self.spinBoxRepas.setValue(value+1)
			elif objet != '':
				self.listWidgetInventaire.addItem(objet)
			self.changerMaxRepas()
	def enleverObjetFeuille(self):
		current = self.listWidgetInventaire.currentRow()
		self.listWidgetInventaire.takeItem(current)
		self.changerMaxRepas()
		

	def changerProgressBar(self):
		value = self.spinBoxEndurance.value()
		self.progressBarEndurance.setValue(value)
	

	def changerMaxRepas(self):
		nombreObjets = self.listWidgetInventaire.count()
		self.spinBoxRepas.setMaximum(8-nombreObjets)
	def changerSpinBoxHabilete(self, spinBox):
		if spinBox == 'livre':
			value = self.spinBoxHabilete.value()
			self.spinBoxHabileteLivre.setValue(value)
		else:
			value = self.spinBoxHabileteLivre.value()
			self.spinBoxHabilete.setValue(value)
	

	def tournerPage(self, livre):
		pageDestination = self.comboBoxPagesSuivantes.currentText()
		self.comboBoxPagesSuivantes.clear()
		tupleLiens = getLiens(pageDestination)
		for lien in tupleLiens:
			page_lien = str(lien[1])
			self.comboBoxPagesSuivantes.addItem(page_lien)
		self.partie(livre, pageDestination)
	
	def sauvegarderPartie(self, livre, chapitre, personnage_id):
		page = getChapitre(livre, chapitre)
		chapitre_id, livre_id, chapitre = page
		updateSauvegarde(personnage_id, chapitre_id)

app = QApplication(sys.argv)

window = MainWindow()


app.exec()