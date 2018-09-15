from telegram_bot import poster
from medium_check import medium_parser
import time
from db import mdb

d = mdb()
_conn = d.get_con()
p = poster()

try:
    cursor = _conn.telegram.medium_users.find({"mstatus":1},{"_id":1,"medium_id":1})
    for user in cursor:
        print(user["medium_id"])
        mp = medium_parser([user["medium_id"],user["_id"]])
        result = mp.get_new_pubs()
        if len(result) > 0:
            for post in result:
                url = mp.get_post_url(post)
                p.send_message(url)
                time.sleep(2)
            mp.insert_new_pubs(result)
except Exception as e:
    print ("Unexpected exception - mcronpy", type(e),e)
