#Chercher lien dans lien_chapitre

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