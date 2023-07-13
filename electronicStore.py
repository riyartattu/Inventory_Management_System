from tkinter import *
import database
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter.messagebox import *
import os
import time
import tempfile
from PIL import ImageTk,Image

def login():
     #getting form data
     uname=txt_username.get()
     pwd=txt_password.get()
     #applying empty validation
     if uname=='Admin' and pwd=='Admin@123':
         tk.messagebox.showinfo("Success","Login success",parent = mainWindow)
         mainWindow.withdraw()
         main_window()
     else:
         tk.messagebox.showerror("Error","Wrong username or password!!!",parent = mainWindow)
         txt_username.delete(0,END)
         txt_password.delete(0,END)
       
global mainWindow

mainWindow = tk.Tk()

mainWindow.title("Login Form")
mainWindow.geometry("700x700")
mainWindow.config(background = "steelblue")

canvas = Canvas(mainWindow, width = 510, height = 500)
canvas.place(x=100,y=200)
my_image = ImageTk.PhotoImage(Image.open("reception.png"))  
canvas.create_image(0,0,anchor=NW,image = my_image)

global txt_username,txt_password

Label(mainWindow,width="300", text="Please enter details below", font = ("ariel",15,"bold"), bg="skyblue",fg="black").pack()
Label(mainWindow, text="Username * ", font = ("ariel",15,"bold"), bg = "steelblue").place(x=150,y=50)
txt_username = Entry(mainWindow,font = ("ariel",15,"bold"))
txt_username.place(x=290,y=52)
#Password Label
Label(mainWindow, text="Password * ", font = ("ariel",15,"bold"), bg = "steelblue").place(x=150,y=90)
#Password textbox
txt_password = Entry(mainWindow,show="*",font = ("ariel",15,"bold"))
txt_password.place(x=290,y=92)
#Login button
Button(mainWindow, text="Login", width=12, height=1, font = ("ariel",15,"bold"), bg="skyblue",command=login).place(x=320,y=140)

#************************************Code for Admin Window*******************************************************************************************

def admin_window():
     global new_window,my_img1
     new_window = Toplevel(root)
     new_window.title("Admin")
     new_window.geometry("400x400")
     new_window.configure(background="steelblue")

     canvas = Canvas(new_window, width = 200, height = 180)
     canvas.place(x=100,y=200)
     my_img1 = ImageTk.PhotoImage(Image.open("admin12.jpg"))  
     canvas.create_image(-45,-20,anchor=NW,image = my_img1)
         
     add_btn = Button(new_window, text="Add Employee Info",font=("ariel", 10, "bold"),width = 25, command = add_employee)
     cha_btn = Button(new_window, text="Change Employee Info",font=("ariel",10, "bold"),width = 25, command = change_employee_info)
     dis_btn = Button(new_window, text="Display Employee Info",font=("ariel",10, "bold"),width = 25, command = display_employee)
     add_btn.place(x=100, y=25)
     cha_btn.place(x=100, y=90)
     dis_btn.place(x=100, y=155)
         
#************************************Code for Item Window*****************************************************************************************

def  items_window():
     global new_window,my_img2
     new_window = Toplevel(root)
     new_window.title("Items")
     new_window.geometry("400x400")
     new_window.configure(background="steelblue")

     canvas = Canvas(new_window, width = 200, height = 180)
     canvas.place(x=100,y=200)
     my_img2 = ImageTk.PhotoImage(Image.open("laptop.png"))  #########ImageTk.PhotoImage(Image.open("download.jpg"))
     canvas.create_image(0,-10,anchor=NW,image = my_img2)
          
     aitems_btn = Button(new_window, text="New Item Info",font=("ariel", 10, "bold"),width = 25, command = add_items)
     citems_btn = Button(new_window, text="Change Item Info",font=("ariel", 10, "bold"),width = 25, command = change_item_info)
     disitems_btn = Button(new_window, text="Display Item Info",font=("ariel", 10, "bold"),width = 25, command = display_items)
     aitems_btn.place(x=100, y=25)
     citems_btn.place(x=100, y=90)
     disitems_btn.place(x=100, y=155)

#************************************Code for Sales Window*******************************************************************************************

def sales_window():
     global new_window,my_img3
     new_window = Toplevel(root)
     new_window.title("Sales")
     new_window.geometry("400x400")
     new_window.configure(background="steelblue")

     canvas = Canvas(new_window, width = 210, height = 240)
     canvas.place(x=100,y=150)
     my_img3 = ImageTk.PhotoImage(Image.open("bills.png"))  #########ImageTk.PhotoImage(Image.open("download.jpg"))
     canvas.create_image(-125,-40,anchor=NW,image = my_img3)

     bill_btn = Button(new_window,text = "Check Out",font=("ariel", 10, "bold"),width = 25,command = bill_window)
     invoice_btn = Button(new_window,text = "Search Invoice",font=("ariel", 10, "bold"),width = 25,command = invoice_window)

     invoice_btn.place(x= 100,y=30)
     bill_btn.place(x=100, y =90)

