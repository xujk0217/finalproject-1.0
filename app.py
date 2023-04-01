from flask import Flask, render_template
from collect import bs

app = Flask(__name__)

@app.route("/")
@app.route("/news")
def news():
    title=bs()
    return render_template('mainnews.html', title1=title[0])







if __name__ == '__main__':
    app.run()
