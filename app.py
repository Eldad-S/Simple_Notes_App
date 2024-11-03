from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

import app_aux

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mongod"
mongo = PyMongo(app)

""" ======
App Routes 
========== """

@app.get('/notes')
def index():
    notes = mongo.db.notes.find()
    return render_template('index.html', notes=notes)

@app.post('/notes')
def add_note():
    content = request.form['content']
    note_id = mongo.db.notes.insert_one({'content': content}).inserted_id
    app_aux.log_action(mongo.db.history, note_id, content, 'add')
    return redirect(url_for('index'))

@app.get('/notes/<note_id>')
def edit_note(note_id):    
    note = mongo.db.notes.find_one({'_id': ObjectId(note_id)})
    return render_template('edit.html', note=note)

@app.post('/notes/<note_id>')
def update_note(note_id):
    content = request.form['content']
    mongo.db.notes.update_one({'_id': ObjectId(note_id)}, {"$set": {'content': content}})
    app_aux.log_action(mongo.db.history, note_id, content, 'update')        
    return redirect(url_for('index'))

@app.route('/notes/delete/<note_id>')
def delete_note(note_id):
    note = mongo.db.notes.find_one({'_id': ObjectId(note_id)})
    if note:
        mongo.db.notes.delete_one({'_id': ObjectId(note_id)})
        app_aux.log_action(mongo.db.history, note_id, note['content'], 'delete')
    return redirect(url_for('index'))

@app.route('/notes/delete-all')
def delete_all_notes():
    return app_aux.delete_many_and_redirect(mongo.db.notes, url_for('index'))

@app.route('/notes/clear-history')
def clear_history():
    return app_aux.delete_many_and_redirect(mongo.db.history, url_for('show_history'))

@app.route('/notes/history')
def show_history():
    history = list(mongo.db.history.find().sort("time", -1))  # Sort by time, descending
    return render_template('history.html', history=history)


""" =========
Main Function 
============= """

if __name__ == '__main__':
    try:
        # Attempt to connect to the MongoDB server
        mongo.cx.server_info()  # This will raise an exception if the server is not reachable
        print("Connected to MongoDB successfully")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        exit(1)

    app.run()
