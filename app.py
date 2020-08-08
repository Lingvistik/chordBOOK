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

# Shows error if the page doesn't exist
@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html"), 404

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
      
# CREATE functionality with validation of the required fields
@app.route('/add_chords', methods=['GET','POST'])
def add_chords():
    if request.method == 'POST':
        if validate_form(request.form):
            chords = mongo.db.chords
            chords.insert_one(request.form.to_dict())
            return redirect(url_for('songs'))
        else:
            return render_template('addchords.html', error=True)   
    else:
        return render_template('addchords.html')

# EDIT functionality with validation of the required fields
@app.route('/edit_chords/<song_id>', methods=['GET','POST'])
def edit_chords(song_id):
    if request.method == 'POST':
        chords = mongo.db.chords
        if validate_form(request.form):
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
            return render_template('editchords.html', chords=the_chord, error=True)
    else:
        the_chord = mongo.db.chords.find_one({"_id": ObjectId(song_id)})
        return render_template('editchords.html', chords=the_chord)

# DELETE functionality
@app.route('/delete_chords/<song_id>')
def delete_chords(song_id):
    mongo.db.chords.remove({'_id': ObjectId(song_id)})
    return redirect(url_for('songs'))

@app.route('/chords_diagram')
def chords_diagram():
    return render_template('chordsdiagram.html')

# Checks if the required fields are populated
def validate_form(form):
    band_name = form.get('band_name')
    song_name = form.get('song_name')
    chords_text = form.get('chords_text')
    if band_name != "" and song_name != "" and chords_text != "":
        return True
    return False

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)