import sqlite3
import requests as requests
from flask import Flask, render_template, redirect, session
from markupsafe import escape
from datetime import datetime, date
import os

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder='templates', static_folder='static_folder')
app.secret_key = "MSI c kro bien !"

class PokedexForm(FlaskForm):
    name = StringField('Pokemon', validators=[DataRequired()])

def show(pokemon):
    r = requests.get('https://api-pokemon-fr.vercel.app/api/v1/pokemon/' + pokemon)
    try :
        info = dict()
        name = r.json()['name']['fr'] 
        info['name'] = name
        info['types'] = r.json()['types']
        info['talents'] = r.json()['talents']
        info['stats'] = r.json()['stats']
        info['pokedexId'] = r.json()['pokedexId']
        info['evolution'] = r.json()['evolution']
        info['sexe'] = r.json()['sexe']
        info['height'] = r.json()['height']
        info['weight'] = r.json()['weight']
        info['image_type'] = r.json()['types']
        info['image'] = r.json()['sprites']['regular']
        info['son'] = storeAudio(name.lower())
        info['shiny'] = r.json()['sprites']['shiny']
        info['ajouter_favoris'] = session.get('ajouter_favoris', 0)
        
        return info
    except :
        return 404

def storeAudio(nomPokemon):
    def trouver_fichier_par_nom(nom_partiel, repertoire):
        fichiers_trouves = []
        for dossier_racine, _, fichiers in os.walk(repertoire):
            for fichier in fichiers:
                if nom_partiel in fichier:
                    chemin_complet = os.path.join(dossier_racine, fichier)
                    fichiers_trouves.append(chemin_complet)
        return fichiers_trouves

    repertoire = "./static_folder/resources"

    resultat = trouver_fichier_par_nom(nomPokemon, repertoire)

    print(resultat)

    if resultat:
        return resultat[0]
    else:
        return 404


@app.route("/", methods=['GET', 'POST'])
def index():
    pokedex = PokedexForm()

    if 'favorites' not in session:
        session['favorites'] = []

    if pokedex.validate_on_submit():
        reponse = show(pokedex.name.data)

        if reponse == 404:
            return render_template('index.html', form=pokedex, reponse=reponse)
        return render_template('index.html', form=pokedex, reponse=reponse, favorites=session['favorites'])
    return render_template('index.html', form=pokedex, favorites=session.get('favorites', []))
