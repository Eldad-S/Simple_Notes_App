import datetime
from flask import redirect

""" ============
Aux Methods Used
================ """

def log_action(database, note_id, content, action):
    database.insert_one({
        "orig_id": str(note_id),
        "content": content,
        "action": action,
        "time": datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    })

def delete_many_and_redirect(database, url_string):
    database.delete_many({})
    return redirect(url_string)
