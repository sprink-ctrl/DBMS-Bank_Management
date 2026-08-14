import mysql.connector
import csv
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234'
)

crsr = db.cursor()
a = [
    'CREATE DATABASE bank_dbms',
    'USE bank_dbms',
    'CREATE TABLE users( username VARCHAR(50) PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(100) UNIQUE NOT NULL, phone VARCHAR(10) UNIQUE NOT NULL, ADDRESS VARCHAR(200), dob DATE, password VARCHAR(100) NOT NULL, date_created DATETIME )',
    ' CREATE TABLE accounts( username VARCHAR(50), account_no VARCHAR(16) PRIMARY KEY, account_type VARCHAR(15) NOT NULL, balance DECIMAL(20,2) DEFAULT 0 , status varchar(12) DEFAULT "ACTIVE", date_created DATETIME, FOREIGN KEY(username) REFERENCES users(username) )',
    ' CREATE TABLE transactions (username VARCHAR(50), account_no VARCHAR(16) , transaction_type VARCHAR(15), amount DECIMAL(12,2) NOT NULL, balance_after DECIMAL(20,2), from_account VARCHAR(16), to_account VARCHAR(16), status VARCHAR(20) DEFAULT "SUCCESS", description VARCHAR(200), timestamp DATETIME, CONSTRAINT fk_user FOREIGN KEY (username) REFERENCES users(username), CONSTRAINT fk_account FOREIGN KEY (account_no) REFERENCES accounts(account_no) ) ' , 
    ' CREATE TABLE admin ( admin_name VARCHAR(50) PRIMARY KEY, password VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, phone VARCHAR(10) NOT NULL )'
     ]
for i in a:
    try:
        crsr.execute(i)
    except:
        continue






crsr.execute("SELECT * FROM users")    
if len(crsr.fetchall())==0: 
    f = open('users.csv', 'r', newline='')
    rdr = csv.reader(f)
    for i in rdr:   
        crsr.execute(f"INSERT INTO users VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}')")
    f.close()




crsr.execute("SELECT * FROM accounts")    
if len(crsr.fetchall())==0: 
    f = open('accounts.csv', 'r', newline='')
    rdr = csv.reader(f)
    for i in rdr:   
        crsr.execute(f"INSERT INTO accounts VALUES ('{i[0]}','{i[1]}','{i[2]}',{float(i[3])},'{i[4]}','{i[5]}')")
    f.close()



crsr.execute("SELECT * FROM transactions")    
if len(crsr.fetchall())==0: 
    f = open('transactions.csv', 'r', newline='')
    rdr = csv.reader(f)
    for i in rdr: 
        for j in range(len(i)):
            if j not in [3,4]:
                if i[j]!='':
                    i[j] = '\'' + i[j] + '\''
                else:
                    i[j] = 'NULL'
  
            
        crsr.execute(f"INSERT INTO transactions VALUES ({i[0]},{i[1]},{i[2]},{float(i[3])},{float(i[4])},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]})")
    f.close()




crsr.execute("SELECT * FROM admin")    
if len(crsr.fetchall())==0: 
    f = open('admin.csv', 'r', newline='')
    rdr = csv.reader(f)
    for i in rdr:   
        crsr.execute(f"INSERT INTO admin VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}')")
    f.close()




db.commit()