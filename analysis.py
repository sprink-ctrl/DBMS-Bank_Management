# analysis.py
import tkinter as tk
from ui import root, db, crsr, navbar
import user_data


current_filter = "OVERALL"


# -------------------------
# Frames
# -------------------------

filter_frame = tk.Frame(root, bg='#00305e', borderwidth=0)
credit_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")
debit_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")
net_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")
avg_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")
largest_frame = tk.Frame(root, bg='#043565', borderwidth=0, relief="groove")


last30_button = tk.Button(
    filter_frame,
    text="Last 30 Days",
    width=15,
    bg='#E3D9F2',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
)
last30_button.grid(row=0, column=0, padx=10)

overall_button = tk.Button(
    filter_frame,
    text="Overall",
    width=15,
    bg='#fdc132',
    font=("Century Gothic", 10, "bold"),
    fg='#000000',
    relief='solid',
    borderwidth=0,
)
overall_button.grid(row=0, column=1, padx=10)


# -------------------------
# Functions
# -------------------------

def show_analysis():
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Frame':
            widget.place_forget()

    navbar.place(relwidth=1)
    filter_frame.place(relx=0.35, rely=0.14, relwidth=0.3, relheight=0.06)

    credit_frame.place(relx=0.03, rely=0.24, relwidth=0.30, relheight=0.32)
    debit_frame.place(relx=0.35, rely=0.24, relwidth=0.30, relheight=0.32)
    net_frame.place(relx=0.67, rely=0.24, relwidth=0.30, relheight=0.32)

    avg_frame.place(relx=0.19, rely=0.60, relwidth=0.30, relheight=0.32)
    largest_frame.place(relx=0.51, rely=0.60, relwidth=0.30, relheight=0.32)

    navbar.tkraise()

    load_stats()


def get_current_timestamp():
    crsr.execute("SELECT CURRENT_TIMESTAMP")
    current_time = crsr.fetchall()[0][0]
    return current_time


def get_date_condition():
    global current_filter
    if current_filter == "LAST_30":
        current_time = get_current_timestamp()
        return f' AND DATEDIFF("{current_time}", timestamp) <= 30'
    else:
        return ''


def set_filter_last30():
    global current_filter
    current_filter = "LAST_30"
    last30_button.config(bg='#fdc132')
    overall_button.config(bg='#E3D9F2')
    load_stats()


def set_filter_overall():
    global current_filter
    current_filter = "OVERALL"
    overall_button.config(bg='#fdc132')
    last30_button.config(bg='#E3D9F2')
    load_stats()


last30_button.config(command=set_filter_last30)
overall_button.config(command=set_filter_overall)


