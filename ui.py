import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import user_data
import auth
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='1234',
    database='bank_dbms'
)
user = None
name =None
crsr = db.cursor()

# -------------------------
# Main Window
# -------------------------

root = tk.Tk()
root.title("Manga Bank")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")


users = {}


# -------------------------
# Functions
# -------------------------
#region show_frame
def show_dashboard():
    welcome_message_widget()
    balance_widget_dashboard()
    transact_widget_dashboard()
    for widget in root.winfo_children():
            if widget.winfo_class() == 'Frame':
                widget.place_forget()
    navbar.place(relwidth=1,)
    welcome_message.place(relwidth=0.7,rely=0.12,relx=0.2)
    balance_dashboard_widget.place(relwidth=0.2,rely=0.33,relx=0.2)
    transaction_dashboard_widget.place(relwidth=0.35,rely=0.55,relx=0.2)
    navbar.tkraise()


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

def show_accounts():
    accounts_page()
    for widget in root.winfo_children():

        widget.place_forget()
    navbar.place(relwidth=1)
    profile_account.place(relwidth=0.3,rely=0.13,relx=0.02,relheight=0.78)
    account_profile.place(relwidth=0.65,rely=0.13,relx=0.33,relheight=0.3)
    account_details.place(relwidth=0.65,rely=0.47,relx=0.33,relheight=0.29)
    edit_account.place(relwidth=0.65,rely=0.768,relx=0.33,relheight=0.12)
    profile_account.tkraise()


def show_transactions():
    transactions_page()
    for widget in root.winfo_children():
        widget.place_forget()
    navbar.place(relwidth=1)
    account_profile_transactions.place(relwidth=0.16,rely=0.13,relx=0.00,relheight=0.37)
    transactions_page_frame.place(relwidth=0.8,rely=0.13,relx=0.2,relheight=0.78)
    transacations_page_filter_frame.place(relwidth=0.16,rely=0.501,relx=0.00,relheight=0.78)
    

def admin_login_successful():
    print("VALID")

def banking_fn():
    banking.show_banking()

def show_edit_details():
    for widget in root.winfo_children():
            if widget.winfo_class() == 'Frame':
                widget.place_forget()
    edit_widget()
    edit_account_frame.place(relx=0.5, rely=0.43, anchor="center")
    frame_border.place(height=500,width=1000,relx=0.5, rely=0.45,anchor="center")
    edit_account_frame.tkraise()

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
def login():
    auth.login(login_username,login_password)


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


def check_username_validity(event):
    auth.check_username_validity(register_username)

def check_username_validity_editing(event):
    auth.check_username_validity_editing(register_username)

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

def register():
    auth.register(register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm)



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


def admin_login():
    auth.admin_login(admin_login_username,admin_login_password)
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

#region welcome_mesage_dashboard

welcome_message = tk.Frame(root, bg="#0a2d56", height=300,width=400)


