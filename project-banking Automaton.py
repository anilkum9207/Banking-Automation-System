#This is banking Application
#At the TOP we import the related module,class, package which is used in this.
from tkinter import Tk,Frame,Label,Button,Entry,messagebox,filedialog,ttk   
import time,os,shutil
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import random
import string
import sqlite3
import banking

#First we create main window,frame,button & label using TKinter library
main_win=Tk()
main_win.state('zoomed')
main_win.resizable(width=False,height=False)
main_win.title('R&T Banking and Finance')
main_win.configure(bg="light grey")

title_lbl=Label(main_win,text='RT Banking & Finance',font=("arial",40,"bold","underline"),fg='Navy blue',bd=5,bg='light grey')
title_lbl.pack()

today_lbl=Label(main_win,text=time.strftime('%A, %d %B %Y'),fg='navy blue',bg='light grey',font=("arial",20,"bold"))
today_lbl.pack()

logo=Image.open('images/RT Banking & Finance(logo).png').resize((200,150))
logo_bitmap=ImageTk.PhotoImage(logo,master=main_win)
logo_lbl=Label(main_win,image=logo_bitmap)
logo_lbl.place(relx=0,rely=0)
logo.close()

money_logo=Image.open('images/money hand logo.jpg').resize((200,150))
money_logobitmap=ImageTk.PhotoImage(money_logo,master=main_win)
money_logolbl=Label(main_win,image=money_logobitmap)
money_logolbl.place(x=1160,y=0)
money_logo.close()

footer_lbl=Label(main_win,text='developed by Anil_kumar',font=("arial",15,"bold","underline"),fg='Navy blue',bd=5,bg='light grey')
footer_lbl.pack(side='bottom',pady=5)

#Create captcha fun()--
def get_captcha():
    chars=string.ascii_letters +string.digits
    captcha=''
    for i in range(6):
        x=random.choice(chars)
        captcha=captcha + x
    return captcha

#create refresh function--
def get_refresh():
    captcha=get_captcha()
    capt_lbl.configure(text=captcha)


def back():
    main_frame()    

