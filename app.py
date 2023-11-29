import sqlite3
import requests as requests
from flask import Flask, render_template, redirect
from markupsafe import escape
from datetime import datetime, date

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "MSI c kro bien !"

class PokedexForm(FlaskForm):
    name = StringField('nom_pokemon', validators=[DataRequired()])

def show(pokemon):
    r = requests.get('https://api-pokemon-fr.vercel.app/api/v1/pokemon/' + pokemon)
    try :
        info = dict()
        print(r.json()['sprites']['regular'])
        image = r.json()['sprites']['regular']
        name = r.json()['name']['fr']
        types = r.json()['types']
        imageType = r.json()['types']
        talents = r.json()['talents']
        stats = r.json()['stats']
        pokedexId = r.json()['pokedexId']
        evolution = r.json()['evolution']
        sexe = r.json()['sexe']
        height = r.json()['height']
        weight = r.json()['weight']
        info['name'] = name
        info['types'] = types
        info['talents'] = talents
        info['stats'] = stats
        info['pokedexId'] = pokedexId
        info['evolution'] = evolution
        info['sexe'] = sexe
        info['height'] = height
        info['weight'] = weight
        info['image_type'] = imageType
        info['image'] = image
        return info
    except :
        return 404


@app.route("/", methods=['GET', 'POST'])
def index():
    pokedex = PokedexForm()
    if pokedex.validate_on_submit():
        print(pokedex.name.data)
        reponse = show(pokedex.name.data)
        if(reponse == 404):
            return render_template('index.html', form=pokedex, reponse=404)
        return render_template('index.html', form=pokedex, reponse=reponse)
    return render_template('index.html', form=pokedex)