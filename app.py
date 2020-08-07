import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from pymongo import MongoClient

db_pass = os.environ.get('DB_PASS')

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'songbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://Lingvistik:'+str(db_pass)+'@prviklaster-v3qci.mongodb.net/songbook?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')
def route():
    return redirect(url_for('songs'))

@app.route('/songs')
def songs():
    return render_template('chordbook.html', chords=mongo.db.chords.find())

@app.route('/song/<song_id>')
def show_chords(song_id):
    the_chord = mongo.db.chords.find_one({"_id": ObjectId(song_id)})
    return render_template('showchords.html', chords=the_chord)
      

@app.route('/add_chords', methods=['GET','POST'])
def add_chords():
    if request.method == 'POST':
        chords = mongo.db.chords
        chords.insert_one(request.form.to_dict())
        return redirect(url_for('songs'))
    else:
        return render_template('addchords.html')

@app.route('/edit_chords/<song_id>', methods=['GET','POST'])
def edit_chords(song_id):
    if request.method == 'POST':
        chords = mongo.db.chords
        chords.update({'_id': ObjectId(song_id)},
        {
            'band_name':request.form.get('band_name'),
            'song_name':request.form.get('song_name'),
            'chords_text': request.form.get('chords_text'),
            'image': request.form.get('image')
        })
        return redirect(url_for('songs'))
    else:
        the_chord = mongo.db.chords.find_one({"_id": ObjectId(song_id)})
        return render_template('editchords.html', chords=the_chord)

@app.route('/delete_chords/<song_id>')
def delete_chords(song_id):
    mongo.db.chords.remove({'_id': ObjectId(song_id)})
    return redirect(url_for('songs'))

@app.route('/chords_diagram')
def chords_diagram():
    return render_template('chordsdiagram.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)