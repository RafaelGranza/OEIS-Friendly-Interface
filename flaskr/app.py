from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello!<h1>"

if __name__ == '__main__':
    app.run()
