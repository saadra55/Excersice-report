# Name- Tahmida Lotif Tarin
# Id- 001125724
import tkinter as tk
import datetime
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter.messagebox import showinfo
import sqlite3 as sq
from tkinter import ttk

# Feature 1 - Saad Rashid

userlist = []
catlist = []
productlist = []


###########################################################################
def database(bool, sql):
    mydatabase = sq.connect("db.db")
    mycursor = mydatabase.cursor()
    mycursor.execute(sql)
    if bool == True:
        data = mycursor.fetchall()
        return data
    mydatabase.commit()


###########################################################################
# defining the classes
class Products:
    def __init__(self, prodID, prodname, category, img, price, discount, stock):
        self.prodID = prodID
        self.prodname = prodname
        self.category = category
        self.img = img
        self.price = price
        self.discount = discount
        self.stock = stock


class Users:
    def __init__(self, pid, name, uname, upass):
        self.pid = pid
        self.name = name
        self.uname = uname
        self.upass = upass


class Catergory:
    def __init__(self, cid, cname):
        self.cid = cid
        self.cname = cname


############################################################################
def loadusers(db):  # function will also add category
    userload = db(True, "select * FROM users")

    for i in userload:
        passing = Users(i[0], i[1], i[2], i[3])
        userlist.append(passing)
    return userlist


# maintaining product list
def loadproducts(db):  # function will also add products
    productload = db(True, "select * FROM Toys")
    for i in productload:
        passing = Products(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        productlist.append(passing)
    return productlist


def loadcate(db):
    catlist.clear()
    catload = db(True, "select * FROM Categories")
    for i in catload:
        passing = Catergory(i[0], i[1])
        catlist.append(passing)
    return catlist


############################################################################

def addcat():
    new_frame.forget()
    addcategory_frame.pack(pady=7)
    categorydisplay_frame.pack(pady=7)
    catergory_print()


# maintaining a list of categories
def check(cate_id, cate_name):
    allow = True
    for cat in catlist:
        if str(cat.cid) == str(cate_id):
            label1 = tk.Label(addcategory_frame, text='Category ID Already Exist')
            label1.pack()
            allow = False
        elif str(cat.cname) == str(cate_name):
            label1 = tk.Label(addcategory_frame, text='Category Name Already Exist')
            label1.pack()
            allow = False
    return allow


def check1(cate_id, cate_name):
    allow = True
    for cat in catlist:
        if str(cat.cid) == str(cate_id):
            allow = False
        elif str(cat.cname) == str(cate_name):
            allow = False
    return allow


def add_categorydb():
    cat_name = entry2.get()
    cat_id = entry1.get()
    allow = check(cat_id, cat_name)
    if allow == True:
        if cat_name != "" and cat_id != "":
            # label1 = tk.Label(addcategory_frame, text='Category Added')
            # label1.pack()
            adding = database(False, f"INSERT INTO `Categories` (`ID`, `Name`) VALUES ('{cat_id}', '{cat_name}');")
            catergory_print()
        else:
            label1 = tk.Label(addcategory_frame, text='Please fill both entry Fields')
            label1.pack()


def edit_category_db():
    cat_name = entry2.get()
    cat_id = entry1.get()
    for cat in catlist:
        if str(cat_id == cat.cid):
            database(False, f"UPDATE Categories SET Name = '{cat_name}' WHERE ID = {cat_id};")
            catergory_print()
    # for label in addcategory_frame.winfo_children():
    #     label.destroy()
    # frame_print()
    # label1 = tk.Label(addcategory_frame, text=f'Category {cat_id} Edited to {cat_name}')
    # label1.pack()


def catergory_print():
    x = 1
    loadcate(database)
    for label in categorydisplay_frame.winfo_children():
        label.destroy()

    label1 = tk.Label(categorydisplay_frame, text="Category Id:        ")
    label1.grid(column=0, row=1)
    label2 = tk.Label(categorydisplay_frame, text="Category Name:      ")
    label2.grid(column=1, row=1)

    for cat in catlist:
        x = x + 1
        label1 = tk.Label(categorydisplay_frame, text=cat.cid)
        label1.grid(column=0, row=x)
        label2 = tk.Label(categorydisplay_frame, text=cat.cname)
        label2.grid(column=1, row=x)


def delete_category_db():
    cat_name = entry2.get()
    cat_id = entry1.get()
    for cat in catlist:
        if str(cat_id == cat.cid):
            database(False, f"DELETE FROM Categories WHERE ID = {cat_id};")
            catergory_print()
    # label1 = tk.Label(addcategory_frame, text=f'Category {cat_id} DELETED')
    # label1.pack()


############################################################################
def addprod_db():
    new_frame.forget()
    addpro.pack()


def addproduct():
    productID = entry_proid.get()
    prodname = entry_proname.get()
    prodca = entry_procate.get()
    prodimg = entry_proimage.get()
    prodprice = entry_price.get()
    prodiscount = entry_discount.get()
    prodstk = entry_stock.get()


    if productID != "" and prodname != "" and prodca != "" and prodimg != "" and prodprice != "" and prodiscount != "" and prodstk != "":
        adding = database(False,f"INSERT INTO Toys (`ID`, `Name`, `Stock`, `Discount`, `Price`, `Image`, `Category`) VALUES ('{productID}', '{prodname}', '{prodstk}', '{prodiscount}', '{prodca}', '{prodimg}', '{prodprice}');")
        print(productlist)
        label3 = tk.Label(addpro, text='Product Added')
        label3.grid()
    else:
        label1 = tk.Label(addpro, text='please enter all the values')
        label1.grid()


def editproducts():
    productID = entry_proid.get()
    prodname = entry_proname.get()
    prodca = entry_procate.get()
    prodimg = entry_proimage.get()
    prodprice = entry_price.get()
    prodiscount = entry_discount.get()
    prodstk = entry_stock.get()
    if productID != "" and prodname != "" and prodca != "" and prodimg != "" and prodprice != "" and prodiscount != "" and prodstk != "":
        for produ in productlist:
            if int(productID) == int(produ.prodID):
                print("correct")
                database(False, f"UPDATE Toys SET 'Name' = '{prodname}','Discount' = '{prodiscount}', 'Stock' = '{prodstk}', 'Category' = '{prodca}', 'Image'='{prodimg}', 'Price'='{prodprice}'  WHERE 'ID' = '{productID}';")
                tk.Label(addpro, text="Product updated").grid()
    else:
        tk.Label(addpro, text="Please enter all the fields").grid()


######################################################################################################
# ----------------------------------------------------------------------------------------------------

def deleteproduct():
    productid = entry_proid.get()
    prodname = entry_proname.get()
    prodca = entry_procate.get()
    prodimg = entry_proimage.get()
    prodprice = entry_price.get()
    for produ in productlist:
        if int(productid == str(produ.prodID)):
            database(False, f"DELETE FROM Toys WHERE ID = {produ.prodID};")
            tk.Label(addpro, text="Product has been deleted").grid()


def take_record():
    all_toys = database(True, "SELECT ID, Name, Stock, Price FROM Toys")

    date = datetime.date.today()
    f = open(str(date) + ".txt", "w+")
    stock_text = ""

    for item in all_toys:
        stock_text = stock_text + "id: " + str(item[0]) + " - name: " + str(item[1]) + " - stock: " + str(
            item[2]) + " - price(£): " + str(item[3]) + "\n"

    f.write(stock_text)
    f.close()


def lowstock():
    a_toys = database(True, "SELECT Name FROM Toys WHERE Stock < '20 ' ")
    messagebox.showinfo('Low Stock alert', message=a_toys)


def login():
    usern = username.get()
    passw = password.get()

    for users in userlist:
        if (str(usern) == users.uname) and (str(passw) == users.upass):
            change_frame()
            lowstock()

    incorrect = tk.Label(login_frame, text="Username and password is incorrect")
    incorrect.pack()


############################################################################


def change_frame():
    login_frame.forget()
    new_frame.pack()


def center_window():
    width, height = 500, 400  # Set the width and height
    screen_width = root.winfo_screenwidth()  # Get the screen width
    screen_height = root.winfo_screenheight()  # Get the screen height
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width,
                                       height,
                                       x_cord,
                                       y_cord))

