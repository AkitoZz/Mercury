from flask import Flask,jsonify
from .auth import auth

app = Flask(__name__)

sources = [
    {
        "id" : 1,
        "title" : "zhihu",
        "description" : "zhihu vevryday",
        "url" : "https://www.zhihu.com/rss"
    },
    {
        "id" : 2,
        "title" : "songshuhui",
        "description" : "songshuhui sinence",
        "url" : "http://songshuhui.net/feed"
    }
]

@app.route("/rss/api/v1.0/sources",method = ["GET"])
def get_sources():
    return jsonify({"sources" : sources})

if __name__ == "__main__":
    app.run(debug=True)    