import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234',
    database='bank_dbms'
)

crsr = db.cursor()

def initialize(user):
    global user_table,accounts_table,transactions_table
    crsr.execute(f"SELECT * from users where username='{user}'")
    user_table = crsr.fetchall()[0]
    crsr.execute(f"SELECT * from accounts where username='{user}'")
    accounts_table = crsr.fetchall()[0]
    crsr.execute(f"SELECT * from transactions where username='{user}'")
    transactions_table = crsr.fetchall()



    




    

    
