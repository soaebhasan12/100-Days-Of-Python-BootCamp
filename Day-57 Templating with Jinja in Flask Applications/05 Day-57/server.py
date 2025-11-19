from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)


@app.route('/home')
def home():
    random_nummber = randint(1, 111)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_nummber, year=year)


@app.route('/guess/<enter_your_name>')
def guess(enter_your_name):
    gender_url = f"https://api.genderize.io?name={enter_your_name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_url = f"https://api.agify.io?name={enter_your_name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    year = age_data['age']

    return render_template('namify.html', person_name=enter_your_name, gender=gender, year=year)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)