#Ensemble des fonctions pour insérer ou supprimer des entrées dans les tables

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


def insertPersonnage(nom_personnage: str, habilete: int, endurance: int, endurance_max: int, bourse: int, objets_speciaux: str)-> int:
    """
    Ajoute un personnage à sa création
    Args:
        nom_personnage (str): nom du personnage    
        habilete (int): habilete
        endurance (int): endurance
        endurance_max (int): endurance fixe
        bourse (int): total pièces d'or
        objets_speciaux (text): texte des objets spéciaux

    Returns:
        personnageId: le id de la feuille d'aventure
    """
    query = """
        INSERT INTO feuille_aventure (nom_personnage, habilete, endurance, endurance_max, bourse, objets_speciaux)
        VALUES(%(nom_personnage)s, %(habilete)s, %(endurance)s, %(endurance_max)s, %(bourse)s, %(objets_speciaux)s);
    """
    parametres = {
        'nom_personnage' : nom_personnage,
        'habilete' : habilete,
        'endurance' : endurance,
        'endurance_max' : endurance_max,
        'bourse' : bourse,
        'objets_speciaux' : objets_speciaux,
    }
    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametres)
        personnageId = cursor.lastrowid

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()

    return personnageId

def insertInventaire(personnage_id: int, nom_personnage:str, objet1: str, objet2: str, objet3: str, objet4: str, objet5: str, objet6: str, objet7: str, objet8: str):
    """
    Ajoute un inventaire à la création

    Args:
        personnage_id (int): id de la feuille d'aventure
        nom_personnage (str): nom du personnage à qui l'inventaire appartient
        objet1 (str): objet 1
        objet2 (str): objet 2
        objet3 (str): objet 3
        objet4 (str): objet 4
        objet5 (str): objet 5
        objet6 (str): objet 6
        objet7 (str): objet 7
        objet8 (str): objet 8

    Returns:
        inventaire_id: le id de l'inventaire créé (int)
    """
    query = """
        INSERT INTO inventaire (personnage_id, nom_personnage, objet1, objet2, objet3, objet4, objet5, objet6, objet7, objet8)
        VALUES(%(personnage_id)s, %(nom_personnage)s, %(objet1)s, %(objet2)s, %(objet3)s, %(objet4)s, %(objet5)s, %(objet6)s, %(objet7)s, %(objet8)s);
    """
    parametres = {
        'personnage_id' : personnage_id,
        'nom_personnage' : nom_personnage,
        'objet1' : objet1,
        'objet2' : objet2,
        'objet3' : objet3,
        'objet4' : objet4,
        'objet5' : objet5,
        'objet6' : objet6,
        'objet7' : objet7,
        'objet8' : objet8,
    }
    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametres)
        inventaireId = cursor.lastrowid

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()

def insertMaitrise(discipline_id: int, personnage_id: int, notes: str):
    """
    Ajoute les maitrises kaï lors d'une nouvelle partie

    Args:
        discipline_id (int): le id de la discipline
        personnage_id (int): le id du personnage
        notes (str): Des notes sur la discipline (text)

    """
    query = """
        INSERT INTO maitrise_kai (discipline_id, personnage_id, notes)
        VALUES(%(discipline_id)s, %(personnage_id)s, %(notes)s);
    """
    parametres = {
        'discipline_id' : discipline_id,
        'personnage_id' : personnage_id,
        'notes' : notes,
    }
    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametres)

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()


def insertInventaireArme(arme_id: int, personnage_id: int):
    """
    Ajoute les armes possédées lors d'une nouvelle partie

    Args:
        arme_id (int): le id de l'arme
        personnage_id (int): le id du personnage
    """
    query = """
        INSERT INTO inventaire_arme (arme_id, personnage_id)
        VALUES(%(arme_id)s, %(personnage_id)s);
    """
    parametres = {
        'arme_id' : arme_id,
        'personnage_id' : personnage_id,
    }
    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametres)

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()


def updateSauvegarde(personnage_id: int, chapitre_id: int):
    """
    Sauvegarde les informations de la partie

    Args:
        personnage_id (int): le id du personnage
        chapitre_id (int): le id du chapitre en cours
    """
    query = """
        UPDATE sauvegarde SET 
            personnage_id = %(personnage_id)s, 
            chapitre_id = %(chapitre_id)s, 
            date_sauvegarde = now()
        WHERE personnage_id = %(personnage_id)s;
    """
    parametres = {
        'personnage_id' : personnage_id,
        'chapitre_id' : chapitre_id
    }
    try:
        connection = mysql.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(query, parametres)

        connection.commit()
    except mysql.Error as erreur:
        print(erreur)
    finally:
        cursor.close()
        connection.close()