def saad_main():
    global new_frame, addcategory_frame, categorydisplay_frame, entry2, entry1, addpro, entry_proid, entry_proname, entry_procate, entry_proimage, entry_price, entry_discount, entry_stock, username, password, login_frame, login_frame, root
    # tkinter interface

    root = tk.Tk()
    center_window()
    ############################################################################
    # Frames
    login_frame = tk.Frame(root)
    new_frame = tk.Frame(root)
    addcategory_frame = tk.Frame(root)
    categorydisplay_frame = tk.Frame(root)
    addpro = tk.Frame(root)

    # login frame
    loadusers(database)
    loadcate(database)
    loadproducts(database)

    label1 = tk.Label(login_frame, text='Username:', font='calibre')
    label1.pack()
    username = tk.Entry(login_frame)
    username.pack()
    label2 = tk.Label(login_frame, text='Password:', font='calibre')
    label2.pack()
    password = tk.Entry(login_frame, show='*')
    password.pack()
    password.bind('<Return>')

    login_button = tk.Button(login_frame, text="Login", command=login)
    login_button.pack()

    # new frame after login
    addcat_button = tk.Button(new_frame, text="Category", command=addcat)
    addcat_button.pack()

    addprod_button = tk.Button(new_frame, text="Products", command=addprod_db)
    addprod_button.pack()

    add_button = tk.Button(new_frame, text="Stock Taking", command=lambda: take_record())
    add_button.pack()

    # Catergory Frame
    label1 = tk.Label(addcategory_frame, text='Category ID')
    label1.pack()
    entry1 = tk.Entry(addcategory_frame, text='')
    entry1.pack()
    label2 = tk.Label(addcategory_frame, text='Category Name')
    label2.pack()
    entry2 = tk.Entry(addcategory_frame, text='')
    entry2.pack()
    add_button = tk.Button(addcategory_frame, text="Add Catergory", command=add_categorydb)
    add_button.pack()
    add_button1 = tk.Button(addcategory_frame, text="Edit Catergory", command=edit_category_db)
    add_button1.pack()
    add_button2 = tk.Button(addcategory_frame, text="Delete Catergory", command=delete_category_db)
    add_button2.pack()

    # pro frame
    label30 = tk.Label(addpro, text='Enter the product ID')
    label30.grid()

    entry_proid = tk.Entry(addpro, text='')
    entry_proid.grid()

    label3 = tk.Label(addpro, text='Enter the product name')
    label3.grid()

    entry_proname = tk.Entry(addpro, text='')
    entry_proname.grid()

    label4 = tk.Label(addpro, text='Enter the category id')
    label4.grid()

    entry_procate = tk.Entry(addpro, text='')
    entry_procate.grid()

    label5 = tk.Label(addpro, text='image')
    label5.grid()

    entry_proimage = tk.Entry(addpro, text='')
    entry_proimage.grid()

    label5 = tk.Label(addpro, text='price')
    label5.grid()

    entry_price = tk.Entry(addpro, text='')
    entry_price.grid()

    label5 = tk.Label(addpro, text='discount')
    label5.grid()

    entry_discount = tk.Entry(addpro, text='')
    entry_discount.grid()

    label5 = tk.Label(addpro, text='stock')
    label5.grid()

    entry_stock = tk.Entry(addpro, text='')
    entry_stock.grid()

    add_button = tk.Button(addpro, text="Add Product", command=addproduct)
    add_button.grid()

    add_button1 = tk.Button(addpro, text="Edit Product", command=editproducts)
    add_button1.grid()

    add_button2 = tk.Button(addpro, text="Delete Product", command=deleteproduct)
    add_button2.grid()

    ##################################################
    login_frame.pack()
    root.mainloop()


# Feature 3 - Sadat Rahman

def receipt():
    global date_and_time
    date_and_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    global receipt_text
    receipt_text = "All About Toys Ltd.\nDate & time: " + str(date_and_time) + "\nProducts purchased:\n"

    for item in basket:
        receipt_text = receipt_text + (str(item[0]) + " - " + item[1] + (40-len(item[1]))*"." + " " + str(item[4]) + "\n")

    extra_label2 = tk.Label(f4, text="                                               ", height=3, bg="pink")
    receipt_label = tk.Label(f4, text=receipt_text, font="Helvetica 12", width=50, justify="left", anchor="w", bg="pink")
    extra_label2.grid(row=0, column=0)
    receipt_label.grid(row=1, column=1)


def visacheck(is_verified):
    if is_verified:
        receipt()


def save_receipt():
    date_and_time2 = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S--")
    f = open(str(date_and_time2) + "receipt.txt", "w+")
    f.write(receipt_text)
    f.close()


