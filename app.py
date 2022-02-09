from flask import Flask, render_template,url_for
from main import *
app = Flask(__name__)

@app.route('/')
def index():
    out= get_heros()
    return render_template('index.html', heros=out )

app.run(host='0.0.0.0', port=81)