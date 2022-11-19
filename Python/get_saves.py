#Cherche sauvegardes dans db

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