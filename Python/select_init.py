#Les fonctions de sélection pour démarrer le jeu

import mysql.connector as mysql

db_config = {
	'host': 'localhost',
	'user': 'loup_Solitaire',
	'password': 'LDVELH2022',
	'database': 'ldvelh',
	'use_unicode': True,
	'charset': 'utf8mb4',
	'collation': 'utf8mb4_general_ci'
}

#Select les disciplines
def getDisciplines()-> list:
	"""
	Sélectionne les disciplines
	Returns:
		Une liste de disciplines, id (int) et nom_discipline (varchar(50))
	"""
	
	query = """
		SELECT id, nom_discipline FROM discipline_kai;
	"""
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query)
		result = cursor.fetchall()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result


#Select les armes
def getArmes()-> list:
	"""
	Sélectionne les armes
	Returns:
		Une liste d'armes, id (int) et nom_arme (varchar(20))
	"""
	
	query = """
		SELECT id, nom_arme FROM arme;
	"""
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query)
		result = cursor.fetchall()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result


#Select les chapitres
def getChapitre(no_livre: int, no_chapitre: int)-> tuple:
	"""
	Sélectionne un chapitre
	Arguments:
		no_livre: le numéro du livre (int)
		no_chapitre: le numéro du chapitre (str)
	Returns:
		Un tuple avec le numéro du chapitre (int) et le texte (text)
	"""
	
	query = """
		SELECT no_chapitre, texte FROM chapitre c
		WHERE c.livre_id = %(no_livre)s AND c.no_chapitre = %(no_chapitre)s;
	"""
	parametres = {
		'no_livre' : no_livre,
		'no_chapitre' : no_chapitre,
		}
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query, parametres)
		result = cursor.fetchone()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result


    #Select les liens entre chapitres
def getLiens(chapitre: int)-> tuple:
	"""
	Sélectionne les liens chapitre
	Arguments:
		chapitre: le numéro du chapitre (str)
	Returns:
		Un tuple avec le numéro du chapitre d'origine (int) et les destinations (int)
	"""
	
	query = """
		SELECT no_chapitre_origine, no_chapitre_destination FROM lien_chapitre l
		WHERE l.no_chapitre_origine = %(chapitre)s;
	"""
	parametres = {
		'chapitre' : chapitre,
		}
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query, parametres)
		result = cursor.fetchall()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result

#Select les livres
def getLivres()-> list:
	"""
	Sélectionne les livres
    Paramètres:
        id (int)
        titre (varchar(30))
	Returns:
		Une liste des livres, id (int) et titre (varchar(30))
	"""
	
	query = """
		SELECT id, titre FROM livre;
	"""
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query)
		result = cursor.fetchall()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result


#Select les sauvegardes
def getSaves()-> tuple:
	"""
	Sélectionne les sauvegardes
	Returns:
		Un tuple de noms de sauvegardes et de dates de sauvegardes
	"""
	
	query = """
		SELECT nom_personnage, date_sauvegarde FROM feuille_aventure
        INNER JOIN sauvegarde ON personnage_id = feuille_aventure.id;
	"""
	try:
		connection = mysql.connect(**db_config)
		cursor = connection.cursor()
		cursor.execute(query)
		result = cursor.fetchall()
	except mysql.Error as erreur:
		print(erreur)
	finally:
		cursor.close()
		connection.close()
		
	return result

#