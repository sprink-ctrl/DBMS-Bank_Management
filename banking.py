import tkinter as tk
from tkinter import messagebox
from ui import root, db, crsr, navbar
import user_data



# -------------------------
# Functions
# -------------------------

def show_banking():
    banking_left_widget()
    recent_contacts_widget()
    

    for widget in root.winfo_children():
        if widget.winfo_class() == 'Frame':
            widget.place_forget()

    navbar.place(relwidth=1)
    profile_account_banking.place(relwidth=0.22,rely=0.13,relx=0.02,relheight=0.39)
    account_profile_banking.place(relwidth=0.22,rely=0.58,relx=0.02,relheight=0.39)
    transfer_frame.place(relwidth=0.30, rely=0.13, relx=0.3, relheight=0.78)
    recent_contacts_frame.place(relwidth=0.25, rely=0.13, relx=0.7, relheight=0.78)

    navbar.tkraise()


def confirm_transfer():
    account_no = transfer_account_no.get()
    amount = transfer_amount.get()
    description = transfer_description.get()

    if account_no == "" or amount == "":
        messagebox.showwarning("Missing Information", "Please enter all fields.")
        return

   
    crsr.execute(f'select account_no from accounts where account_no="{account_no}"')
    records = crsr.fetchall()
    if (account_no,) not in records:
        messagebox.showwarning('', "Account does not exist")
        return



    # PLACEHOLDER: check sufficient balance
    if float(amount) > user_data.accounts_table[3]:
        messagebox.showwarning('', "Insufficient balance")
        return

    # PLACEHOLDER: SQL - deduct amount from sender's account
    crsr.execute(f'update accounts set balance = balance - {float(amount)} where account_no="{user_data.accounts_table[1]}"')

    # PLACEHOLDER: SQL - add amount to receiver's account
    crsr.execute(f'update accounts set balance = balance + {float(amount)} where account_no="{account_no}"')
    a = user_data.accounts_table
    crsr.execute(f"SELECT * from accounts where account_no = {account_no}")
    b = crsr.fetchall()[0]
    # PLACEHOLDER: SQL - insert transaction record(s) into transactions table
    crsr.execute(f'insert into transactions values ("{a[0]}","{a[1]}","DEBIT",{float(amount)},{float(a[3])-float(amount)},"{a[1]}","{account_no}","SUCCESS","{description}",CURRENT_TIMESTAMP)')
    crsr.execute(f'insert into transactions values ("{b[0]}","{account_no}","CREDIT",{float(amount)},{float(b[3])+float(amount)},"{a[1]}","{account_no}","SUCCESS","{description}",CURRENT_TIMESTAMP)')
    db.commit()

    messagebox.showinfo("Success", "Transfer completed successfully!")

    transfer_account_no.delete(0, tk.END)
    transfer_amount.delete(0, tk.END)
    transfer_description.delete(0, tk.END)
    user_data.initialize(a[0])
    show_banking()


# -------------------------
# Left Pane - Profile (subset)
# -------------------------

profile_account_banking = tk.Frame(root, bg="#0a2d56")
account_profile_banking = tk.Frame(root, bg="#0a2d56")



