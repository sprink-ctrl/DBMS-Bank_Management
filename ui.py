import tkinter as tk
from tkinter import messagebox
import mysql.connector
import csv
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234',
    database='bank_dbms'
)

crsr = db.cursor()

# -------------------------
# Main Window
# -------------------------

root = tk.Tk()
root.title("Login System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")


users = {}


# -------------------------
# Functions
# -------------------------
#region show_frame
def show_login():
    register_frame.place_forget()
    frame_border.place_forget()
    frame_border.place(height=400,width=350,relx=0.5, rely=0.45,anchor="center")
    login_frame.place(relx=0.5, rely=0.43, anchor="center")
    login_frame.tkraise()



def show_register():
    frame_border.place_forget()
    login_frame.place_forget()
    
    register_frame.place(relx=0.5, rely=0.43, anchor="center")
    frame_border.place(height=500,width=1000,relx=0.5, rely=0.45,anchor="center")
    register_frame.tkraise()


def show_adminlogin():
    frame_border.place_forget()
    login_frame.place_forget()
    admin_login_frame.place(relx=0.5, rely=0.43, anchor="center")
    frame_border.place(height=400,width=350,relx=0.5, rely=0.45,anchor="center")
    admin_login_frame.tkraise()
#endregion


#region input_fields
def login():
    username = login_username.get()
    password = login_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    crsr.execute('select username from users')
    user_records = crsr.fetchall()
    if (username,) in user_records:
        crsr.execute('Select password from users')
        pass_records = crsr.fetchall()
        if (password,) in pass_records:
            login_username.delete(0,tk.END)
            login_password.delete(0,tk.END)
            show_dashboard()
            return

        else:
            messagebox.showwarning('',"Incorrect Password")
    else:
        messagebox.showwarning('',"Invalid Username")

def login_successful():
    print("VALID")


def check_username_validity(event):
    print("check")
    crsr.execute('select username from users')
    user_records = crsr.fetchall()
    username = register_username.get()
    if (username,) in user_records:
        messagebox.showwarning('',"Username already exists.")
        return False
    else:
        return True


def register():
    print(1)
    a = check_username_validity('')
    if a ==True:
        print(2)
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
                print(3)
                if password==confirm:
                    if len(phone)==10 and phone.isdigit():
                        print(4)
                        crsr.execute( f"INSERT INTO users VALUES ('{username}','{name}','{email}','{phone}','{address}','{dob}','{password}',CURRENT_TIMESTAMP)")
                        messagebox.showinfo("Success", "Account created successfully!")
                        db.commit()
                        show_login()
                    else:
                        messagebox.showwarning('',"Invalid Phone Number")
                else:
                    messagebox.showwarning('',"Passwords do not match")
                    print(5)
            else:
                messagebox.showwarning('',"Fields cannot be empty")
                print(6)
        except 'get_mysql_exception':
            messagebox.showwarning('',"Something went wrong. Try checking date format")
    if a==False:
        print(7)
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
    

def admin_login():
    username = admin_login_username.get()
    password = admin_login_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    crsr.execute('select admin_name from admin')
    user_records = crsr.fetchall()
    if (username,) in user_records:
        crsr.execute('Select password from admin')
        pass_records = crsr.fetchall()
        if (password,) in pass_records:
            admin_login_username.delete(0,tk.END)
            admin_login_password.delete(0,tk.END)
            admin_login_successful()
            return

        else:
            messagebox.showwarning('',"Incorrect Password")
    else:
        messagebox.showwarning('',"Invalid Username")

def admin_login_successful():
    print("VALID")














#endregion





#region Login
# -------------------------
# Login Frame
# -------------------------

login_frame = tk.Frame(root,bg='#043565',borderwidth=0,relief="groove")
tk.Label(
    login_frame,
    text="Welcome back.",
    font=("Trebuchet MS", 22, "bold"),
    bg='#043565',
    fg='#86ADE5',
    anchor='w'
).grid(row=0, column=0, columnspan=2, pady=(0,5),sticky='w')


tk.Label(
    login_frame,
    text="Log in",
    font=("Trebuchet MS", 16, "bold"),
    bg='#043565',
    fg='#E3D9F2',
    anchor='w'
).grid(row=1, column=0, columnspan=2, pady=(5,20),sticky='w')



tk.Label(login_frame, text="Username",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=2, column=0,sticky='w')

