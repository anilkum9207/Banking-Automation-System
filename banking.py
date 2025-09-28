import sqlite3
import gmail
import random

from tkinter import messagebox


sql_con=sqlite3.connect(database='banking_tables_SQLite')
sql_cur=sql_con.cursor()
sql_cur.execute('''create table if not exists Accounts(
Name text,
Mobile text,
Email text,
Address text,
Gender text,
Account_type text,
Balance float,
Aadhar_number text,
Pan_Number text,
Pincode text,
account_number integer primary key autoincrement,
IFSC text,
Password text)
''')
sql_con.close()

sql_con=sqlite3.connect(database='banking_tables_SQLite')
sql_cur=sql_con.cursor()
sql_cur.execute('''create table if not exists Account_statements(
Account_number integer,
amount float,
transfer_type text,
txn_date text,
Updated_Balance float,
Txn_ID text primary key)
''')
sql_con.close()


def mail_send(tomail,acnumber,name,password):
    mail_ID='xxxxxx@gmail.com'
    mail_app_code='xxxxxxxxx'
    gmail_con=gmail.GMail(mail_ID,mail_app_code)
    sub='Welcome to RT Banking & Finance | Your New Account Details'
    body=f'''
Dear [{name}],

Thank you for choosing RT Banking & Finance. We are pleased to inform you that your account has been successfully opened.

Please find your account details below:

Account Number: [{acnumber}]

Temporary Password: [{password}]

For security purposes, you will be required to change your password upon your first login. We recommend creating a strong password that you do not share with anyone.

We are delighted to have you with us and look forward to serving your banking needs.

Best regards,
RT Banking & Finance
'''
    gmail_msg=gmail.Message(to=tomail,subject=sub,text=body)
    gmail_con.send(gmail_msg)

 

def otp_send(tomail,name,otp):
    gmail_con=gmail.GMail('topprimehub@gmail.com','tomk gsig rvkr tzpu')
    sub='Your One-Time Password (OTP)'
    body=f'''
Dear {name},

Your One-Time Password (OTP) is: [{otp}]

Please do not share it with anyone.

If you did not request this OTP, please ignore this message.

Thank you,
RT Banking & Finance
'''
    gmail_msg=gmail.Message(to=tomail,subject=sub,text=body)
    gmail_con.send(gmail_msg)
