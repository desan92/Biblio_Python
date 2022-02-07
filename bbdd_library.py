import pymysql

class bbdd_biblioteca:

    def __init__(self):
        self.connexio = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="biblioteca"
        )

        self.cursor = self.connexio.cursor()

    #SELECT
    def SelectAllBooks(self):
        SQL = "SELECT * FROM llibre_biblioteca"
        self.cursor.execute(SQL)
        return self.cursor.fetchall()


    def SelectAllUsers(self):
        SQL = "SELECT * FROM usuari_biblioteca"
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectAllBooksUser(self, id):
        SQL = "SELECT ll.nom_llibre, ll.nom_autor, alb.id_arrendament, alb.tornat_llibre, ub.* " \
              "FROM llibre_biblioteca ll " \
              "LEFT JOIN arrendament_llibres_biblioteca alb ON ll.id_llibre = alb.id_llibre " \
              "LEFT JOIN usuari_biblioteca ub ON alb.id_usuari = ub.id_usuari " \
              "WHERE ll.id_llibre = '{}' AND alb.tornat_llibre = FALSE;".format(id)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectBooks(self, nomLlibre, nomAutor):
        SQL = "SELECT * FROM llibre_biblioteca WHERE nom_llibre = '{}' AND nom_autor = '{}'".format(nomLlibre, nomAutor)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectUser(self, id):
        SQL = "SELECT * FROM usuari_biblioteca WHERE id_usuari = {}".format(id)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectIdArrendat(self, id):
        SQL = "SELECT * FROM arrendament_llibres_biblioteca WHERE id_llibre = '{}' AND tornat_llibre = 0".format(id)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    #INSERT
    def InsertUser(self, element):
        SQL = "INSERT INTO `usuari_biblioteca`(`nom_usuari`, `cognoms_usuari`, `tlf_usuari`, `email_usuari`) " \
              "VALUES('{}', '{}', '{}', '{}')".format(element[0], element[1], element[2], element[3])
        self.cursor.execute(SQL)
        self.connexio.commit()

    def InsertBook(self, element):
        SQL = "INSERT INTO `llibre_biblioteca`(`nom_llibre`, `nom_autor`, `editorial`, `disponible_llibre`) " \
              "VALUES('{}', '{}', '{}', TRUE)".format(element[0], element[1], element[2])
        self.cursor.execute(SQL)
        self.connexio.commit()

    def InsertLlogar(self, idu, idb):
        SQL = "INSERT INTO `arrendament_llibres_biblioteca`(`id_usuari`, `id_llibre`) " \
              "VALUES('{}', '{}')".format(idu, idb)
        self.cursor.execute(SQL)
        self.connexio.commit()

    # UPDATE
    def UpdateArrendat(self, id):
        SQL = "UPDATE arrendament_llibres_biblioteca SET tornat_llibre = TRUE WHERE id_arrendament = '{}'".format(id)
        self.cursor.execute(SQL)
        self.connexio.commit()

    def UpdateUser(self, element, id):
        SQL = "UPDATE usuari_biblioteca SET nom_usuari = '{}', cognoms_usuari = '{}', tlf_usuari = '{}', email_usuari = '{}' WHERE id_usuari = '{}'".format(element[0], element[1], element[2], element[3], id)
        self.cursor.execute(SQL)
        self.connexio.commit()

    def UpdateBook(self, element, id):
        SQL = "UPDATE llibre_biblioteca SET nom_llibre = '{}', nom_autor = '{}', editorial = '{}' WHERE id_llibre = '{}'".format(element[0], element[1], element[2], id)
        self.cursor.execute(SQL)
        self.connexio.commit()

    #DELETE
    def DeleteUser(self, id):
        SQL = "DELETE FROM usuari_biblioteca WHERE id_usuari = '{}'".format(id)
        self.cursor.execute(SQL)
        self.connexio.commit()

    def DeleteBook(self, id):
        SQL = "DELETE FROM llibre_biblioteca WHERE id_llibre = '{}'".format(id)
        self.cursor.execute(SQL)
        self.connexio.commit()