def banking_left_widget():

    tk.Label(
                profile_account_banking,
                text='USER PROFILE',
                font=("Trebuchet MS", 13, "bold"),
                bg='#0a2d56',
                fg='#fdc132',
                anchor='center'
            ).grid(row=0,column=0,columnspan=2,padx=10,pady=(10,0),sticky='w')
    tk.Label(
            profile_account_banking,
            text='🤵',
            font=("Trebuchet MS", 40, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=1,column=0,columnspan=2,padx=10,pady=(10,0),sticky='nsew')

    tk.Label(
            profile_account_banking,
            text=f'{user_data.user_table[1]}',
            font=("Trebuchet MS", 20, "bold"),
            bg='#0a2d56',
            fg='#E3D9F2',
            anchor='center'
        ).grid(row=2,column=0,columnspan=2,padx=10,pady=(5,5),sticky='nsew')

    tk.Label(
                profile_account_banking,
                text=f'Username:',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=3,column=0,padx=10,pady=(10,5),sticky='nw')
    tk.Label(
                profile_account_banking,
                text=f'{user_data.user_table[0]}',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=3,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'Phone:',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=4,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'{user_data.user_table[3]}',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=4,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'Email:',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=5,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'{user_data.user_table[2]}',
                font=("Trebuchet MS", 8, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=5,column=1,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'Date of Birth:',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=6,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                profile_account_banking,
                text=f'{user_data.user_table[5]}',
                font=("Trebuchet MS", 12, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=6,column=1,padx=10,pady=(10,5),sticky='w')
    


    #####################################################################################

    # PLACEHOLDER: SQL - fetch account details
    # crsr.execute(f' SELECT * from accounts where username="{user_data.user}"')
    # a = crsr.fetchall()

    tk.Label(
                    account_profile_banking,
                    text=f'ACCOUNT PROFILE',
                    font=("Trebuchet MS", 14, "bold"),
                    bg='#0a2d56',
                    fg='#fdc132',
                    anchor='center'
                ).grid(row=0,column=0,padx=10,pady=(10,5),sticky='w')
    
    tk.Label(
                account_profile_banking,
                text=f'🏦{user_data.accounts_table[2].capitalize()} Account',
                font=("Trebuchet MS", 16, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='center'
            ).grid(row=1,column=0,padx=10,pady=(10,5),sticky='w')
    tk.Label(
                account_profile_banking,
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
                    account_profile_banking,
                    text=f'{user_data.accounts_table[4]}',
                    font=("Trebuchet MS", 8, "bold"),
                    bg='#0a2d56',
                    fg=color_status,
                    anchor='center'
                ).grid(row=3,column=0,padx=10,pady=(0,5),sticky='w')

    tk.Label(
                account_profile_banking,
                text=f'Available Balance',
                font=("Trebuchet MS", 14, "bold"),
                bg='#0a2d56',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=4,column=0,padx=10,pady=(5,5),sticky='w')
    tk.Label(
                    account_profile_banking,
                    text=f'₹{user_data.accounts_table[3]}',
                    font=("Trebuchet MS", 16, "bold"),
                    bg='#0a2d56',
                    fg='#00FF00',
                    anchor='w'
                ).grid(row=5,column=0,padx=10,pady=(5,5),sticky='w')


# -------------------------
# Transfer Frame
# -------------------------

transfer_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")




tk.Label(
    transfer_frame,
    text="Transfer Money",
    font=("Trebuchet MS", 22, "bold"),
    bg='#043565',
    fg='#fdc132',
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
# Recent Contacts Frame (right side of Banking page)
# -------------------------

recent_contacts_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")



def copy_to_clipboard(account_no):
    root.clipboard_clear()
    root.clipboard_append(account_no)
    root.update()


def recent_contacts_widget():


    for widget in recent_contacts_frame.winfo_children():
        widget.destroy()

    tk.Label(
        recent_contacts_frame,
        text="Recent Contacts",
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=20, sticky='w')

    global other_accounts
    other_accounts = []

    for row in user_data.transactions_table:
        transaction_type = row[2]
        from_account = row[5]
        to_account = row[6]

        if transaction_type == "DEBIT":
            other_account = to_account
        elif transaction_type == "CREDIT":
            other_account = from_account

        if other_account not in other_accounts:
            other_accounts.append(other_account)

        if len(other_accounts) == 3:
            break

    current_row = 1
    global total_records
    total_records=[]
    for other_account in other_accounts:

        crsr.execute(f'select username from accounts where account_no="{other_account}"')
        account_owner_records = crsr.fetchall()

        other_username = account_owner_records[0][0]

        crsr.execute(f'select name, email from users where username="{other_username}"')
        user_records = crsr.fetchall()

        other_name = user_records[0][0]
        other_email = user_records[0][1]

        total_records.append([other_username,other_name,other_email,other_account])


    def copy_clip_1():
        copy_to_clipboard(total_records[0][3])
    def copy_clip_2():
        copy_to_clipboard(total_records[1][3])
    def copy_clip_3():
        copy_to_clipboard(total_records[2][3])

    if len(total_records) >0:

        tk.Label(
            recent_contacts_frame,
            text=f'{total_records[0][1]}',
            font=("Trebuchet MS", 16, "bold"),
            bg='#043565',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=current_row, column=0, columnspan=2, padx=20, pady=(15, 0), sticky='w')
        current_row = current_row + 1

        tk.Label(
            recent_contacts_frame,
            text=f'{total_records[0][2]}',
            font=("Century Gothic", 12, "bold"),
            bg='#043565',
            fg='#86ADE5',
            anchor='w'
        ).grid(row=current_row, column=0, columnspan=2, padx=20, sticky='w')
        current_row = current_row + 1

        tk.Label(
            recent_contacts_frame,
            text=f'{total_records[0][3]}',
            font=("Century Gothic", 12, "bold"),
            bg='#043565',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=current_row, column=0, padx=(20, 5), sticky='w')

        tk.Button(
            recent_contacts_frame,
            text="📋",
            command=copy_clip_1,
            bg='#043565',
            fg='#E3D9F2',
            relief='flat',
            borderwidth=0,
            activebackground='#043565',
            font=("Century Gothic", 12, "bold"),
        ).grid(row=current_row, column=1, padx=(0, 20), sticky='w')
        current_row = current_row + 1


    if len(total_records) >1:
    
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[1][1]}',
                font=("Trebuchet MS", 16, "bold"),
                bg='#043565',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=current_row, column=0, columnspan=2, padx=20, pady=(15, 0), sticky='w')
            current_row = current_row + 1
    
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[1][2]}',
                font=("Century Gothic", 12, "bold"),
                bg='#043565',
                fg='#86ADE5',
                anchor='w'
            ).grid(row=current_row, column=0, columnspan=2, padx=20, sticky='w')
            current_row = current_row + 1
    
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[1][3]}',
                font=("Century Gothic", 12, "bold"),
                bg='#043565',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=current_row, column=0, padx=(20, 5), sticky='w')
    
            tk.Button(
                recent_contacts_frame,
                text="📋",
                command=copy_clip_2,
                bg='#043565',
                fg='#E3D9F2',
                relief='flat',
                borderwidth=0,
                font=("Century Gothic", 12, "bold"),
                activebackground='#043565'
            ).grid(row=current_row, column=1, padx=(0, 20), sticky='w')
            current_row = current_row + 1


    if len(total_records) >2:
        
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[2][1]}',
                font=("Trebuchet MS", 16, "bold"),
                bg='#043565',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=current_row, column=0, columnspan=2, padx=20, pady=(15, 0), sticky='w')
            current_row = current_row + 1
    
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[2][2]}',
                font=("Century Gothic", 12, "bold"),
                bg='#043565',
                fg='#86ADE5',
                anchor='w'
            ).grid(row=current_row, column=0, columnspan=2, padx=20, sticky='w')
            current_row = current_row + 1
    
            tk.Label(
                recent_contacts_frame,
                text=f'{total_records[2][3]}',
                font=("Century Gothic", 12, "bold"),
                bg='#043565',
                fg='#E3D9F2',
                anchor='w'
            ).grid(row=current_row, column=0, padx=(20, 5), sticky='w')
    
            tk.Button(
                recent_contacts_frame,
                text="📋",
                command=copy_clip_3,
                font=("Century Gothic", 12, "bold"),
                bg='#043565',
                fg='#E3D9F2',
                relief='flat',
                borderwidth=0,
                activebackground='#043565'
            ).grid(row=current_row, column=1, padx=(0, 20), sticky='w')
            current_row = current_row + 1




