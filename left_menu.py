from main import *
from app_master import *
from app_sales import *

from PIL import ImageTk, Image


def control(a):

    ############## novo #############
    if a == 'home':
        for widget in frame_main.winfo_children():
            widget.destroy()
        ############### App Master ###########
        home()

    if a == 'master':
        for widget in frame_main.winfo_children():
            widget.destroy()
        ############# App Motoristas #########
        master()

    if a == 'sales':
        for widget in frame_main.winfo_children():
            widget.destroy()
        ############### App Despesa ###########
        sales()

    if a == 'retirar':
        for widget in frame_main.winfo_children():
            widget.destroy()
        ############### App Retirar ###########
        #app_retirar_frame()


################ Buttons on frame_left  ##################

img_app = Image.open('images/bill1.png')
img_app = img_app.resize((50, 50), Image.ANTIALIAS)
img_app = ImageTk.PhotoImage(img_app)
app_ = Label(frame_top,width=1380, text=" Billing Software", image=img_app, compound=LEFT,
             relief="raised", anchor=CENTER, font=('Ivy 16 bold'), bg=co9, fg=co1)
app_.place(x=0, y=0)

img_home = Image.open('images/livro-1.png')
img_home = img_home.resize((25, 25), Image.ANTIALIAS)
img_home = ImageTk.PhotoImage(img_home)

b_home = Button(frame_left, text="Home", width=50,image=img_home, compound=LEFT,  bg=co4, fg="white",
                  font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('home'))
b_home.grid(row=0, column=0,  sticky=NSEW, pady=15, padx=5)


img_master = Image.open('images/livro-3.png')
img_master = img_master.resize((25, 25), Image.ANTIALIAS)
img_master = ImageTk.PhotoImage(img_master)
b_master = Button(frame_left, text=" Master", width=50,image=img_master, compound=LEFT,  bg=co4, fg="white",
                  font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('master'))
b_master.grid(row=1, column=0,  sticky=NSEW, pady=7, padx=5)

img_sales = Image.open('images/livro-4.png')
img_sales = img_sales.resize((25, 25), Image.ANTIALIAS)
img_sales = ImageTk.PhotoImage(img_sales)

b_sales = Button(frame_left, text=" Sales", width=50, image=img_sales, compound=LEFT,  bg=co4, fg="white",
                    font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('sales'))
b_sales.grid(row=2, column=0,  sticky=NSEW, pady=7, padx=5)


img_purchase = Image.open('images/membro.png')
img_purchase = img_purchase.resize((25, 25), Image.ANTIALIAS)
img_purchase = ImageTk.PhotoImage(img_purchase)

b_purchase = Button(frame_left, text=" Purchase", width=50, image=img_purchase, compound=LEFT,  bg=co4, fg="white",
                   font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('carro'))
b_purchase.grid(row=3, column=0,  sticky=NSEW, pady=7, padx=5)

img_inventory = Image.open('images/reporte.png')
img_inventory = img_inventory.resize((25, 25), Image.ANTIALIAS)
img_inventory = ImageTk.PhotoImage(img_inventory)

b_inventory = Button(frame_left, text=" Inventory", width=80, image=img_inventory, compound=LEFT,  bg=co4, fg="white",
                   font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('carro'))
b_inventory.grid(row=4, column=0,  sticky=NSEW, pady=7, padx=5)

img_help = Image.open('images/admin.png')
img_help = img_help.resize((25, 25), Image.ANTIALIAS)
img_help = ImageTk.PhotoImage(img_help)

b_help = Button(frame_left, text=" Help", width=150, image=img_help, compound=LEFT,  bg=co4, fg="white",
                 font=('Ivy 10 bold'), anchor="nw", relief=FLAT, command=lambda: control('carro'))
b_help.grid(row=5, column=0,  sticky=NSEW, pady=7, padx=5)


root_main.mainloop()
