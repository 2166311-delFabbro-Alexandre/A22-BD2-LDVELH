#inserer objet dans inventaire

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

def insertObjetInventaire(objet: str)-> bool:
    """
    Ajoute un objet à la table inventaire
    Argument:
        objet: str
    Returns:
        bool true si insert réussi
    """

    query = """
        INSERT INTO inventaire (classe_id, nom, prenom, no_civique, adresse, ville, pin, credit_initial) 
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