def get_from_database(*args):
    db = sq.connect("db.db")
    c = db.cursor()

    if args:
        c.execute("DELETE FROM Basket WHERE ID=" + str(args[0]))

    global basket
    basket = c.execute("SELECT ID, Name, Stock, Discount, Price FROM Basket").fetchall()
    print(basket)
    db.commit()
    c.close()
    db.close()


def show_frame(xframe):
    xframe.tkraise()


def calculate_totals_1_and_2(row_id):
    # Calculating total 1
    print(row_id)
    all_prices = []

    for i in range(row_id):
        all_prices.append(labels[str(i) + "_price"].cget("text"))

    total = list(map(float, all_prices))

    print(total)

    total1 = round(sum(total), 2)

    # Calculating total 2
    i = 0
    for toy in basket:
        if toy[3] == "10%":
            total[i] = round(toy[4] * 0.9, 2)
        i += 1

    total2 = round(sum(total), 2)

    print(total)

    return total1, total2


def radiobutton():
    print(radio.get())
    global tot2
    if radio.get() == 3:
        tot2 = tot[1]+5
        l2_value3.config(text=tot2)
    else:
        tot2 = tot[1]
        l2_value3.config(text=tot2)


def delete(row_id):
    print(row_id)
    get_from_database(labels[str(row_id) + "_id"].cget("text"))

    try:
        for i in range(1000):
            labels[str(i) + "_id"].destroy()
            labels[str(i) + "_name"].destroy()
            labels[str(i) + "_quantity"].destroy()
            labels[str(i) + "_discount"].destroy()
            labels[str(i) + "_price"].destroy()
            buttons[str(i) + "_delete_button"].destroy()
            print(i)
    except:
        pass

    labels.clear()
    f1_show_products_on_basket()


def f1_show_products_on_basket():

    global labels
    global buttons
    labels = dict()
    buttons = dict()
    x = 1
    y = 2
    global row_id
    row_id = 0
    for item in basket:
        # Adding the labels/buttons in dictionaries.
        labels[str(row_id) + "_id"] = tk.Label(f1, text=item[0], bg="white", height=2)
        labels[str(row_id) + "_name"] = tk.Label(f1, text=item[1], bg="white", height=2)
        labels[str(row_id) + "_quantity"] = tk.Label(f1, text=int(item[2]/item[2]), bg="white", height=2)
        labels[str(row_id) + "_discount"] = tk.Label(f1, text=item[3], bg="white", height=2)
        labels[str(row_id) + "_price"] = tk.Label(f1, text=str((item[4])), bg="white", height=2)
        buttons[str(row_id) + "_delete_button"] = tk.Button(f1, text="x", bg="red", command=lambda row_id=row_id: delete(row_id))

        # Displaying the labels/buttons.
        labels[str(row_id) + "_id"].grid(row=y, column=x)
        labels[str(row_id) + "_name"].grid(row=y, column=x+1)
        labels[str(row_id) + "_quantity"].grid(row=y, column=x+2)
        labels[str(row_id) + "_discount"].grid(row=y, column=x+3)
        labels[str(row_id) + "_price"].grid(row=y, column=x+4)
        buttons[str(row_id) + "_delete_button"].grid(row=y, column=x+5)
        y += 1
        row_id += 1

    for i in range(len(basket)):
        if labels[str(i)+"_discount"].cget("text") == "10%" or labels[str(i)+"_discount"].cget("text") == "BOGOF":
            tk.Label(f1, text="Discounts will be\napplied at checkout.", bg="white").grid(row=50, column=2)
            break


def display_total():
    global tot
    tot = calculate_totals_1_and_2(row_id)

    global l2_value1
    global l2_value2
    global l2_value3
    l2_value1 = tk.Label(f2, text=tot[0], font="Helvetica 10", anchor="w", width=36, bg="cyan")
    l2_value2 = tk.Label(f2, text=tot[1], font="Helvetica 10", anchor="w", width=36, bg="cyan")
    l2_value3 = tk.Label(f2, text=tot[1], font="Helvetica 10 bold", anchor="w", width=36, bg="cyan")

    l2_value1.grid(row=12, column=2)
    l2_value2.grid(row=13, column=2)
    l2_value3.grid(row=14, column=2)


def save_sales_info():
    db = sq.connect("db.db")
    c = db.cursor()

    items = ""
    for toy in basket:
        items += toy[1] + ", "
    items = items[:-2]

    if radio.get() == 1:
        delivery_address = "10 Stockwell St, London SE10 9BD"
    elif radio.get() == 2:
        delivery_address = "Bexley Rd, London SE9 2PQ"
    else:
        delivery_address = address_line_2.get() + ", " + address_line_1.get() + ", " + city.get() + " " + post_code.get()

    if delivery_address[0] == ",":
        delivery_address = delivery_address[2:]

    contact = contact_number.get()

    sales_info = (items, tot2, delivery_address, contact)

    c.execute("INSERT INTO Sales (Items, Total_price, Delivery_address, Contact_phone) VALUES (?,?,?,?)", sales_info)

    db.commit()
    c.close()
    db.close()


def update_stock():
    db = sq.connect("db.db")
    c = db.cursor()

    for toy in basket:
        c.execute("UPDATE Toys SET Stock = " + str(toy[2]-1) + " WHERE ID = " + str(toy[0]))

    c.execute("DELETE FROM Basket")

    db.commit()
    c.close()
    db.close()


