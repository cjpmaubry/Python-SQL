import mysql.connector
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/display')
def display():

    mydb = mysql.connector.connect(user='root', password='esilvs6', database='voituredb')
    cursor = mydb.cursor()
    query = ('SELECT id, mark, model, maxspeed, consumption FROM voiture')
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    mydb.close()

    return render_template('display.html', data=data)


@app.route('/request')
def resquest():
    return render_template('request.html')


@app.route('/simplesearch')
def simplesearch():
    return render_template('simplesearch.html')

@app.route('/result', methods=['POST'])
def resultsimple():
    result = request.form
    data = choosequery(result)
    return render_template('result.html', data=data)


@app.route('/searchconsumption')
def searchconsumption():
    return render_template('searchconsumption.html')

@app.route('/resultconsumption', methods=['POST'])
def resultconsumption():
    result = request.form
    value1=result['val1']
    value2=result['val2']
    mydb = mysql.connector.connect(user='root', password='esilvs6', database='voituredb')
    cursor = mydb.cursor()
    query = ('SELECT id, mark, model, maxspeed, consumption FROM voiture WHERE consumption between '+value1+' and '+value2)
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('result.html', data=data)


@app.route('/searchspeed', methods=['GET', 'POST'])
def searchspeed():
    return render_template('searchspeed.html')

@app.route('/resultspeed', methods=['POST'])
def resultspeed():
    result = request.form
    value1=result['val1']
    value2=result['val2']
    mydb = mysql.connector.connect(user='root', password='esilvs6', database='voituredb')
    cursor = mydb.cursor()
    query = ('SELECT id, mark, model, maxspeed, consumption FROM voiture WHERE maxspeed between '+value1+' and '+value2)
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('result.html', data=data)



def choosequery(result):
    id = result['id']
    mark = result['mark']
    model = result['model']
    maxspeed = result['maxspeed']
    consumption = result['consumption']
    info = ''

    if(id != ''):
        info += ('id = '+ id +',')
    if (mark !=''):
        info += ('mark = \''+ mark +'\' ,')
    if(model!=''):
        info += ('model = \''+model+'\' ,')
    if(maxspeed!=''):
        info += ('maxspeed = '+maxspeed+',')
    if(consumption!=''):
        info += ('consumption = '+consumption+',')

    length=len(info)
    if(length != 0):
        line = info[0:length-1]
        info = ('WHERE '+line)

    mydb = mysql.connector.connect(user='root', password='esilvs6', database='voituredb')
    cursor = mydb.cursor()
    query = ('SELECT id, mark, model, maxspeed, consumption FROM voiture '+info)
    cursor.execute(query)
    data = cursor.fetchall()

    return data






if __name__ == "__main__":
    app.run(debug=True)


