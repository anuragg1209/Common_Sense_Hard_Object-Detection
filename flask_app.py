from flask import *
import pandas as pd
import os
from subprocess import Popen, PIPE

app=Flask(__name__)

PEOPLE_FOLDER = os.path.join('static', 'Images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def my_form():
    return render_template('search_page.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method=='POST':
        query = request.form['t']
        p0 = Popen(['python', 'main.py', '--image_search_term', f'{query}'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out0, err0 = p0.communicate()
        print(f"working0 with err {err0} and\n output {out0}")
        return render_template('home_page.html')

@app.route('/home_page')
def home_page():
     return render_template("home_page.html")

@app.route('/get_img')
def get_img():
    names=os.listdir('./static/Images/')
    return render_template("images.html", image_names = names[1:])

@app.route("/get_collocations")
def get_collocations():
        with open("tsv_files/collocations.tsv",'r') as f:
            data=pd.read_csv(f,sep='\t')
            data.columns=["Spatial Collocations","Count"]

        return render_template("collocation.html", name='Collocations Map', data=data)

@app.route("/get_index")
def get_index():
    with open("tsv_files/inverted_index.tsv", 'r') as file:
        data = pd.read_csv(file, sep='\t')
        data.columns = ["Spatial Collocations", "Img_ID"]
    return render_template("index.html", name='Inverted Index', data=data)

@app.route("/get_error_set")
def get_error_set():
    with open("error_set.tsv", 'r') as f:
        data = pd.read_csv(f,sep='\t')
        data.columns = ["Image_ID","Orig_Prediction","Disagreeing_csk"]
    return render_template("index.html", name='Error Set', data=data)

@app.route("/get_csk")
def get_csk():
    with open("F:/csk.csv",'r') as file:
        data=pd.read_csv(file)
    return render_template("index.html", name='Common Sense Knowledge Graph', data=data)

if __name__=="__main__":
    app.run(debug=True)