def main_gui():
    window = tk.Tk()
    window.title("Shopping Basket")

    # Frames
    global f1, f2, f3, f4
    f1 = tk.LabelFrame(window, text="Shopping Cart", bg="white", height=500, width=575)
    f2 = tk.LabelFrame(window, text="Checkout", bg="cyan", height=500, width=575)
    f3 = tk.LabelFrame(window, text="Payment", bg="gold", height=500, width=575)
    f4 = tk.LabelFrame(window, text="Receipt", bg="pink", height=500, width=575)

    # Buttons
    b1 = tk.Button(f1, text="Checkout", bg="lime", width=15, command=lambda: [show_frame(f2), display_total()])
    b2 = tk.Button(f2, text="Go to payment", width=15, bg="lime", command=lambda: show_frame(f3))
    b3 = tk.Button(f3, text="Pay", bg="lime", width=15, command=lambda: [radiobutton(), show_frame(f4), visacheck(True), save_sales_info(), update_stock()])
    b4 = tk.Button(f4, text="Save receipt", bg="lime", width=15, command=lambda: save_receipt())

    # Receiving the items' info from the database.
    get_from_database()

    # F1. Shopping Basket

    f1_show_products_on_basket()

    tk.Label(f1, text="", bg="white").grid(row=0)
    tk.Label(f1, text="ID", bg="white", width=12, font="Helvetica 10 bold").grid(row=1, column=1)
    tk.Label(f1, text="Item name", bg="white", width=12, font="Helvetica 10 bold").grid(row=1, column=2)
    tk.Label(f1, text="Quantity", bg="white", width=12, font="Helvetica 10 bold").grid(row=1, column=3)
    tk.Label(f1, text="Discount", bg="white", width=12, font="Helvetica 10 bold").grid(row=1, column=4)
    tk.Label(f1, text="Price", bg="white", width=12, font="Helvetica 10 bold").grid(row=1, column=5)
    tk.Label(f1, text="", bg="white").grid(row=49)

    # F2. Checkout

    tk.Label(f2, text="     ", bg="cyan").grid(row=0, column=0)
    tk.Label(f2, text="     ", bg="cyan").grid(row=1, column=0)
    tk.Label(f2, text="Delivery options:", anchor="w", width=36, bg="cyan").grid(row=2, column=1)




    global radio
    radio = tk.IntVar()
    tk.Radiobutton(f2, text="Click and collect from our main physical store at: \n10 Stockwell St, London SE10 9BD",
                          justify=tk.LEFT, width=36, anchor="w", bg="cyan", variable=radio, value=1, command=lambda: radiobutton()).grid(row=3, column=1)
    tk.Radiobutton(f2, text="Click and collect from our pickup location at: \nBexley Rd, London SE9 2PQ",
                          justify=tk.LEFT, width=36, anchor="w", bg="cyan", variable=radio, value=2, command=lambda: radiobutton()).grid(row=4, column=1)
    tk.Radiobutton(f2, text="Enter your address details: ", width=36, anchor="w", bg="cyan",
                          variable=radio, value=3, command=lambda: radiobutton()).grid(row=5, column=1)
    radio.set(1)






    tk.Label(f2, text="Address Line 1: ", anchor="w", width=36, bg="cyan").grid(row=6, column=1)
    tk.Label(f2, text="Address Line 2: ", anchor="w", width=36, bg="cyan").grid(row=7, column=1)
    tk.Label(f2, text="City: ", anchor="w", width=36, bg="cyan").grid(row=8, column=1)
    tk.Label(f2, text="Post code: ", anchor="w", width=36, bg="cyan").grid(row=9, column=1)
    tk.Label(f2, text="Contact number: ", anchor="w", width=36, bg="cyan").grid(row=10, column=1)

    global address_line_1, address_line_2, city, post_code, contact_number
    address_line_1 = tk.Entry(f2, width=30)
    address_line_2 = tk.Entry(f2, width=30)
    city = tk.Entry(f2, width=30)
    post_code = tk.Entry(f2, width=30)
    contact_number = tk.Entry(f2, width=30)

    f = 6
    for entry in (address_line_1, address_line_2, city, post_code, contact_number):
        entry.grid(row=f, column=2)
        f += 1
 # Ihave edit comment here to better understand thi s
    tk.Label(f2, text="", anchor="w", width=36, height=4, bg="cyan").grid(row=11, column=1)
    tk.Label(f2, text="Total price..................................................................... ",
             anchor="w", width=36, bg="cyan").grid(row=12, column=1)
    tk.Label(f2, text="Total price with discount applied............................... ",
             anchor="w", width=36, bg="cyan").grid(row=13, column=1)
    tk.Label(f2, text="Total price with delivery fee applied........................... ",
             anchor="w", width=36, bg="cyan").grid(row=14, column=1)

    # F3. Payment

    tk.Label(f3, text="                ", bg="gold").grid(row=0, column=0)
    tk.Label(f3, text="       ", bg="gold").grid(row=1, column=0)
    tk.Label(f3, text="       ", bg="gold").grid(row=2, column=0)
    tk.Label(f3, text="       ", bg="gold").grid(row=3, column=0)
    tk.Label(f3, text="       ", bg="gold").grid(row=4, column=0)

    tk.Label(f3, text="Enter payment details:", anchor="w", width=36, bg="gold").grid(row=5, column=1)

    tk.Label(f3, text="VISACheck", anchor="w", width=16, font="Times 20 bold", bg="gold").grid(row=3, column=1)

    tk.Label(f3, text="Name:", anchor="w", width=36, bg="gold").grid(row=6, column=1)
    tk.Label(f3, text="Card number:", anchor="w", width=36, bg="gold").grid(row=7, column=1)
    tk.Label(f3, text="CVV:", anchor="w", width=36, bg="gold").grid(row=8, column=1)
    tk.Label(f3, text="Expiration date:", anchor="w", width=36, bg="gold").grid(row=9, column=1)
    tk.Label(f3, text="Address:", anchor="w", width=36, bg="gold").grid(row=10, column=1)
    tk.Label(f3, text="City:", anchor="w", width=36, bg="gold").grid(row=11, column=1)
    tk.Label(f3, text="Post code:", anchor="w", width=36, bg="gold").grid(row=12, column=1)
    tk.Label(f3, text="", bg="gold", width=30).grid(row=13, column=2)
    tk.Label(f3, text="", bg="gold", width=30).grid(row=14, column=2)

    e3_1 = tk.Entry(f3, width=30).grid(row=6, column=2)
    e3_2 = tk.Entry(f3, width=30).grid(row=7, column=2)
    e3_3 = tk.Entry(f3, width=30).grid(row=8, column=2)
    e3_4 = tk.Entry(f3, width=30).grid(row=9, column=2)
    e3_5 = tk.Entry(f3, width=30).grid(row=10, column=2)
    e3_6 = tk.Entry(f3, width=30).grid(row=11, column=2)
    e3_7 = tk.Entry(f3, width=30).grid(row=12, column=2)

    # Deploying frames and buttons.

    for frame in (f1, f2, f3, f4):
        frame.grid(row=0, column=0)
        frame.grid_propagate(0)

    b1.grid(row=50, column=5)
    b2.grid(row=50, column=2)
    b3.grid(row=50, column=2)
    b4.grid(row=50, column=1)

    show_frame(f1)

    window.mainloop()


def add_to_basket(id):
    import sqlite3 as sq

    db = sq.connect("db.db")
    c = db.cursor()

    try:
        c.execute(
            "INSERT INTO Basket (ID, Name, Stock, Discount, Price, Image, Category) SELECT * FROM Toys WHERE ID=" + str(id))
    except:
        pass

    db.commit()
    c.close()
    db.close()

