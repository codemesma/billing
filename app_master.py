from main import *


################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date


def master():

	######################### Tab master ################################

	tab_control = ttk.Notebook(frame_main,width=1245, height=6805)

	tab1 = ttk.Frame(tab_control)
	tab2 = ttk.Frame(tab_control)
	tab3 = ttk.Frame(tab_control)
	tab4 = ttk.Frame(tab_control)
	tab5 = ttk.Frame(tab_control)
	tab6 = ttk.Frame(tab_control)
	tab7 = ttk.Frame(tab_control)
	tab8 = ttk.Frame(tab_control)
	tab9 = ttk.Frame(tab_control)
	tab10 = ttk.Frame(tab_control)
	tab11 = ttk.Frame(tab_control)
	tab12 = ttk.Frame(tab_control)
	tab13 = ttk.Frame(tab_control)
	tab14 = ttk.Frame(tab_control)
	tab15 = ttk.Frame(tab_control)
	

	tab_control.add(tab1, text='Company')
	tab_control.add(tab2, text='Customer details')
	tab_control.add(tab3, text='Supplier Master')
	tab_control.add(tab4, text='Unit')
	tab_control.add(tab5, text='Item Group')
	tab_control.add(tab6, text='Item Details')
	tab_control.add(tab7, text='Employee Master')
	tab_control.add(tab8, text='Month details')
	tab_control.add(tab9, text='Country Mt')
	tab_control.add(tab10, text='State Details')
	tab_control.add(tab11, text='City/District')
	tab_control.add(tab12, text='Place Details')
	tab_control.add(tab13, text='Role Mt')
	tab_control.add(tab14, text='Role maping')
	tab_control.add(tab15, text='Transaction details')

	tab_control.place(x=2, y=0)


	######################### Tab Company ################################

	tab_company = ttk.Notebook(tab1,width=1220, height=680)
	tab_company_details = ttk.Frame(tab_company)
	tab_company_contact = ttk.Frame(tab_company)
	tab_company_ac_details = ttk.Frame(tab_company)

	tab_company.add(tab_company_details, text='Company details')
	tab_company.add(tab_company_contact, text='Contact details')
	tab_company.add(tab_company_ac_details, text='Company Account details')

	tab_company.place(x=2, y=5)

