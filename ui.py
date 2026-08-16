import tkinter as tk
from tkinter import messagebox

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

def login():
    username = login_username.get()
    password = login_password.get()

    if username == "" or password == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def register():
    username = register_username.get()
    password = register_password.get()
    confirm = register_confirm.get()

    if username == "" or password == "" or confirm == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    if username in users:
        messagebox.showerror("Registration Failed", "Username already exists.")
        return

    if password != confirm:
        messagebox.showerror("Registration Failed", "Passwords do not match.")
        return

    users[username] = password

    messagebox.showinfo("Success", "Account created successfully!")

    # Clear fields
    register_username.delete(0, tk.END)
    register_password.delete(0, tk.END)
    register_confirm.delete(0, tk.END)

    show_login()

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

login_username = tk.Entry(login_frame, width=37, bg='#E3D9F2',  borderwidth=0,fg='#E3D9F2',insertbackground="#E3D9F2",font=("Arial", 10, "bold"))
login_username.grid(row=3, column=0, columnspan=2, pady=5,ipady=4)

tk.Label(login_frame, text="Password",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=4, column=0,sticky='w')

login_password = tk.Entry(
    login_frame,
    width=37,
    show="*",
    bg='#E3D9F2', 
    borderwidth=0,
    fg='#E3D9F2',
    insertbackground="#E3D9F2",
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
register_username = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_username.grid(row=2, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Name", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=1, column=1, sticky='w',padx=40)
register_name = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_name.grid(row=2, column=1, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Email ID", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=0, sticky='w',padx=40)
register_email = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_email.grid(row=4, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Date of Birth(YYYY-MM-DD)", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=3, column=1, sticky='w',padx=40)
register_dob = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_dob.grid(row=4, column=1, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Phone Number", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=0, sticky='w',padx=40)
register_phone = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_phone.grid(row=6, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Address", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=5, column=1, sticky='w',padx=40)
register_dob = tk.Entry(register_frame, width=37, bg='#E3D9F2', borderwidth=0, fg='#1b1c1f', insertbackground="#E3D9F2", font=("Arial", 10, "bold"))
register_dob.grid(row=6, column=1, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=0,  sticky='w',padx=40)
register_password = tk.Entry(register_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#E3D9F2",font=("Arial", 10, "bold"),)
register_password.grid(row=8, column=0, pady=5, ipady=4,padx=40)

tk.Label(register_frame, text="Confirm Password", bg='#043565', fg='#E3D9F2', font=("Century Gothic", 10, "bold"), anchor='w').grid(row=7, column=1, sticky='w',padx=40)
register_confirm = tk.Entry(register_frame,width=37,show="*",bg='#E3D9F2',borderwidth=0,fg='#1b1c1f',insertbackground="#E3D9F2",font=("Arial", 10, "bold"),)
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

admin_login_username = tk.Entry(admin_login_frame, width=37, bg='#E3D9F2',  borderwidth=0,fg='#1b1c1f',insertbackground="#E3D9F2",font=("Arial", 10, "bold"))
admin_login_username.grid(row=2, column=0, columnspan=2, pady=5,ipady=4,sticky='w')

tk.Label(admin_login_frame, text="Password",bg='#043565',fg='#E3D9F2',font=("Century Gothic", 10, "bold"),anchor='w').grid(row=3, column=0,sticky='w')

admin_login_password = tk.Entry(admin_login_frame,width=37,show="*",bg='#E3D9F2', borderwidth=0,fg='#1b1c1f',insertbackground="#E3D9F2",font=("Arial", 10, "bold"))
admin_login_password.grid(row=4, column=0, columnspan=2, pady=(5,20),ipady=4,stick='w')

tk.Button(
    admin_login_frame,
    text="Login",
    width=12,
    command=login,                               #Change to admin login
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









# Start with Login screen
frame_border = tk.Frame(root,borderwidth=0,relief="groove",bg='#043565')
frame_border.place(height=500,width=400,relx=0.5, rely=0.45,anchor="center")
login_frame.place(relx=0.5, rely=0.43, anchor="center")
login_frame.tkraise()




root.configure(bg='#00305e')    
root.mainloop()