import mysql.connector
from tkinter import messagebox
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234',
    database='bank_dbms'
)

crsr = db.cursor()

def initialize(user):
    db.commit()
    global user_table,accounts_table,transactions_table
    crsr.execute(f"SELECT * from users where username='{user}'")
    user_table = crsr.fetchall()[0]
    crsr.execute(f"SELECT * from accounts where username='{user}'")
    accounts_table = crsr.fetchall()[0]
    crsr.execute(f"SELECT * from transactions where username='{user}' ORDER BY timestamp DESC")
    transactions_table = crsr.fetchall()



    
def apply_filter(from_date_transact_filter,to_date_transact_filter,max_amt_transact_filter,min_amt_transact_filter,transaction_type,tree):
    db.commit()
    from_date = from_date_transact_filter.get()
    to_date = to_date_transact_filter.get()
    min_amt=min_amt_transact_filter.get()
    max_amt= max_amt_transact_filter.get()
    type = transaction_type.get()
    query = f'Select * from transactions where username = "{user_table[0]}" AND'
    try:
        if from_date!='':
            query=query+f' timestamp>"{from_date} 00:00:00" AND'
        if to_date!='':
            query=query+f' timestamp<"{to_date} 23:59:59" AND'
        if min_amt!='':
            query=query+f' amount>{min_amt} AND'
        if max_amt!='':
            query=query+f' amount<{max_amt} AND'
        if type not in ['All','']:
            query=query+f' transaction_type="{type}" AND'
        if query.endswith('AND'):
            query = query[:-3]
        query = query+' ORDER BY timestamp DESC'

        for row in tree.get_children():
                    tree.delete(row)
        


        a = crsr.execute(query)
        b = crsr.fetchall()
        for i in b:
                transact_data = (i[9],i[8],i[2],i[3],i[5],i[6],i[4])
                tree.insert(
                    "",
                    "end",
                    values=transact_data
                )


        


    except:
        messagebox.showwarning('',"Something went wrong")


        







    

    