############################# Company details form ##################################
	
	l_app = Label(tab_company_details, text="Company details", width=27, height=1,anchor=N, font=('Ivy 14 bold'), fg=co4,relief="groove")
	l_app.place(x=440, y=25)


	l_name = Label(tab_company_details, text="Comapany name", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_name.place(x=440, y=80)

	e_name = Entry(tab_company_details, width=27, justify='center',relief="ridge")
	e_name.place(x=570, y=80)


	l_trade = Label(tab_company_details, text="Trade name *", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_trade.place(x=440, y=120)
	e_trade = Entry(tab_company_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=570, y=120)

	l_logo = Label(tab_company_details, text="Logo *", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_logo.place(x=440, y=160)
	b_upload = Button(tab_company_details, text="upload file", width=10, height=1, bg=co2, fg=co1, font=('Ivy 7 bold'), relief=FLAT, overrelief=RIDGE)
	b_upload.place(x=570, y=160)

	
	b_new = Button(tab_company_details, text="New", width=10, height=1, bg=co9, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	b_new.place(x=570, y=220)

	b_save = Button(tab_company_details, text="Save", width=10, height=1, bg=co2, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	b_save.place(x=670, y=220)
	


############################# Contact details form ###########################################################

	######################### General details form ################################

	l_app_info = Label(tab_company_contact, text="General details *", width=30, height=1,anchor=N, font=('Ivy 11 bold'), fg=co4,relief="groove")
	l_app_info.place(x=10, y=40)

	l_address1_contact = Label(tab_company_contact, text="Address - 1", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_address1_contact.place(x=10, y=100)
	e_address1_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_address1_contact.place(x=120, y=100)

	l_address2_contact = Label(tab_company_contact, text="Address - 2", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_address2_contact.place(x=10, y=130)
	e_address2_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_address2_contact.place(x=120, y=130)

	l_address3_contact = Label(tab_company_contact, text="Address - 3", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_address3_contact.place(x=10, y=160)
	e_address3_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_address3_contact.place(x=120, y=160)

	l_state_contact = Label(tab_company_contact, text="State", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_state_contact.place(x=10, y=190)
	e_state_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_state_contact.place(x=120, y=190)

	l_city_contact = Label(tab_company_contact, text="City", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_city_contact.place(x=10, y=220)
	e_city_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_city_contact.place(x=120, y=220)

	l_place_contact = Label(tab_company_contact, text="Place", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_place_contact.place(x=10, y=250)
	e_place_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_place_contact.place(x=120, y=250)

	l_pin_contact = Label(tab_company_contact, text="Pin code", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_pin_contact.place(x=10, y=280)
	e_pin_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_pin_contact.place(x=120, y=280)

	l_email_contact = Label(tab_company_contact, text="email id", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_email_contact.place(x=10, y=310)
	e_email_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_email_contact.place(x=120, y=310)

	l_web_contact = Label(tab_company_contact, text="Website", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_web_contact.place(x=10, y=340)
	e_web_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_web_contact.place(x=120, y=340)

	l_phone_contact = Label(tab_company_contact, text="Phone No.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_phone_contact.place(x=10, y=370)
	e_phone_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_phone_contact.place(x=120, y=370)

	l_mob_contact = Label(tab_company_contact, text="Mob", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_mob_contact.place(x=10, y=400)
	e_mob_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_mob_contact.place(x=120, y=400)

	l_fax_contact = Label(tab_company_contact, text="Fax No.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_fax_contact.place(x=10, y=430)
	e_fax_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_fax_contact.place(x=120, y=430)

	
	
	b1_save_contact = Button(tab_company_contact, text="Save", width=10, height=1, bg=co2, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
	b1_save_contact.place(x=205, y=480)

	######################### General details form ################################

	l_app_info = Label(tab_company_contact, text="Other details *", width=30, height=1,anchor=N, font=('Ivy 11 bold'), fg=co4,relief="groove")
	l_app_info.place(x=500, y=40)

	l_estab_contact = Label(tab_company_contact, text="Establishment", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_estab_contact.place(x=500, y=100)
	e_estab_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_estab_contact.place(x=610, y=100)

	l_cinno_contact = Label(tab_company_contact, text="CIN NO.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_cinno_contact.place(x=500, y=130)
	e_cinno_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_cinno_contact.place(x=610, y=130)

	l_cindate_contact = Label(tab_company_contact, text="CIN Date", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_cindate_contact.place(x=500, y=160)
	e_cindate_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_cindate_contact.place(x=610, y=160)

	l_gst_contact = Label(tab_company_contact, text="GST Applicable", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_gst_contact.place(x=500, y=190)
	
	def gst_event():
		if stat_value.get() ==0:
			e_gstno_contact.configure(state = 'disabled')
			e_gstindate_contact.configure(state = 'disabled')
			e_gstcat_contact.configure(state = 'disabled')

		if stat_value.get() ==1:
			e_gstno_contact.configure(state = 'normal')
			e_gstindate_contact.configure(state = 'normal')
			e_gstcat_contact.configure(state = 'normal')

	stat_value = BooleanVar()
	stat_value.set(False) #set check state
	ch_gst_contact = Checkbutton(tab_company_contact, var=stat_value, onvalue=1, offvalue=0, command=gst_event, justify='center',relief="flat")
	ch_gst_contact.place(x=610, y=190)

	l_gstno_contact = Label(tab_company_contact, text="GSTIN NO.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_gstno_contact.place(x=500, y=220)
	e_gstno_contact = Entry(tab_company_contact, width=27, state = 'disabled', justify='center',relief="ridge")
	e_gstno_contact.place(x=610, y=220)

	l_gstindate_contact = Label(tab_company_contact, text="GSTIN DATE", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_gstindate_contact.place(x=500, y=250)
	e_gstindate_contact = DateEntry(tab_company_contact,state = 'disabled', width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
	e_gstindate_contact.place(x=610, y=250)

	l_gstcat_contact = Label(tab_company_contact, text="GST Category.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_gstcat_contact.place(x=500, y=280)
	e_gstcat_contact = Entry(tab_company_contact, width=27,state = 'disabled', justify='center',relief="ridge")
	e_gstcat_contact.place(x=610, y=280)	


	l_panno_contact = Label(tab_company_contact, text="PAN NO.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_panno_contact.place(x=500, y=310)
	e_panno_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_panno_contact.place(x=610, y=310)

	l_pandate_contact = Label(tab_company_contact, text="PAN DATE", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_pandate_contact.place(x=500, y=340)
	e_pandate_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_pandate_contact.place(x=610, y=340)

	l_tanno_contact = Label(tab_company_contact, text="TAN NO.", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_tanno_contact.place(x=500, y=370)
	e_tanno_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_tanno_contact.place(x=610, y=370)

	l_tandate_contact = Label(tab_company_contact, text="TAN DATE", height=1,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_tandate_contact.place(x=500, y=400)
	e_tandate_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_tandate_contact.place(x=610, y=400)

	l_turn_contact = Label(tab_company_contact, text="Aggregate Turnover of Previuos Financial Year", wraplength=130,compound=LEFT,justify='left' ,height=3,anchor=NW, font=('Ivy 10 bold'), fg=co4)
	l_turn_contact.place(x=500, y=430)
	e_turn_contact = Entry(tab_company_contact, width=27, justify='center',relief="ridge")
	e_turn_contact.place(x=610, y=430)

	b2_save_contact = Button(tab_company_contact, text="Save", width=10, height=1, bg=co2, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
	b2_save_contact.place(x=697, y=480)


############################# Company Account details form ##################################
	
	l_app = Label(tab_company_ac_details, text="Company Account details", width=27, height=1,anchor=N, font=('Ivy 14 bold'), fg=co4,relief="groove")
	l_app.place(x=435, y=25)


	l_name = Label(tab_company_ac_details, text="Bank Name", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_name.place(x=440, y=80)
	e_name = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_name.place(x=590, y=80)


	l_trade = Label(tab_company_ac_details, text="Bank Address ", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_trade.place(x=440, y=120)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=120)

	l_logo = Label(tab_company_ac_details, text="Account No", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_logo.place(x=440, y=160)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=160)

	l_name = Label(tab_company_ac_details, text="Account type", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_name.place(x=440, y=200)
	e_name = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_name.place(x=590, y=200)

	l_trade = Label(tab_company_ac_details, text="Place ", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_trade.place(x=440, y=240)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=240)

	l_logo = Label(tab_company_ac_details, text="Branch", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_logo.place(x=440, y=280)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=280)

	l_logo = Label(tab_company_ac_details, text="IFSC", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_logo.place(x=440, y=320)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=320)

	l_logo = Label(tab_company_ac_details, text="MICR No.", height=1,anchor=NW, font=('Ivy 11 bold'), fg=co4)
	l_logo.place(x=440, y=360)
	e_trade = Entry(tab_company_ac_details, width=27, justify='center',relief="ridge")
	e_trade.place(x=590, y=360)

	b2_save_contact = Button(tab_company_ac_details, text="Save", width=10, height=1, bg=co2, fg=co1, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
	b2_save_contact.place(x=675, y=400)






	
