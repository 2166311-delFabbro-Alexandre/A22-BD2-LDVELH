create DATABASE if not exists ldvelh CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
create user if not exists 'loup_Solitaire' IDENTIFIED BY 'ldvelh2022';
GRANT ALL ON ldvelh.* TO loup_Solitaire;
use ldvelh;

-- Création des tables
create table if not exists ldvelh.livre (
	id INT auto_increment NOT NULL,
	titre varchar(30) NOT NULL,
	CONSTRAINT livre_pk PRIMARY KEY (id)
);

create table if not exists ldvelh.chapitre (
	id INT auto_increment NOT NULL,
	livre_id INT NOT NULL,
	no_chapitre varchar(30) NOT NULL,
	texte TEXT NOT NULL,
	CONSTRAINT chapitre_pk PRIMARY KEY (id),
	CONSTRAINT chapitre_FK FOREIGN KEY (livre_id) REFERENCES ldvelh.livre(id)
);

create table if not exists ldvelh.lien_chapitre (
	id INT auto_increment NOT NULL,
	livre_id INT NOT NULL
	no_chapitre_origine INT NOT NULL,
	no_chapitre_destination INT NOT NULL,
	CONSTRAINT lien_chapitre_pk PRIMARY KEY (id),
	CONSTRAINT lien_chapitre_FK FOREIGN KEY (livre_id) REFERENCES ldvelh.livre(id)
);

create table if not exists ldvelh.feuille_aventure (
	id INT auto_increment NOT NULL,
	nom_personnage varchar(30) NOT NULL,
	habilete INT NOT NULL,
	endurance INT NOT NULL,
	endurance_max INT NOT NULL,
	bourse INT NOT NULL,
	objets_speciaux TEXT,
	CONSTRAINT feuille_aventure_pk PRIMARY KEY (id)
);

create table if not exists ldvelh.inventaire (
	id INT auto_increment NOT NULL,
	feuille_aventure_id INT NOT NULL,
	nom_personnage varchar(30) NOT NULL,
	objet1 varchar(20),
	objet2 varchar(20),
	objet3 varchar(20),
	objet4 varchar(20),
	objet5 varchar(20),
	objet6 varchar(20),
	objet7 varchar(20),
	objet8 varchar(20),
	CONSTRAINT inventaire_pk PRIMARY KEY (id),
	CONSTRAINT inventaire_fk FOREIGN KEY (feuille_aventure_ID) REFERENCES ldvelh.feuille_aventure(id)
);

create table if not exists ldvelh.discipline_kai (
	id INT auto_increment NOT NULL,
	nom_discipline varchar(50) NOT NULL,
	description text NOT NULL,
	CONSTRAINT disciplique_kai_pk PRIMARY KEY (id)
);

create table if not exists ldvelh.maitrise_kai (
	id INT auto_increment NOT NULL,
	discipline_id INT NOT NULL,
	personnage_id INT NOT NULL,
	notes text,
	CONSTRAINT maitrise_kai_pk PRIMARY KEY (id),
	CONSTRAINT maitrise_kai_FK FOREIGN KEY (discipline_id) REFERENCES ldvelh.discipline_kai(id),
	CONSTRAINT maitrise_kai_FK2  FOREIGN KEY (personnage_id) REFERENCES ldvelh.feuille_aventure(id)
);

create table if not exists ldvelh.arme (
	id INT auto_increment NOT NULL,
	nom_arme varchar(20) NOT NULL,
	CONSTRAINT arme_pk PRIMARY KEY (id)
);

create table if not exists ldvelh.inventaire_arme (
	id INT auto_increment NOT NULL,
	arme_id INT NOT NULL,
	personnage_id INT NOT NULL,
	CONSTRAINT inventaire_arme_pk PRIMARY KEY (id),
	CONSTRAINT inventaire_arme_FK FOREIGN KEY (arme_id) REFERENCES ldvelh.arme(id),
	CONSTRAINT inventaire_arme_FK2 FOREIGN KEY (personnage_id) REFERENCES ldvelh.feuille_aventure(id)
);

create table if not exists ldvelh.sauvegarde (
	id INT auto_increment NOT NULL,
	personnage_id INT NOT NULL,
	chapitre_id INT NOT NULL,
	date_sauvegarde DATETIME NOT NULL,
	CONSTRAINT sauvegarde_pk PRIMARY KEY (id),
	CONSTRAINT sauvegarde_FK FOREIGN KEY (personnage_id) REFERENCES ldvelh.feuille_aventure(id),
	CONSTRAINT sauvegarde_FK2 FOREIGN KEY (chapitre_id) REFERENCES ldvelh.chapitre(id)
);