CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE usuari_biblioteca (
	id_usuari INT(11) AUTO_INCREMENT PRIMARY KEY,
	nom_usuari VARCHAR(30) NOT NULL,
	cognoms_usuari VARCHAR(30) NOT NULL,
	tlf_usuari VARCHAR(30) NOT NULL,
	email_usuari VARCHAR(30) NOT NULL
);

CREATE TABLE llibre_biblioteca (
    id_llibre INT(11) AUTO_INCREMENT PRIMARY KEY,
    nom_llibre VARCHAR(30) NOT NULL,
    nom_autor VARCHAR(30) NOT NULL,
    editorial VARCHAR(30) NOT NULL,
    disponible_llibre BOOLEAN
);

CREATE TABLE arrendament_llibres_biblioteca (
	id_arrendament INT(11) AUTO_INCREMENT PRIMARY KEY,
	id_usuari INT(11),
    id_llibre INT(11),
	data_lloguer DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_tornar_llibre DATETIME,
    tornat_llibre BOOLEAN,
    FOREIGN KEY (id_usuari) REFERENCES usuari_biblioteca(id_usuari),
    FOREIGN KEY (id_llibre) REFERENCES llibre_biblioteca(id_llibre)
);

CREATE TRIGGER add_date BEFORE INSERT ON `arrendament_llibres_biblioteca`
FOR EACH ROW
BEGIN

	DECLARE llogat TYPE OF llibre_biblioteca.disponible_llibre;

	SELECT disponible_llibre INTO llogat
	FROM llibre_biblioteca
	WHERE llibre_biblioteca.id_llibre = NEW.id_llibre;


	IF llogat = TRUE THEN
	    SET NEW.data_lloguer = IFNULL(NEW.data_lloguer, NOW());
	    SET NEW.data_tornar_llibre = TIMESTAMPADD(DAY, 30, NEW.data_lloguer);
	    SET NEW.tornat_llibre = false;

	   	UPDATE llibre_biblioteca
	   	SET disponible_llibre = NEW.tornat_llibre
	   	WHERE llibre_biblioteca.id_llibre = NEW.id_llibre;

	ELSEIF llogat = FALSE THEN
		SIGNAL SQLSTATE 'HY000'
		SET MESSAGE_TEXT = 'AQUET LLIBRE ESTA LLOGAT';

   END IF;

END

CREATE TRIGGER update_disponible_llibre AFTER UPDATE ON arrendament_llibres_biblioteca FOR EACH ROW
BEGIN
	DECLARE tornat TYPE OF arrendament_llibres_biblioteca.tornat_llibre;

	SET tornat = NEW.tornat_llibre;

	UPDATE llibre_biblioteca
	SET disponible_llibre = tornat
	WHERE llibre_biblioteca.id_llibre = OLD.id_llibre;

END

CREATE TRIGGER control_delete BEFORE DELETE ON usuari_biblioteca FOR EACH ROW
BEGIN

	DECLARE llogat TYPE OF arrendament_llibres_biblioteca.tornat_llibre;

	SELECT `tornat_llibre` INTO llogat
	FROM `arrendament_llibres_biblioteca`
	WHERE id_usuari = OLD.id_usuari ORDER BY `tornat_llibre` ASC LIMIT 1;

	IF llogat = FALSE THEN
		SIGNAL SQLSTATE 'HY000'
		SET MESSAGE_TEXT = 'USUARI TE ALGUN LLIBRE LLOGAT';
	END IF;

END






