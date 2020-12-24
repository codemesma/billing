################# Tkinter ###############
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


################# colours ###############

co0 = "#f0f3f5"  # black
co1 = "#feffff"  # white
co2 = "#4fa882"  # Green
co3 = "#38576b"  # values
co4 = "#403d3d"   # letters
co5 = "#e06636"   # - profit
co6 = "#ff9166"   # + profit
co7 = "#ef5350"   # red
co8 = "#263238"   # + green
co9 = "#34495E"   # dark blue

background = "#5899DA"


root_main = Tk()
root_main.geometry('1360x750+0+0')
root_main.title('')
root_main.state('zoomed')

#root_main.configure(background=background)



######################### frame top ######################################

frame_top = Frame(root_main, width=1380,height=63, bg=co9, relief="flat",)
frame_top.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)

######################### frame left ######################################

frame_left = Frame(root_main, width=150,height=700, bg=co4, relief="flat",)
frame_left.grid(row=1, column=0, sticky=NSEW, padx=0, columnspan=1)

######################### frame right ( main ) ############################

frame_main = Frame(root_main, width=1210,height=700, relief="flat",)
frame_main.grid(row=1, column=1, sticky=NSEW, padx=1, columnspan=1)