#***************************************************************
def bill_window():
    global new_window1,Add_Cart_Frame,Variable_cal_input,cart_list,Product_Table,Cart_Table,Variable_Pro_id,Variable_Pro_Brand,Variable_Pro_model,Variable_Pro_MRP,Variable_Pro_Quantity,Variable_Pro_Discount,Variable_search,txt_P_brand,txt_P_model,txt_P_qty
    global lbl_amt,lbl_discount,lbl_net_pay,Cart_title,Variable_name,Variable_contact,txt_bill_area,lbl_clk
    
    new_window1 = Toplevel(root)
    new_window1.title("Check Out")
    new_window1.geometry("1370x700")
    new_window1.configure(background = "steelblue")
    cart_list = []


    title = Label(new_window1, text = "Electronic Store Management System", compound = LEFT, font = ("times new roman", 35, "bold"), bg = "#010c48", fg = "white", anchor = 'w', padx = 300).place(x=0,y=0,relwidth=1,height=70)
    lbl_clk = Label(new_window1, text="Welcome to Tech2go \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg = "white")
    lbl_clk.place(x=0,y=70,relwidth=1,height=30)
    
    Variable_search = tk.StringVar()
    Variable_name= tk.StringVar()
    Variable_contact = tk.StringVar()

    Product_Frame = Frame(new_window1,bd=4,relief = 'ridge')
    Product_Frame.place(x=6,y=100,width = 410,height=590)
    P_title = Label(Product_Frame,text = "All Products ", font = ('Ariel',20,'bold'), bg = '#262626',fg = 'white').pack(side = TOP,fill = X)
    
    Product_Frame2 = Frame(Product_Frame,bd = 2,relief ='ridge',bg = 'white')
    Product_Frame2.place(x=2,y=42,width = 398,height = 130)
    
    Label_Search = Label(Product_Frame2, text = 'Search Product | By Name', font = ('times new roman',15,'bold'),bg = 'white',fg = 'green').place(x=2,y=5)
    Label_Search = Label(Product_Frame2, text = 'Product Name',font = ('times new roman',15,'bold'),bg = 'white',fg = 'black').place(x=2,y=45)
    
    Text_Search = Entry(Product_Frame2, textvariable = Variable_search,font = ('times new roman',15),bg = 'light yellow').place(x=128,y=47,width = 150,height = 22)
    
    button_search = Button(Product_Frame2,text ='search',font = ('ariel',15),bg = '#2196f3',fg = 'white',cursor = 'hand2',command = search).place(x=280,y=45,width = 100,height=25)
    button_showall = Button(Product_Frame2,text ='Show All',font = ('ariel',15),bg = '#083531',fg = 'white',cursor = 'hand2',command=show_data).place(x=280,y=10,width = 100,height=25)
    
    Product_Frame3 = Frame(Product_Frame,bd = 3,relief ='ridge',bg = 'white')
    Product_Frame3.place(x=2,y=140,width = 398,height = 425)
    
    Scrolly = Scrollbar(Product_Frame3,orient = VERTICAL)
    Scrollx = Scrollbar(Product_Frame3,orient = HORIZONTAL)
    
    Product_Table = ttk.Treeview(Product_Frame3,columns = ('Product_id','Product_brand','Product_model','Product_MRP'))
    Product_Table.configure(yscrollcommand=Scrolly.set,xscrollcommand = Scrollx.set)
    Scrollx.pack(side=BOTTOM, fill=X)
    Scrollx.config(command=Product_Table.xview)
    Scrolly.pack(side=RIGHT, fill=Y)
    Scrolly.config(command=Product_Table.yview)
    
    Product_Table.heading("Product_id", text="Pro_Id")
    Product_Table.heading("Product_brand", text="Pro_Brand")
    Product_Table.heading("Product_model", text="Pro_model")
    Product_Table.heading("Product_MRP", text="Pro_MRP")
    Product_Table["show"] = "headings"
     
    Product_Table.column("Product_id", width=60)
    Product_Table.column("Product_brand", width=60)
    Product_Table.column("Product_model", width=60)
    Product_Table.column("Product_MRP", width=40)
    
    Product_Table.pack(fill = BOTH, expand = 1)
    Product_Table.bind("<ButtonRelease - 1>",get_data)
    lbl_note = Label(Product_Frame3,text = "Note:'Enter 0 quantity to remove product from the cart'",font = ('ariel',10),bg = 'white',fg = 'red').pack(side=BOTTOM,fill = X)
    
    Customer_Frame = Frame(new_window1,bd=4,relief = 'ridge')
    Customer_Frame.place(x=420,y=100,width = 530,height=70)
    C_title = Label(Customer_Frame,text = "Customer Details", font = ('Ariel',15), bg = 'lightgray').pack(side = TOP,fill = X)
    
    Label_Name = Label(Customer_Frame, text = 'Name',font = ('times new roman',15),bg = 'white').place(x=5,y=35)
    Text_Name = Entry(Customer_Frame, textvariable = Variable_name,font = ('times new roman',13),bg = 'light yellow').place(x=80,y=35,width = 180)
    Label_Contact = Label(Customer_Frame, text = 'Contact No.',font = ('times new roman',15),bg = 'white').place(x=270,y=35)
    Text_Contact = Entry(Customer_Frame, textvariable = Variable_contact,font = ('times new roman',13),bg = 'light yellow').place(x=380,y=35,width = 140)
    
    Cal_Cart_Frame = Frame(new_window1,bd = 4,relief ='ridge',bg = 'white')
    Cal_Cart_Frame.place(x=420,y=175,width = 530,height = 360)
    
    Cart_Frame = Frame(Cal_Cart_Frame,bd = 3,relief ='ridge',bg = 'white')
    Cart_Frame.place(x=5,y=8,width = 510,height = 342)
    
    Cart_title = Label(Cart_Frame,text = "Cart \t Total Product:[0]", font = ('Ariel',15), bg = 'lightgray')
    Cart_title.pack(side = TOP,fill = X)
    
    Scrolly = Scrollbar(Cart_Frame,orient = VERTICAL)
    Scrollx = Scrollbar(Cart_Frame,orient = HORIZONTAL)

    Cart_Table = ttk.Treeview(Cart_Frame,columns = ('Sr.No.','Product_id','Product_brand','Product_model','Product_MRP','Product_Quantity'))
    Cart_Table.config(yscrollcommand=Scrolly.set,xscrollcommand = Scrollx.set)
    Scrollx.pack(side=BOTTOM, fill=X)
    Scrollx.config(command=Cart_Table.xview)
    Scrolly.pack(side=RIGHT, fill=Y)
    Scrolly.config(command=Cart_Table.yview)
    
    Cart_Table.heading("Sr.No.", text="Sr.No.")
    Cart_Table.heading("Product_id", text="Pro_Id")
    Cart_Table.heading("Product_brand", text="Pro_Brand")
    Cart_Table.heading("Product_model", text="Pro_Model")
    Cart_Table.heading("Product_MRP", text="Pro_MRP")
    Cart_Table.heading("Product_Quantity", text="Pro_Qty")
    Cart_Table["show"] = "headings"
    
    Cart_Table.column("Sr.No.", width=40)
    Cart_Table.column("Product_id", width=40)
    Cart_Table.column("Product_brand", width=100)
    Cart_Table.column("Product_model", width=100)
    Cart_Table.column("Product_MRP", width=100)
    Cart_Table.column("Product_Quantity", width=60)
    Cart_Table.pack(fill = BOTH, expand = 1)
    
    # Add cart buttons 
    
    Add_Cart_Frame = Frame(new_window1,bd = 2,relief ='ridge',bg = 'white')
    Add_Cart_Frame.place(x=420,y=540,width = 530,height = 150)
    
    Variable_Pro_id = tk.StringVar()
    Variable_Pro_Brand = tk.StringVar()
    Variable_Pro_model = tk.StringVar()
    Variable_Pro_MRP = tk.StringVar()
    Variable_Pro_Quantity = tk.StringVar()
    
    lbl_P_id = Label(Add_Cart_Frame,text = "Product Id", font = ('times new roman',15), bg = 'white').place(x= 5, y = 5)
    txt_P_id = Entry(Add_Cart_Frame,textvariable=Variable_Pro_id,font = ('times new roman',15), bg = 'light yellow',cursor = 'hand2').place(x= 5, y = 35,width = 190, height = 22)
    
    lbl_P_brand = Label(Add_Cart_Frame,text = "Product Brand", font = ('times new roman',15), bg = 'white').place(x= 230, y = 5)
    txt_P_brand = Entry(Add_Cart_Frame,textvariable = Variable_Pro_Brand,font = ('times new roman',15),  bg = 'light yellow',cursor = 'hand2').place(x= 230, y = 35,width = 150, height = 22)
    
    lbl_P_model = Label(Add_Cart_Frame,text = "Product Model", font = ('times new roman',15), bg = 'white').place(x=390, y = 5)
    txt_P_model = Entry(Add_Cart_Frame,textvariable = Variable_Pro_model,font = ('times new roman',15), bg = 'light yellow',cursor = 'hand2').place(x= 390, y = 35,width = 100, height = 22)
        
    lbl_P_mrp = Label(Add_Cart_Frame,text = "Product MRP", font = ('times new roman',15), bg = 'white').place(x= 5, y = 70)
    txt_P_mrp = Entry(Add_Cart_Frame,textvariable = Variable_Pro_MRP,font = ('times new roman',15),bg = 'light yellow',cursor = 'hand2').place(x= 130, y = 70,width = 150, height = 22)
    
    lbl_P_qty = Label(Add_Cart_Frame,text = "Quantity", font = ('times new roman',15), bg = 'white').place(x= 5, y = 110)
    txt_P_qty = Entry(Add_Cart_Frame,textvariable = Variable_Pro_Quantity, font = ('times new roman',15),bg = 'light yellow',cursor = 'hand2').place(x= 130, y = 110,width = 150, height = 22)

    Clear_btn = Button(Add_Cart_Frame,text ='Clear',font = ('ariel',15),bg = 'lightgray',cursor = 'hand2',command=clear_cart).place(x=300,y=110,width = 80,height=30)
    Add_btn = Button(Add_Cart_Frame,text ='Add',font = ('ariel',15),bg = 'lightgray',cursor = 'hand2',command=add_update_cart).place(x=400,y=110,width = 80,height=30)
    
    bill_frame = Frame(new_window1,bd = 2,relief = 'ridge',bg ='white')
    bill_frame.place(x=953,y=100,width = 410,height=410)
    
    Bill_title = Label(bill_frame,text = "Customer Bill Area", font = ('Ariel',20,'bold'), bg = '#262626',fg= 'white').pack(side = TOP,fill = X)
    
    Scrolly = Scrollbar(bill_frame,orient = VERTICAL)
    Scrolly.pack(side = RIGHT,fill = Y)
    txt_bill_area = Text(bill_frame,yscrollcommand = Scrolly.set)
    txt_bill_area.pack(fill=BOTH,expand = 1)
    Scrolly.config(command = txt_bill_area.yview)
    
    bill_menu_frame = Frame(new_window1,bd = 2,relief = 'ridge',bg ='white')
    bill_menu_frame.place(x=953,y=510,width = 410,height=180)
    
    lbl_amt = Label(bill_menu_frame,text='Bill Amount \n Rs.[0]',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white')
    lbl_amt.place(x=2,y=5,width = 120,height = 80)
    lbl_discount = Label(bill_menu_frame,text='Discount\n[0]%',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white')
    lbl_discount.place(x=124,y=5,width = 120,height = 80)
    lbl_net_pay = Label(bill_menu_frame,text='Net Pay \n Rs.[0] ',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white')
    lbl_net_pay.place(x=246,y=5,width = 160,height = 80)
    
    btn_print = Button(bill_menu_frame,text='Print',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white',cursor = 'hand2',command = print_bill).place(x=2,y=95,width = 120,height = 80)
    btn_clearall = Button(bill_menu_frame,text='Clear All',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white',cursor = 'hand2',command=clear_all).place(x=124,y=95,width = 120,height = 80)
    b_generate= Button(bill_menu_frame,text='Generate Bill',font = ('Ariel',15,'bold'),bg = '#3f51b5',fg = 'white',cursor = 'hand2',command=generate_bill).place(x=246,y=95,width = 160,height = 80)
    update_datetime()
    
#****************************************************************

def show_data():
    result = database.selected_items()
    Product_Table.delete(*Product_Table.get_children())
    for row in result:
        Product_Table.insert('',END,values = row)
   
def search():
    val = (Variable_search.get(),) 
    result = database.Product_search(val)
    Product_Table.delete(*Product_Table.get_children())
    for row in result:
        Product_Table.insert('',END,values = row)
            
def add_update_cart():
    price_cal = Variable_Pro_MRP.get()
    serial_no = len(cart_list) +1   
    cart_data = [serial_no,Variable_Pro_id.get(),Variable_Pro_Brand.get(),Variable_Pro_model.get(),Variable_Pro_MRP.get(),Variable_Pro_Quantity.get()]

    present = 'no'
    index = 0
    for row in cart_list:
        if Variable_Pro_id.get() == row[1]:
            present = 'yes'
            break
        index += 1
    if present == 'yes':
        op = tk.messagebox.askyesno("Confirm ","Do you want to replace",parent=new_window1)
        if op == True:
            cart_list[index][5] = Variable_Pro_Quantity.get()
    else:
        serial_no += 1
        cart_list.append(cart_data)
            
    show_cart()
    bill_updates()

def show_cart():
    Cart_Table.delete(*Cart_Table.get_children())
    for row in cart_list:
        Cart_Table.insert('',END,values = row)

def generate_bill():
    global chk_print 
    chk_print = 0
    if Variable_name.get() == '' or Variable_contact.get() == '':
        tk.messagebox.showerror("Error",f'Customer Details are required', parent = new_window1)
    elif len(cart_list) == 0:
        tk.messagebox.showerror("Error",f'Please add product to cart', parent = new_window1)
    else:
        #=======BILL TOP===========
        bill_top()
        #=======BILL MIDDLE==========
        bill_middle()
        #=======BILL BOTTOM=========
        bill_bottom()
        fp = open(fr'C:/Users/Akshata/Desktop/sumeet/Bill/{str(invoice)}.txt','w')
        fp.write(txt_bill_area.get('1.0',END))
        fp.close()
        tk.messagebox.showinfo("Saved","Bill has been saved",parent = new_window1)
        chk_print = 1
        
def update_datetime():
    global time_,date_
    time_ = time.strftime("%I:%M:%S")
    date_ = time.strftime("%d-%m-%Y")
    lbl_clk = Label(new_window1, text="Welcome to Tech2go \t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font = ("times new roman", 15), bg="#4d636d", fg = "white")
    lbl_clk.config(text="Welcome to Tech2go\t\t Date: {} \t\t Time: {}".format(date_,time_))
    lbl_clk.after(200,update_datetime)
    
    
def bill_top():
    global invoice
    invoice = int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
    bill_top_temp = f"""
\t\t  Tech2go
  Phone No. 9872565596, Mumbai-400014
{str("="*47)}
Customer Name : {Variable_name.get()}
Phone No: {Variable_contact.get()}
Bill No. {str(invoice)}\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
Sr.No.\tProduct Name\t\tQTY\tPrice
{str("="*47)}
"""
    txt_bill_area.delete('1.0',END)
    txt_bill_area.insert('1.0',bill_top_temp)

def bill_bottom():
    bill_bottom_temp = f"""
{str("="*47)}
Bill Amount:\t\t\t\tRs.{bill_amt}
Discount Percent:\t\t\t\t{5}%
Net Pay:\t\t\t\tRs.{net_pay}
{str("="*47)}\n
"""
    txt_bill_area.insert(END,bill_bottom_temp)

def bill_middle():
    for row in cart_list:
        sr_no = str(row[0])
        name = row[2]
        qty = row[5]
        price = float(row[4])*int(row[5])
        price = str(price)
        txt_bill_area.insert(END,'\n'+sr_no+'\t ' + name + "\t\t" + qty + "\tRs." + price)

def print_bill():
    if chk_print == 1:
        tk.messagebox.showinfo("Print","Please wait while printing",parent = new_window1)  
        new_file = tempfile.mktemp('.txt')
        open(new_file, 'w').write(txt_bill_area.get('1.0',END))
        os.startfile(new_file,'print')
    else:
        tk.messagebox.showerror("Print","Please generate bill to print the receipt",parent = new_window1)
       
def clear_cart():
    Variable_Pro_id.set('')
    Variable_Pro_Brand.set('')
    Variable_Pro_model.set('')
    Variable_Pro_MRP.set('')
    Variable_Pro_Quantity.set('')

def clear_all():
    del cart_list[:]
    Variable_name.set('')
    Variable_contact.set('')
    txt_bill_area.delete('1.0',END)
    Cart_title.config(text = f"Cart \t Total Product : [0]")
    clear_cart()
    show_data()
    show_cart()
    chk_print = 0
    
def bill_updates():
    global bill_amt,net_pay
    bill_amt = 0
    net_pay = 0
    for row in cart_list:
        bill_amt =  bill_amt + (float(row[4])*int(row[5]))
    net_pay = bill_amt - ((bill_amt * float(5)/100))
    
    lbl_amt.config(text = f'Bill Amt\n[{str(bill_amt)}]')
    lbl_discount.config(text = f"Discount\n[{str(5)}%]")
    lbl_net_pay.config(text = f'Net Pay\n[{str(net_pay)}]')
    Cart_title.config(text = f"Cart \t Total Product:[{str(len(cart_list))}]")

def get_data(ev):
    f=Product_Table.focus()
    content=(Product_Table.item(f))
    row=content['values']
    Variable_Pro_id.set(row[0])
    Variable_Pro_Brand.set(row[1])
    Variable_Pro_model.set(row[2])
    Variable_Pro_MRP.set(row[3])
    Variable_Pro_Quantity.set('1')

    
#****************************************************************
def invoice_window():
    global t_invoice_id,t_Item_number,t_Date,t_Customer_contact,t_Product_id,t_Quantity,t_MRP,t_Discount,t_Acutal_Sale_Price,new_window,t_Customer_name
    new_window = Toplevel(root)
    new_window.title("Search Invoice")
    new_window.geometry("500x550")
    new_window.configure(background = "steelblue")
    
    l_invoice_id = Label(new_window,text= "Invoice Id",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_invoice_id.grid(row = 0, column = 0)
    
    t_invoice_id = Entry(new_window,width = 30)
    t_invoice_id.grid(row = 0, column = 1)
    
    search_btn = Button(new_window, text="Search", width = 10,command = display_invoice) 
    search_btn.place(x = 330, y = 14)
    
    clear_btn = Button(new_window, text="Clear", width = 10,command = delete_invoice)
    clear_btn.place(x = 330, y = 44)
    
    l_Item_number = Label(new_window,text= "Item Number",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Date = Label(new_window,text= "Date",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Customer_contact = Label(new_window,text= "Customer Contact",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Customer_name = Label(new_window,text= "Customer Name",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Product_id = Label(new_window,text= "Product id",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Quantity = Label(new_window,text= "Quantity",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_MRP = Label(new_window,text= "MRP",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Discount = Label(new_window,text= "Discount",height = 3, width=15, bg="steelblue", anchor = 'w')
    l_Actual_Sale_Price = Label(new_window,text= "Acutal Sale Price",height = 3, width=15, bg="steelblue", anchor = 'w')
    
    l_Item_number.grid(row = 1, column = 0)
    l_Date.grid(row = 2, column = 0)
    l_Customer_contact.grid(row = 3, column = 0)
    l_Customer_name.grid(row = 4, column = 0)
    l_Product_id.grid(row = 5, column = 0)
    l_Quantity.grid(row = 6, column = 0)
    l_MRP.grid(row = 7, column = 0)
    l_Discount.grid(row = 8, column = 0)
    l_Actual_Sale_Price.grid(row = 9, column = 0)
    
    t_Item_number = Entry(new_window, width = 30)
    t_Date = Entry(new_window, width = 30)
    t_Customer_contact = Entry(new_window, width = 30)
    t_Customer_name = Entry(new_window, width = 30)
    t_Product_id = Entry(new_window, width = 30)
    t_Quantity = Entry(new_window, width = 30)
    t_MRP = Entry(new_window, width = 30)
    t_Discount = Entry(new_window, width = 30)
    t_Acutal_Sale_Price = Entry(new_window, width = 30)
    
    t_Item_number.grid(row = 1, column = 1)
    t_Date.grid(row = 2, column = 1)
    t_Customer_contact.grid(row = 3, column = 1)
    t_Customer_name.grid(row = 4, column = 1)
    t_Product_id.grid(row = 5, column = 1)
    t_Quantity.grid(row = 6, column = 1)
    t_MRP.grid(row = 7, column = 1)
    t_Discount.grid(row = 8, column = 1)
    t_Acutal_Sale_Price.grid(row = 9, column = 1)
    
#***************************************#

def display_invoice():
    val = (t_invoice_id.get(),t_Item_number.get(),)
    result = database.display_invoice_info(val)
    row = result
    
    #t_Item_number.delete(0,END)
    t_Date.delete(0,END)
    t_Customer_contact.delete(0,END)
    t_Customer_name.delete(0,END)
    t_Product_id.delete(0,END)
    t_Quantity.delete(0,END)
    t_MRP.delete(0,END)
    t_Discount.delete(0,END)
    t_Acutal_Sale_Price.delete(0,END)
    
##    t_Item_number.insert(END,row[0])
    t_Date.insert(END,row[1])
    t_Customer_contact.insert(END,row[2])
    t_Customer_name.insert(END,row[3])
    t_Product_id.insert(END,row[4])
    t_Quantity.insert(END,row[5])
    t_MRP.insert(END,row[6])
    t_Discount.insert(END,row[7])
    t_Acutal_Sale_Price.insert(END,row[8])
    
#************************************

def delete_invoice():
    
    t_invoice_id.delete(0,END)
    t_Item_number.delete(0,END)
    t_Date.delete(0,END)
    t_Customer_contact.delete(0,END)
    t_Customer_name.delete(0,END)
    t_Product_id.delete(0,END)
    t_Quantity.delete(0,END)
    t_MRP.delete(0,END)
    t_Discount.delete(0,END)
    t_Acutal_Sale_Price.delete(0,END)
    
#************************************Code for Customer Window****************************************************************************************

def customer_window():
     global new_window,my_img4
     new_window = Toplevel(root)
     new_window.title("Customer")
     new_window.geometry("400x400")
     new_window.configure(background="steelblue")

     canvas = Canvas(new_window, width = 250, height = 200)
     canvas.place(x=80,y=180)
     my_img4 = ImageTk.PhotoImage(Image.open("customer_multiple.jpg"))  #########ImageTk.PhotoImage(Image.open("download.jpg"))
     canvas.create_image(-20,-4,anchor=NW,image = my_img4)
     
     ncus_btn = Button(new_window, text="New Customer Info",font=("ariel", 10, "bold"),width = 25, command = add_customer)
     chcus_btn = Button(new_window, text="Change Customer Info",font=("ariel", 10, "bold"),width = 25, command = change_cust_info)
     dispcus_btn = Button(new_window, text="Display Customer Info",font=("ariel", 10, "bold"),width = 25, command = display_customers)
     ncus_btn.place(x=100, y=25)
     chcus_btn.place(x=100, y=80)
     dispcus_btn.place(x=100, y=145)

#************************************Code for Adding Employee Window*********************************************************************************

def add_employee():
    global t_empid,t_empname,t_empcon,cmb,t_empage,new_window
    new_window = Toplevel(root)
    n = tk.StringVar()
    new_window.title("Add Employee")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_empid = Label(new_window, text = "Employee_id", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empname = Label(new_window, text = "Employee_name", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empcon = Label(new_window, text = "Employee_contact", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empgen = Label(new_window, text = "Employee_gender", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empage = Label(new_window, text = "Employee_age", height = 3, width=15, bg="steelblue", anchor = 'w')

    #textboxes
    t_empid = Entry(new_window, width = 30)
    t_empname = Entry(new_window, width = 30)
    t_empcon = Entry(new_window, width = 30)
    cmb = ttk.Combobox(new_window, textvariable=n, values=("select","M","F"), state='readonly',width=27)
    t_empage = Entry(new_window, width = 30)

    #submit button
    save_btn = Button(new_window, text="Save", width = 10,command = insert_admin_values)

    #placing labels
    l_empid .grid(row=0, column=0)
    l_empname .grid(row=1, column=0)
    l_empcon.grid(row=2, column=0)
    l_empgen.grid(row=3, column=0)
    l_empage.grid(row=4, column=0)

    #placing textboxes
    t_empid.grid(row=0, column=1)
    t_empname.grid(row=1, column=1)
    t_empcon.grid(row=2, column=1)
    cmb.grid(row=3, column=1)
    t_empage.grid(row=4, column=1)
    cmb.current(0)
    
    #placing submit button
    save_btn.grid(row=5,column=1)
    
#************************************SQL Code for Adding Employee to database************************************************************************

def insert_admin_values():
    val = (t_empid.get(),t_empname.get(),t_empcon.get(),cmb.get(),t_empage.get())
    database.admin_values(val)
    tk.messagebox.showinfo("Saved","Your values have been added", parent = new_window)

    t_empid.delete(0, END)
    t_empname.delete(0, END)
    t_empcon.delete(0, END)
    cmb.delete(END,0)
    t_empage.delete(0, END)

#************************************Code for Update Employee Window********************************************************************************

def change_employee_info():
    global t_empid,t_empname,t_empcon,t_empgen,t_empage,new_window
    new_window = Toplevel(root)
    new_window.title("Change Employee Info")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_empid = Label(new_window, text = "Employee_id", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empname = Label(new_window, text = "Employee_name", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empcon = Label(new_window, text = "Employee_contact", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empgen = Label(new_window, text = "Employee_gender", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_empage = Label(new_window, text = "Employee_age", height = 3, width=15, bg="steelblue", anchor = 'w')

    #textboxes
    t_empid = Entry(new_window, width = 30)
    t_empname = Entry(new_window, width = 30)
    t_empcon = Entry(new_window, width = 30)
    t_empgen = Entry(new_window, width = 30)
    t_empage = Entry(new_window, width = 30)

    #buttons
    search_btn = Button(new_window, text="Search", width = 10,command = display_employee_values) 
    save_btn = Button(new_window, text="Save", width = 10,command = update_admin_values)
    delete_btn = Button(new_window, text="Delete", width = 10,command = delete_admin_values)
    
    #placing labels
    l_empid .grid(row=0, column=0)
    l_empname .grid(row=1, column=0)
    l_empcon.grid(row=2, column=0)
    l_empgen.grid(row=3, column=0)
    l_empage.grid(row=4, column=0)

    #placing textboxes
    t_empid.grid(row=0, column=1)
    t_empname.grid(row=1, column=1)
    t_empcon.grid(row=2, column=1)
    t_empgen.grid(row=3, column=1)
    t_empage.grid(row=4, column=1)
     
    #placing submit button
    search_btn.place(x = 310, y = 14)
    save_btn.place(x = 120, y = 270)
    delete_btn.place(x = 220, y = 270)

#***********************************SQL Code to search Employee from database*************************************************************************

def display_employee_values():
    val = (t_empid.get(),)
    result = database.display_employee_info(val)
    row = result
    
    t_empname.delete(0, END)
    t_empcon.delete(0, END)
    t_empgen.delete(0, END)
    t_empage.delete(0, END)
    
    t_empname.insert(END,row[0])
    t_empcon.insert(END,row[1])
    t_empgen.insert(END,row[2])
    t_empage.insert(END,row[3])
    
#************************************SQL Code to Update Employee to database********************************************************************************

def update_admin_values():
    val = (t_empname.get(),t_empcon.get(),t_empgen.get(),t_empage.get(),t_empid.get())
    if t_empid.get() == "":
        tk.messagebox.showerror("Error","Input is required", parent = new_window)
    else:
        op = tk.messagebox.askyesno("Confirm ","Do you want to update",parent=new_window)
        if op == True:
             database.admin_update(val)
    
    t_empname.delete(0, END)
    t_empcon.delete(0, END)
    t_empgen.delete(0, END)
    t_empage.delete(0, END)
    t_empid.delete(0, END)
    
def delete_admin_values():
    val = (t_empid.get(),)
    op = tk.messagebox.askyesno("Confirm ","Do you want to delete",parent=new_window)
    if op == True:
         database.delete_admin(val)
        
    t_empname.delete(0, END)
    t_empcon.delete(0, END)
    t_empgen.delete(0, END)
    t_empage.delete(0, END)
    t_empid.delete(0, END)

#************************************Code for Display Employee Window********************************************************************************

def display_employee():
    global t_empid,t_empname,t_empcon,cmb,t_empage
    new_window = Toplevel(root)
    new_window.title("Display Employee")
    new_window.geometry("555x600")
    new_window.configure(background="steelblue")
    
    result = database.get_employee()
    i=1 
    for row in result: 
        for j in range(len(row)):
            e= Label(new_window,width=15, text=row[j]) 
            e.grid(row=i, column=j)
        i=i+1  

    e = Label(new_window,width=15, text=row[j],borderwidth=2,relief='ridge', anchor="w")
    
    e=Label(new_window,width=15,text='Employee_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(new_window,width=15,text='Employee_name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(new_window,width=15,text='Employee_contact',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(new_window,width=15,text='Employee_gender',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(new_window,width=15,text='Employee_age',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    
#************************************Code for Add Customer Window************************************************************************************

def add_customer():
    global t_cusid,t_cusname,t_cuscon,cmb,t_cusloc,t_cusage,new_window
    new_window = Toplevel(root)
    n = tk.StringVar()
    new_window.title("Add Customer")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_cusid = Label(new_window, text = "Customer_id", height = 3,width=15, bg="steelblue", anchor = 'w')
    l_cusname = Label(new_window, text = "Customer_name", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cuscon = Label(new_window, text = "Customer_contact", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusgen = Label(new_window, text = "Customer_gender", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusloc = Label(new_window, text = "Customer_location", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusage = Label(new_window, text = "Customer_age", height = 3, width=15, bg="steelblue", anchor = 'w')

    #textboxes
    t_cusid = Entry(new_window, width = 30)
    t_cusname = Entry(new_window, width = 30)
    t_cuscon = Entry(new_window, width = 30)
    cmb=ttk.Combobox(new_window, textvariable=n, values=("select","M","F"), state='readonly',width=27)
    t_cusloc = Entry(new_window, width = 30)
    t_cusage = Entry(new_window, width = 30)
    
    #submit button
    save_btn = Button(new_window, text="Save", width = 10,command = insert_customer_values)

    #placing labels
    l_cusid .grid(row=0, column=0)
    l_cusname .grid(row=1, column=0)
    l_cuscon.grid(row=2, column=0)
    l_cusgen.grid(row=3, column=0)
    l_cusloc.grid(row=4, column=0)
    l_cusage.grid(row=5, column=0)

    #placing textboxes
    t_cusid.grid(row=0, column=1)
    t_cusname.grid(row=1, column=1)
    t_cuscon.grid(row=2, column=1)
    cmb.grid(row=3, column=1)
    t_cusloc.grid(row=4, column=1)
    t_cusage.grid(row=5, column=1)
    cmb.current(0)
    
    #placing submit button
    save_btn.grid(row=6,column=1)

#************************************SQL Code for Adding Customer to database************************************************************************

def insert_customer_values():   
    val = (t_cusid.get(),t_cusname.get(),t_cuscon.get(),cmb.get(),t_cusloc.get(),t_cusage.get())
    database.customer_values(val)
    tk.messagebox.showinfo("Saved","Your values have been added", parent = new_window)
     
    t_cusid.delete(0, END)
    t_cusname.delete(0, END)
    t_cuscon.delete(0, END)
    cmb.delete(END,0)
    t_cusloc.delete(0, END)
    t_cusage.delete(0, END)
    
#************************************Code for Change Customer Window*********************************************************************************

def change_cust_info():
    global t_cusid,t_cusname,t_cuscon,t_cusgen,t_cusloc,t_cusage,new_window
    new_window = Toplevel(root)
    #n = tk.StringVar()
    new_window.title("Change Customer Info")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_cusid = Label(new_window, text = "Customer_id", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusname = Label(new_window, text = "Customer_name", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cuscon = Label(new_window, text = "Customer_contact", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusgen = Label(new_window, text = "Customer_gender", height = 3, width=15, bg="steelblue",anchor = 'w')
    l_cusloc = Label(new_window, text = "Customer_location", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_cusage = Label(new_window, text = "Customer_age", height = 3, width=15, bg="steelblue", anchor = 'w')

    #textboxes
    t_cusid = Entry(new_window, width = 30)
    t_cusname = Entry(new_window, width = 30)
    t_cuscon = Entry(new_window, width = 30)
    t_cuscon = Entry(new_window, width = 30)
    t_cusgen = Entry(new_window, width = 30)
    #cmb = ttk.Combobox(new_window, textvariable=n, values=("select","M","F"), state='readonly',width=30)
    t_cusloc = Entry(new_window, width = 30)
    t_cusage = Entry(new_window, width = 30)
    
    #buttons
    search_btn = Button(new_window, text="Search", width = 10,command = display_customer_values)
    save_btn = Button(new_window, text="Save", width = 10,command = update_customer_values)
    delete_btn = Button(new_window, text="Delete", width = 10,command = delete_customer_values)

    #placing labels
    l_cusid .grid(row=0, column=0)
    l_cusname .grid(row=1, column=0)
    l_cuscon.grid(row=2, column=0)
    l_cusgen.grid(row=3,column=0)
    l_cusloc.grid(row=4, column=0)
    l_cusage.grid(row=5, column=0)

    #placing textboxes
    t_cusid.grid(row=0, column=1)
    t_cusname.grid(row=1, column=1)
    t_cuscon.grid(row=2, column=1)
    t_cusgen.grid(row=3, column=1)
    t_cusloc.grid(row=4, column=1)
    t_cusage.grid(row=5, column=1)

    #placing buttons
    search_btn.place(x = 310, y = 116)
    save_btn.place(x = 120, y = 320)
    delete_btn.place(x = 220, y = 320)

#**************************************SQL Code for Displaying Customer values from database*******************************************************
    
def display_customer_values():
    val = (t_cuscon.get(),)
    result = database.display_customer_info(val)
    row = result
    
    t_cusid.delete(0, END)
    t_cusname.delete(0, END)
    t_cusgen.delete(0, END)
    t_cusloc.delete(0, END)
    t_cusage.delete(0, END)
    
    t_cusid.insert(END,row[0])
    t_cusname.insert(END,row[1])
    t_cusgen.insert(END,row[2])
    t_cusloc.insert(END,row[3])
    t_cusage.insert(END,row[4])
    
#************************************SQL Code for Updating Customer to database**********************************************************************

def update_customer_values():
    val = (t_cusid.get(),t_cusname.get(),t_cusgen.get(),t_cusloc.get(),t_cusage.get(),t_cuscon.get())
    if t_cuscon.get() == "":
        tk.messagebox.showerror("Error","Input is required",parent = new_window)
    else:
        op = tk.messagebox.askyesno("Confirm ","Do you want to update",parent=new_window)
        if op == True:
             database.customer_update(val)
    
    t_cusid.delete(0, END)
    t_cusname.delete(0, END)
    t_cuscon.delete(0, END)
    t_cusgen.delete(0, END)
    t_cusloc.delete(0, END)
    t_cusage.delete(0, END)
    
def delete_customer_values():
    val = (t_cuscon.get(),)
    op = tk.messagebox.askyesno("Confirm ","Do you want to delete",parent=new_window)
    if op == True:
         database.delete_customer(val)

    t_cusid.delete(0, END)
    t_cusname.delete(0, END)
    t_cuscon.delete(0, END)
    t_cusgen.delete(0, END)
    t_cusloc.delete(0, END)
    t_cusage.delete(0, END)

#************************************Code for Display Customer Window********************************************************************************

def display_customers():
    global t_cusid,t_cusname,t_cuscon,cmb,t_cusloc,t_cusage
    new_window = Toplevel(root)
    new_window.title("Display Customer")
    new_window.geometry("660x600")
    new_window.configure(background="steelblue")
    
    result = database.get_customer()
    
    i = 1
    for row in result:
        for j in range(len(row)):
            e = Label(new_window,width=15, text=row[j]) 
            e.grid(row = i, column = j)
        i = i + 1    
        
    e = Label(new_window,width=15, text=row[j],borderwidth=2,relief='ridge', anchor="w")
    e=Label(new_window,width=15,text='Customer_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(new_window,width=15,text='Customer_name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(new_window,width=15,text='Customer_contact',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(new_window,width=15,text='Customer_gender',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(new_window,width=15,text='Customer_location',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(new_window,width=15,text='Customer_age',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    
#************************************Code for Add Items Window***************************************************************************************

def add_items():
    global t_proid,t_protype,t_probrand,t_promodel,t_promrp,t_procp,new_window
    new_window = Toplevel(root)
    new_window.title("Add Items")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_proid = Label(new_window, text = "Product_id",height = 3,width=20, bg="steelblue", anchor = 'w')
    l_protype = Label(new_window, text = "Product_type",height = 3,width=20, bg="steelblue", anchor = 'w')
    l_probrand = Label(new_window, text = "Product_brand",height = 3,width=20, bg="steelblue", anchor = 'w')
    l_promodel = Label(new_window, text = "Product_model",height = 3,width=20, bg="steelblue", anchor = 'w')
    l_promrp = Label(new_window, text = "Product_MRP",height = 3,width=20, bg="steelblue", anchor = 'w')
    l_procp = Label(new_window, text = "Product_CP",height = 3,width=20, bg="steelblue", anchor = 'w')

    #textboxes
    t_proid = Entry(new_window, width = 30)
    t_protype = Entry(new_window, width = 30)
    t_probrand = Entry(new_window, width = 30)
    t_promodel = Entry(new_window, width = 30)
    t_promrp = Entry(new_window, width = 30)
    t_procp = Entry(new_window, width = 30)
    
    #submit button
    save_btn = Button(new_window, text="Save", width = 10,command = insert_items_values)    

    #placing labels
    l_proid.grid(row=0, column=0)
    l_protype.grid(row=1, column=0)
    l_probrand.grid(row=2, column=0)
    l_promodel.grid(row=3, column=0)
    l_promrp.grid(row=4, column=0)
    l_procp.grid(row=5, column=0)

    #placing textboxes
    t_proid.grid(row=0, column=1)
    t_protype.grid(row=1, column=1)
    t_probrand.grid(row=2, column=1)
    t_promodel.grid(row=3, column=1)
    t_promrp.grid(row=4, column=1)
    t_procp.grid(row=5, column=1)

    #placing submit button
    save_btn.grid(row=6,column=1)
    
#************************************SQL Code to Add Item to database********************************************************************************

def insert_items_values():   
    val = (t_proid.get(),t_protype.get(),t_probrand.get(),t_promodel.get(),t_promrp.get(),t_procp.get())
    database.items_values(val)
    tk.messagebox.showinfo("Saved","Your values have been added", parent = new_window)

    t_proid.delete(0, END)
    t_protype.delete(0, END)
    t_probrand.delete(0, END)
    t_promodel.delete(0, END)
    t_promrp.delete(0, END)
    t_procp.delete(0, END)
    
#************************************Code for Update Item Info Window********************************************************************************

def change_item_info():
    global t_proid,t_protype,t_probrand,t_promodel,t_promrp,t_procp,new_window
    new_window = Toplevel(root)
    new_window.title("Change Item Info")
    new_window.geometry("400x400")
    new_window.configure(background="steelblue")
    
    #Labels
    l_proid = Label(new_window, text = "Product_id", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_protype = Label(new_window, text = "Product_type", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_probrand = Label(new_window, text = "Product_brand", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_promodel = Label(new_window, text = "Product_model", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_promrp = Label(new_window, text = "Product_MRP", height = 3, width=15, bg="steelblue", anchor = 'w')
    l_procp = Label(new_window, text = "Product_CP", height = 3, width=15, bg="steelblue", anchor = 'w')

    #textboxes
    t_proid = Entry(new_window, width = 30)
    t_protype = Entry(new_window, width = 30)
    t_probrand = Entry(new_window, width = 30)
    t_promodel = Entry(new_window, width = 30)
    t_promrp = Entry(new_window, width = 30)
    t_procp = Entry(new_window, width = 30)

    #buttons
    search_btn = Button(new_window, text="Search", width = 10,command = display_product_values)
    save_btn = Button(new_window, text="Save", width = 10,command =update_product_values)    
    delete_btn = Button(new_window, text ="Delete", width = 10,command = delete_product_values)
    
    #placing labels
    l_proid.grid(row=0, column=0)
    l_protype.grid(row=1, column=0)
    l_probrand.grid(row=2, column=0)
    l_promodel.grid(row=3, column=0)
    l_promrp.grid(row=4, column=0)
    l_procp.grid(row=5, column=0)

    #placing textboxes
    t_proid.grid(row=0, column=1)
    t_protype.grid(row=1, column=1)
    t_probrand.grid(row=2, column=1)
    t_promodel.grid(row=3, column=1)
    t_promrp.grid(row=4, column=1)
    t_procp.grid(row=5, column=1)

    #placing buttons
    search_btn.place(x = 310, y = 14)
    save_btn.place(x = 115, y = 320)
    delete_btn.place(x = 215, y = 320)

#**************************************SQL Code for Displaying Customer values from database*******************************************************
    
def display_product_values():
    val = (t_proid.get(),)
    result = database.display_items_info(val)
    row = result
    
    t_protype.delete(0, END)
    t_probrand.delete(0, END)
    t_promodel.delete(0, END)
    t_promrp.delete(0, END)
    t_procp.delete(0, END)
    
    t_protype.insert(END,row[0])
    t_probrand.insert(END,row[1])
    t_promodel.insert(END,row[2])
    t_promrp.insert(END,row[3])
    t_procp.insert(END,row[4])
    
#************************************SQL Code to Change Item in database********************************************************************************

def update_product_values():
    val = (t_protype.get(),t_probrand.get(),t_promodel.get(),t_promrp.get(),t_procp.get(),t_proid.get())
    if t_proid.get() == "":
        tk.messagebox.showerror("Error","Input is required",parent = new_window)
    else:
        op = tk.messagebox.askyesno("Confirm ","Do you want to update",parent=new_window)
        if op == True:
             database.item_update(val)

    t_protype.delete(0, END)
    t_probrand.delete(0, END)
    t_promodel.delete(0, END)
    t_promrp.delete(0, END)
    t_procp.delete(0, END)
    t_proid.delete(0, END)


def delete_product_values():
    val = (t_proid.get(),)
    op = tk.messagebox.askyesno("Confirm ","Do you want to delete",parent=new_window)
    if op == True:
         database.delete_item(val)

    t_protype.delete(0, END)
    t_probrand.delete(0, END)
    t_promodel.delete(0, END)
    t_promrp.delete(0, END)
    t_procp.delete(0, END)
    t_proid.delete(0, END)
    
#************************************Code for Display Item Window************************************

def display_items():
    global t_proid,t_protype,t_probrand,t_promodel,t_promrp,t_procp
    new_window = Toplevel(root)
    new_window.title("Display Items")
    new_window.geometry("660x600")
    new_window.configure(background="steelblue")
    
    result = database.get_item()
    
    i = 1
    for row in result:
        for j in range(len(row)):
            e = Label(new_window,width=15, text=row[j]) 
            e.grid(row = i, column = j)
        i = i + 1    
        
    e = Label(new_window,width=15, text=row[j],borderwidth=2,relief='ridge', anchor="w")
    e=Label(new_window,width=15,text='Product_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(new_window,width=15,text='Product_type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(new_window,width=15,text='Product_brand',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(new_window,width=15,text='Product_model',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(new_window,width=15,text='Product_MRP',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(new_window,width=15,text='Product_CP',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
        
#**********************************************************************************************************************************

def insert_sales_values():
    val = (Invoice_id.get(),Item_number.get(),Date.get(),Customer_id.get(),Product_id.get(),Quantity.get(),MRP.get(),Discount.get(),Actual_Sale_Price.get(),Total_Amount.get())
    database.sales_values(val)
    tk.messagebox.showinfo("Saved","Your values have been added", parent = new_window)

    Invoice_id.delete(0, END)
    Item_number.delete(0, END)
    Date.delete(0, END)
    Customer_id.delete(0, END)
    Product_id.delete(0, END)
    Quantity.delete(0, END)
    MRP.delete(0, END)
    Discount.delete(0, END)
    Actual_Sale_Price.delete(0, END)
    Total_Amount.delete(0, END)

#************************************Code for Main Window********************************************************************************************

def main_window():
    global root,lbl_clk,my_img
    root = Toplevel(mainWindow)
    root.title("Store Management")
    root.geometry("1200x700")
    root.configure(background="orange")
    title = Label(root, text = "Electronic Store Management System", compound = LEFT, font = ("times new roman", 35, "bold"), bg = "#010c48", fg = "white", anchor = 'w', padx = 200).place(x=0,y=0,relwidth=1,height=70)
    
    my_img = ImageTk.PhotoImage(Image.open("Tech2go.jpg"))
    my_label = Label(root,image = (my_img))
    my_label.place(x=350, y = 200)
       
    lbl_clk = Label(root, text="Welcome to Tech2go\t   Date: DD/MM/YYYY \t\t Time: HH:MM:SS", font = ("times new roman",25,'bold'), bg="#4d636d", fg = "white")
    lbl_clk.place(x=0,y=70,relwidth=1,height=50)
    
    admin_btn = Button(root, text = "Admin",width = 15 , padx = 5, pady = 5, font=("ariel", 15, "bold"), command = admin_window)
    admin_btn.place(x=20, y=150)
    customer_btn = Button(root, text = "Customer",width = 15 , padx = 5, pady = 5, font=("ariel", 15, "bold"), command = customer_window)
    customer_btn.place(x=20, y=250)
    items_btn = Button(root, text = "Items",width = 15 , padx = 5, pady = 5, font=("ariel", 15, "bold"), command = items_window)
    items_btn.place(x=20, y=350)
    sales_btn = Button(root, text = "Sales",width = 15 , padx = 5, pady = 5, font=("ariel", 15, "bold"), command = sales_window)
    sales_btn.place(x=20, y=450)
    logout_btn = Button(root, text = "Log Out",width = 15 , padx = 5, pady = 5, font=("ariel", 15, "bold"), command = root.destroy)
    logout_btn.place(x=20, y=550)
    
    title = Label(root,text = 'Hope You Have A Good Day!!!!!!!!!', compound = LEFT, font = ("times new roman", 35, "bold"), bg = "#010c48", fg = "white", anchor = 'w', padx = 220).place(x=0,y=630,relwidth=1,height=70)
    update_date_time()

def update_date_time():
    global time_,date_
    time_ = time.strftime("%I:%M:%S")
    date_ = time.strftime("%d-%m-%Y")
    lbl_clk.config(text="Welcome to Tech2go \t\t Date: {} \t\t Time: {}".format(date_,time_))
    lbl_clk.after(200,update_date_time)
    
    
