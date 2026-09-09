import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234',
    database='bank_dbms'
)


crsr = db.cursor()

def login(login_username,login_password):
    username = login_username.get()
    password = login_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    crsr.execute('select username from users')
    user_records = crsr.fetchall()
    if (username,) in user_records:
        crsr.execute(f'Select password from users where username = "{username}"')
        pass_records = crsr.fetchall()
        if (password,) in pass_records:
            login_username.delete(0,tk.END)
            login_password.delete(0,tk.END)

            import user_data
            user_data.initialize(username)
            import ui
            ui.show_dashboard()
            return

        else:
            messagebox.showwarning('',"Incorrect Password")
    else:
        messagebox.showwarning('',"Invalid Username")

def admin_login(admin_login_username,admin_login_password):
    username = admin_login_username.get()
    password = admin_login_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    crsr.execute('select admin_name from admin')
    user_records = crsr.fetchall()
    if (username,) in user_records:
        crsr.execute(f'Select password from admin where admin_name="{username}"')
        pass_records = crsr.fetchall()
        if (password,) in pass_records:
            admin_login_username.delete(0,tk.END)
            admin_login_password.delete(0,tk.END)
            import ui
            ui.admin_login_successful()
            return

        else:
            messagebox.showwarning('',"Incorrect Password")
    else:
        messagebox.showwarning('',"Invalid Username")



def check_username_validity(register_username):
    crsr.execute('select username from users')
    user_records = crsr.fetchall()
    username = register_username.get()
    if (username,) in user_records:
        messagebox.showwarning('',"Username already exists.")
        return False
    else:
        return True











def register(register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm):
    a = check_username_validity(register_username)
    if a ==True:
        username = register_username.get()
        name = register_name.get()
        email = register_email.get()
        phone = register_phone.get()
        address= register_address.get()
        dob = register_dob.get()
        password = register_password.get()
        confirm = register_confirm.get()
        try:
            if '' not in [username,name,email,dob,phone,address,password,confirm]:
                if password==confirm:
                    if len(phone)==10 and phone.isdigit():
                        crsr.execute( f"INSERT INTO users VALUES ('{username}','{name}','{email}','{phone}','{address}','{dob}','{password}',CURRENT_TIMESTAMP)")
                        messagebox.showinfo("Success", "Account created successfully!")
                        db.commit()
                        import ui
                        ui.show_login()
                    else:
                        messagebox.showwarning('',"Invalid Phone Number")
                else:
                    messagebox.showwarning('',"Passwords do not match")
            else:
                messagebox.showwarning('',"Fields cannot be empty")
        except:
            messagebox.showwarning('',"Something went wrong. Try checking date format")
    if a==False:
        messagebox.showwarning('',"Username already exists.")

    print(a,8)
    # Clear fields
    register_username.delete(0, tk.END)
    register_password.delete(0, tk.END)
    register_confirm.delete(0, tk.END)
    register_name.delete(0, tk.END)
    register_email.delete(0, tk.END)
    register_address.delete(0, tk.END)
    register_phone.delete(0, tk.END)
    register_dob.delete(0, tk.END)
    

def check_username_validity_editing(register_username):
    crsr.execute('select username from users')
    user_records = crsr.fetchall()
    username = register_username.get()
    import user_data
    if (username,) in user_records and username!=user_data.user_table[0]:
        messagebox.showwarning('',"Username already exists.")
        return False
    else:
        return True


def edit_details(register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm):
    a = check_username_validity_editing(register_username)
    if a ==True:
        username = register_username.get()
        name = register_name.get()
        email = register_email.get()
        phone = register_phone.get()
        address= register_address.get()
        dob = register_dob.get()
        password = register_password.get()
        confirm = register_confirm.get()
        try:
            if '' not in [username,name,email,dob,phone,address,password,confirm]:
                if password==confirm:
                    if len(phone)==10 and phone.isdigit():
                        import user_data
                        crsr.execute(f' UPDATE users SET username="{username}",name="{name}",email="{email}",phone="{phone}",address="{address}",dob="{dob}",password="{password}" WHERE username="{user_data.user_table[0]}"')

                        messagebox.showinfo("Success", "Account updated successfully!")
                        db.commit()
                        user_data.initialize(username)
                        import ui
                        ui.show_accounts()
                    else:
                        messagebox.showwarning('',"Invalid Phone Number")
                else:
                    messagebox.showwarning('',"Passwords do not match")
            else:
                messagebox.showwarning('',"Fields cannot be empty")
        except:
            messagebox.showwarning('',"Something went wrong. Try checking date format")
    if a==False:
        messagebox.showwarning('',"Username already exists.")

    print(a,8)
    # Clear fields
