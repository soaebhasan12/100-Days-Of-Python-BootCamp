from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)


@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    year = age_data['age']

    return render_template('index.html', person_name=name, gender=gender, year=year)
    


if __name__ == '__main__':
    app.run(debug=True)