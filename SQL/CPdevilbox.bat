@ECHO OFF

::Batch pour copie scripts sur devilbox-mysql-1

cd c:/users/alexa/documents/a22/bd2/ldvelh/scripts

docker cp .\LDVELH_creation_tables.sql devilbox-mysql-1:/scripts_ldvelh
docker cp .\ex11_insert_chapitre.sql devilbox-mysql-1:/scripts_ldvelh
docker cp .\ex11_insert_lien_chapitre.sql devilbox-mysql-1:/scripts_ldvelh
docker cp .\insertion_armes.sql devilbox-mysql-1:/scripts_ldvelh
docker cp .\insertion_disciplines.sql devilbox-mysql-1:/scripts_ldvelh
docker cp .\insertion_livres.sql devilbox-mysql-1:/scripts_ldvelh
