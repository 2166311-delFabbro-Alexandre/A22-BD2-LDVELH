#Chercher chapitre dans db

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