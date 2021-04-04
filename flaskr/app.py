import random

import pyoeis
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        seq = str(request.form["search"])
        try:
            rand = str(request.form["random"])
            ids = "A0000001"
            rand_id = str(random.randrange(1, 100000))
            ids = ids[:-len(rand_id)] + rand_id
            return redirect(url_for("sequence", seq_id=ids))
        except:
            pass
        return redirect(url_for("search", content=seq))
    return render_template("index.html")


@app.route("/search=<content>", methods=["GET", "POST"])
def search(content):
    if content == "":
        return redirect(url_for("home"))

    client = pyoeis.OEISClient()
    if request.method == "POST":
        try:
            seq_id = str(request.form["id"])
            return redirect(url_for("sequence", seq_id=seq_id))
        except:
            pass

        try:
            seq_id = str(request.form["name"])
            return redirect(url_for("sequence", seq_id=seq_id))
        except:
            pass

        try:
            seq = str(request.form["search"])
            return redirect(url_for("search", content=seq))
        except:
            pass

    else:
        integers = [int(i) for i in content.split()]
        lst = client.lookup_by_terms(integers)
        return render_template("search.html", seq=content, lst=lst)


@app.route("/sequence=<seq_id>", methods=["GET", "POST"])
def sequence(seq_id):
    if request.method == "POST":
        try:
            seq = str(request.form["search"])
            return redirect(url_for("search", content=seq))
        except:
            pass

    client = pyoeis.OEISClient()
    seq = client.get_by_id(seq_id)
    return render_template("sequence.html", sequence=seq)


if __name__ == '__main__':
    app.run()
