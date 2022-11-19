#insert personnage

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

def insertPersonnageCreation():
    """
    Ajoute une feuille d'aventure
    Arguments:
        nom du personnage: un string
        habileté: int
        endurance: int
        endurance_max: int
        bourse: int
        
    Returns:
        Le id du citoyen créé (integer)
    """

    query = """
        INSERT INTO citoyen (classe_id, nom, prenom, no_civique, adresse, ville, pin, credit_initial) 
        VALUES (%(classe_id)s, %(nom)s, %(prenom)s, %(no_civique)s, %(adresse)s, %(ville)s, %(pin)s, %(credit_initial)s);
    """
    parametre = {
        'classe_id' : 4,
        'nom' : nom,
        'prenom' : prenom,
        'no_civique' : noCivique,
        'adresse' : adresse,
        'ville' : ville,
        'pin' : pin,
        'credit_initial' : 500,
    }

    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametre)
        citoyenId = cursor.lastrowid

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()