def welcome_message_widget():
    tk.Label(
        welcome_message,
        text=f'Welcome Back, {user_data.user_table[1].split()[0]}!',
        font=("Trebuchet MS", 32, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=0,column=0,padx=10,pady=(10,0))

    tk.Label(
            welcome_message,
            text='Your financial overview at a glance.',
            font=("Trebuchet MS", 12, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=1,column=0,padx=10,sticky='w',pady=(0,30))

#endregion
#region balance_dashboard_widget
balance_dashboard_widget = tk.Frame(root, bg="#0a2d56", height=300,width=100)
def balance_widget_dashboard():
    
    tk.Label(
        balance_dashboard_widget,
        text='Total Balance',
        font=("Trebuchet MS", 16, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=0,column=0,padx=10,pady=(10,5),sticky='w')

    tk.Label(
            balance_dashboard_widget,
            text=f'₹ {user_data.accounts_table[3]}',
            font=("Trebuchet MS", 26, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=1,column=0,padx=10,sticky='w',pady=(0,30))

    
#endregion

#region transaction_dashboard_widget
    
transaction_dashboard_widget = tk.Frame(root, bg="#0a2d56", height=300,width=100)
def transact_widget_dashboard():
    
    
    tk.Label(
        transaction_dashboard_widget,
        text='Recent Transactions ',
        font=("Trebuchet MS", 16, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=0,column=0,padx=10,pady=(10,5),sticky='w')

    tk.Label(
            transaction_dashboard_widget,
            text='Transaction 1',
            font=("Trebuchet MS", 26, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=1,column=0,padx=10,sticky='w',pady=(0,30))
    tk.Label(
            transaction_dashboard_widget,
            text='Transaction 2',
            font=("Trebuchet MS", 16, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=2,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
            transaction_dashboard_widget,
            text='Transaction 3',
            font=("Trebuchet MS", 16, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=3,column=0,padx=10,pady=(10,5),sticky='w')


#endregion


#region nav_frame
# NAVIGATION FRAME
navbar = tk.Frame(root, bg="#043565", height=60)
tk.Button(
    navbar,
    text="🥭Manga Bank         🏚️",
    width=20,
    command=show_dashboard,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w',
    activeforeground='#fdc132',
    activebackground='#043565'
).grid(row=0, column=0,  pady=15,sticky='w',padx=(0,32))

tk.Button(
    navbar,
    text="Accounts🧾",
    width=10,
    command=show_accounts,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w',
    activeforeground='#fdc132',
    activebackground='#043565'
).grid(row=0, column=1,  pady=15,sticky='w',padx=50)

tk.Button(
    navbar,
    text="Banking💵",
    width=10,
    command=banking_fn,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w',
    activeforeground='#fdc132',
    activebackground='#043565'
).grid(row=0, column=2,  pady=15,sticky='w',padx=50)

tk.Button(
    navbar,
    text="Transactions💲",
    width=13,
    command=show_transactions,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w',
    activeforeground='#fdc132',
    activebackground='#043565'
).grid(row=0, column=3,  pady=15,sticky='w',padx=50)

import analysis
tk.Button(
    navbar,
    text="Analytics📈",
    width=10,
    command=analysis.show_analysis,
    bg='#043565',
    font=("Century Gothic", 18, "bold"),
    fg='#E3D9F2',
    relief='solid',
    borderwidth=0,
    anchor='w',
    activeforeground='#fdc132',
    activebackground='#043565'
).grid(row=0, column=4,  pady=15,sticky='w',padx=50)


#endregion


profile_account = tk.Frame(root, bg="#0a2d56",)
account_profile = tk.Frame(root, bg="#0a2d56",)
account_details = tk.Frame(root, bg="#0a2d56",)
edit_account = tk.Frame(root, bg="#0a2d56",)

#region accounts_page
def accounts_page():
    for frame in (profile_account, account_profile, account_details, edit_account):
        for widget in frame.winfo_children():
            widget.destroy()

    tk.Label(
                profile_account,
                text='USER PROFILE',
                font=("Trebuchet MS", 15, "bold"),
                bg='#0a2d56',
                fg='#fdc132',
                anchor='center'
            ).grid(row=0,column=0,columnspan=2,padx=10,pady=(10,0),sticky='w')
    tk.Label(
            profile_account,
            text='🤵',
            font=("Trebuchet MS", 80, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=1,column=0,columnspan=2,padx=10,pady=(10,0),sticky='nsew')

    tk.Label(
            profile_account,
            text=f'{user_data.user_table[1]}',
            font=("Trebuchet MS", 24, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=2,column=0,columnspan=2,padx=10,pady=(5,5),sticky='nsew')

    tk.Label(
                profile_account,
                text=f'Username:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=3,column=0,padx=10,pady=(10,5),sticky='nw')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[0]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=3,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'Phone:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=4,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[3]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=4,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'Email:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=5,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[2]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=5,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'Date of Birth:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=6,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[5]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=6,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'Address:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=7,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[4].split(',')[0]}\n{user_data.user_table[4].split(',')[1]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=7,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'Account Since:',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=8,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account,
                text=f'{user_data.user_table[7]}',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=8,column=1,padx=10,pady=(10,5),sticky='w')


    #####################################################################################\
    
    tk.Label(
                account_profile,
                text=f'ACCOUNT PROFILE',
                font=("Trebuchet MS", 15, "bold"),
                bg='#0a2d56',
                fg='#fdc132',
                anchor='center'
            ).grid(row=0,column=0,padx=10,pady=(10,5),sticky='w')
    
    tk.Label(
                account_profile,
                text=f'🏦{user_data.accounts_table[2].capitalize()} Account',
                font=("Trebuchet MS", 32, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=1,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                account_profile,
                text=f'{user_data.accounts_table[1]}',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=2,column=0,padx=10,pady=(10,0),sticky='w')

    if user_data.accounts_table[4] == 'ACTIVE':
        color_status='#00FF00'
    else:
        color_status='#FF7F7F'
    tk.Label(
                    account_profile,
                    text=f'{user_data.accounts_table[4]}',
                    font=("Trebuchet MS", 8, "bold"),
                    bg='#0a2d56',
                    fg=color_status,
                    anchor='center'
                ).grid(row=3,column=0,padx=10,pady=(0,5),sticky='w')

    tk.Label(
                account_profile,
                text=f'Available Balance',
                font=("Trebuchet MS", 15, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='e'
            ).grid(row=1,column=1,padx=(200,0),pady=(5,5),sticky='e')
    tk.Label(
                    account_profile,
                    text=f'₹{user_data.accounts_table[3]}',
                    font=("Trebuchet MS", 24, "bold"),
                    bg='#0a2d56',
                    fg='#00FF00',
                    anchor='e'
                ).grid(row=2,column=1,padx=(200,0),pady=(5,5),sticky='e')
    


###################################################


    tk.Label(
                    account_details,
                    text=f'Account No:',
                    font=("Trebuchet MS", 14, "bold"),
                    bg='#0a2d56',
                    fg='#E3D9F2',
                    anchor='w'
                ).grid(row=0,column=0,padx=(10,40),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.accounts_table[1]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=0,column=1,padx=(40,10),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'Account Type:',
                        font=("Trebuchet MS", 14, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=1,column=0,padx=(10,40),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.accounts_table[2]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=1,column=1,padx=(40,10),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'Account Holder:',
                        font=("Trebuchet MS", 14, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=2,column=0,padx=(10,40),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.user_table[1]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=2,column=1,padx=(40,10),pady=(10,5),sticky='w')

    tk.Label(
                        account_details,
                        text=f'IFSC Code:',
                        font=("Trebuchet MS", 14, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=0,column=3,padx=40,pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.accounts_table[7]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=0,column=4,padx=(40,0),pady=(10,5),sticky='w')

    tk.Label(
                        account_details,
                        text=f'Branch:',
                        font=("Trebuchet MS", 14, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=1,column=3,padx=(40,0),pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.accounts_table[6]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=1,column=4,padx=40,pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'Account Status:',
                        font=("Trebuchet MS", 14, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=2,column=3,padx=40,pady=(10,5),sticky='w')
    tk.Label(
                        account_details,
                        text=f'{user_data.accounts_table[4]}',
                        font=("Trebuchet MS", 10, "bold"),
                        bg='#0a2d56',
                        fg='#E3D9F2',
                        anchor='w'
                    ).grid(row=2,column=4,padx=(40,0),pady=(10,5),sticky='w')


    #################################
    
    tk.Button(
                edit_account,
                text="Edit Account ✍️",
                width=15,
                command=show_edit_details,
                bg='#0a2d56', 
                font=("Century Gothic", 20, "bold"),
                fg='#fdc132',
                relief='solid',  
                borderwidth=0,
                anchor='center' 
            ).grid(row=0, column=2,columnspan=4,pady=35,sticky='nsew',padx=12)
edit_account_frame = tk.Frame(root, bg="#0a2d56",)



def edit_widget():
    import user_data
    global register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm
    for widget in edit_account_frame.winfo_children():
        if widget.winfo_class() in ('Label', 'Entry'):
            widget.destroy()

    tk.Label(edit_account_frame, text="Username", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=1, column=0, sticky='w',padx=40)
    register_username = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_username.grid(row=2, column=0, pady=5, ipady=4,padx=40)
    register_username.insert(0, user_data.user_table[0])

    tk.Label(edit_account_frame, text="Name", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=1, column=1, sticky='w',padx=40)
    register_name = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_name.grid(row=2, column=1, pady=5, ipady=4,padx=40)
    register_name.bind("<Button-1>",check_username_validity_editing)
    register_name.insert(0, user_data.user_table[1])

    tk.Label(edit_account_frame, text="Email ID", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=0, sticky='w',padx=40)
    register_email = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_email.grid(row=4, column=0, pady=5, ipady=4,padx=40)
    register_email.bind("<Button-1>",check_username_validity_editing)
    register_email.insert(0, user_data.user_table[2])

    tk.Label(edit_account_frame, text="Date of Birth(YYYY-MM-DD)", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=1, sticky='w',padx=40)
    register_dob = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_dob.grid(row=4, column=1, pady=5, ipady=4,padx=40)
    register_dob.insert(0, user_data.user_table[5])

    tk.Label(edit_account_frame, text="Phone Number", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=0, sticky='w',padx=40)
    register_phone = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_phone.grid(row=6, column=0, pady=5, ipady=4,padx=40)
    register_phone.insert(0, user_data.user_table[3])

    tk.Label(edit_account_frame, text="Address", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=1, sticky='w',padx=40)
    register_address = tk.Entry(edit_account_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#000000", font=("Arial", 10, "bold"))
    register_address.grid(row=6, column=1, pady=5, ipady=4,padx=40)
    register_address.insert(0, user_data.user_table[4])


    tk.Label(edit_account_frame, text="Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=0,  sticky='w',padx=40)
    register_password = tk.Entry(edit_account_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"),)
    register_password.grid(row=8, column=0, pady=5, ipady=4,padx=40)
    register_password.insert(0, user_data.user_table[6])

    tk.Label(edit_account_frame, text="Confirm Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=1, sticky='w',padx=40)
    register_confirm = tk.Entry(edit_account_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#000000",font=("Arial", 10, "bold"),)
    register_confirm.grid(row=8, column=1, pady=5, ipady=4,padx=40)
    register_confirm.insert(0, user_data.user_table[6])

def edit_details():
    global register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm
    auth.edit_details(register_username,register_name,register_email,register_dob,register_phone,register_address,register_password,register_confirm)

tk.Button(
    edit_account_frame,
    text="Confirm Edit",
    width=20,
    command=edit_details,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
).grid(row=9, column=0,  pady=15)

tk.Button(
    edit_account_frame,
    text="Back to Accounts",
    command=show_accounts,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
    width=20
).grid(row=9, column=1, pady=15)


























#endregion accounts_page

account_profile_transactions= tk.Frame(root, bg="#0a2d56",)
transactions_page_frame = tk.Frame(root, bg="#0a2d56",)
transacations_page_filter_frame = tk.Frame(root, bg="#0a2d56",)
def transactions_page():
    global tree
    tk.Label(
                    account_profile_transactions,
                    text=f'ACCOUNT PROFILE',
                    font=("Trebuchet MS", 14, "bold"),
                    bg='#0a2d56',
                    fg='#fdc132',
                    anchor='center'
                ).grid(row=0,column=0,padx=10,pady=(10,5),sticky='w')
    
    tk.Label(
                account_profile_transactions,
                text=f'🏦{user_data.accounts_table[2].capitalize()} Account',
                font=("Trebuchet MS", 16, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=1,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                account_profile_transactions,
                text=f'{user_data.accounts_table[1]}',
                font=("Trebuchet MS", 10, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=2,column=0,padx=10,pady=(10,0),sticky='w')

    if user_data.accounts_table[4] == 'ACTIVE':
        color_status='#00FF00'
    else:
        color_status='#FF7F7F'
    tk.Label(
                    account_profile_transactions,
                    text=f'{user_data.accounts_table[4]}',
                    font=("Trebuchet MS", 8, "bold"),
                    bg='#0a2d56',
                    fg=color_status,
                    anchor='center'
                ).grid(row=3,column=0,padx=10,pady=(0,5),sticky='w')

    tk.Label(
                account_profile_transactions,
                text=f'Available Balance',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=4,column=0,padx=10,pady=(5,5),sticky='w')
    tk.Label(
                    account_profile_transactions,
                    text=f'₹{user_data.accounts_table[3]}',
                    font=("Trebuchet MS", 16, "bold"),
                    bg='#0a2d56',
                    fg='#00FF00',
                    anchor='w'
                ).grid(row=5,column=0,padx=10,pady=(5,5),sticky='w')


    columns_ = (
        "timestamp",
        "description",
        "transaction_type",
        "amount",
        "from_account",
        "to_account",
        "balance_after"
    )

    tree = ttk.Treeview(
        transactions_page_frame,
        columns=columns_,
        show="headings"
        
    )
    tree.heading("transaction_type", text=" Type")
    tree.heading("amount", text="Amount")
    tree.heading("balance_after", text="Balance")
    tree.heading("from_account", text="From")
    tree.heading("to_account", text="To ")
    tree.heading("description", text="Description")
    tree.heading("timestamp", text="Time")



    tree.column("transaction_type", width=130, anchor="center")
    tree.column("amount", width=100, anchor="center")
    tree.column("balance_after", width=150, anchor="center")
    tree.column("from_account", width=130, anchor="center")
    tree.column("to_account", width=130, anchor="center")
    tree.column("description", width=190, anchor="center")
    tree.column("timestamp", width=150, anchor="center")

    vertical_scroll = ttk.Scrollbar(
        transactions_page_frame,
        orient="vertical",
        command=tree.yview
    )    

    tree.grid(row=0, column=0, sticky="nsew",)
    vertical_scroll.grid(row=0, column=1, sticky="ns")

    transactions_page_frame.rowconfigure(0, weight=1)
    transactions_page_frame.columnconfigure(0, weight=1)



    style = ttk.Style()
    style.theme_use('clam')

   
    style.configure("Treeview",
                    background='#0a2d56',      
                    foreground="#E3D9F2",        
                    fieldbackground='#0a2d56',
                    borderwidth=0,
                    font=("Trebuchet MS", 12),
                    relief="flat",
                    rowheight=35) 


    style.configure("Treeview.Heading",
                    background='#0a2d56',      
                    foreground="#fdc132",
                    font=("Trebuchet MS", 14, "bold"),
                    borderwidth=0,
                    relief="flat"
                    )      


    for i in user_data.transactions_table:
        transact_data = (i[9],i[8],i[2],i[3],i[5],i[6],i[4])
        tree.insert(
            "",
            "end",
            values=transact_data
        )


    ################################## FILTERS #########################################
    global from_date_transact_filter, to_date_transact_filter,min_amt_transact_filter, max_amt_transact_filter,transaction_type
    tk.Label(
            transacations_page_filter_frame,
            text=f'Filters',
            font=("Trebuchet MS", 14, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=0,column=0,padx=10,pady=5,sticky='w')

    tk.Button(
            transacations_page_filter_frame,
            text="Reset",
            width=10,
            command=reset_filters_transact,
            bg='#0a2d56', 
            font=("Century Gothic", 10, "bold"),
            fg='#fdc132',
            relief='solid',  
            borderwidth=1, 
        ).grid(row=0, column=1,pady=5,sticky='w',padx=10)

    tk.Label(
                transacations_page_filter_frame,
                text=f'Date Range',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=1,column=0,padx=10,pady=5,sticky='w',columnspan=2)
    
    from_date_transact_filter = tk.Entry(
        transacations_page_filter_frame,
        width=12,
        bg='#E3D9F2', 
        borderwidth=0,
        fg='#1b1c1f',
        insertbackground="#000000",
        font=("Arial", 10, "bold"),
    )
    from_date_transact_filter.grid(row=2,column=0,padx=10,pady=5,sticky='w')

    to_date_transact_filter = tk.Entry(
            transacations_page_filter_frame,
            width=12,
            bg='#E3D9F2', 
            borderwidth=0,
            fg='#1b1c1f',
            insertbackground="#000000",
            font=("Arial", 10, "bold"),
        )
    to_date_transact_filter.grid(row=2,column=1,padx=10,pady=5,sticky='w')

    tk.Label(
                    transacations_page_filter_frame,
                    text=f'Transaction Type',
                    font=("Trebuchet MS", 12, "bold"),
                    bg='#0a2d56',
                    fg='#E3D9F2',
                    anchor='center'
                ).grid(row=3,column=0,padx=10,pady=5,sticky='w',columnspan=2)

    transaction_type = ttk.Combobox(
        transacations_page_filter_frame,
        values=["All", "Deposit", "Withdraw", "Credit","Debit"],
        state="readonly"
            )
    transaction_type.grid(row=4,column=0,padx=10,pady=5,sticky='w',columnspan=2)


    tk.Label(
            transacations_page_filter_frame,
            text=f'Amount Range ',
            font=("Trebuchet MS", 12, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=5,column=0,padx=10,pady=5,sticky='w',columnspan=2)
        
    min_amt_transact_filter = tk.Entry(
        transacations_page_filter_frame,
        width=12,
        
        bg='#E3D9F2', 
        borderwidth=0,
        fg='#1b1c1f',
        insertbackground="#000000",
        font=("Arial", 10, "bold"),
    )
    min_amt_transact_filter.grid(row=6,column=0,padx=10,pady=5,sticky='w')

    max_amt_transact_filter = tk.Entry(
            transacations_page_filter_frame,
            width=12,
            
            bg='#E3D9F2', 
            borderwidth=0,
            fg='#1b1c1f',
            insertbackground="#000000",
            font=("Arial", 10, "bold"),
        )
    max_amt_transact_filter.grid(row=6,column=1,padx=10,pady=5,sticky='w')

    tk.Button(
                transacations_page_filter_frame,
                text="Apply Filters",
                width=10,
                command=apply_filter,
                bg='#0a2d56', 
                font=("Century Gothic", 18, "bold"),
                fg='#fdc132',
                relief='solid',  
                borderwidth=1, 
            ).grid(row=7, column=0,pady=5,sticky='w',padx=10,columnspan=2)


    
    
def apply_filter():
        user_data.apply_filter(from_date_transact_filter,to_date_transact_filter,max_amt_transact_filter,min_amt_transact_filter,transaction_type,tree)
    



    
























def reset_filters_transact():
    from_date_transact_filter.delete(0,tk.END)
    to_date_transact_filter.delete(0,tk.END)
    min_amt_transact_filter .delete(0,tk.END)
    max_amt_transact_filter.delete(0,tk.END)
    transaction_type.set('')



# region mainloop





# Start with Login screen
frame_border = tk.Frame(root,borderwidth=0,relief="groove",bg='#043565')
frame_border.place(height=500,width=400,relx=0.5, rely=0.45,anchor="center")
login_frame.place(relx=0.5, rely=0.43, anchor="center")
login_frame.tkraise()    

import banking


root.configure(bg='#00305e')    



def run():
    root.mainloop()
#endregion

#043565 -> frame border