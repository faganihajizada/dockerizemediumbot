import pymongo

class mdb:
    _con = None

    def __init__(self):
        self._con = pymongo.MongoClient("mongodb://localhost",username='teluser',password='tel123',authSource='telegram')

    def __exit__(self,exc_type, exc_val, exc_tb):
        self._con.close()

    def get_con(self):
        return self._con
