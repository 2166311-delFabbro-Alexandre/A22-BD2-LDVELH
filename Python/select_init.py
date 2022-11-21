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
def getChapitre(chapitre_id: int)-> tuple:
	"""
	Sélectionne un chapitre
	Arguments:
		chapitre_id: le id du chapitre (int)
	Returns:
		Un tuple avec le id du chapitre, le numéro du chapitre (int) et le texte (text)
	"""
	
	query = """
		SELECT id, no_chapitre, texte FROM chapitre c
		WHERE c.id = %(chapitre_id)s;
	"""
	parametres = {
		'chapitre_id' : chapitre_id
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
def getLiens(chapitre_id: int)-> tuple:
	"""
	Sélectionne les liens chapitre
	Arguments:
		chapitre_id: le id du chapitre (int),

	Returns:
		Un tuple avec le numéro du chapitre d'origine (int) et les destinations (int)
	"""
	
	query = """
		SELECT no_chapitre_origine, no_chapitre_destination FROM lien_chapitre lc
		INNER JOIN chapitre c ON c.id = %(chapitre_id)s
		WHERE lc.no_chapitre_origine = c.no_chapitre AND ls.livre_id = c.livre_id;
	"""
	parametres = {
		'chapitre_id' : chapitre_id,
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
		SELECT s.id, concat(f.nom_personnage, " ", s.date_sauvegarde) FROM feuille_aventure f
        INNER JOIN sauvegarde s ON s.personnage_id = f.id;
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

