#Cherche titres livres dans db

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