def open_basket():
    main_gui()

# Feature 4 - Rutik Ramniklal

class loginscreen:

    def __init__(self,master = tk.Tk()):

        self.master = master
        master.title("STAFF LOGIN TOYSHOP ")
        master.geometry("450x230+450+170")

        tk.Label(master, text="STAFF LOGIN ", font=(None, 20)).pack()

        # Creating describtions

        self.username = tk.Label(master, text="Username:")
        self.username.place(relx=0.285, rely=0.298, height=20, width=55)

        self.password = tk.Label(master, text="Password:")
        self.password.place(relx=0.285, rely=0.468, height=20, width=55)

        # Creating Buttons

        self.login_button = tk.Button(master, text="Login")
        self.login_button.place(relx=0.440, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_verify)

        # Creating entry boxes

        self.username_box = tk.Entry(master)
        self.username_box.place(relx=0.440, rely=0.298, height=20, relwidth=0.35)

        self.password_box = tk.Entry(master)
        self.password_box.place(relx=0.440, rely=0.468, height=20, relwidth=0.35)
        self.password_box.configure(show="*")
        self.password_box.configure(background="white")

    def login_verify(self):
        #Database

        conn = sq.connect("db.db")

        c = conn.cursor()

        c.execute("SELECT * FROM StaffLogin")
        v_username = self.username_box.get()
        v_password = self.password_box.get()

        for rows in c.fetchall():

            if v_username == rows[1] and v_password == rows[3]:
                showinfo("Login Successful", "Welcome Staff")
                self.master.withdraw()
                mainwindow = mainscreen()



            else:
                showinfo("Error Message", "Username and password not Found")


    def mainloop_window(self): #This is the class function that helps me to mainloop the window
        self.master.mainloop()



class mainscreen:

    def __init__(self,mainwindow = tk.Tk()):
        self.mainwindow = mainwindow
        mainwindow.title("STAFF MENU")
        mainwindow.geometry("450x300")

        tk.Label(mainwindow, text="STAFF MENU ", font=(None, 20)).pack()

        self.customer_query_button = tk.Button(mainwindow, text="Customer Queries")
        self.customer_query_button .pack()
        self.customer_query_button .configure(height = 3, width = 30, command= self.open_customer_queries)

        self.generate_report_button  = tk.Button(mainwindow, text="Generate Report")
        self.generate_report_button .pack()
        self.generate_report_button .configure(height = 3, width = 30)

        self.maintain_scheme_button  = tk.Button(mainwindow, text="Maintain Scheme")
        self.maintain_scheme_button .pack()
        self.maintain_scheme_button .configure(height = 3, width = 30, command= self.open_scheme)

    def open_customer_queries(self):
        customerwindow = customerqurey()


    #def open_generate_report(self):
       # customerwindow = customerqurey()

    def open_scheme(self):
        schemewindow = scheme()




class customerqurey:

    def __init__(self,customerwindow = tk.Tk()):

        self.customerwindow = customerwindow
        customerwindow.title("STAFF MENU")
        customerwindow.geometry("1000x500")

        tk.Label(customerwindow, text="Customer Review ", font=(None, 20)).pack()

        viewFrame = tk.Frame(customerwindow, width=600, height=100)
        viewFrame.pack(fill = tk.BOTH)


        self.querylist = ttk.Treeview(viewFrame, column=("column1", "column2", "column3", "column4", "column5"),
                                 show='headings')
        self.querylist.heading("#1", text="ToyID")
        self.querylist.heading("#2", text="Toy Name")
        self.querylist.heading("#3", text="User Name")
        self.querylist.heading("#4", text="Review")
        self.querylist.heading("#5", text="Response")
        self.querylist.grid(row=0, column=0, padx=50)

        self.querylist.pack(fill = tk.BOTH, expand=1)

        ################################

        self.connection = sq.connect("db.db")  # connect to db
        cur = self.connection.cursor()
        cur.execute("SELECT *, oid FROM Reviews")  # take all data from  table
        rows = cur.fetchall()
        for row in rows:
            print(row)  # it print all records in the database
            self.querylist.insert('', tk.END, values=row)  # insert in the treeview table
        self.connection.commit()  # commit changes
        self.connection.close()  # close connection

        self.lblid = tk.Label(customerwindow, text="Select ID;").pack()
        self.entrycustomerid = tk.Entry(customerwindow)
        self.entrycustomerid.pack()

        self.lblreply = tk.Label(customerwindow, text="Reply;").pack()
        self.entryreply = tk.Entry(customerwindow)
        self.entryreply.pack()


        self.btnreply = tk.Button(customerwindow, text="Reply", command=self.customerreply)
        self.btnreply.pack()

        self.btnresetcustomerdisplay = tk.Button(customerwindow, text="Reset Display", command=self.remove_all)
        self.btnresetcustomerdisplay.pack()

        self.btndisplay= tk.Button(customerwindow, text="Display", command=self.displayRec)
        self.btndisplay.pack()

        self.btndeletecustomer = tk.Button(customerwindow, text="Delete", command=self.deleteCustomer)
        self.btndeletecustomer.pack()

    def customerreply(self):

        conn = sq.connect("db.db")

        c = conn.cursor()

        staff_reply = self.entryreply.get()
        select_cusomterid = self.entrycustomerid.get()

        c.execute("UPDATE Reviews SET  StaffResponse = ? WHERE ToyID = ?", (str(staff_reply), int(select_cusomterid)))

        conn.commit()
        conn.close()

    def remove_all(self):
        for record in self.querylist.get_children():
            self.querylist.delete(record)

    def displayRec(self):
        conn = sq.connect("db.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM Reviews")  # take all data from  table
        rows = c.fetchall()
        for row in rows:
            print(row)  # it print all records in the database
            self.querylist.insert('', tk.END, values=row)  # insert in the treeview table
        self.connection.commit()  # commit changes
        self.connection.close()

    def deleteCustomer(self):

        conn = sq.connect("db.db")

        c = conn.cursor()

        select_cusomterid = self.entrycustomerid.get()

        c.execute("DELETE from Reviews where ToyID = ?", (str(select_cusomterid)))

        conn.commit()
        conn.close()



