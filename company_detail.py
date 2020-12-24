import mysql.connector
cur = mysql.connector.connect(user="root",password="",host="localhost",database='billing_software')
mycursor = cur.cursor()

def insert1():
    sql = "INSERT INTO company_detail (company_name, trade_name,logo) VALUES (%s, %s, %s)"
    val = ("HSG", "Highway1" ,"gh1" )
    mycursor.execute(sql, val)
insert1()
def inser2():
    sql1 = "INSERT INTO contact_detail (address1, address2,address3,state,city,place,pin_code,email_id,website,phon_no,mob_no,fax_no) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ("HSG", "Highway1" ,"gh1" ,"Highway1","jaipur","gh","78547","gh@gmail.com","www,mail.com",7854151411,478541111,78547)
    mycursor.execute(sql1, val)
inser2()

def inser3():
    sql2 = "INSERT INTO company_account (bank_name, bank_address,account_no,account_type,place,branch,ifsc_code,micr_no) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    val = ("HSG", "Highway1" ,475478544,"joint","jaipur","jaipur","475Gh47",785411)
    mycursor.execute(sql2, val)
inser3()

def inser4():
    sql3 = "INSERT INTO customer_detail (name, print_name,address1,address2,address3,Country,state,place,pin_code,phone_no,mob_no,email,GSTIN,GSTIN_UIN,GST_Category,PAN_No,TAN_No,All_Data_verified,	Contact_Title,contact_pname,Designation	,contact_Phone_No,Mobile_No,WhatsApp_No,Other_No,Email_ID) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ("HSggG", "Highway1" ,"gggg","ggg","ggg","india","Up","Mp",754785,78547,78541582,"poo@gmail.com",84521,652,"None",45125522,522222,"Yes","ghbjn","jaya","manager",7847854785,78447854,7854125,4757855,"ghj@gmail.com")
    mycursor.execute(sql3, val)
inser4()

def inser5():
    sql4 = "INSERT INTO  supplier_master (name, print_name,address1,address2,address3,Country,state,place,pin_code,phone_no,Mobile_No,Email_ID,GSTIN,GSTIN_UIN,GST_Category,PAN_No,TAN_No,All_Data_verified,	Contact_Title,contact_Name,Designation	,contact_Phone_No,contact_Mobile_No,WhatsApp_No,Other_No,contact_Email_ID) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ("HSggG", "Highway1" ,"gggg","ggg","ggg","india","Up","Mp",754785,78547,78541582,"poo@gmail.com",84521,652,"None",45125522,522222,"Yes","ghbjn","jaya","manager",7847854785,78447854,7854125,4757855,"ghj@gmail.com")
    mycursor.execute(sql4, val)
inser5()

def inser6():
    sql4 = "INSERT INTO  unit (Unite_Code, Description) VALUES (%s, %s)"
    val = ("252", "Highway1" )
    mycursor.execute(sql4, val)
inser6()

def inser7():
    sql4 = "INSERT INTO   item_group (Group_Name, Parent_Group,Item_Category,HSN_SAC_Code,Tax_Rate,CESS_Rate,Add_Quantities_Items) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = ("44", "Highway1","NOne","fghb",25,45,1 )
    mycursor.execute(sql4, val)
inser7()

def inser8():
    sql4 = "INSERT INTO   item_details (Item_Name, Item_Type,Item_Display,Item_Code,HSN_SAC_Code,Item_Group,Item_Category,Unit,Purchase_rate,Sales_Rate,Tax_Rate,CESS_Rate,Description,Is_Credit_Available) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ("shirt", "cloth","sale",252,455,"h","None","ghj",25,45,78,58,"gvhbnm","yes" )
    mycursor.execute(sql4, val)
inser8()

def inser9():
    sql4 = "INSERT INTO    employee_master (Employee_Name, Use_ID,User_Login,E_mail_ID) VALUES (%s, %s,%s,%s)"
    val = ("karan1", 100,"karan121","karan1@gmail.com" )
    mycursor.execute(sql4, val)
inser9()


def inser10():
    sql4 = "INSERT INTO    month_details (Month, Financial_Year,Locked) VALUES (%s, %s,%s)"
    val = ("january", 2020,"yes" )
    mycursor.execute(sql4, val)
inser10()


# def inser11():
#     sql5 = "INSERT INTO     country_master (Country_Name) VALUES (%s)"
#     val = ("India")
#     mycursor.execute(sql5, val)
# inser11()

def inser12():
    sql4 = "INSERT INTO    state_details (Country_Name, State_Name,State_Code) VALUES (%s, %s,%s)"
    val = ("India", "Up",256325 )
    mycursor.execute(sql4, val)
inser12()

def inser13():
    sql4 = "INSERT INTO    city_district (State_Name, City_Name) VALUES (%s, %s)"
    val = ("Up", "Jaipur" )
    mycursor.execute(sql4, val)
inser13()

def inser14():
    sql4 = "INSERT INTO    place_details (State_Name, City_Name,Place_Name,PIN_Code) VALUES (%s, %s,%s,%s)"
    val = ("Up", "Jaipur" ,"banglore",541254)
    mycursor.execute(sql4, val)
inser14()

def inser15():
    sql4 = "INSERT INTO     role_master (Role_Name, Landing_From) VALUES (%s, %s)"
    val = ("Uphh", "Jaipur" )
    mycursor.execute(sql4, val)
inser15()

def inser16():
    sql4 = "INSERT INTO      transaction_settings (Transaction_Type, Transaction_Series_Name,Prefix,Suffix,Starting_No,Digits) VALUES (%s, %s,%s,%s,%s,%s)"
    val = (Transaction_Type, Transaction_Series_Name,Prefix,Suffix,Starting_No,Digits)
    mycursor.execute(sql4, val)
inser16()








cur.commit()
print(mycursor.rowcount, "record inserted.")