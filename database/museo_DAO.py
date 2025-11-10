from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_all_musei():
        musei=[]
        cnx=ConnessioneDB.get_connection()
        if cnx is None:
            print("Conessione fallita")
            return musei
        else:
            cursor=cnx.cursor(dictionary=True)
            query=("SELECT nome FROM museo")
            cursor.execute(query)

            for row in cursor:
                musei.append(row["nome"])
            cnx.close()
            cursor.close()
        return musei