class scheme:



    def __init__(self, schemewindow = tk.Tk()):


        self.schemewindow = schemewindow
        self.schemewindow.title("Schemes")
        self.schemewindow.geometry("1350x800+0+0")

        #Label

        self.lblstaffName = tk.Label(schemewindow, text="staffName:", font="bold")
        self.lblstaffName.pack()

        self.entrystaffName = tk.Entry(schemewindow)
        self.entrystaffName.pack()
        #Label

        self.lblschemeName = tk.Label(schemewindow, text="schemeName:", font="bold")
        self.lblschemeName.pack()

        self.entryschemeName = tk.Entry(schemewindow)
        self.entryschemeName.pack()

        self.lblschemeDetails = tk.Label(schemewindow, text="schemeDetails:", font="bold")
        self.lblschemeDetails.pack()

        self.entryschemeDetails = tk.Entry(schemewindow)
        self.entryschemeDetails.pack()

        self.lblPercentage = tk.Label(schemewindow, text="Discount Percentage%:", font="bold")
        self.lblPercentage.pack()

        self.entryPercentage = tk.Entry(schemewindow)
        self.entryPercentage.pack()

        #Button Add
        self.btnAddScheme = tk.Button(schemewindow, text="Add", font="bold", command=self.addScheme)
        self.btnAddScheme.pack()

        # Button Display
        self.btnDisplayScheme = tk.Button(schemewindow, text="Display Result", font="bold", command=self.displayScheme)
        self.btnDisplayScheme.pack()

        ###### Button Reset Display #######

        self.btnResetDisplay = tk.Button(schemewindow, text="Reset Display", font="bold", command=self.display_reset)
        self.btnResetDisplay.pack()

        ######################### select
        self.btnselectRec = tk.Button(schemewindow, text="Select Record", font="bold", command=self.selectRecord)
        self.btnselectRec.pack()
        ############################## update
        self.btneditRec = tk.Button(schemewindow, text="Edit Record", font="bold", command=self.editRecord)
        self.btneditRec.pack()


        ########################################################
        def schemetable(self):
            viewFrame = tk.Frame(schemewindow, width=600, height=100)
            viewFrame.pack(fill=tk.BOTH)

            self.schemelist = ttk.Treeview(viewFrame, column=("column1", "column2", "column3", "column4", "column5"),
                                           show='headings')
            self.schemelist.heading("#1", text="schID")
            self.schemelist.heading("#2", text="staffName")
            self.schemelist.heading("#3", text="schemeName")
            self.schemelist.heading("#4", text="schemeDetails")
            self.schemelist.heading("#5", text="Discount Percentage%:")

            self.schemelist.pack()

            self.schemelist.pack(fill=tk.BOTH, expand=1)
            import sqlite3

            self.connection = sqlite3.connect("db.db")  # connect to db
            cur = self.connection.cursor()
            cur.execute("SELECT *, oid FROM tblScheme")  # take all data from  table
            rows = cur.fetchall()
            for row in rows:
                print(row)  # it print all records in the database
                self.schemelist.insert('', tk.END, values=row)  # insert in the treeview table
            self.connection.commit()  # commit changes
            self.connection.close()  # close connection

        schemetable(self)


        ###### Entry and Label#######
        self.lblSeletedSchID = tk.Label(schemewindow, text="SELECTED ID :", font="bold")
        self.lblSeletedSchID.pack()

        self.entrySeletedSchID = tk.Entry(schemewindow)
        self.entrySeletedSchID.pack()

        ###### Button Delete #######

        self.btnDeleteScheme = tk.Button(schemewindow, text="Delete", font="bold", command=self.deleteScheme)
        self.btnDeleteScheme.pack()

    def selectRecord(self):
        conn = sq.connect("db.db")

        c = conn.cursor()

        selectedSchemeID = self.entrySeletedSchID.get()

        c.execute("SELECT * from tblScheme where schID = ?", (str(selectedSchemeID)))
        scheme_value = c.fetchall()

        for selected_scheme in scheme_value:
            self.entrystaffName.insert(0, selected_scheme[1])
            self.entryschemeName.insert(0, selected_scheme[2])
            self.entryschemeDetails.insert(0, selected_scheme[3])
            self.entryPercentage.insert(0, selected_scheme[4])


    def editRecord(self):

        conn = sq.connect("db.db")

        c = conn.cursor()

        selectedSchemeID = self.entrySeletedSchID.get()

        c.execute("""UPDATE tblScheme SET
        staffName = :sname,
        schemeName = :schname ,
        schemeDetails  = :schdetail,
        Percentage = :schpercentage
        WHERE schID = :id""", {'sname':  self.entrystaffName.get(),
                                     'schname':  self.entryschemeName.get(),
                                     'schdetail':  self.entryschemeDetails.get(),
                                     'schpercentage':  self.entryPercentage.get(),
                                     'id': selectedSchemeID})



        conn.commit()
        conn.close()





    def addScheme(self):
        conn = sq.connect("db.db")

        c = conn.cursor()

        staff_Name = self.entrystaffName.get()
        scheme_Name = self.entryschemeName.get()
        schemeDetails = self.entryschemeDetails.get()
        Discount_Percentage = self.entryPercentage.get()

        c.execute("INSERT INTO tblScheme (staffName, schemeName,schemeDetails,Percentage) VALUES (?,?,?,?)",
                  (str(staff_Name), str(scheme_Name), str(schemeDetails), int(Discount_Percentage)))

        conn.commit()
        conn.close()

    def display_reset(self):
        for record in self.schemelist.get_children():
            self.schemelist.delete(record)

    def displayScheme(self):
        conn = sq.connect("db.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM tblScheme")  # take all data from  table
        rows = c.fetchall()
        for row in rows:
            print(row)  # it print all records in the database
            self.schemelist.insert('', tk.END, values=row)  # insert in the treeview table
        self.connection.commit()  # commit changes
        self.connection.close()

    def deleteScheme(self):

        conn = sq.connect("db.db")

        c = conn.cursor()

        selectedSchemeID = self.entrySeletedSchID.get()

        c.execute("DELETE from tblScheme where schID = ?", (str(selectedSchemeID)))

        conn.commit()
        conn.close()

def rutik():
    login = loginscreen()

    login.mainloop_window()

# Feature 2 - Tahmida Lotif Tarin

