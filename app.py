from flask import Flask, render_template
from collect import bsbbc
from collect import bswsj
from collect import bsyahoo
from collect import bsmappa
from collect import bsufo
from collect import bscw
from collect import bsuni

app = Flask(__name__)

@app.route("/")
def bbcnews():
    bbcbata=bsbbc()
    mappabata=bsmappa()
    yahoobata=bsyahoo()
    ufobata=bsufo()
    cwbata=bscw()
    wsjbata=bswsj()
    unibata=bsuni()
    # return render_template('mainnews.html', bbcfnew=bbcbata[0], bbcsnew=bbcbata[1])
    return render_template('mainnews.html', bbcdata=bbcbata, mappadata=mappabata, yahoodata=yahoobata, ufodata=ufobata, cwdata=cwbata, wsjdata=wsjbata, unidata=unibata)


if __name__ == '__main__':
    app.run()
