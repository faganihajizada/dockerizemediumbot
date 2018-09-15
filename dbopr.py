import pymongo
from db import mdb

class dbopr:

    _conn = None
    _db = None

    def __init__(self):
        d = mdb()
        self._conn = d.get_con()
        self._db = self._conn.telegram
    

    def __exit__(self,exc_type, exc_val, exc_tb):
        self._conn.close()

    def help(self):
        print("Available commands:")
        print("add_user(<username>) - Add new Medium userid to database.")
        print("disable_user(<username>) - Disable Medium user publications to be publiched on telegram channel.")
        print("enable_user(<username>) - Enable Medium user publications to be published on telegram channel.")
        print("get_userlist() - Print existing users.")

    def get_muserid(self,username):
        q = {"medium_id":username}
        uid = []
        try:
            cursor = self._db.medium_users.find_one(q)
            
            if cursor is not None:
                uid.append(cursor["_id"])
        except Exception as e:
            print ("Unexpected exception", type(e), e)
        return uid
        

    def add_user(self,username):

        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) == 0:
                q = {"medium_id":username,"mstatus":1}
                try:
                    cursor = self._db.medium_users.insert_one(q)
                except Exception as e:
                    print ("Unexpected exception", type(e), e)
            else:
                print (username, " already exists. You can enable user with enable_user(<username>) method.")
        else:
            print("Username parameter is empty")

    def disable_user(self, username):
        q = {"medium_id":username}
        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) > 0:
                try:
                    cursor = self._db.medium_users.update_one(q,{"$set":{"mstatus":0}})
                    print ("Done!")
                except Exception as e:
                    print("Unexpected exception", type(e), e)
            else:
                print (username, " not exists. Use add_user(<username>) method to add.")

    def enable_user(self, username):
        q = {"medium_id":username}
        if len(username) > 0:
            uid = self.get_muserid(username)
            if len(uid) > 0:
                cursor = self._db.medium_users.update_one(q,{"$set":{"mstatus":1}})
                print ("Done!")
            else:
                print (username, " not exists. Use add_user(<username>) method to add.")

    def get_userlist(self):
        try:
            cursor = self._db.medium_users.find()
        except Exception as e:
            print ("Unexpected exception", type(e), e)
        for user in cursor:
            print ("------------------------------------")
            print (str(user["_id"])," - ",user["medium_id"]," - ",str(user["mstatus"]))