class FeatureTwo(tk.Tk):
    # This is a class i used to switch between multiple frame

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=20, weight="bold")

        # the container is where we'll keep all the frames on top of each other,
        # then the one we want visible
        # will be shown above the other ones
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, ProductMenu, ReviewPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        """this will display a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    """This is the main menu page from where we will go to different pages.
    the search feature is implemented here and i gets the data typed by the user and
    get the info about the particular product and pack it at the bottom of the page """

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title('All About Toys LTD')
        self.controller.state('zoomed')
        # self.controller.iconphoto(False,
        #                           tk.PhotoImage(file='toys.png'))
        label1 = tk.Label(self,
                          text='Main Menu',
                          font=controller.title_font)
        label1.pack()

        def product():
            controller.show_frame('ProductMenu')  # take user to product page

        all_product_btn = tk.Button(self,
                                    text='All Products',
                                    font='Helvetica',
                                    bg='white',
                                    fg='blue',
                                    command=product)
        all_product_btn.pack(padx=10, pady=20, ipadx=137)
        search_lbl = tk.Label(self,
                              text='Search Product',
                              font='Helvetica',
                              fg='blue')
        search_lbl.pack(ipady=7)
        search_variable = tk.StringVar()
        search_entry = tk.Entry(self,
                                textvariable=search_variable,
                                width=22)
        search_entry.pack(padx=10, pady=10, ipadx=137, ipady=7)  # here take search variable from user

        def search():  # this function find the item info searched by the user
            import sqlite3
            conn = sqlite3.connect('db.db')
            c = conn.cursor()
            name = search_entry.get()
            row = c.execute("SELECT ID, Name, Stock, Price, Category FROM Toys WHERE Name =?", (name,), ).fetchall()
            if not row:
                try:
                    row1 = c.execute("SELECT ID, Name, Stock, Price, Category FROM Toys WHERE Category =?",
                                     (name,), ).fetchall()
                    search_product_label = tk.Label(self, text=row1)
                    search_product_label.pack()
                except:
                    search_product_label = tk.Label(self, text=row)
                    search_product_label.pack()
            else:
                search_product_label = tk.Label(self, text=row)
                search_product_label.pack()
            conn.commit()
            c.close()
            conn.close()
            search_entry.delete(0, tk.END)

        search_btn = tk.Button(self,
                               text='Search',
                               font='Helvetica',
                               bg='white',
                               fg='blue',
                               command=search)
        search_btn.pack(padx=10, pady=20, ipadx=137)

        def review():
            controller.show_frame('ReviewPage')  # take user to review page

        review_btn = tk.Button(self,
                               text='Reviews',
                               font='Helvetica',
                               bg='white',
                               fg='blue',
                               command=review)
        review_btn.pack(padx=10, pady=20, ipadx=137)

        administration_btn = tk.Button(self,
                               text='Administration',
                               font='Helvetica',
                               bg='white',
                               fg='blue',
                               command=lambda: saad_main())
        administration_btn.pack(padx=10, pady=20, ipadx=137)

        staff_btn = tk.Button(self,
                               text='Staff',
                               font='Helvetica',
                               bg='white',
                               fg='blue',
                               command=lambda: rutik())
        staff_btn.pack(padx=10, pady=20, ipadx=137)


class ProductMenu(tk.Frame):
    """This the the first sub feature of system feature two and it shows user all the available toys in the system
    and the user will be able to add an item from here to their basket and also go see reviews"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#ffffff')
        self.controller = controller
        self.controller.state('zoomed')
        # self.controller.iconphoto(False,
        #                           tk.PhotoImage(file='toys.png'))

        def available_product():
            import sqlite3
            conn = sqlite3.connect('db.db')
            c = conn.cursor()

            # see all existing review from the database
            c.execute("SELECT Id, Name, Stock, Price, Category, Image  FROM Toys")
            products = c.fetchall()

            def buy():
                messagebox.showinfo('Info', 'Item added to basket')

            def review():
                controller.show_frame('ReviewPage')

            # Loop Through Results

            nem = 2
            for product in products:
                row_thingy = product[0]
                tid = tk.Label(self, text=str(product[0]))
                tid.grid(row=nem, column=0, padx=10, pady=10)
                tname = tk.Label(self, text=product[1])
                tname.grid(row=nem, column=1, padx=10, pady=10)
                stock = tk.Label(self, text=str(product[2]))
                stock.grid(row=nem, column=2, padx=10, pady=10)
                price = tk.Label(self, text=str(product[3]))
                price.grid(row=nem, column=3, padx=10, pady=10)
                category = tk.Label(self, text=product[4])
                category.grid(row=nem, column=4, padx=10, pady=10)
                purchase_button = tk.Button(self, text='Purchase', command=lambda row_thingy=row_thingy: add_to_basket(row_thingy))
                purchase_button.grid(row=nem, column=6, padx=10, pady=10)
                review_button = tk.Button(self, text='Review', command=review)
                review_button.grid(row=nem, column=7, padx=10, pady=10)
                nem = nem + 1

            conn.commit()
            conn.close()

        def mainpage():
            controller.show_frame('MainMenu')

        all_available_product_btn = tk.Button(self, text="All Available Product",
                                              bg='white',
                                              fg='blue',
                                              command=available_product)
        all_available_product_btn.grid(row=0, column=0, columnspan=2, ipadx=20, ipady=10)
        main_page_btn = tk.Button(self, text="Main Page",
                                  bg='white',
                                  fg='blue',
                                  command=mainpage)
        main_page_btn.grid(row=0, column=3, columnspan=2, ipadx=10, ipady=10)

        toyid_lbl = tk.Label(self, text='Toy Id')
        toyid_lbl.grid(row=1, column=0, ipadx=10, ipady=10)
        toyname_lbl = tk.Label(self, text='Toy Name')
        toyname_lbl.grid(row=1, column=1, ipadx=10, ipady=10)
        stock_lbl = tk.Label(self, text='Stock')
        stock_lbl.grid(row=1, column=2, ipadx=10, ipady=10)
        price_lbl = tk.Label(self, text='Price')
        price_lbl.grid(row=1, column=3, ipadx=10, ipady=10)
        category_lbl = tk.Label(self, text='Category')
        category_lbl.grid(row=1, column=4, ipadx=10, ipady=10)
        image_lbl = tk.Label(self, text='Image')
        image_lbl.grid(row=1, column=5, ipadx=10, ipady=10)
        shopping_basket = tk.Button(self, text="Shopping Basket",
                                    bg='white',
                                    fg='blue', command=lambda: open_basket())
        shopping_basket.grid(row=1, column=5, ipadx=10, ipady=10)

        '''#I tried to show image manually but for some reason it did not show on the GUI
        image1 = tk.PhotoImage(file="barbie1.png") 
        image1.label = tk.Label(self, image=image1).grid(row=2, column=5)
        image2 = tk.PhotoImage(file='buzz.png')
        image2.label = tk.Label(self, image=image2).grid(row=3, column=5)
        image3 = tk.PhotoImage(file='chess.png')
        image3.label = tk.Label(self, image=image3).grid(row=4, column=5)
        image4 = tk.PhotoImage(file='flash.png')
        image4.label = tk.Label(self, image=image4).grid(row=5, column=5)
        image5 = tk.PhotoImage(file='monopoly.png')
        image5.label = tk.Label(self, image=image1).grid(row=6, column=5)
        image6 = tk.PhotoImage(file='ken.png')
        image6.label = tk.Label(self, image=image6).grid(row=7, column=5)
        image7 = tk.PhotoImage(file='shooky.png')
        image7.label = tk.Label(self, image=image7).grid(row=8, column=5)
        image8 = tk.PhotoImage(file='pikachu.png')
        image8.label = tk.Label(self, image=image8).grid(row=9, column=5)
        image9 = tk.PhotoImage(file='spider.png')
        image9.label = tk.Label(self, image=image9).grid(row=10, column=5)
        image10 = tk.PhotoImage(file='superman.png')
        image10.label = tk.Label(self, image=image10).grid(row=11, column=5)
        image11 = tk.PhotoImage(file='uno.png')
        image11.label = tk.Label(self, image=image11).grid(row=12, column=5)
        image12 = tk.PhotoImage(file='spongebob.png')
        image12.label = tk.Label(self, image=image1).grid(row=13, column=5)'''


