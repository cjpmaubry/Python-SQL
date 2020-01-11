import mysql.connector
from flask import Flask, render_template

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="esilvs6"
)

mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)
mycursor.close()
mydb.close()



cnx = mysql.connector.connect(user='root', password='esilvs6', database='voituredb')
cursor = cnx.cursor()

query = ('SELECT mark, model, maxspeed, consumption FROM voiture WHERE id=1')
cursor.execute(query)

for (mark, model, maxspeed, consumption) in cursor:
    print("The ID number 1 refers to  {} {}, max speed : {} km/h, consumption : {} l/100km".format(mark, model, maxspeed, consumption))

cursor.close()
cnx.close()



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/request')
def resquest():
    return render_template('request.html')

if __name__ == "__main__":
    app.run(debug=True)


