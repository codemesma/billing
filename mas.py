from tkinter import *
import tkinter.messagebox
import tkinter
from tkinter import ttk
import tkinter as tk
from datetime import date
from tkcalendar import Calendar, DateEntry
import sqlite3
from PIL import Image, ImageTk
import os
import datetime
import time
from tkinter.font import Font
from tkinter import filedialog

#import mysql.connector


class home:

    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        
        self.root.config(bg='white')
        photoimage = ImageTk.PhotoImage(Image.open('bg1.png'))
        l=Label(self.root, image=photoimage)
        l.image=photoimage
        l.place(x=0,y=0)
        
        l1=Label(self.root,text="Total"+"\n"+"Sales: ",font=("Goudy old styel",30,'bold'),fg='white',bg="#22c0e1")
        l1.place(x=300,y=100)

        l1=Label(self.root,text="Total"+"\n"+"Purchases:",font=("Goudy old styel",25,'bold'),fg='white',bg="#2076ad")
        l1.place(x=600,y=100)

        l1=Label(self.root,text="Total"+"\n"+"Inventory:",font=("Goudy old styel",25,'bold'),fg='white',bg="#2340cd")
        l1.place(x=1000,y=100)
   
       
       
        #========================================Heading=========================================================#
        def tick():
            time_string = time.strftime('%H:%M:%S')
            # if time string has changed, update it
            schltime.config(text=time_string)
            schltime.after(200, tick)

        Time=StringVar()
        Time.set(time.strftime("%H:%M:%S"))
        schltitle=Label(self.root,relief=GROOVE,text="Billing Software",font=('Voice In My Head',30,'bold'),bd=10,bg="Grey",fg="Orange")
        schltitle.pack(side=TOP,fill=X)
        schltime=Label(self.root,relief=GROOVE,text=Time.get(),font=('Arial',15,'bold'),bd=0,bg="Grey",fg="white")
        schltime.place(x=1250,y=17)
        tick()
        
        #============================================Left frame==================================================#
       
       
                
        leftframe=Frame(self.root,height=100,width=40,bd=5,relief=GROOVE,bg="#22cfed")
        leftframe.pack(side=LEFT,fill=Y)
       
        B1=Button(leftframe,text="Home",width=8,relief=GROOVE,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="Grey",command="#").grid(row=0,column=0,sticky=W)
        #B2=Button(leftframe,text="Master",relief=SUNKEN,width=8,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,bg="#fa3030",fg="white",command=self.window).grid(row=1,column=0,sticky=W)
        B3=Button(leftframe,text="Sales",width=8,relief=GROOVE,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white",command="#").grid(row=2,column=0,sticky=W)
        B4=Button(leftframe,text="Purchase",width=8,relief=GROOVE,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white",command="#").grid(row=3,column=0,sticky=W)
        B5=Button(leftframe,text="Inventory",width=8,relief=GROOVE,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white").grid(row=4,column=0,sticky=W)
        B5=Button(leftframe,text="Help",width=8,relief=GROOVE,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white").grid(row=5,column=0,sticky=W)
        B6=Button(leftframe,text="Logout",width=8,relief=GROOVE,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white",command=self.root.destroy).grid(row=6,column=0,sticky=W)
   
       
        
       
                
       
        
       
        mb=Menubutton(leftframe,text="Master",relief=GROOVE,width=8,font=('Copperplate Gothic Bold',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white")
        mb.menu=Menu(mb)
        mb['menu']=mb.menu
        mb.menu.add_command(label="Comapany details",command=self.company_details)
        mb.menu.add_command(label="Contact details",command=self.contact_details)
        mb.menu.add_command(label="comapany Account details",command=self.company_Account_details)
        mb.menu.add_command(label="Customer details",command=self.Customer_details)
        mb.menu.add_command(label="Supplier Master",command=self.supplier_details)
        mb.menu.add_command(label="Unit",command=self.unit)
        mb.menu.add_command(label="Item Group",command=self.item_group)
        mb.menu.add_command(label="Item Details",command=self.item_details)
        mb.menu.add_command(label="Employee Master",command=self. Employee_Master)
        mb.menu.add_command(label="Month details",command=self.month_details)
        mb.menu.add_command(label="Country Master",command=self. Country_master)
        mb.menu.add_command(label="State Details",command=self.state_details)
        mb.menu.add_command(label="City/District",command=self.city)
        mb.menu.add_command(label="Place Details",command=self.Place_details)
        mb.menu.add_command(label="Role Master",command=self.role_master)
        mb.menu.add_command(label="Role maping",command="#")
        mb.menu.add_command(label="Transaction Setting details",command=self.transaction_setting_details)
        mb.grid(row=1,column=0)



     
    def company_details(self):
        #root=Toplevel()
        company_name=StringVar()
        trade_name=StringVar()
        # logo=StringVar()
        def quit():
            mainframe1.destroy()
        def openfile():

            filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            print(filename)
            f=filename.replace("/","\\")
            print(f)
            with open(f, 'rb') as file:
                 binaryData = file.read()
            return binaryData
        def insert1():
            print(company_name.get())
            print(trade_name.get())
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            t=openfile()
            print(t)
            sql = "INSERT INTO company_detail (company_name, trade_name,logo) VALUES (%s, %s, %s)"
            val = (company_name.get(), trade_name.get(),t )
            mycursor.execute(sql, val)
            cur.commit()
            messagebox.showinfo("showinfo", "Details are Succesfully Added") 
        mainframe1=Frame(self.root, bd=4, width=600, relief=RIDGE, bg='white')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        

        hlabel=Label(mainframe1,text="COMAPANY DETAILS",font=("Dash Horizon",20,'bold'),bg='white')
        hlabel.place(x=400,y=10)

        clabel=Label(mainframe1,text="Comapany Name",font=("Code New Roman",20,'bold'),bg='white').place(x=300,y=100)

        tlabel=Label(mainframe1,text="Trade Name",font=("Code New Roman",20,'bold'),bg='white').place(x=300,y=150)
        llabel=Label(mainframe1,text="Logo",font=("Code New Roman",20,'bold'),bg='white').place(x=300,y=200)

       

        e1=Entry(mainframe1,font=("Times New Roman",15,'bold') ,bd=2,textvariable=company_name).place(x=600,y=100)

        e2=Entry(mainframe1,font=("Times New Roman",15,'bold') ,bd=2,textvariable=trade_name).place(x=600,y=150)
        #e3=Entry(mainframe1,font=("Times New Roman",15,'bold'), bd=2,textvariable=logo).grid(row=3,column=4)

##        photo1=PhotoImage(file="submit.png")
##        image1 = photo1.subsample(3, 3)
##
##        b1=  Button(mainframe1, image=image1,borderwidth=0,bg="white",command=insert1)
##        b1.image=image1
##        b1.place(x=300,y=250)
        B1=Button(mainframe1,text="New",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="blue",command="#").place(x=200,y=250)
        B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="Red",command=insert1).place(x=400,y=250)
        B1=Button(mainframe1,text="Cancel",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="Grey",command=quit)
        B1.place(x=800,y=250)
        B1=Button(mainframe1,text="upload file",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="green",command=openfile)
        B1.place(x=600,y=200)
        
    def company_Account_details(self):
        def quit():
             mainframe1.destroy()
##        self.root=Toplevel()
##        self.root.title("company_Account_details")
##        self.root.geometry("900x700")
##        self.root.config(bg='black')
        bank_name=StringVar()
        bank_address=StringVar()
        account_no=StringVar()
        account_type=StringVar()
        place=StringVar()
        branch=StringVar()
        ifsc_code=StringVar()
        micr_no=StringVar()
        def inser3():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql2 = "INSERT INTO company_account (bank_name, bank_address,account_no,account_type,place,branch,ifsc_code,micr_no) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
            val = (bank_name.get(), bank_address.get(),account_no.get(),account_type.get(),place.get(),branch.get(),ifsc_code.get(),micr_no.get())
            mycursor.execute(sql2, val)
            cur.commit()

        mainframe1=Frame(self.root,highlightthickness=20,highlightbackground='pink',bg='white')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

       


        clabel=Label(mainframe1,text="Bank Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0)

        tlabel=Label(mainframe1,text="Bank Address",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0)
        llabel=Label(mainframe1,text="Account No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0)

        llabel=Label(mainframe1,text="Account type",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0)
        llabel=Label(mainframe1,text="Place",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0)
        llabel=Label(mainframe1,text="Branch",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0)
        llabel=Label(mainframe1,text="IFSC",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0)
        llabel=Label(mainframe1,text="MICR No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0)
        

       

        e1=Entry(mainframe1,textvariable=bank_name ,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=1)

        e2=Entry(mainframe1,textvariable=bank_address,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=1)
        e3=Entry(mainframe1,textvariable=account_no, font=("Times New Roman",15,'bold'), bd=2).grid(row=2,column=1)

        e3=Entry(mainframe1,textvariable =account_type, font=("Times New Roman",15,'bold'), bd=2).grid(row=3,column=1)
        e3=Entry(mainframe1,textvariable=place, font=("Times New Roman",15,'bold'), bd=2).grid(row=4,column=1)
        e3=Entry(mainframe1,textvariable=branch, font=("Times New Roman",15,'bold'), bd=2).grid(row=5,column=1)
        e3=Entry(mainframe1,textvariable=ifsc_code,font=("Times New Roman",15,'bold'), bd=2).grid(row=6,column=1)
        e3=Entry(mainframe1,textvariable=micr_no, font=("Times New Roman",15,'bold'), bd=2).grid(row=7,column=1)
        

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button(mainframe1, image=image1,borderwidth=0,bg="white",command=inser3)
        b1.image=image1
        b1.grid(row=9,column=0)
        b2=Button(mainframe1,text="Cancel",font=("Arial",20,'bold'),fg="white",bg='Grey',bd=4,command=quit).grid(row=9,column=1)

     
    def contact_details(self):
##        self.root=Toplevel()
##        self.root.title("Masters")
##        self.root.geometry("1350x700+0+0")
##        self.root.config(bg='Ghost White')
       
        def tick():
             time_string = time.strftime('%H:%M:%S')
             # if time string has changed, update it
             htime.config(text=time_string)
             htime.after(200, tick)
        def general_details():
            address1=StringVar()
            address2=StringVar()
            address3=StringVar()
            state=StringVar()
            city=StringVar()
            place=StringVar()
            pin_code=StringVar()
            email_id=StringVar()
            website=StringVar()
            phon_no=StringVar()
            mob_no=StringVar()
            fax_no=StringVar()
            def quit():
                mainframe1.destroy()
            def inser2():
                print(address1.get())
                cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
                mycursor = cur.cursor()
                sql1 = "INSERT INTO contact_detail (address1, address2,address3,state,city,place,pin_code,email_id,website,phon_no,mob_no,fax_no) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (address1.get(), address2.get(),address3.get(),state.get(),city.get(),place.get(),pin_code.get(),email_id.get(),website.get(),phon_no.get(),mob_no.get(),fax_no.get())
                mycursor.execute(sql1, val)
                cur.commit()

            mainframe1=Frame(self.root, bd=4, width=600,bg="white")
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

            

            clabel=Label(mainframe1,text="Address1",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="Address2",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Address3",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe4=Label(mainframe1,text="state",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe5=Label(mainframe1,text="City",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe6=Label(mainframe1,text="Place",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0,padx=10,pady=10)
            clabe7=Label(mainframe1,text="Pin code",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0,padx=10,pady=10)
            clabe8=Label(mainframe1,text="Email Id",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0,padx=10,pady=10)
            clabe9=Label(mainframe1,text="Website",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=2,padx=10,pady=10)
            clabe10=Label(mainframe1,text="Phone No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=2,padx=10,pady=10)
            clabe11=Label(mainframe1,text="Mob",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=2)
            clabe12=Label(mainframe1,text="Fax No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=2,padx=10,pady=10)

           
           

            e1=Entry(mainframe1,textvariable=address1 ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=address2 ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable= address3,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e1=Entry(mainframe1,textvariable=state ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=3,column=1,padx=10,pady=10)
            e2=Entry(mainframe1,textvariable= city,font=("Times New Roman",20,'bold') ,bd=2).grid(row=4,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=place ,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            e1=Entry(mainframe1,textvariable= pin_code,font=("Times New Roman",20,'bold') ,bd=2).grid(row=6,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=email_id ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=7,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=website ,font=("Times New Roman",20,'bold'), bd=2).grid(row=0,column=3,padx=10,pady=10)
            e1=Entry(mainframe1,textvariable= phon_no,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=3,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable= mob_no,font=("Times New Roman",20,'bold') ,bd=2).grid(row=2,column=3,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable= fax_no,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=3,padx=10,pady=10)
            
            B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser2).grid(row=11,column=0,sticky=W)
            B2=Button(mainframe1,text="Cancel",relief=SUNKEN,width=8,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="Gray",fg="white",command=quit).grid(row=11,column=2,sticky=W)
        
        def other_details():
      
            def quit():
                mainframe1.destroy()

            def gst():
                win=Toplevel()
                mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
                mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
                clabel=Label(mainframe1,text="  GSTIN NO." ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
                clabe2=Label(mainframe1,text="GSTIN DATE.",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
                clabe3=Label(mainframe1,text="GST Category",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
                e1=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

                e2=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
                e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
                #B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command="#").grid(row=3,column=0,sticky=W)
                

            mainframe1=Frame(self.root, bd=4, width=600, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

            

            clabel=Label(mainframe1,text="Establishment"+"\n"+" Date",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="CIN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="CIN Date",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe4=Label(mainframe1,text="GST Applicable",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe5=Label(mainframe1,text="PAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe6=Label(mainframe1,text="PAN DATE",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0,padx=10,pady=10)
            clabe7=Label(mainframe1,text="TAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0,padx=10,pady=10)
            clabe8=Label(mainframe1,text="TAN DATE",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0,padx=10,pady=10)
            clabe9=Label(mainframe1,text="Aggregate Turnover"+"\n"+"of Previuos"+"\n"+"Financial Year",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=2,padx=10,pady=10)
           

           
           

            e1=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e1=Button(mainframe1,text="Click Here",font=("Times New Roman",20,'bold') ,bd=2,command=gst).grid(row=3,column=1,padx=10,pady=10)
            e2=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=4,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            e1=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=6,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,font=("Times New Roman",20,'bold') ,bd=2).grid(row=7,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=0,column=3,padx=10,pady=10)
           
            
            B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command="#").grid(row=11,column=0,sticky=W)
            B2=Button(mainframe1,text="Cancel",relief=SUNKEN,width=8,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white",command=quit).grid(row=11,column=2,sticky=W)

     


        def quit():
            leftframe.destroy()


        leftframe=Frame(self.root,height=100,width=50,bd=5,relief=GROOVE,bg="#0d43f0")
        leftframe.pack(side=LEFT,fill=Y)
       
        B1=Button(leftframe,text="General"+"\n"+"Details",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="#7202fc",command=general_details).grid(row=0,column=0,sticky=W)
        B2=Button(leftframe,text="Other"+"\n"+"Details",relief=SUNKEN,width=8,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="#7202fc",fg="white",command=other_details).grid(row=1,column=0,sticky=W)
 
        B3=Button(leftframe,text="Exit",relief=SUNKEN,width=8,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,bg="Grey",fg="white",command=quit).grid(row=2,column=0,sticky=W)
 
     
    def Customer_details(self):
        name=StringVar()
        print_name=StringVar()
        address1=StringVar()
        address2=StringVar()
        address3=StringVar()
        Country=StringVar()
        state=StringVar()
        place=StringVar()
        pin_code=StringVar()
        phone_no=StringVar()
        mob_no=StringVar()
        email=StringVar()
        GSTIN=StringVar()
        GSTIN_UIN=StringVar()
        GST_Category=StringVar()
        PAN_No=StringVar()
        TAN_No=StringVar()
        All_Data_verified=StringVar()
        Contact_Title=StringVar()
        contact_pname=StringVar()
        Designation=StringVar()
        contact_Phone_No=StringVar()
        Mobile_No=StringVar()
        WhatsApp_No=StringVar()
        Other_No=StringVar()
        Email_ID=StringVar()
        def add():
            l=[address1.get(),address2.get(),address3.get(),Country.get(),state.get(),place.get(),pin_code.get(),phone_no.get(),mob_no.get(),email.get()]
            return l
        def address():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            llabel=Label(mainframe1,text="Address1",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0)
            llabel=Label(mainframe1,text="Address2",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0)
            llabel=Label(mainframe1,text="Address3",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0)
            llabel=Label(mainframe1,text="Country",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0)
            llabel=Label(mainframe1,text="State",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0)
            llabel=Label(mainframe1,text="Place",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0)
            llabel=Label(mainframe1,text="Pin code",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0)
            llabel=Label(mainframe1,text="Phone No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0)
            llabel=Label(mainframe1,text="Mobile No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=8,column=0)
            llabel=Label(mainframe1,text="Email Id",font=("Code New Roman",20,'bold'),bg='white').grid(row=9,column=0)
            

            e1=Entry(mainframe1,textvariable=address1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=1)
            e2=Entry(mainframe1,textvariable=address2 ,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=1)
            e3=Entry(mainframe1,textvariable=address3 ,font=("Times New Roman",15,'bold'), bd=2).grid(row=2,column=1)
            e3=Entry(mainframe1,textvariable=Country,font=("Times New Roman",15,'bold'), bd=2).grid(row=3,column=1)
            e3=Entry(mainframe1,textvariable=state ,font=("Times New Roman",15,'bold'), bd=2).grid(row=4,column=1)
            e3=Entry(mainframe1,textvariable= place,font=("Times New Roman",15,'bold'), bd=2).grid(row=5,column=1)
            e3=Entry(mainframe1,textvariable= pin_code,font=("Times New Roman",15,'bold'), bd=2).grid(row=6,column=1)
            e3=Entry(mainframe1,textvariable=phone_no, font=("Times New Roman",15,'bold'), bd=2).grid(row=7,column=1)
            e3=Entry(mainframe1,textvariable=  mob_no,font=("Times New Roman",15,'bold'), bd=2).grid(row=8,column=1)
            e3=Entry(mainframe1,textvariable= email, font=("Times New Roman",15,'bold'), bd=2).grid(row=9,column=1)
            B1=Button(mainframe1, text="Submit",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add).grid(row=10,column=1)
        def add1():
            g=[GSTIN.get(),GSTIN_UIN.get(),GST_Category.get(),PAN_No.get(),TAN_No.get(),All_Data_verified.get()]
            return g


        def gst():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            clabel=Label(mainframe1,text="  GSTIN/UIN" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="GSTIN/UIN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="GST Category",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="PAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="TAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe3=Checkbutton(mainframe1,text="All data Verified",font=("Code New Roman",20,'bold'),bg='white',command="#").grid(row=5,column=0,padx=10,pady=10)
            e1=Entry(mainframe1,textvariable=GSTIN,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=GSTIN_UIN,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=GST_Category,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=PAN_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=TAN_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
            #e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add1).grid(row=6,column=0,sticky=W)

        def add2():
            c=[Contact_Title.get(),contact_pname.get(),Designation.get()]
            return c

        def contact():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            clabel=Label(mainframe1,text="Contact Title" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Desigination",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Phone No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Mobile No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Whatsapp No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Other No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Email",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0,padx=10,pady=10)
            
            e1=Entry(mainframe1,textvariable=Contact_Title,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=contact_pname,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Designation,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=contact_Phone_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Mobile_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=WhatsApp_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Other_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=6,column=1,padx=10,pady=10)

            e3=Entry(mainframe1,textvariable=Email_ID,font=("Times New Roman",20,'bold'), bd=2).grid(row=7,column=1,padx=10,pady=10)
            
            B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add2).grid(row=8,column=0,sticky=W)
            
        def inser4():
            a=add()
            g=add1()
            c=add2()
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql3 = "INSERT INTO customer_detail (name, print_name,address1,address2,address3,Country,state,place,pin_code,phone_no,mob_no,email,GSTIN,GSTIN_UIN,GST_Category,PAN_No,TAN_No,All_Data_verified,	Contact_Title,contact_pname,Designation	,contact_Phone_No,Mobile_No,WhatsApp_No,Other_No,Email_ID) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (name.get(), print_name.get(),a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],g[0],g[1],g[2],g[3],g[4],g[5],c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7])
            mycursor.execute(sql3, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        

        mainframe1=Frame(self.root,highlightthickness=20,highlightbackground='orange',bg='white')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)


        clabel=Label( mainframe1,text="Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)

        tlabel=Label( mainframe1,text="Print Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        b=Button( mainframe1,text="Address",width=10,font=("Code New Roman",20,'bold'),bg='blue',fg="white",command=address).grid(row=3,column=0,padx=10,pady=10)
        b=Checkbutton( mainframe1,text="GST Applicable",font=("Code New Roman",20,'bold'),bg='white',command=gst).grid(row=5,column=0,padx=10,pady=10)

        b=Button( mainframe1,text="Contact details",font=("Code New Roman",20,'bold'),bg='green',fg="white",command=contact).grid(row=6,column=0,padx=10,pady=10)

        b=Button( mainframe1,text="Exit",font=("Code New Roman",20,'bold'),bg='Grey',fg="white",command=quit).grid(row=6,column=5,padx=10,pady=10)
        
        e1=Entry( mainframe1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=2,padx=10,pady=10)
        e2=Entry( mainframe1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=2,padx=10,pady=10)
        
        

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button( mainframe1, image=image1,borderwidth=0,bg="white",command=inser4)
        b1.image=image1
        b1.grid(row=8,column=0,padx=10,pady=10)
    def supplier_details(self):
        name=StringVar()
        print_name=StringVar()
        address1=StringVar()
        address2=StringVar()
        address3=StringVar()
        Country=StringVar()
        state=StringVar()
        place=StringVar()
        pin_code=StringVar()
        phone_no=StringVar()
        mob_no=StringVar()
        email=StringVar()
        GSTIN=StringVar()
        GSTIN_UIN=StringVar()
        GST_Category=StringVar()
        PAN_No=StringVar()
        TAN_No=StringVar()
        All_Data_verified=StringVar()
        Contact_Title=StringVar()
        contact_pname=StringVar()
        Designation=StringVar()
        contact_Phone_No=StringVar()
        Mobile_No=StringVar()
        WhatsApp_No=StringVar()
        Other_No=StringVar()
        Email_ID=StringVar()
        def add():
            l=[address1.get(),address2.get(),address3.get(),Country.get(),state.get(),place.get(),pin_code.get(),phone_no.get(),mob_no.get(),email.get()]
            return l
        def address():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            llabel=Label(mainframe1,text="Address1",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0)
            llabel=Label(mainframe1,text="Address2",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0)
            llabel=Label(mainframe1,text="Address3",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0)
            llabel=Label(mainframe1,text="Country",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0)
            llabel=Label(mainframe1,text="State",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0)
            llabel=Label(mainframe1,text="Place",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0)
            llabel=Label(mainframe1,text="Pin code",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0)
            llabel=Label(mainframe1,text="Phone No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0)
            llabel=Label(mainframe1,text="Mobile No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=8,column=0)
            llabel=Label(mainframe1,text="Email Id",font=("Code New Roman",20,'bold'),bg='white').grid(row=9,column=0)
            

            e1=Entry(mainframe1,textvariable=address1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=1)
            e2=Entry(mainframe1,textvariable=address2 ,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=1)
            e3=Entry(mainframe1,textvariable=address3 ,font=("Times New Roman",15,'bold'), bd=2).grid(row=2,column=1)
            e3=Entry(mainframe1,textvariable=Country,font=("Times New Roman",15,'bold'), bd=2).grid(row=3,column=1)
            e3=Entry(mainframe1,textvariable=state ,font=("Times New Roman",15,'bold'), bd=2).grid(row=4,column=1)
            e3=Entry(mainframe1,textvariable= place,font=("Times New Roman",15,'bold'), bd=2).grid(row=5,column=1)
            e3=Entry(mainframe1,textvariable= pin_code,font=("Times New Roman",15,'bold'), bd=2).grid(row=6,column=1)
            e3=Entry(mainframe1,textvariable=phone_no, font=("Times New Roman",15,'bold'), bd=2).grid(row=7,column=1)
            e3=Entry(mainframe1,textvariable=  mob_no,font=("Times New Roman",15,'bold'), bd=2).grid(row=8,column=1)
            e3=Entry(mainframe1,textvariable= email, font=("Times New Roman",15,'bold'), bd=2).grid(row=9,column=1)
            B1=Button(mainframe1, text="Submit",width=8,relief=SUNKEN,font=('Arial',15,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add).grid(row=10,column=1)
        def add1():
            g=[GSTIN.get(),GSTIN_UIN.get(),GST_Category.get(),PAN_No.get(),TAN_No.get(),All_Data_verified.get()]
            return g


        def gst():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            clabel=Label(mainframe1,text="  GSTIN/UIN" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="GSTIN/UIN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="GST Category",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="PAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="TAN NO.",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe3=Checkbutton(mainframe1,text="All data Verified",font=("Code New Roman",20,'bold'),bg='white',command="#").grid(row=5,column=0,padx=10,pady=10)
            e1=Entry(mainframe1,textvariable=GSTIN,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=GSTIN_UIN,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=GST_Category,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=PAN_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=TAN_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
            #e3=Entry(mainframe1,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add1).grid(row=6,column=0,sticky=W)

        def add2():
            c=[Contact_Title.get(),contact_pname.get(),Designation.get()]
            return c

        def contact():
            win=Toplevel()
            mainframe1=Frame(win, bd=4, width=500, relief=RIDGE, bg='white')
            mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
            clabel=Label(mainframe1,text="Contact Title" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
            clabe2=Label(mainframe1,text="Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Desigination",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Phone No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Mobile No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Whatsapp No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Other No.",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0,padx=10,pady=10)
            clabe3=Label(mainframe1,text="Email",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0,padx=10,pady=10)
            
            e1=Entry(mainframe1,textvariable=Contact_Title,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)

            e2=Entry(mainframe1,textvariable=contact_pname,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Designation,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=contact_Phone_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Mobile_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=WhatsApp_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
            e3=Entry(mainframe1,textvariable=Other_No,font=("Times New Roman",20,'bold'), bd=2).grid(row=6,column=1,padx=10,pady=10)

            e3=Entry(mainframe1,textvariable=Email_ID,font=("Times New Roman",20,'bold'), bd=2).grid(row=7,column=1,padx=10,pady=10)
            
            B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=add2).grid(row=8,column=0,sticky=W)
            
        def inser4():
            a=add()
            g=add1()
            c=add2()
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql3 = "INSERT INTO customer_detail (name, print_name,address1,address2,address3,Country,state,place,pin_code,phone_no,mob_no,email,GSTIN,GSTIN_UIN,GST_Category,PAN_No,TAN_No,All_Data_verified,	Contact_Title,contact_pname,Designation	,contact_Phone_No,Mobile_No,WhatsApp_No,Other_No,Email_ID) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (name.get(), print_name.get(),a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],g[0],g[1],g[2],g[3],g[4],g[5]	,c[0],c[1],c[2]	,c[3],c[4],c[5],c[6],c[7])
            mycursor.execute(sql3, val)
            cur.commit()

        

        def quit():
            mainframe1.destroy()
        

        mainframe1=Frame(self.root,highlightthickness=20,highlightbackground='orange',bg='white')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)


        clabel=Label( mainframe1,text="Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)

        tlabel=Label( mainframe1,text="Print Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        b=Button( mainframe1,text="Address",width=10,font=("Code New Roman",20,'bold'),bg='blue',fg="white",command=address).grid(row=3,column=0,padx=10,pady=10)
        b=Checkbutton( mainframe1,text="GST Applicable",font=("Code New Roman",20,'bold'),bg='white',command=gst).grid(row=5,column=0,padx=10,pady=10)

        b=Button( mainframe1,text="Contact details",font=("Code New Roman",20,'bold'),bg='green',fg="white",command=contact).grid(row=6,column=0,padx=10,pady=10)

        b=Button( mainframe1,text="Exit",font=("Code New Roman",20,'bold'),bg='Grey',fg="white",command=quit).grid(row=6,column=5,padx=10,pady=10)
        
        e1=Entry( mainframe1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=2,padx=10,pady=10)
        e2=Entry( mainframe1,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=2,padx=10,pady=10)
        
        

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button( mainframe1, image=image1,borderwidth=0,bg="white",command=inser4)
        b1.image=image1
        b1.grid(row=8,column=0,padx=10,pady=10) 
    def unit(self):
        
        Unite_Code=StringVar()
        Description=StringVar()
        def inser6():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO  unit (Unite_Code, Description) VALUES (%s, %s)"
            val = (Unite_Code.get(), Description.get() )
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()

        mainframe1=Frame(self.root,highlightthickness=20)
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

        

        clabel=Label(mainframe1,text="Unit Code",font=("Code New Roman",15,'bold'),bg='white').grid(row=0,column=8)

        tlabel=Label(mainframe1,text="Description",font=("Code New Roman",15,'bold'),bg='white').grid(row=1,column=8)
        

       

        e1=Entry(mainframe1,textvariable=Unite_Code, font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=9)

        e2=Entry(mainframe1,textvariable=Description,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=9)
       

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button(mainframe1, image=image1,borderwidth=0,bg="white",command= inser6)
        b1.image=image1
        b1.grid(row=2,column=8)        
        b2=Button(mainframe1,text="Cancle", font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=2,column=9)
     
    def item_group(self):
        Group_Name=StringVar()
        Parent_Group=StringVar()
        Item_Category=StringVar()
        HSN_SAC_Code=StringVar()
        Tax_Rate=StringVar()
        CESS_Rate=StringVar()
        Add_Quantities_Items=StringVar()

        def inser7():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO   item_group (Group_Name, Parent_Group,Item_Category,HSN_SAC_Code,Tax_Rate,CESS_Rate,Add_Quantities_Items) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val = (Group_Name.get(), Parent_Group.get(),Item_Category.get(),HSN_SAC_Code.get(),Tax_Rate.get(),CESS_Rate.get(),Add_Quantities_Items.get() )
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root,highlightthickness=20)
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

        clabel=Label(mainframe1,text="Group Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0)

        tlabel=Label(mainframe1,text="Parent Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0)
        tlabel=Label(mainframe1,text="item Category",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0)
        
        llabel=Label(mainframe1,text="HSN/SAC CODE",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0)
        llabel=Label(mainframe1,text="Tax Rate",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0)
        llabel=Label(mainframe1,text="Css Rate",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0)
        llabel=Label(mainframe1,text="Add Quantities"+"\n"+"of items",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0)

       

        e1=Entry(mainframe1,textvariable=Group_Name, font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=1)

        e2=Entry(mainframe1,textvariable= Parent_Group,font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=1)
        e5=ttk.Combobox(mainframe1,width=18,font=('Times',15,'bold'),state='readonly',textvariable="#")
        e5['values']=("Taxable","Exempted","Nil Rated","Non-GST")
        e5.grid(row=2,column=1)
        e3=Entry(mainframe1,textvariable=HSN_SAC_Code,font=("Times New Roman",15,'bold'), bd=2).grid(row=3,column=1)
        e3=Entry(mainframe1,textvariable=Tax_Rate,font=("Times New Roman",15,'bold'), bd=2).grid(row=4,column=1)
        e3=Entry(mainframe1,textvariable=CESS_Rate,font=("Times New Roman",15,'bold'), bd=2).grid(row=5,column=1)
        e3=Entry(mainframe1,textvariable=Add_Quantities_Items,font=("Times New Roman",15,'bold'), bd=2).grid(row=6,column=1)
        #

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button(mainframe1, image=image1,borderwidth=0,bg="white",command=inser7)
        b1.image=image1
        b1.grid(row=7,column=0)
        b2=Button(mainframe1,text="Exit", font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=7,column=5)
     
        

     
    def item_details(self):
        
        Item_Name=StringVar()
        Item_Type=StringVar()
        Item_Display=StringVar()
        Item_Code=StringVar()
        HSN_SAC_Code=StringVar()
        Item_Group=StringVar()
        Item_Category=StringVar()
        Unit=StringVar()
        Purchase_rate=StringVar()
        Sales_Rate=StringVar()
        Tax_Rate=StringVar()
        CESS_Rate=StringVar()
        Description=StringVar()
        Is_Credit_Available=StringVar()
        def inser8():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO   item_details (Item_Name, Item_Type,Item_Display,Item_Code,HSN_SAC_Code,Item_Group,Item_Category,Unit,Purchase_rate,Sales_Rate,Tax_Rate,CESS_Rate,Description,Is_Credit_Available) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Item_Name.get(), Item_Type.get(),Item_Display.get(),Item_Code.get(),HSN_SAC_Code.get(),Item_Group.get(),Item_Category.get(),Unit.get(),Purchase_rate.get(),Sales_Rate.get(),Tax_Rate.get(),CESS_Rate.get(),Description.get(),Is_Credit_Available.get())
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()

        mainframe1=Frame(self.root,highlightthickness=20,bg='Ghost White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)

        

        clabel=Label(mainframe1,text="Item Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0)

        tlabel=Label(mainframe1,text="Item Type",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0)
        tlabel=Label(mainframe1,text="item display",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0)
        
        llabel=Label(mainframe1,text="item code",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0)
        llabel=Label(mainframe1,text="HSN/SAC CODE",font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0)
        llabel=Label(mainframe1,text="item group",font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0)
        llabel=Label(mainframe1,text="Item Category",font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0)
        llabel=Label(mainframe1,text="unit",font=("Code New Roman",20,'bold'),bg='white').grid(row=7,column=0)
        llabel=Label(mainframe1,text="purchase",font=("Code New Roman",20,'bold'),bg='white').grid(row=8,column=0)
        llabel=Label(mainframe1,text="Sales rate",font=("Code New Roman",20,'bold'),bg='white').grid(row=9,column=0)
        llabel=Label(mainframe1,text="Tax Rate",font=("Code New Roman",20,'bold'),bg='white').grid(row=10,column=0)
        llabel=Label(mainframe1,text="CESS RATE",font=("Code New Roman",20,'bold'),bg='white').grid(row=11,column=0)
        llabel=Label(mainframe1,text="Description",font=("Code New Roman",20,'bold'),bg='white').grid(row=12,column=0)
        llabel=Label(mainframe1,text="Is Credit"+"\n"+" Avilable",font=("Code New Roman",20,'bold'),bg='white').grid(row=13,column=0)

       

        e1=Entry(mainframe1,textvariable=Item_Name,font=("Times New Roman",15,'bold') ,bd=2).grid(row=0,column=1)

        e2=Entry(mainframe1,textvariable=Item_Type , font=("Times New Roman",15,'bold') ,bd=2).grid(row=1,column=1)
    
        e3=Entry(mainframe1,textvariable= Item_Display,font=("Times New Roman",15,'bold'), bd=2).grid(row=2,column=1)
        e3=Entry(mainframe1,textvariable= Item_Code,font=("Times New Roman",15,'bold'), bd=2).grid(row=3,column=1)
        e3=Entry(mainframe1,textvariable= HSN_SAC_Code,font=("Times New Roman",15,'bold'), bd=2).grid(row=4,column=1)
        e3=Entry(mainframe1,textvariable=Item_Group,font=("Times New Roman",15,'bold'), bd=2).grid(row=5,column=1)
        e5=ttk.Combobox(mainframe1,width=18,font=('Times',15,'bold'),state='readonly',textvariable="#")
        e5['values']=("Taxable","Exempted","Nil Rated","Non-GST")
        e5.grid(row=6,column=1)
        e3=Entry(mainframe1,textvariable=Unit ,font=("Times New Roman",15,'bold'), bd=2).grid(row=7,column=1)
        e3=Entry(mainframe1,textvariable=Purchase_rate ,font=("Times New Roman",15,'bold'), bd=2).grid(row=8,column=1)
        e3=Entry(mainframe1,textvariable= Sales_Rate,font=("Times New Roman",15,'bold'), bd=2).grid(row=9,column=1)
        e3=Entry(mainframe1,textvariable=Tax_Rate ,font=("Times New Roman",15,'bold'), bd=2).grid(row=10,column=1)
        e3=Entry(mainframe1,textvariable=CESS_Rate ,font=("Times New Roman",15,'bold'), bd=2).grid(row=11,column=1)
        e3=Entry(mainframe1,textvariable=Description,font=("Times New Roman",15,'bold'), bd=2).grid(row=12,column=1)
        e3=Entry(mainframe1,textvariable= Is_Credit_Available,font=("Times New Roman",15,'bold'), bd=2).grid(row=13,column=1)
        

        photo1=PhotoImage(file="submit.png")
        image1 = photo1.subsample(3, 3)

        b1=  Button(mainframe1, image=image1,borderwidth=0,bg="white",command=inser8)
        b1.image=image1
        b1.grid(row=14,column=0)
        b2=Button(mainframe1,text="Exit", width=10,font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=13,column=9)
     
     
    def Employee_Master(self):
        Employee_Name=StringVar()
        Use_ID=StringVar()
        User_Login=StringVar()
        E_mail_ID=StringVar()
        def inser9():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO    employee_master (Employee_Name, Use_ID,User_Login,E_mail_ID) VALUES (%s, %s,%s,%s)"
            val = (Employee_Name.get(), Use_ID.get(),User_Login.get(),E_mail_ID.get() )
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500,relief=RIDGE, highlightthickness=20,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        clabel=Label(mainframe1,text="Employee Name" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
        clabe2=Label(mainframe1,text="User Id",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="User Login",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="Email Id",font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
        
        e2=Entry(mainframe1,textvariable=Employee_Name ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable=Use_ID ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=User_Login ,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable= E_mail_ID,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
       
        B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser9).grid(row=4,column=1,sticky=W)
        b2=Button(mainframe1,text="Exit",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=4,column=9)
     
     
    def month_details(self):
       
        Month=StringVar()
        Financial_Year=StringVar()
        Locked=StringVar()
        def inser10():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO    month_details (Month, Financial_Year,Locked) VALUES (%s, %s,%s)"
            val = (Month.get(), Financial_Year.get(),Locked.get() )
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        clabel=Label(mainframe1,text="Month" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
        clabe2=Label(mainframe1,text="Financial Year",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="Locked",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
       
        
        e2=Entry(mainframe1,textvariable=Month ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable= Financial_Year,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=Locked ,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
      
       
        B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser10).grid(row=4,column=1,sticky=W)
        b2=Button(mainframe1,text="Exit",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=4,column=9)
     
    def Country_master(self):
        
        Country_Name=StringVar()
        def inser11():
             cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
             mycursor = cur.cursor()
             sql5 = "INSERT INTO     country_master (Country_Name) VALUES (%s)"
             val = (Country_Name.get(),)
             mycursor.execute(sql5, val)
             cur.commit()

        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        clabel=Label(mainframe1,text="Country Name" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=Country_Name ,font=("Times New Roman",20,'bold'), bd=2).grid(row=0,column=1,padx=10,pady=10)
      
       
        B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser11).grid(row=4,column=1,sticky=W)
        b2=Button(mainframe1,text="Exit",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=4,column=9)
    def state_details(self):
        Country_Name=StringVar()
        State_Name=StringVar()
        State_Code=StringVar()
        def inser12():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO    state_details (Country_Name, State_Name,State_Code) VALUES (%s, %s,%s)"
            val = (Country_Name.get(), State_Name.get(),State_Code.get() )
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        clabel=Label(mainframe1,text="Country Name" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=0,column=0,padx=10,pady=10)
        clabe2=Label(mainframe1,text="State Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="State Code",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
       
        
        e2=Entry(mainframe1,textvariable= Country_Name, font=("Times New Roman",20,'bold') ,bd=2).grid(row=0,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable=State_Name ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=State_Code ,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
      
       
        B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser12).grid(row=4,column=1,sticky=W)
        b2=Button(mainframe1,text="Cancle",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=4,column=9)
     
    def city(self):

        State_Name=StringVar()
        City_Name=StringVar()

        def inser13():
                cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
                mycursor = cur.cursor()
                sql4 = "INSERT INTO    city_district (State_Name, City_Name) VALUES (%s, %s)"
                val = (State_Name.get(), City_Name.get())
                mycursor.execute(sql4, val)
                cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        clabe2=Label(mainframe1,text="State Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="city Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
       
        
       
        e2=Entry(mainframe1,textvariable= State_Name, font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=City_Name ,font=("Times New Roman",20,'bold'), bd=2).grid(row=2,column=1,padx=10,pady=10)
      
       
        B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser13).grid(row=4,column=1,sticky=W)
        b2=Button(mainframe1,text="Cancle",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=4,column=9)

     
    def Place_details(self):
        State_Name=StringVar()
        City_Name=StringVar()
        Place_Name=StringVar()
        PIN_Code=StringVar()

        def inser14():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO    place_details (State_Name, City_Name,Place_Name,PIN_Code) VALUES (%s, %s,%s,%s)"
            val = (State_Name.get(), City_Name.get(),Place_Name.get(),PIN_Code.get())
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        
        clabe2=Label(mainframe1,text="State Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="City Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Place Name" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Pin Code" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
       
        
        e2=Entry(mainframe1,textvariable=State_Name ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable=City_Name ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=2,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable= Place_Name, font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=PIN_Code ,font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
      
      
       
        B1=Button(mainframe1,text="Submit",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser14).grid(row=5,column=1,sticky=W)
        b2=Button(mainframe1,text="Exit",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=5,column=9)

     
    def role_master(self):
        
        Role_Name=StringVar()
        Landing_From=StringVar()
        def inser15():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO     role_master (Role_Name, Landing_From) VALUES (%s, %s)"
            val = (Role_Name.get(), Landing_From.get())
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        
        clabe2=Label(mainframe1,text="Role Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="Landing From",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
       
       
        
        e2=Entry(mainframe1,textvariable= Role_Name, font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable=Landing_From , font=("Times New Roman",20,'bold') ,bd=2).grid(row=2,column=1,padx=10,pady=10)
       
      
      
       
        B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser15).grid(row=5,column=1,sticky=W)
        b2=Button(mainframe1,text="Cancle",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=5,column=9)


     

    def transaction_setting_details(self):
        Transaction_Type=StringVar()
        Transaction_Series_Name=StringVar()
        Prefix=StringVar()
        Suffix=StringVar()
        Starting_No=StringVar()
        Digits=StringVar()

        def inser16():
            cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
            mycursor = cur.cursor()
            sql4 = "INSERT INTO      transaction_settings (Transaction_Type, Transaction_Series_Name,Prefix,Suffix,Starting_No,Digits) VALUES (%s, %s,%s,%s,%s,%s)"
            val = (Transaction_Type.get(), Transaction_Series_Name.get(),Prefix.get(),Suffix.get(),Starting_No.get(),Digits.get())
            mycursor.execute(sql4, val)
            cur.commit()
        def quit():
            mainframe1.destroy()
        mainframe1=Frame(self.root, bd=4, width=500, relief=RIDGE,bg='White')
        mainframe1.pack(side=LEFT,fill=BOTH,expand=True)
        
        clabe2=Label(mainframe1,text="Transaction Type",font=("Code New Roman",20,'bold'),bg='white').grid(row=1,column=0,padx=10,pady=10)
        clabe3=Label(mainframe1,text="Transaction Series Name",font=("Code New Roman",20,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Prefix" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=3,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Suffix" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=4,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Starting No." ,font=("Code New Roman",20,'bold'),bg='white').grid(row=5,column=0,padx=10,pady=10)
        clabel=Label(mainframe1,text="Digits" ,font=("Code New Roman",20,'bold'),bg='white').grid(row=6,column=0,padx=10,pady=10)
       
        
        e2=Entry(mainframe1,textvariable=Transaction_Type , font=("Times New Roman",20,'bold') ,bd=2).grid(row=1,column=1,padx=10,pady=10)
        e2=Entry(mainframe1,textvariable =Transaction_Series_Name ,font=("Times New Roman",20,'bold') ,bd=2).grid(row=2,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable= Prefix,font=("Times New Roman",20,'bold'), bd=2).grid(row=3,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable= Suffix, font=("Times New Roman",20,'bold'), bd=2).grid(row=4,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=Starting_No ,font=("Times New Roman",20,'bold'), bd=2).grid(row=5,column=1,padx=10,pady=10)
        e3=Entry(mainframe1,textvariable=Digits ,font=("Times New Roman",20,'bold'), bd=2).grid(row=6,column=1,padx=10,pady=10)
        
       
      
      
       
        B1=Button(mainframe1,text="Save",width=8,relief=SUNKEN,font=('Arial',10,'bold'),padx=10,pady=10,bd=5,fg="white",bg="red",command=inser16).grid(row=7,column=1,sticky=W)
        b2=Button(mainframe1,text="Cancle",width=10, font=("Times New Roman",15,'bold') ,bd=2,bg="Grey",fg="white",command=quit).grid(row=7,column=9)
root=Tk()
app=home(root)
root.mainloop()