class ReviewPage(tk.Frame):
    """This is where the review feature is implemented.The customer will be able to post review about toys here and
    it will be stored in the database.They will also be able to review all existing reviews in the database """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.state('zoomed')
        # self.controller.iconphoto(False,
        #                           tk.PhotoImage(file='toys.png'))

        # Creating post review Function For database
        def post_review():
            import sqlite3
            # Create a database or connect to one
            conn = sqlite3.connect('db.db')
            # Create cursor
            c = conn.cursor()

            # Insert Into Table
            c.execute("INSERT INTO reviews (ToyID, ToyName, CustomerName, Review) VALUES (:toy_id, :toy_name, :user_name, :review)",
                      {
                          'toy_id': toy_id.get(),
                          'toy_name': toy_name.get(),
                          'user_name': user_name.get(),
                          'review': review.get(),
                      })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()
            toy_id.delete(0, tk.END)
            toy_name.delete(0, tk.END)
            user_name.delete(0, tk.END)
            review.delete(0, tk.END)

        # Create see all review Function
        def see_all_review():
            import sqlite3
            # Create a database or connect to one
            conn = sqlite3.connect('db.db')
            # Create cursor
            c = conn.cursor()

            # see all existing review from the database
            c.execute("SELECT *, oid FROM reviews")
            reviews = c.fetchall()
            # print(records)

            # Loop Through Results
            nem = 10
            for i in reviews:
                tid = tk.Label(self, text=i[0])
                tid.grid(row=nem, column=0, padx=10, pady=10)
                tname = tk.Label(self, text=i[1])
                tname.grid(row=nem, column=1, padx=10, pady=10)
                uname = tk.Label(self, text=i[2])
                uname.grid(row=nem, column=2, padx=10, pady=10)
                review = tk.Label(self, text=i[3])
                review.grid(row=nem, column=3, padx=10, pady=10)
                response = tk.Label(self, text=i[4])
                response.grid(row=nem, column=4, padx=10, pady=10)


                nem = nem + 1

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

        # Create entry boxes
        toy_id = tk.Entry(self, width=30)
        toy_id.grid(row=0, column=1)
        toy_name = tk.Entry(self, width=30)
        toy_name.grid(row=1, column=1, padx=20, pady=(10, 0))
        user_name = tk.Entry(self, width=30)
        user_name.grid(row=2, column=1)
        review = tk.Entry(self, width=30)
        review.grid(row=3, column=1)

        # Create entry box Labels
        toyid_label = tk.Label(self, text="Toy Id",
                               font='Helvetica',
                               bg='white',
                               fg='blue')
        toyid_label.grid(row=0, column=0)
        toyname_label = tk.Label(self, text="Toy Name",
                                 font='Helvetica',
                                 bg='white',
                                 fg='blue')
        toyname_label.grid(row=1, column=0, pady=(10, 0))
        username_label = tk.Label(self, text="Username",
                                  font='Helvetica',
                                  bg='white',
                                  fg='blue')
        username_label.grid(row=2, column=0)
        review_label = tk.Label(self, text="Review",
                                font='Helvetica',
                                bg='white',
                                fg='blue')
        review_label.grid(row=3, column=0)

        # Create post review Button
        post_review_btn = tk.Button(self, text="Post Review",
                                    font='Helvetica',
                                    bg='white',
                                    fg='blue',
                                    command=post_review)
        post_review_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

        # Create a show all review Button
        show_all_review_btn = tk.Button(self, text="Show All Reviews",
                                        font='Helvetica',
                                        bg='white',
                                        fg='blue',
                                        command=see_all_review)
        show_all_review_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        tid_lbl = tk.Label(self, text='Toy Id', font='Helvetica', bg='white', fg='blue')
        tid_lbl.grid(row=9, column=0, padx=10, pady=10)
        tname_lbl = tk.Label(self, text='Toy Name', font='Helvetica', bg='white', fg='blue')
        tname_lbl.grid(row=9, column=1, padx=10, pady=10)
        uname_lbl = tk.Label(self, text='User Name', font='Helvetica', bg='white', fg='blue')
        uname_lbl.grid(row=9, column=2, padx=10, pady=10)
        r_lbl = tk.Label(self, text='Reviews', font='Helvetica', bg='white', fg='blue')
        r_lbl.grid(row=9, column=3, padx=10, pady=10)
        response_lbl = tk.Label(self, text='Response', font='Helvetica', bg='white', fg='blue')
        response_lbl.grid(row=9, column=4, padx=10, pady=10)


        def mainpage():
            controller.show_frame('MainMenu')

        def productpage():
            controller.show_frame('ProductMenu')

        back_btn = tk.Button(self, text='Main Page',
                             font='Helvetica',
                             bg='white',
                             fg='blue',
                             command=mainpage)
        back_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
        back_product_btn = tk.Button(self, text='Product Page',
                                     font='Helvetica',
                                     bg='white',
                                     fg='blue',
                                     command=productpage)
        back_product_btn.grid(row=8, column=3, columnspan=2, pady=10, padx=10, ipadx=137)


if __name__ == "__main__":
    app = FeatureTwo()
    app.mainloop()
