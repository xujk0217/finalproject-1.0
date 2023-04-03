from flask import Flask, render_template
from collect import bsbbc

app = Flask(__name__)

@app.route("/")
@app.route("/news")
def news():
    bbcbata=bsbbc()
    # return render_template('mainnews.html', bbcfnew=bbcbata[0], bbcsnew=bbcbata[1])
    return render_template('mainnews.html', bbcdata=bbcbata)



if __name__ == '__main__':
    app.run()
