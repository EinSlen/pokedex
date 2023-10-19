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
    name = StringField('name', validators=[DataRequired()])

def show(pokemon):
    r = requests.get('https://api-pokemon-fr.vercel.app/api/v1/pokemon/' + pokemon)# put application's code here
    try :
        info = dict()
        name = r.json()['name']['fr']
        types = r.json()['types']
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
        return info
    except :
        return 404


@app.route("/", methods=['GET', 'POST'])
def index():
    pokedex = PokedexForm()
    if pokedex.validate_on_submit():
        reponse = show(pokedex.name.data)
        if(reponse == 404):
            return render_template('not_found.html')
        return render_template('featch_reponse.html', reponse=reponse)
    return render_template('render.html', form=pokedex)