login_username = tk.Entry(login_frame, width=37, bg='#E3D9F2',  borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"))
login_username.grid(row=3, column=0, columnspan=2, pady=5,ipady=4)

tk.Label(login_frame, text="Password",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=4, column=0,sticky='w')

login_password = tk.Entry(
    login_frame,
    width=37,
    show="*",
    bg='#E3D9F2', 
    borderwidth=0,
    fg='#1b1c1f',
    insertbackground="#000000",
    font=("Arial", 10, "bold"),
)
login_password.grid(row=5, column=0, columnspan=2, pady=5,ipady=4)

tk.Button(
    login_frame,
    text="Login",
    width=20,
    command=login,
    bg='#E3D9F2', 
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',  
    borderwidth=0, 
    
    
).grid(row=6, column=0, columnspan=2, pady=30)

tk.Button(
    login_frame,
    text="Create Account",
    command=show_register,
    bg='#E3D9F2', 
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',  
    borderwidth=0 
    ).grid(row=7, column=0, padx=5)

tk.Button(
    login_frame,
    text="Admin Login",
    bg='#E3D9F2', 
    font=("Century Gothic", 10, "bold"),
    height=1,
    width=12,
    fg='#000000',
    relief='solid',  
    borderwidth=0,
    command=show_adminlogin

    
).grid(row=7, column=1, padx=5)
#endregion

#region Register_frame

# -------------------------
# Register Frame
# -------------------------

register_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")

tk.Label(
    register_frame,
    text="    Register",
    font=("Trebuchet MS", 25, "bold"),
    bg='#043565',
    fg='#E3D9F2',
    
).grid(row=0, column=0, pady=(20,30),sticky='w')




tk.Label(register_frame, text="Username", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=1, column=0, sticky='w',padx=40)
register_username = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_username.grid(row=2, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Name", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=1, column=1, sticky='w',padx=40)
register_name = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_name.grid(row=2, column=1, pady=5, ipady=4,padx=40)
register_name.bind("<Button-1>",check_username_validity)

tk.Label(register_frame, text="Email ID", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=0, sticky='w',padx=40)
register_email = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_email.grid(row=4, column=0, pady=5, ipady=4,padx=40)
register_email.bind("<Button-1>",check_username_validity)

tk.Label(register_frame, text="Date of Birth(YYYY-MM-DD)", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=1, sticky='w',padx=40)
register_dob = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_dob.grid(row=4, column=1, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Phone Number", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=0, sticky='w',padx=40)
register_phone = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_phone.grid(row=6, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Address", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=1, sticky='w',padx=40)
register_address = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
register_address.grid(row=6, column=1, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=0,  sticky='w',padx=40)
register_password = tk.Entry(register_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"),)
register_password.grid(row=8, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Confirm Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=1, sticky='w',padx=40)
register_confirm = tk.Entry(register_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"),)
register_confirm.grid(row=8, column=1, pady=5, ipady=4,padx=40)

tk.Button(
    register_frame,
    text="Register",
    width=20,
    command=register,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
).grid(row=9, column=0,  pady=15)

tk.Button(
    register_frame,
    text="Back to Login",
    command=show_login,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
    width=20
).grid(row=9, column=1, pady=15)
#endregion


#region ADMIN_LOGIN 
# -------------------------
# ADMIN-Login Frame
# -------------------------

admin_login_frame = tk.Frame(root,bg='#043565',borderwidth=0,relief="groove")

tk.Label(
    admin_login_frame,
    text="Admin Login",
    font=("Trebuchet MS", 22, "bold"),
    bg='#043565',
    fg='#E3D9F2',
    anchor='w'
).grid(row=0, column=0, columnspan=2, pady=(0,40),sticky='w')

tk.Label(admin_login_frame, text="Username",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=1, column=0,sticky='w')

admin_login_username = tk.Entry(admin_login_frame, width=37, bg='#E3D9F2',  borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"))
admin_login_username.grid(row=2, column=0, columnspan=2, pady=5,ipady=4,sticky='w')

tk.Label(admin_login_frame, text="Password",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=3, column=0,sticky='w')

admin_login_password = tk.Entry(admin_login_frame,width=37,show="*",bg='#E3D9F2', borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"))
admin_login_password.grid(row=4, column=0, columnspan=2, pady=(5,20),ipady=4,stick='w')

tk.Button(
    admin_login_frame,
    text="Login",
    width=12,
    command=admin_login,                              
    bg='#E3D9F2', 
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',  
    borderwidth=0, 
    
).grid(row=5, column=0,  pady=15)




tk.Button(
    admin_login_frame,
    text="Back to Login",
    command=show_login,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
    width=12
).grid(row=5, column=1, pady=15)





 #endregion 

def show_dashboard():
    frame_border.place_forget()
    login_frame.place_forget()
    navbar.place(relwidth=1,)
    navbar.tkraise()



# NAVIGATION FRAME
navbar = tk.Frame(root, bg="#043565", height=60)
tk.Button(
    navbar,
    text="Manga Bank🥭",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w'
).grid(row=0, column=0,  pady=15,sticky='w',padx=10)

tk.Button(
    navbar,
    text="Accounts🧾",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w'
).grid(row=0, column=1,  pady=15,sticky='w',padx=5)

tk.Button(
    navbar,
    text="Banking💵",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w'
).grid(row=0, column=2,  pady=15,sticky='w',padx=5)

tk.Button(
    navbar,
    text="Transactions💲",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w'
).grid(row=0, column=3,  pady=15,sticky='w',padx=5)

tk.Button(
    navbar,
    text="Analytics📈",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w'
).grid(row=0, column=4,  pady=15,sticky='w',padx=5)































# region mainloop





# Start with Login screen
frame_border = tk.Frame(root,borderwidth=0,relief="groove",bg='#043565')
frame_border.place(height=500,width=400,relx=0.5, rely=0.45,anchor="center")
login_frame.place(relx=0.5, rely=0.43, anchor="center")
login_frame.tkraise()




root.configure(bg='#00305e')    
root.mainloop()
#endregion

#043565 -> frame border