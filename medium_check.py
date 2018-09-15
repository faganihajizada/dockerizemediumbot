import requests
import json
from db import mdb

class medium_parser:
    
    _conn = None
    muser = None
    muser_id = 0

    def __init__(self,userdetails):
        self.muser = userdetails[0]
        self.muser_id = userdetails[1]
        print(self.muser)
        d = mdb()
        self._conn = d.get_con()
        self._db = self._conn.telegram

    def get_username(self):
        return self.muser

    def clean_json_response(self,response):
        return json.loads(response.text.split('])}while(1);</x>')[1])

    def get_list_of_latest_posts_ids(self):
        post_ids = []
        MEDIUM = 'https://medium.com'
        url = MEDIUM + '/@' + self.muser + '/latest?format=json'
        response = requests.get(url)
        response_dict = self.clean_json_response(response)
        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []
        if posts:
            for key in posts.keys():
                post_ids.append(posts[key]['id'])
            return post_ids

    def get_list_of_user_posts(self):
        try:
            q = {"muser_id":self.muser_id}
            upub_list = []
            pubs = self._db.medium_publications.find(q)
            if pubs is not None:
                for pub in pubs:
                    upub_list.append(pub['muserpub_id'])
                return upub_list
        except Exception as e:
            print ("Unexpected exception - get_list_of_user_posts", type(e),e)
        return upub_list


    def get_post_url(self,post_id):
        MEDIUM = 'https://medium.com'
        url = MEDIUM + '/@' + self.muser + '/' + post_id
        return url


    def insert_new_pubs(self,publist):
        try:
            for pub in publist:
                q = {"muser_id":self.muser_id,"muserpub_id":pub}
                cursor = self._db.medium_publications.insert_one(q)
        except Exception as e:
            print("Unexpected excption - insert_new_pubs", type(e),e)
    def get_new_pubs(self):
        latest = self.get_list_of_latest_posts_ids()
        stored = self.get_list_of_user_posts()
        pub_dif = set(latest).difference(stored)

        return list(pub_dif)
