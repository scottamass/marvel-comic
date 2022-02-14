from flask import Flask, render_template,url_for,request
from main import *
app = Flask(__name__)

@app.route('/')
def index():
    out= get_heros()
    return render_template('index.html', heros=out )

@app.route('/search',methods=['POST'])
def search():
   if request.method =='POST': 
    search=request.form.get('hero')
    out= search_hero(search)
    return render_template('index.html', heros=out, search=search )  


@app.route('/hero/<id>')
def display(id):
    out= display_hero(id)
    comics = get_comics(id)
    for i in out:
        print(i['name'])
       
    return render_template('results.html',out=out,comics=comics )

    
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)