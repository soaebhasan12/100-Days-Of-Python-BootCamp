from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1> ' \
    '<p> this is home page!' \
    '<br><img src="https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif" width="300">'

@app.route("/bye")
def bye():
    return "Goodbye, world!"


@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello there {name}, you are {age} years old!"


if __name__ == "__main__":
    app.run(debug=True)