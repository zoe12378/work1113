from flask import Flask, render_template, request
from datetime import datetime,timezone,timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411150765 黃昕柔的網頁</h1>"
    homepage += "<a href=/self>我的自我介紹</a><br>"
    homepage += "<a href=/mis>MIS相關工作</a><br>"
    return homepage


@app.route("/all")
def course():
    return "<h1>資管二B 411150765 黃昕柔的網頁</h1>"

@app.route("/self")
def self():
    return render_template("self.html")

@app.route("/mis")
def mis():
    return render_template("mis.html")



#if __name__ == "__main__":
#   app.run()