def load_stats():

    for widget in credit_frame.winfo_children():
        widget.destroy()
    for widget in debit_frame.winfo_children():
        widget.destroy()
    for widget in net_frame.winfo_children():
        widget.destroy()
    for widget in avg_frame.winfo_children():
        widget.destroy()
    for widget in largest_frame.winfo_children():
        widget.destroy()

    username = user_data.user_table[0]
    date_condition = get_date_condition()

    # -------------------------
    # Total Credits
    # -------------------------

    crsr.execute(f'SELECT SUM(amount) FROM transactions WHERE username="{username}" AND transaction_type="CREDIT"{date_condition}')
    total_credit = crsr.fetchall()[0][0]
    if total_credit is None:
        total_credit = 0

    tk.Label(
        credit_frame,
        text='Total Credits',
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, padx=15, pady=(15, 0), sticky='w')

    tk.Label(
        credit_frame,
        text=f'₹ {total_credit}',
        font=("Trebuchet MS", 24, "bold"),
        bg='#043565',
        fg='#00FF00',
        anchor='w'
    ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky='w')

    crsr.execute(f'SELECT from_account, amount FROM transactions WHERE username="{username}" AND transaction_type="CREDIT"{date_condition} ORDER BY timestamp DESC LIMIT 2')
    last_credits = crsr.fetchall()

    tk.Label(
            credit_frame,
            text=f'Recent Credits',
            font=("Trebuchet MS", 14, "bold"),
            bg='#043565',
            fg='#fdc132',
            anchor='w'
        ).grid(row=2, column=0, padx=15, pady=(0, 15), sticky='w')
    credit_row = 3
    for credit_record in last_credits:
        tk.Label(
            credit_frame,
            text=f'From {credit_record[0]}   ₹{credit_record[1]}',
            font=("Century Gothic", 10, "bold"),
            bg='#043565',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=credit_row, column=0, padx=15, pady=(0, 5), sticky='w')
        credit_row = credit_row + 1

    # -------------------------
    # Total Debits
    # -------------------------

    crsr.execute(f'SELECT SUM(amount) FROM transactions WHERE username="{username}" AND transaction_type="DEBIT"{date_condition}')
    total_debit = crsr.fetchall()[0][0]
    if total_debit is None:
        total_debit = 0

    tk.Label(
        debit_frame,
        text='Total Debits',
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, padx=15, pady=(15, 0), sticky='w')

    tk.Label(
        debit_frame,
        text=f'₹ {total_debit}',
        font=("Trebuchet MS", 24, "bold"),
        bg='#043565',
        fg='#FF7F7F',
        anchor='w'
    ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky='w')

    crsr.execute(f'SELECT to_account, amount FROM transactions WHERE username="{username}" AND transaction_type="DEBIT"{date_condition} ORDER BY timestamp DESC LIMIT 2')
    last_debits = crsr.fetchall()

    tk.Label(
            debit_frame,
            text=f'Recent Debits',
            font=("Trebuchet MS", 14, "bold"),
            bg='#043565',
            fg='#fdc132',
            anchor='w'
        ).grid(row=2, column=0, padx=15, pady=(0, 15), sticky='w')
    debit_row = 3
    for debit_record in last_debits:
        tk.Label(
            debit_frame,
            text=f'To {debit_record[0]}   ₹{debit_record[1]}',
            font=("Century Gothic", 10, "bold"),
            bg='#043565',
            fg='#E3D9F2',
            anchor='w'
        ).grid(row=debit_row, column=0, padx=15, pady=(0, 5), sticky='w')
        debit_row = debit_row + 1

    # -------------------------
    # Net Movement
    # -------------------------

    net_movement = float(total_credit) - float(total_debit)

    if net_movement >= 0:
        net_color = '#00FF00'
    else:
        net_color = '#FF7F7F'

    tk.Label(
        net_frame,
        text='Net Movement',
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, padx=15, pady=(15, 0), sticky='w')

    tk.Label(
        net_frame,
        text=f'₹ {net_movement}',
        font=("Trebuchet MS", 24, "bold"),
        bg='#043565',
        fg=net_color,
        anchor='w'
    ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky='w')

    # -------------------------
    # Average Transaction
    # -------------------------

    crsr.execute(f'SELECT AVG(amount) FROM transactions WHERE username="{username}"{date_condition}')
    avg_transaction = crsr.fetchall()[0][0]
    
    if avg_transaction is None:
        avg_transaction = 0
    
    round(avg_transaction,2)

    tk.Label(
        avg_frame,
        text='Average Transaction',
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, padx=15, pady=(15, 0), sticky='w')

    tk.Label(
        avg_frame,
        text=f'₹ {avg_transaction}',
        font=("Trebuchet MS", 24, "bold"),
        bg='#043565',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky='w')

    # -------------------------
    # Largest Transaction
    # -------------------------

    crsr.execute(f'SELECT MAX(amount) FROM transactions WHERE username="{username}"{date_condition}')
    largest_transaction = crsr.fetchall()[0][0]
    if largest_transaction is None:
        largest_transaction = 0

    tk.Label(
        largest_frame,
        text='Largest Transaction',
        font=("Trebuchet MS", 18, "bold"),
        bg='#043565',
        fg='#fdc132',
        anchor='w'
    ).grid(row=0, column=0, padx=15, pady=(15, 0), sticky='w')

    tk.Label(
        largest_frame,
        text=f'₹ {largest_transaction}',
        font=("Trebuchet MS", 24, "bold"),
        bg='#043565',
        fg='#E3D9F2',
        anchor='w'
    ).grid(row=1, column=0, padx=15, pady=(0, 15), sticky='w')


