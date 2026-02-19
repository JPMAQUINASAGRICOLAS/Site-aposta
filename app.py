from flask import Flask, jsonify
import requests
import datetime
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return "Site-aposta online"

@app.route("/jogos")
def jogos():
    hoje = datetime.date.today().strftime("%Y-%m-%d")

    url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?date={hoje}"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return jsonify(response.json())
