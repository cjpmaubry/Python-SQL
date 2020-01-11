import mysql.connector
from flask import Flask, render_template


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

if __name__ == "__main__":
    app.run(debug=True)


