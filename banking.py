import tkinter as tk
from tkinter import messagebox
from ui import root, db, crsr, navbar
import user_data

# -------------------------
# banking.py stays a separate file. 'root', 'db', 'crsr' and 'navbar' are
# imported from ui.py. 'user' and 'name' are accessed as user_data.user and
# user_data.name (looked up at the point of use, not imported directly),
# since login() in ui.py updates user_data.py only after banking.py has
# already been imported.
# -------------------------

# -------------------------
# Functions
# -------------------------

def show_banking():
    banking_left_widget()
    transfer_form_widget()

    for widget in root.winfo_children():
        if widget.winfo_class() == 'Frame':
            widget.place_forget()

    navbar.place(relwidth=1)
    profile_account_banking.place(relwidth=0.2, rely=0.13, relx=0.02, relheight=0.35)
    account_profile_banking.place(relwidth=0.2, rely=0.5, relx=0.02, relheight=0.4)
    transfer_frame.place(relwidth=0.4, rely=0.13, relx=0.3, relheight=0.78)

    navbar.tkraise()


def confirm_transfer():
    account_no = transfer_account_no.get()
    amount = transfer_amount.get()
    description = transfer_description.get()

    if account_no == "" or amount == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

    # PLACEHOLDER: SQL - check account_no exists in accounts table
    # crsr.execute(f'select account_no from accounts where account_no="{account_no}"')
    # records = crsr.fetchall()
    # if (account_no,) not in records:
    #     messagebox.showwarning('', "Account does not exist")
    #     return

    # PLACEHOLDER: SQL - verify account_no exists
    # crsr.execute(f'select account_no from accounts where account_no="{account_no}"')
    # target_records = crsr.fetchall()
    # if (account_no,) not in target_records:
    #     messagebox.showwarning('', "Account does not exist")
    #     return

    # PLACEHOLDER: SQL - fetch sender's account and balance
    # crsr.execute(f'select account_no, balance from accounts where username="{user_data.user}"')
    # sender_record = crsr.fetchall()[0]
    # sender_account_no = sender_record[0]
    # sender_balance = sender_record[1]

    # PLACEHOLDER: check sufficient balance
    # if float(amount) > sender_balance:
    #     messagebox.showwarning('', "Insufficient balance")
    #     return

    # PLACEHOLDER: SQL - deduct amount from sender's account
    # crsr.execute(f'update accounts set balance = balance - {float(amount)} where account_no="{sender_account_no}"')

    # PLACEHOLDER: SQL - add amount to receiver's account
    # crsr.execute(f'update accounts set balance = balance + {float(amount)} where account_no="{account_no}"')

    # PLACEHOLDER: SQL - insert transaction record(s) into transactions table
    # crsr.execute(f'insert into transactions (username, account_no, transaction_type, amount, from_account, to_account, description, timestamp) values ("{user_data.user}","{sender_account_no}","TRANSFER",{float(amount)},"{sender_account_no}","{account_no}","{description}",CURRENT_TIMESTAMP)')

    # PLACEHOLDER: db.commit()

    messagebox.showinfo("Success", "Transfer completed successfully!")

    transfer_account_no.delete(0, tk.END)
    transfer_amount.delete(0, tk.END)
    transfer_description.delete(0, tk.END)


# -------------------------
# Left Pane - Profile (subset)
# -------------------------

profile_account_banking = tk.Frame(root, bg="#0a2d56")
account_profile_banking = tk.Frame(root, bg="#0a2d56")


