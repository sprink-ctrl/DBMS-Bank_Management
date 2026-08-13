import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234'
)

crsr = db.cursor()
a = [
    'CREATE DATABASE bank_dbms',
    'USE bank_dbms'
     ]
for i in a:
    try:
        crsr.execute(i)
    except:
        continue