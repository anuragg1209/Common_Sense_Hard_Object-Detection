from flask import *
import pandas as pd
import main

app=Flask(__name__)

@app.route('/')
def my_form():
    return render_template('hello.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return main.invoke_scripts(text)


@app.route('/index')
def index():
     return render_template("index.html")

@app.route("/get_collocations")
def get_collocations():
        with open("tsv_files/collocations.tsv",'r') as f:
            data=pd.read_csv(f,sep='\t')
            data.columns=["Spatial Collocations","Count"]

        return render_template("analysis.html", name='collocations.tsv', data=data)

if __name__=="__main__":
    app.run(debug=True)

