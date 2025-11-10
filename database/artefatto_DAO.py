from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # prendo artefatti filtrati per museo ed epoca
    def read_all_artefatti(self, museo, epoca):
        artefatti = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Conessione fallita")
            return artefatti
        else:
            cursor=cnx.cursor(dictionary=True)
            query=("SELECT artefatto.nome as nomeArtefatto FROM artefatto JOIN museo ON museo.id=artefatto.id_museo "
                   "WHERE epoca=%s AND museo.nome=%s")

            cursor.execute(query, (epoca,museo))

            for row in cursor:

                artefatti.append(row["nomeArtefatto"])
            cursor.close()
            cnx.close()
            return artefatti

    @staticmethod

    def read_all_epoche():
        epoche = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Conessione fallita")
            return epoche
        else:
            cursor=cnx.cursor(dictionary=True)
            query="SELECT epoca FROM artefatto GROUP BY epoca ORDER BY epoca ASC"

            cursor.execute(query)
            for row in cursor:
                epoche.append(row["epoca"])
            cnx.close()
            cursor.close()

            return epoche
    @staticmethod

    def read_all_artefatti_tutti_i_musei():
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connessione fallita")
            return artefatti
        else:
            cursor = cnx.cursor(dictionary=True)
            # Seleziona il nome di tutti gli artefatti
            query = "SELECT nome FROM artefatto"

            cursor.execute(query)

            for row in cursor:
                # Assumendo che la colonna si chiami 'nome' nella tabella artefatto
                artefatti.append(row["nome"])

            cursor.close()
            cnx.close()
            return artefatti

    def read_artefatti_per_museo(self, nome):
        artefatti = []
        cnx = ConnessioneDB.get_connection()

        if cnx is None:
            print("Connessione fallita")
            return artefatti
        else:
            cursor = cnx.cursor(dictionary=True)
            # Seleziona gli artefatti unendo artefatto e museo, filtrando per nome del museo
            query = ("SELECT artefatto.nome as nomeArtefatto FROM artefatto "
                     "JOIN museo ON museo.id = artefatto.id_museo "
                     "WHERE museo.nome = %s")

            cursor.execute(query, (nome,))

            for row in cursor:
                artefatti.append(row["nomeArtefatto"])

            cursor.close()
            cnx.close()
            return artefatti

    def read_artefatti_per_epoca(self, epoca):
     artefatti = []
     cnx = ConnessioneDB.get_connection()

     if cnx is None:
        print("Connessione fallita")
        return artefatti
     else:
        cursor = cnx.cursor(dictionary=True)
        # Seleziona gli artefatti filtrando per epoca
        query = "SELECT nome FROM artefatto WHERE epoca = %s"

        cursor.execute(query, (epoca,))

        for row in cursor:
            artefatti.append(row["nome"])

        cursor.close()
        cnx.close()
        return artefatti










