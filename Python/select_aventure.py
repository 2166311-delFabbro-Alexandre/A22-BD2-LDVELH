#Les fonctions de sélection pour le jeu

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

#Select la feuille d'aventure
def getFeuilleAventure(personnage_id: int)-> tuple:
	"""
	Sélectionne la feuille d'aventure
    Arguments:
		personnage_id: le id de la feuille (int)
	Returns:
		Un tuple avec le nom du personnage, l'habileté, l'endurance, l'endurance max, le nombre de pieces d'or et les objets spéciaux
	"""

	query = """
		SELECT nom_personnage, habilete, endurance, endurance_max, bourse, objets_speciaux FROM feuille_aventure f
        WHERE f.id = %(personnage_id)s;
	"""

	parametres = {
		'personnage_id' : personnage_id,
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

#Select les maitrises kai
def getMaitrises(personnage_id: int)-> list:
	"""
	Sélectionne les maitrises du personnage
    Arguments:
		personnage_id: le id de la feuille (int)
	Returns:
		Un tuple avec l'id de la maitrise, le nom de la discipline et les notes
	"""

	query = """
		SELECT mk.id, dk.nom_discipline, mk.notes FROM maitrise_kai mk
		INNER JOIN discipline_kai dk ON mk.discipline_id = dk.id
        WHERE mk.personnage_id = %(personnage_id)s;
	"""

	parametres = {
		'personnage_id' : personnage_id,
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

#Select l'inventaire des armes
def getInventaireArmes(personnage_id: int)-> list:
	"""
	Sélectionne les armes du personnage
    Arguments:
		personnage_id: le id du personnage
	Returns:
		Un tuple avec l'id de l'arme, le nom de l'arme
	"""

	query = """
		SELECT ia.id, a.nom_arme FROM inventaire_arme ia
		INNER JOIN arme a ON ia.arme_id = a.id
        WHERE ia.personnage_id = %(personnage_id)s;
	"""

	parametres = {
		'personnage_id' : personnage_id,
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

