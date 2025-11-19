from flask import Flask, render_template
from random import randint
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    random_nummber = randint(1, 111)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_nummber, year=year)


if __name__ == '__main__':
    app.run(debug=True)