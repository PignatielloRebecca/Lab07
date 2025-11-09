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

            return epoche