def banking_left_widget():
    # PLACEHOLDER: SQL - fetch user details
    # crsr.execute(f' SELECT * from users where username="{user_data.user}"')
    # a = crsr.fetchall()

    tk.Label(
        profile_account_banking,
        text='USER PROFILE',
        font=("Trebuchet MS", 15, "bold"),
        bg='#0a2d56',
        fg='#fdc132',
        anchor='center'
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='w')

    tk.Label(
        profile_account_banking,
        text='🤵',
        font=("Trebuchet MS", 60, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='center'
    ).grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='nsew')

    tk.Label(
        profile_account_banking,
        text=f'{user_data.user_table[1]}',
        font=("Trebuchet MS", 18, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='center'
    ).grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 5), sticky='nsew')

    tk.Label(
        profile_account_banking,
        text='Username:',
        font=("Trebuchet MS", 12, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='center'
    ).grid(row=3, column=0, padx=10, pady=(10, 5), sticky='w')

    tk.Label(
        profile_account_banking,
        text=f'{user_data.user_table[0]}',
        font=("Trebuchet MS", 12, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='center'
    ).grid(row=3, column=1, padx=10, pady=(10, 5), sticky='w')

    #####################################################################################

    # PLACEHOLDER: SQL - fetch account details
    # crsr.execute(f' SELECT * from accounts where username="{user_data.user}"')
    # a = crsr.fetchall()

    tk.Label(
        account_profile_banking,
        text='ACCOUNT PROFILE',
        font=("Trebuchet MS", 15, "bold"),
        bg='#0a2d56',
        fg='#fdc132',
        anchor='center'
    ).grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

    tk.Label(
        account_profile_banking,
        text='🏦Account Type',
        font=("Trebuchet MS", 16, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 5), sticky='w')

    tk.Label(
        account_profile_banking,
        text='Account Number',
        font=("Trebuchet MS", 10, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='w')

    tk.Label(
        account_profile_banking,
        text='Status',
        font=("Trebuchet MS", 8, "bold"),
        bg='#0a2d56',
        fg='#00FF00',
        anchor='w'
    ).grid(row=3, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='w')

    tk.Label(
        account_profile_banking,
        text='Available Balance',
        font=("Trebuchet MS", 12, "bold"),
        bg='#0a2d56',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='w')

    tk.Label(
        account_profile_banking,
        text='₹0.00',
        font=("Trebuchet MS", 20, "bold"),
        bg='#0a2d56',
        fg='#00FF00',
        anchor='w'
    ).grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 5), sticky='w')


# -------------------------
# Transfer Frame
# -------------------------

transfer_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")


def transfer_form_widget():
    pass


tk.Label(
    transfer_frame,
    text="Transfer Money",
    font=("Trebuchet MS", 22, "bold"),
    bg='#043565',
    fg='#E3D9F2',
    anchor='w'
).grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=20, sticky='w')

tk.Label(
    transfer_frame,
    text="Enter Account Number",
    bg='#043565',
    fg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    anchor='w'
).grid(row=1, column=0, columnspan=2, padx=20, sticky='w')

transfer_account_no = tk.Entry(
    transfer_frame,
    width=37,
    bg='#E3D9F2',
    borderwidth=0,
    fg='#1b1c1f',
    insertbackground="#000000",
    font=("Arial", 10, "bold")
)
transfer_account_no.grid(row=2, column=0, columnspan=2, pady=5, ipady=4, padx=20)

tk.Label(
    transfer_frame,
    text="Amount",
    bg='#043565',
    fg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    anchor='w'
).grid(row=3, column=0, columnspan=2, padx=20, pady=(15, 0), sticky='w')

transfer_amount = tk.Entry(
    transfer_frame,
    width=37,
    bg='#E3D9F2',
    borderwidth=0,
    fg='#1b1c1f',
    insertbackground="#000000",
    font=("Arial", 10, "bold")
)
transfer_amount.grid(row=4, column=0, columnspan=2, pady=5, ipady=4, padx=20)

tk.Label(
    transfer_frame,
    text="Description",
    bg='#043565',
    fg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    anchor='w'
).grid(row=5, column=0, columnspan=2, padx=20, pady=(15, 0), sticky='w')

transfer_description = tk.Entry(
    transfer_frame,
    width=37,
    bg='#E3D9F2',
    borderwidth=0,
    fg='#1b1c1f',
    insertbackground="#000000",
    font=("Arial", 10, "bold")
)
transfer_description.grid(row=6, column=0, columnspan=2, pady=5, ipady=4, padx=20)

tk.Button(
    transfer_frame,
    text="Confirm Transfer",
    width=30,
    command=confirm_transfer,
    bg='#fdc132',
    font=("Century Gothic", 12, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
).grid(row=7, column=0, columnspan=2, pady=30, padx=20)


# -------------------------
# In ui.py: add 'import banking' right before root.mainloop() (after navbar
# and all widgets are built), and point the navbar's "Banking💵" button's
# command to banking.show_banking instead of show_dashboard.
# -------------------------