#we create main_frame() funcation so we can use later in project.
def main_frame():
    def login():
        utype=user_combox.get()
        global uacn
        uacn=int(acn_entry.get())
        upass=pwd_entry.get()
        ucapt=capt_entry.get()
        ucapt1=capt_lbl.cget('text')

        if utype=='Admin':
            if utype=='Admin' and uacn==12345 and upass=='Admin01':
                if ucapt==ucapt1:
                    main_frm.destroy()
                    adminfrm()   
                else:
                    messagebox.showerror('Login','Invalid Captcha')
            else:
                messagebox.showerror('Login','Invalid Details "Retry" ')
        elif utype=="User":
            sql_con=sqlite3.connect(database='banking_tables_SQLite')
            sql_cur=sql_con.cursor()
            query=('Select * from Accounts where account_number=?;')
            sql_cur.execute(query,(uacn,))
            row=sql_cur.fetchone()  # fetch only once
            sql_con.close()

            if utype=='User' and uacn==row[10] and upass==row[12]:
                if ucapt==ucapt1:
                    main_frm.destroy()
                    user_frame()
                else:
                    messagebox.showerror('Login','Invalid Captcha')
            else:
                messagebox.showerror('Error','Invalid Details')
        else:
            messagebox.showerror('Error','Please select the User.')
     

    def adminfrm():
        def open_account():
            def user_acopen():
                try:
                    uname=name_entry.get()
                    umobile=mobile_entry.get()
                    uaddress=add_entry.get()
                    uemail=email_entry.get()
                    ugender=gender_combo.get()
                    uactype=actype_combo.get()
                    uaadhar=Eadhar_entry.get()
                    upan=Epan_entry.get()
                    upincode=pcode_entry.get()
                    upassword=get_captcha()
                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                    sql_cur=sql_con.cursor()
                    query='insert into accounts values(?,?,?,?,?,?,?,?,?,?,Null,?,?)'
                    sql_cur.execute(query,(uname,umobile,uemail,uaddress,ugender,uactype,0,uaadhar,upan,upincode,'RTB5353',upassword))
                    sql_con.commit()
                    sql_con.close()

                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                    sql_cur=sql_con.cursor()
                    query=('Select account_number,Password from Accounts where account_number=(SELECT MAX(account_number) FROM Accounts);')
                    sql_cur.execute(query)
                    sql_con.commit()
                    row = sql_cur.fetchone()  # fetch only once
                    sql_con.close()

                    if row:  # check row is not None
                        uac_number = row[0]   # first column
                        uac_password = row[1] # second column

                    else:
                        uac_number, uac_password = None, None
    

                    banking.mail_send(uemail,uac_number,uname,uac_password)
                    messagebox.showinfo('Account',f'your account is successfully open your account number and password will be sent to regeristed {uemail}')

                except Exception as msg:
                    messagebox.showerror('Error',msg)
                    


            openacn_frm=Frame(admfrm, bg='light grey')
            openacn_frm.place(relx=.1, rely=.15,relwidth=.8,relheight=.75)

            welc_lbl=Label(openacn_frm,text='Account Opening Screen-',font=("arial",15,"bold"),bg='light grey',fg="Navy blue")
            welc_lbl.place(relx=0,rely=0)

            name_lbl=Label(openacn_frm,text='Full Name',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            name_lbl.place(relx=.05,rely=.15,relwidth=.2)
            name_entry=Entry(openacn_frm,bd=3,font=("",12))
            name_entry.place(relx=.05,rely=.25,relwidth=.2,relheight=.06)
            name_entry.focus()

            mobile_lbl=Label(openacn_frm,text='Mobile Number',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            mobile_lbl.place(relx=.05,rely=.35,relwidth=.2)
            mobile_entry=Entry(openacn_frm,bd=3,font=("",12))
            mobile_entry.place(relx=.05,rely=.45,relwidth=.2,relheight=.06)

            add_lbl=Label(openacn_frm,text='Complete Address',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            add_lbl.place(relx=.05,rely=.55,relwidth=.2)
            add_entry=Entry(openacn_frm,bd=3,font=("",12,))
            add_entry.place(relx=.05,rely=.65,relwidth=.2,relheight=.06)

            email_lbl=Label(openacn_frm,text='Email ID',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            email_lbl.place(relx=.4,rely=.15,relwidth=.2)
            email_entry=Entry(openacn_frm,bd=3,font=("",12))
            email_entry.place(relx=.4,rely=.25,relwidth=.2,relheight=.06)

            gender_lbl=Label(openacn_frm,text='Gender',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            gender_lbl.place(relx=.4,rely=.35,relwidth=.2)
            gender_combo=Combobox(openacn_frm,values=['Male','Female','Others','---Select---'],state="readonly",font=('arial',12,))
            gender_combo.current(3)
            gender_combo.place(relx=.4,rely=.45)

            actype_lbl=Label(openacn_frm,text='Account Type',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            actype_lbl.place(relx=.4,rely=.55,relwidth=.2)
            actype_combo=Combobox(openacn_frm,values=['Savings','Current','---Select---'],state='readonly',font=('arial',12,))
            actype_combo.current(2)
            actype_combo.place(relx=.4,rely=.65)

            Eadhar_lbl=Label(openacn_frm,text='Aadhar Number-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Eadhar_lbl.place(relx=.75,rely=.15,relwidth=.2)
            Eadhar_entry=Entry(openacn_frm,bd=3,font=("",12))
            Eadhar_entry.place(relx=.75,rely=.25,relwidth=.2,relheight=.06)

            Epan_lbl=Label(openacn_frm,text='PAN Number-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Epan_lbl.place(relx=.75,rely=.35,relwidth=.2)
            Epan_entry=Entry(openacn_frm,bd=3,font=("",12))
            Epan_entry.place(relx=.75,rely=.45,relwidth=.2,relheight=.06)

            pcode_lbl=Label(openacn_frm,text='Pincode-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            pcode_lbl.place(relx=.75,rely=.55,relwidth=.2)
            pcode_entry=Entry(openacn_frm,bd=3,font=("",12))
            pcode_entry.place(relx=.75,rely=.65,relwidth=.2,relheight=.06)

            submit_btn=Button(openacn_frm,text="Submit",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=user_acopen)
            submit_btn.place(relx=.35,rely=.8,relwidth=.1,relheight=.06)

            reset_btn=Button(openacn_frm,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=open_account)
            reset_btn.place(relx=.55,rely=.8,relwidth=.1,relheight=.06)

            

        def dlt_account():       #Account deleting fun() for admin--

            def delete_uacn():
                    uacn=int(acn_entry.get())
                    uotp=int(Eotp_entry.get())
                    if uotp==otp:
                        ures=messagebox.askyesno('Delete Account','Are your sure want to Delete account ?')
                        if ures==True:
                            sql_con=sqlite3.connect(database='banking_tables_SQLite')
                            sql_cur=sql_con.cursor()
                            query=('delete from Accounts where account_number=?;')
                            sql_cur.execute(query,(uacn,))
                            sql_con.commit()
                            sql_con.close()
                            messagebox.showinfo('Account Delete',f' Your account number {uacn} has been successfully deleted')
                        else:
                            pass
                    else:
                        messagebox.showerror('Enter OTP','Invalid OTP')

            def send_otp():  
            
                uacn=int(acn_entry.get())
                uname=name_entry.get()

                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                sql_cur=sql_con.cursor()
                query=('Select * from Accounts where account_number=?;')
                sql_cur.execute(query,(uacn,))
                row=sql_cur.fetchone()  # fetch only once
                sql_con.close()

                if row==None:
                    messagebox.showerror('Error','Details not found')

                elif uacn==row[10] and uname==row[0]:
                    global otp
                    otp=random.randint(1000,9999)
                    banking.otp_send(row[2],uname,otp)
                    messagebox.showinfo('OTP Sent',f'Your one time password has been sent to your email {row[2]}')

                else:
                    messagebox.showerror('Error','Invalid details')

            dltacn_frm=Frame(admfrm)
            dltacn_frm.configure(bg='light grey')
            dltacn_frm.place(relx=.1, rely=.15,relwidth=.8,relheight=.75)
            welc_lbl=Label(dltacn_frm,text='Account Delete Screen-',font=("arial",15,"bold"),bg='light grey',fg="Navy blue")
            welc_lbl.place(relx=0,rely=0)

            acn_lbl=Label(dltacn_frm,text='Account number',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            acn_lbl.place(relx=.2,rely=.15,relwidth=.15)
            acn_entry=Entry(dltacn_frm,bd=3,font=("",12))
            acn_entry.place(relx=.4,rely=.15,relwidth=.15,relheight=.05)

            name_lbl=Label(dltacn_frm,text='Account holder Name',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            name_lbl.place(relx=.2,rely=.25,relwidth=.15)
            name_entry=Entry(dltacn_frm,bd=3,font=("",12))
            name_entry.place(relx=.4,rely=.25,relwidth=.15,relheight=.05)

            snotp_btn=Button(dltacn_frm,text="Send OTP",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=send_otp)
            snotp_btn.place(relx=.35,rely=.35,relwidth=.1,relheight=.05)

            Eotp_lbl=Label(dltacn_frm,text='Enter OTP',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            Eotp_lbl.place(relx=.2,rely=.55,relwidth=.15)
                    
            Eotp_entry=Entry(dltacn_frm,bd=3,font=("",12))
            Eotp_entry.place(relx=.4,rely=.55,relwidth=.15,relheight=.05)

            reset_btn=Button(dltacn_frm,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=dlt_account)
            reset_btn.place(relx=.5,rely=.35,relwidth=.1,relheight=.05)

            delete_btn=Button(dltacn_frm,text="Delete Account",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=delete_uacn)
            delete_btn.place(relx=.4,rely=.65,relwidth=.15,relheight=.05)



        
        def view_account():     # Account viewing fun() for Admin--

            def view_uacn():
                uacn=int(acn_entry.get())
                uname=name_entry.get()

                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                sql_cur=sql_con.cursor()
                query=('select * from Accounts where account_number=?')
                sql_cur.execute(query,(uacn,))
                sql_con.commit()
                row=sql_cur.fetchone()
                sql_con.close()

                if row==None:
                    messagebox.showerror('Error','Details Not found')

                elif uacn==row[10] and uname==row[0]:
                    details=f'''
Name- {row[0]}
Mobile - {row[1]}
Email - {row[2]}
Address - {row[3]}
Gender - {row[4]}
Account_type - {row[5]}
Balance - {row[6]}
Aadhar_number - {row[7]}
Pan_Number - {row[8]}
Pincode - {row[9]}
account_number - {row[10]}
'''
                    udetails_lbl=Label(viewacn_frm,text=details,bg='white',fg='blue',font=('',12,"bold"))
                    udetails_lbl.place(relx=.55, rely=.15,relheight=.75,relwidth=.35)
                else:
                    messagebox.showerror('Error','Invalid Details')


            viewacn_frm=Frame(admfrm)
            viewacn_frm.configure(bg='light grey')
            viewacn_frm.place(relx=.1, rely=.15,relwidth=.8,relheight=.75)
            welc_lbl=Label(viewacn_frm,text='Account View Screen-',font=("arial",15,"bold"),bg='light grey',fg="Navy blue")
            welc_lbl.place(relx=0,rely=0)

            acn_lbl=Label(viewacn_frm,text='Account number',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            acn_lbl.place(relx=.1,rely=.3,relwidth=.15)
            acn_entry=Entry(viewacn_frm,bd=3,font=("",12))
            acn_entry.place(relx=.3,rely=.3,relwidth=.15,relheight=.05)

            name_lbl=Label(viewacn_frm,text='Account holder Name',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            name_lbl.place(relx=.1,rely=.4,relwidth=.15)
            name_entry=Entry(viewacn_frm,bd=3,font=("",12))
            name_entry.place(relx=.3,rely=.4,relwidth=.15,relheight=.05)

            
            viewacdtls_acnbtn=Button(admfrm,text='View Details',font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=view_uacn)
            viewacdtls_acnbtn.place(relx=.35,rely=.55,relheight=.07,relwidth=.1)

            reset_btn=Button(admfrm,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=view_account)
            reset_btn.place(relx=.35,rely=.65,relwidth=.1,relheight=.07)
            

        admfrm=Frame(main_win)
        admfrm.configure(bg="Grey")
        admfrm.place(relx=0, rely=0.18,relwidth=1,relheight=.75)
        welc_lbl=Label(admfrm,text='Welcome Admin--',font=("arial",15,"bold"),bg='grey',fg="Navy blue")
        welc_lbl.place(relx=0,rely=0)


        def admin_logout():
            opt=messagebox.askyesno("logout","Are you sure want to logout ?")
            if opt==True:
                main_frame()

        open_acnbtn=Button(admfrm,text='Open Account',font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=open_account)
        open_acnbtn.place(relx=.2,rely=0,relheight=.07,relwidth=.1)
        
        dlt_acnbtn=Button(admfrm,text='Delete Account',font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=dlt_account)
        dlt_acnbtn.place(relx=.4,rely=0,relheight=.07,relwidth=.1)

        view_acnbtn=Button(admfrm,text='View Account',font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=view_account)
        view_acnbtn.place(relx=.6,rely=0,relheight=.07,relwidth=.1)

        logout_btn=Button(admfrm,text='Logout',font=("arial",15,"bold"),bg='light grey',fg="Navy blue",command=admin_logout)
        logout_btn.place(relx=.9,rely=0,)


    main_frm=Frame(main_win)
    main_frm.configure(bg='grey')
    main_frm.place(relx=0, rely=0.18,relwidth=1,relheight=.75)

    #for user input we use combox to dropdown list--
    user_combox=Combobox(main_frm,values=['---Select---','User','Admin'],font=("",12,"bold"),state='readonly')
    user_combox.current(0)
    user_combox.place(relx=.4,rely=.2)

    user_lbl=Label(main_frm,text='Select from drop down',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    user_lbl.place(relx=.2,rely=.2,relwidth=.15)

    #make label & entry for account number--
    acn_lbl=Label(main_frm,text='Account number',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    acn_lbl.place(relx=.2,rely=.3,relwidth=.15)
    acn_entry=Entry(main_frm,bd=3,font=("",12,))
    acn_entry.place(relx=.4,rely=.3,relwidth=.15,relheight=.05)

    #Make Label & entry for password--
    pwd_lbl=Label(main_frm,text='Password',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    pwd_lbl.place(relx=.2,rely=.4,relwidth=.15)
    pwd_entry=Entry(main_frm,bd=3,show='*',font=("",12))
    pwd_entry.place(relx=.4,rely=.4,relwidth=.15,relheight=.05)

    global capt_lbl
    capt_lbl=Label(main_frm,text=get_captcha(),font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    capt_lbl.place(relx=.4,rely=.5,relwidth=.1)


    input_capt_lbl=Label(main_frm,text='Enter captcha',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    input_capt_lbl.place(relx=.25,rely=.6,relwidth=.1)

    capt_entry=Entry(main_frm,bd=3,font=("",10,))
    capt_entry.place(relx=.4,rely=.6,relwidth=.15,relheight=.05)

    #ref_logo=Image.open('refresh logo.png').resize((25,25))
    #ref_logobitmap=ImageTk.PhotoImage(ref_logo,master=main_frm)
    
    ref_logo_btn=Button(main_frm,text="Refresh",command=get_refresh)
    ref_logo_btn.place(relx=.52,rely=.5)

    login_btn=Button(main_frm,text="Login",font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=login)
    login_btn.place(relx=.42,rely=.7,relwidth=.05,relheight=.05)

    reset_btn=Button(main_frm,text="Reset",font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    reset_btn.place(relx=.48,rely=.7,relwidth=.05,relheight=.05)

    forget_btn=Button(main_frm,text="Forget password",font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=forget)
    forget_btn.place(relx=.4,rely=.8,relwidth=.15,relheight=.05)
    
    def user_frame():

        sql_con=sqlite3.connect(database='banking_tables_SQLite')
        sql_cur=sql_con.cursor()
        query=('select * from Accounts where account_number=?')
        sql_cur.execute(query,(uacn,))
        row=sql_cur.fetchone()
        sql_con.close()

        userfrm=Frame(main_win)
        userfrm.configure(bg='grey')
        userfrm.place(relx=0,rely=.18,relwidth=1,relheight=.75)

        welc_label=Label(userfrm,text=f'Welcome {row[0]}',font=('arial',15,'bold'),bg='grey',fg='navy blue')
        welc_label.place(relx=0,rely=0)

        def logout():
            opt=messagebox.askyesno('Logout','Are your sure want to Logout?')
            if opt==True:
                main_frame()
            else:
                pass

        def user_update():

            sql_con=sqlite3.connect(database='banking_tables_SQLite')
            sql_cur=sql_con.cursor()
            query=('select * from Accounts where account_number=?')
            sql_cur.execute(query,(uacn,))
            sql_con.commit()
            row=sql_cur.fetchone()
            sql_con.close()

            def uupdate_details():
                uname=name_entry.get()
                umob=mobile_entry.get()
                uadd=add_entry.get()
                uemail=email_entry.get()
                uadhar=Eadhar_entry.get()
                upan=Epan_entry.get()
                upincode=pcode_entry.get()
                upswrd=password_entry.get()

                ures=messagebox.askyesno("Update Details","Are you sure want to update details")
                if ures==True:
                    try:
                        sql_con=sqlite3.connect(database='banking_tables_SQLite')
                        sql_cur=sql_con.cursor()
                        query=('update Accounts set name=?,mobile=?,email=?,address=?,aadhar_number=?,pan_number=?,pincode=?,password=? where account_number=?')
                        sql_cur.execute(query,(uname,umob,uemail,uadd,uadhar,upan,upincode,upswrd,uacn))
                        sql_con.commit()
                        sql_con.close()
                        messagebox.showinfo('Details','Your account details has been successfully Updated')
                    except Exception as error:
                        messagebox.showerror('Error',error)
                else:
                    pass

            
            def uprofile_pic():
                path=filedialog.askopenfilename()
                shutil.copy(path,f"images/{uacn}.jpg")

                if os.path.exists(f"images/{uacn}.jpg"):
                    upath=(f"images/{uacn}.jpg")
                else:
                    upath=(f"images/Default-pic.jpg")

                default_pic=Image.open(upath).resize((50,50))
                default_pic_bitmap=ImageTk.PhotoImage(default_pic,master=uframe)
                default_pic_lbl=Label(uframe,image=default_pic_bitmap)
                default_pic_lbl.image=default_pic_bitmap
                default_pic_lbl.place(relx=.47,rely=.52)

            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is Update Screen',font=('arial',15,'bold','underline'),bg='light grey',fg='navy blue')
            welc_label.pack()
    

            profilepic_btn=Button(uframe,text='profile pic',font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=uprofile_pic)
            profilepic_btn.place(relx=.4,rely=.65,relwidth=.2)

            if os.path.exists(f'images/{uacn}.jpg'):
                upath=(f'images/{uacn}.jpg')
                default_pic=Image.open(upath).resize((50,50))
                default_pic_bitmap=ImageTk.PhotoImage(default_pic,master=uframe)
                default_pic_lbl=Label(uframe,image=default_pic_bitmap)
                default_pic_lbl.image=default_pic_bitmap
                default_pic_lbl.place(relx=.47,rely=.52)
            else:
                upath=(f'images/Default-pic.jpg')
                default_pic=Image.open(upath).resize((50,50))
                default_pic_bitmap=ImageTk.PhotoImage(default_pic,master=uframe)
                default_pic_lbl=Label(uframe,image=default_pic_bitmap)
                default_pic_lbl.image=default_pic_bitmap
                default_pic_lbl.place(relx=.47,rely=.52)

            name_lbl=Label(uframe,text='Full Name',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            name_lbl.place(relx=.05,rely=.15,relwidth=.2)
            name_entry=Entry(uframe,bd=3,font=("",12))
            name_entry.place(relx=.05,rely=.25,relwidth=.2,relheight=.06)
            name_entry.insert(0,row[0])
            name_entry.focus()

            mobile_lbl=Label(uframe,text='Mobile Number',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            mobile_lbl.place(relx=.05,rely=.35,relwidth=.2)
            mobile_entry=Entry(uframe,bd=3,font=("",12))
            mobile_entry.place(relx=.05,rely=.45,relwidth=.2,relheight=.06)
            mobile_entry.insert(0,row[1])

            add_lbl=Label(uframe,text='Complete Address',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            add_lbl.place(relx=.05,rely=.55,relwidth=.2)
            add_entry=Entry(uframe,bd=3,font=("",12,))
            add_entry.place(relx=.05,rely=.65,relwidth=.2,relheight=.06)
            add_entry.insert(0,row[3])

            email_lbl=Label(uframe,text='Email ID',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            email_lbl.place(relx=.4,rely=.15,relwidth=.2)
            email_entry=Entry(uframe,bd=3,font=("",12))
            email_entry.place(relx=.4,rely=.25,relwidth=.2,relheight=.06)
            email_entry.insert(0,row[2])

            password_lbl=Label(uframe,text='Password',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            password_lbl.place(relx=.4,rely=.35,relwidth=.2)
            password_entry=Entry(uframe,bd=3,font=("",12))
            password_entry.place(relx=.4,rely=.45)
            password_entry.insert(0,row[12])

            Eadhar_lbl=Label(uframe,text='Aadhar Number-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Eadhar_lbl.place(relx=.75,rely=.15,relwidth=.2)
            Eadhar_entry=Entry(uframe,bd=3,font=("",12))
            Eadhar_entry.place(relx=.75,rely=.25,relwidth=.2,relheight=.06)
            Eadhar_entry.insert(0,row[7])

            Epan_lbl=Label(uframe,text='PAN Number-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Epan_lbl.place(relx=.75,rely=.35,relwidth=.2)
            Epan_entry=Entry(uframe,bd=3,font=("",12))
            Epan_entry.place(relx=.75,rely=.45,relwidth=.2,relheight=.06)
            Epan_entry.insert(0,row[8])

            pcode_lbl=Label(uframe,text='Pincode-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            pcode_lbl.place(relx=.75,rely=.55,relwidth=.2)
            pcode_entry=Entry(uframe,bd=3,font=("",12))
            pcode_entry.place(relx=.75,rely=.65,relwidth=.2,relheight=.06)
            pcode_entry.insert(0,row[9])

            upd_btn=Button(uframe,text="Update",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=uupdate_details)
            upd_btn.place(relx=.35,rely=.8,relwidth=.1,relheight=.06)

            reset_btn=Button(uframe,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            reset_btn.place(relx=.55,rely=.8,relwidth=.1,relheight=.06)

        def usercheck_details():
            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is check details Screen',font=('arial',15,'bold','underline'),bg='light grey',fg='navy blue')
            welc_label.pack()

            sql_con=sqlite3.connect(database='banking_tables_SQLite')
            sql_cur=sql_con.cursor()
            query=('select * from Accounts where account_number=?')
            sql_cur.execute(query,(uacn,))
            sql_con.commit()
            row=sql_cur.fetchone()
            sql_con.close()
            details=f'''
            Name - {row[0]}
            Mobile - {row[1]}
            Email - {row[2]}
            Address - {row[3]}
            Gender - {row[4]}
            Account_type - {row[5]}
            Balance - {row[6]}
            Aadhar_number - {row[7]}
            Pan_Number - {row[8]}
            Pincode - {row[9]}
            account_number - {row[10]}
            '''
            udetails_lbl=Label(uframe,text=details,bg='white',fg='blue',font=('',12,"bold"))
            udetails_lbl.place(relx=.15, rely=.15,relheight=.75,relwidth=.65)
               

        def user_deposit():

            def useramt_deposit():
                user_deposit_amt=int(Eamount_entry.get())
                user_entcap=capt_entry.get()
                cap_lbl=ucapt_lbl.cget('text')

                if user_entcap==cap_lbl:
                   ures=messagebox.askyesno('Deposit Money','Are you sure want to deposit')
                   if ures==True:
                    try:
                        sql_con=sqlite3.connect(database='banking_tables_SQLite')
                        sql_cur=sql_con.cursor()
                        query='Update accounts set Balance= Balance + ? where account_number=?;'
                        sql_cur.execute(query,(user_deposit_amt,uacn,))
                        sql_con.commit()
                        sql_con.close()
                
                        sql_con=sqlite3.connect(database='banking_tables_SQLite')
                        sql_cur=sql_con.cursor()
                        query='select balance from accounts where account_number=?'
                        sql_cur.execute(query,(uacn,))
                        ubal=sql_cur.fetchone()[0]
                        sql_con.close()

                        t=str(time.time())
                        utxnid='Txn'+'CR'+(t[:t.index('.')])
                        sql_con=sqlite3.connect(database='banking_tables_SQLite')
                        sql_cur=sql_con.cursor()
                        query='insert into account_statements values(?,?,?,?,?,?)'
                        sql_cur.execute(query,(uacn,user_deposit_amt,'CR',time.strftime("%d-%m-%Y %r"),ubal,utxnid))
                        sql_con.commit()
                        sql_con.close()
                        messagebox.showinfo("Deposit",f'{user_deposit_amt} has been successfully deposit in your account')
                        uframe.destroy()

                    except Exception as msg:
                        messagebox.showerror('Error',msg)

            def get_refresh():
                captcha=get_captcha()
                ucapt_lbl.configure(text=captcha)

            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is deposit Screen',font=('arial',15,'bold','underline'),bg='light grey',fg='navy blue')
            welc_label.pack()

            Eamount_lbl=Label(uframe,text='Enter Amount-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Eamount_lbl.place(relx=.15,rely=.25,relwidth=.2)
            Eamount_entry=Entry(uframe,bd=3,font=("",12))
            Eamount_entry.place(relx=.4,rely=.25,relwidth=.2,relheight=.06)
            Eamount_entry.focus()
            
            ucapt_lbl=Label(uframe,text=get_captcha(),font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            ucapt_lbl.place(relx=.4,rely=.35,relwidth=.1)

            refresh_btn=Button(uframe,text='Refresh',font=("arial",10),bg='white',fg="Navy blue",command=get_refresh)
            refresh_btn.place(relx=.5,rely=.35,relwidth=.08)

            input_capt_lbl=Label(uframe,text='Enter captcha',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            input_capt_lbl.place(relx=.15,rely=.45,relwidth=.2)

            capt_entry=Entry(uframe,bd=3,font=("",10,))
            capt_entry.place(relx=.4,rely=.45,relwidth=.2,relheight=.06)

            udeposit_btn=Button(uframe,text="Deposit",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=useramt_deposit)
            udeposit_btn.place(relx=.35,rely=.65,relwidth=.1,relheight=.06)

            reset_btn=Button(uframe,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=user_deposit)
            reset_btn.place(relx=.48,rely=.65,relwidth=.1,relheight=.06)

        def user_withdrawal():
            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is withdrawal Screen',font=('arial',15,'bold','underline'),bg='light grey',fg='navy blue')
            welc_label.pack()

            def useramt_withdrawal():
                user_withdrawal_amt=int(Eamount_entry.get())
                user_entcap=capt_entry.get()
                cap_lbl=ucapt_lbl.cget('text')

                if user_entcap==cap_lbl:
                   ures=messagebox.askyesno('Withdrawal Money',f'Are you sure want to withdrawal {user_withdrawal_amt} ?')
                   if ures==True:
                        sql_con=sqlite3.connect(database='banking_tables_SQLite')
                        sql_cur=sql_con.cursor()
                        query=('select * from Accounts where account_number=?')
                        sql_cur.execute(query,(uacn,))
                        sql_con.commit()
                        row=sql_cur.fetchone()
                        sql_con.close()
                        try:
                            if row[6]>=user_withdrawal_amt:
                                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                sql_cur=sql_con.cursor()
                                query='Update accounts set Balance= Balance - ? where account_number=?;'
                                sql_cur.execute(query,(user_withdrawal_amt,uacn,))
                                sql_con.commit()
                                sql_con.close()

                                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                sql_cur=sql_con.cursor()
                                query='select balance from accounts where account_number=?'
                                sql_cur.execute(query,(uacn,))
                                ubal=sql_cur.fetchone()[0]
                                sql_con.close()

                                t=str(time.time())
                                utxnid='Txn'+'DR'+(t[:t.index('.')])
                                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                sql_cur=sql_con.cursor()
                                query='insert into account_statements values(?,?,?,?,?,?)'
                                sql_cur.execute(query,(uacn,user_withdrawal_amt,'DR',time.strftime("%d-%m-%Y %r"),ubal,utxnid))
                                sql_con.commit()
                                sql_con.close()
                                messagebox.showinfo("Withdrawal",f'{user_withdrawal_amt} has been successfully withdrawal from your account')
                                uframe.destroy()
                            else:
                                messagebox.showerror('Error','Insufficient Balance')
                        except Exception as msg:
                            messagebox.showerror('Error',msg)
          

            def get_refresh():
                captcha=get_captcha()
                ucapt_lbl.configure(text=captcha)

            Eamount_lbl=Label(uframe,text='Enter Amount -',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Eamount_lbl.place(relx=.15,rely=.25,relwidth=.2)
            Eamount_entry=Entry(uframe,bd=3,font=("",12))
            Eamount_entry.place(relx=.4,rely=.25,relwidth=.2,relheight=.06)
            Eamount_entry.focus()
            
            ucapt_lbl=Label(uframe,text=get_captcha(),font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            ucapt_lbl.place(relx=.4,rely=.35,relwidth=.1)

            refresh_btn=Button(uframe,text='Refresh',font=("arial",10),bg='white',fg="Navy blue",command=get_refresh)
            refresh_btn.place(relx=.5,rely=.35,relwidth=.08)

            input_capt_lbl=Label(uframe,text='Enter captcha',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            input_capt_lbl.place(relx=.15,rely=.45,relwidth=.2)

            capt_entry=Entry(uframe,bd=3,font=("",10,))
            capt_entry.place(relx=.4,rely=.45,relwidth=.2,relheight=.06)

            uwithdrawal_btn=Button(uframe,text="Withdrawal",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=useramt_withdrawal)
            uwithdrawal_btn.place(relx=.35,rely=.65,relwidth=.1,relheight=.06)

            reset_btn=Button(uframe,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=user_withdrawal)
            reset_btn.place(relx=.48,rely=.65,relwidth=.1,relheight=.06)


        def user_transfer():
            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is Money Transfer Screen',font=('arial',15,'bold','underline'),bg='light grey',fg='navy blue')
            welc_label.pack()

            def useramt_transfer():
                transfer_acn=int(Toacn_entry.get())
                user_transfer_amt=int(Eamount_entry.get())
                user_entcap=capt_entry.get()
                cap_lbl=ucapt_lbl.cget('text')

                sql_con1=sqlite3.connect(database='banking_tables_SQLite')
                sql_cur1=sql_con1.cursor()
                query='select account_number from Accounts where account_number=?;'
                sql_cur1.execute(query,(transfer_acn,))
                exits=sql_cur1.fetchone()
                if not exits:
                    messagebox.showerror('Error','Account Number not exists..!')
                    return
                sql_con1.close()

                if user_entcap==cap_lbl:
                    ures=messagebox.askyesno('Transfer Money',f'Are you sure want to Transfer {user_transfer_amt}  ?')
                    if ures==True:
                            try:
                                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                sql_cur=sql_con.cursor()
                                query='select * from Accounts where account_number=?;'
                                sql_cur.execute(query,(uacn,))
                                row=sql_cur.fetchone()
                                sql_con.close()
                                if row[6]>=user_transfer_amt:
                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='Update accounts set Balance= Balance - ? where account_number=?;'
                                    sql_cur.execute(query,(user_transfer_amt,uacn,))
                                    sql_con.commit()
                                    sql_con.close()

                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='Update accounts set Balance= Balance + ? where account_number=?;'
                                    sql_cur.execute(query,(user_transfer_amt,transfer_acn,))
                                    sql_con.commit()
                                    sql_con.close()

                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='select balance from accounts where account_number=?'
                                    sql_cur.execute(query,(uacn,))
                                    ubal=sql_cur.fetchone()[0]
                                    sql_con.close()

                                    t=str(time.time())
                                    utxnid='Txn'+'DR'+(t[:t.index('.')])
                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='insert into account_statements values(?,?,?,?,?,?)'
                                    sql_cur.execute(query,(uacn,user_transfer_amt,'DR',time.strftime("%d-%m-%Y %r"),ubal,utxnid))
                                    sql_con.commit()
                                    sql_con.close()

                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='select balance from accounts where account_number=?'
                                    sql_cur.execute(query,(transfer_acn,))
                                    ubal=sql_cur.fetchone()[0]
                                    sql_con.close()

                                    t=str(time.time())
                                    utxnid='Txn'+'CR'+(t[:t.index('.')])
                                    sql_con=sqlite3.connect(database='banking_tables_SQLite')
                                    sql_cur=sql_con.cursor()
                                    query='insert into account_statements values(?,?,?,?,?,?)'
                                    sql_cur.execute(query,(transfer_acn,user_transfer_amt,'CR',time.strftime("%d-%m-%Y %r"),ubal,utxnid))
                                    sql_con.commit()
                                    sql_con.close()
                                    uframe.destroy()
                                    messagebox.showinfo("Transferred",f'{user_transfer_amt} has been successfully Transfer from your account to {transfer_acn}')
                                else:
                                    messagebox.showerror('Error','Insufficient Balance')
                            except Exception as msg:
                                messagebox.showerror('Error',msg)
                      
                    else:
                        pass

            def get_refresh():
                captcha=get_captcha()
                ucapt_lbl.configure(text=captcha)

            Toacn_lbl=Label(uframe,text='Enter Account Number-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Toacn_lbl.place(relx=.15,rely=.25,relwidth=.2)
            Toacn_entry=Entry(uframe,bd=3,font=("",12))
            Toacn_entry.place(relx=.4,rely=.25,relwidth=.2,relheight=.06)
            Toacn_entry.focus()


            Eamount_lbl=Label(uframe,text='Enter Transfer Amount-',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            Eamount_lbl.place(relx=.15,rely=.35,relwidth=.2)
            Eamount_entry=Entry(uframe,bd=3,font=("",12))
            Eamount_entry.place(relx=.4,rely=.35,relwidth=.2,relheight=.06)
           
            
            ucapt_lbl=Label(uframe,text=get_captcha(),font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            ucapt_lbl.place(relx=.4,rely=.45,relwidth=.1)

            refresh_btn=Button(uframe,text='Refresh',font=("arial",10),bg='white',fg="Navy blue",command=get_refresh)
            refresh_btn.place(relx=.55,rely=.45,relwidth=.08)

            input_capt_lbl=Label(uframe,text='Enter captcha',font=("arial",12,"bold"),bg='grey',fg="Navy blue")
            input_capt_lbl.place(relx=.15,rely=.55,relwidth=.2)

            capt_entry=Entry(uframe,bd=3,font=("",10,))
            capt_entry.place(relx=.4,rely=.55,relwidth=.2,relheight=.06)

            utransfer_btn=Button(uframe,text="Transfer",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=useramt_transfer)
            utransfer_btn.place(relx=.35,rely=.8,relwidth=.1,relheight=.06)

            reset_btn=Button(uframe,text="Reset",font=("arial",12,"bold"),bg='grey',fg="Navy blue",command=user_transfer)
            reset_btn.place(relx=.48,rely=.8,relwidth=.1,relheight=.06)

        
        def user_history():
            uframe=Frame(userfrm,bg='light grey')
            uframe.place(relx=.2,rely=.17,relwidth=.75,relheight=.75)

            welc_label=Label(uframe,text='This is transaction History Screen',font=('arial',15,'bold'),bg='light grey',fg='navy blue')
            welc_label.pack()
            
            try:
                table_headers=('Txn_ID','Account_number',
                'Amount',
                'transfer_type',
                'Txn_date',
                'Updated_Balance',)
                txn_table=ttk.Treeview(uframe,columns=table_headers,show='headings')
                for col in table_headers:
                    txn_table.heading(col,text=col)
                    txn_table.column(col,width=120,anchor='center')
                    txn_table.pack(fill='both',expand=True)

                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                sql_cur=sql_con.cursor()
                query='select Txn_ID,account_number,amount,transfer_type,txn_date,updated_Balance from Account_statements where account_number=?'
                sql_cur.execute(query,(uacn,))
                rows=sql_cur.fetchall()
                for tup in rows:
                    txn_table.insert('','end',values=tup)
                sql_con.close()
            except Exception as msg:
                messagebox.showerror('Error',msg)
            

        if os.path.exists(f"images/{uacn}.jpg"):
            upath=f'images/{uacn}.jpg'
        else:
            upath="images/Default-pic.jpg"
       
        upic=Image.open(upath).resize((50,50))
        upic_bitmap=ImageTk.PhotoImage(upic,master=userfrm)
        upic_lbl=Label(userfrm,image=upic_bitmap)
        upic_lbl.image=upic_bitmap
        upic_lbl.place(relx=0.01,rely=0.085)
        upic.close()

        logout_btn=Button(userfrm,text='Logout',font=('arial',15,"bold"),bg='light grey',fg='Navy blue',command=logout)
        logout_btn.place(relx=.9,rely=0.05)

        update_btn=Button(userfrm,text="Update Details",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=user_update)
        update_btn.place(relx=.01, rely=0.2,relwidth=.15)

        check_btn=Button(userfrm,text="Check Details",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=usercheck_details)
        check_btn.place(relx=.01, rely=0.3,relwidth=.15)

        deposit_btn=Button(userfrm,text="Deposit",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=user_deposit)
        deposit_btn.place(relx=.01, rely=0.4,relwidth=.15)

        withdrawal_btn=Button(userfrm,text="Withdrawal",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=user_withdrawal)
        withdrawal_btn.place(relx=.01, rely=0.5,relwidth=.15)

        transfer_btn=Button(userfrm,text="Transfer",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=user_transfer)
        transfer_btn.place(relx=.01, rely=0.6,relwidth=.15)

        txn_btn=Button(userfrm,text="Txn History",font=('arial',15,"bold"),bg='Light Grey',fg='Navy Blue',command=user_history)
        txn_btn.place(relx=.01, rely=0.7,relwidth=.15)



def forget():
    def fgsend_otp():  
        uacn=int(acn_entry.get())
        uemail=email_entry.get()

        sql_con=sqlite3.connect(database='banking_tables_SQLite')
        sql_cur=sql_con.cursor()
        query=('Select * from Accounts where account_number=?;')
        sql_cur.execute(query,(uacn,))
        row=sql_cur.fetchone()  # fetch only once
        sql_con.close()

        if row==None:
            messagebox.showerror('Error','Details not found')

        elif uacn==row[10] and uemail==row[2]:
            global otp
            otp=random.randint(1000,9999)
            banking.otp_send(row[2],row[0],otp)
            messagebox.showinfo('OTP Sent',f'Your one time password has been sent to your email {row[2]}')

        else:
            messagebox.showerror('Error','Invalid details')

    def resetpass_uacn():

        def update_password():
            newpassword=ent_newpass_lbl_entry.get()
            ures=messagebox.askyesno('Update Password','Are you sure want to update password ?')
            if ures==True:
                sql_con=sqlite3.connect(database='banking_tables_SQLite')
                sql_cur=sql_con.cursor()
                query=('update Accounts set password=? where account_number=?;')
                sql_cur.execute(query,(newpassword,uacn,))
                sql_con.commit()
                sql_con.close()
                messagebox.showinfo('Password Update',f' Your Account Password has been successfully Updated')
            else:
                pass

        uacn=int(acn_entry.get())
        uotp=int(entotp_entry.get())
        if uotp==otp:
            ent_newpass_lbl=Label(forget_frm,text='Enter New Password-',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
            ent_newpass_lbl.place(relx=.25,rely=.7,relwidth=.2)
            ent_newpass_lbl_entry=Entry(forget_frm,bd=3,font=("",12))
            ent_newpass_lbl_entry.place(relx=.5,rely=.7,relwidth=.2,relheight=.05)
            update_btn=Button(forget_frm,text="Update",font=('arial',12,"bold"),bg='Light Grey',fg='Navy Blue',command=update_password)
            update_btn.place(relx=.4, rely=.8,relwidth=.15)

        else:
            messagebox.showerror('Enter OTP','Invalid OTP')

    forget_frm=Frame(main_win)
    forget_frm.configure(bg='grey')
    forget_frm.place(relx=.1, rely=0.18,relwidth=.75,relheight=.75)

    wlc_lbl=Label(forget_frm,text='Password Recovery Window',font=("arial",18,"bold",'underline'),bg='grey',fg="Navy blue")
    wlc_lbl.pack()

    back_btn=Button(forget_frm,text="Back",font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=back)
    back_btn.place(relx=0,rely=.01,relwidth=.1,relheight=.05)

    acn_lbl=Label(forget_frm,text='Account number',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    acn_lbl.place(relx=.25,rely=.2,relwidth=.15)
    acn_entry=Entry(forget_frm,bd=3,font=("",12,))
    acn_entry.place(relx=.45,rely=.2,relwidth=.2,relheight=.05)
    acn_entry.focus()

    email_lbl=Label(forget_frm,text='Email ID',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    email_lbl.place(relx=.25,rely=.3,relwidth=.15)
    email_entry=Entry(forget_frm,bd=3,font=("",12))
    email_entry.place(relx=.45,rely=.3,relwidth=.2,relheight=.05)

    snotp_btn=Button(forget_frm,text="Send OTP",font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=fgsend_otp)
    snotp_btn.place(relx=.32,rely=.4,relwidth=.1,relheight=.05)

    reset_btn=Button(forget_frm,text="Reset",font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    reset_btn.place(relx=.45,rely=.4,relwidth=.1,relheight=.05)

    entotp_lbl=Label(forget_frm,text='ENTER OTP',font=("arial",12,"bold"),bg='light grey',fg="Navy blue")
    entotp_lbl.place(relx=.25,rely=.5,relwidth=.15)
    entotp_entry=Entry(forget_frm,bd=3,font=("",12))
    entotp_entry.place(relx=.45,rely=.5,relwidth=.15,relheight=.05)

    submit_otp_btn=Button(forget_frm,text="Submit",font=("arial",12,"bold"),bg='light grey',fg="Navy blue",command=resetpass_uacn)
    submit_otp_btn.place(relx=.4,rely=.6,relwidth=.1,relheight=.05)
    
    

main_frame()
main_win.mainloop() # To display we use this command..
