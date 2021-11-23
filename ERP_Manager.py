from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from datetime import datetime
import SQL_Tools
import re
import pandas as pd

window = Tk()

window.title("NotFashion ERP - Manager")

tab_control = ttk.Notebook(window)
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
tab_control.add(tab1, text='Status Input')
tab_control.add(tab2, text='Status List')
tab_control.add(tab3, text='New Order')
tab_control.add(tab4, text='New Return')
tab_control.add(tab5, text='Returns List')
tab_control.add(tab6, text='Inventory Input')
tab_control.add(tab7, text='Inventory List')
tab_control.add(tab8, text='Products')
tab_control.add(tab9, text='Search ID')
tab_control.pack(expand=1, fill='both')

distribution_center_1_lbl = Label(tab1, text="Distribution Center :")
distribution_center_1_lbl.grid(column=5, row=1)
distribution_center_1_txt = ttk.Combobox(tab1)
distribution_center_1_txt.grid(column=6, row=1)

user_1_lbl = Label(tab1, text="User :")
user_1_lbl.grid(column=5, row=2)
user_1_txt = ttk.Combobox(tab1)
user_1_txt.grid(column=6, row=2)

status_1_lbl = Label(tab1, text="Status input :")
status_1_lbl.grid(column=5, row=3)
status_1_combo = ttk.Combobox(tab1)
status_1_combo['values'] = ("Prepared", "Sent", "Received")
status_1_combo.current(0)
status_1_combo.grid(column=6, row=3)

box1_1_lbl = Label(tab1, text="N° Box 1 : ")
box1_1_lbl.grid(column=5, row=4)
box1_1_stock = Label(tab1, text=" ")
box1_1_stock.grid(column=7, row=4)
var_b1 = tk.DoubleVar(value=0)
box1_1_txt = ttk.Spinbox(tab1, from_=0, to=5, width=20, textvariable=var_b1)
box1_1_txt.grid(column=6, row=4)

box2_1_lbl = Label(tab1, text="N° Box 2 : ")
box2_1_lbl.grid(column=5, row=5)
box2_1_stock = Label(tab1, text=" ")
box2_1_stock.grid(column=7, row=5)
var_b2 = tk.DoubleVar(value=0)
box2_1_txt = ttk.Spinbox(tab1, from_=0, to=5, width=20, textvariable=var_b2)
box2_1_txt.grid(column=6, row=5)

order_id_1_lbl = Label(tab1, text="Order ID : ")
order_id_1_lbl.grid(column=5, row=6)
order_id_1_txt = Entry(tab1, width=20)
order_id_1_txt.grid(column=6, row=6)

return_id_1_lbl = Label(tab1, text="Return ID :")
return_id_1_lbl.grid(column=5, row=7)
return_id_1_txt = Entry(tab1, width=20)
return_id_1_txt.grid(column=6, row=7)

datetime_1_lbl = Label(tab1, text="Time Tag :")
datetime_1_lbl.grid(column=5, row=8)
datetime_1_txt = Entry(tab1, width=20)
datetime_1_txt.grid(column=6, row=8)

supplies_1_lbl = Label(tab1, text="Supplies")
supplies_1_lbl.grid(column=5, row=10)
labels_1_lbl = Label(tab1, text="Printing labels :")
labels_1_lbl.grid(column=5, row=11)
labels_1_stock = Label(tab1, text="")
labels_1_stock.grid(column=7, row=11)
labels_1_txt = ttk.Spinbox(tab1, from_=0, to=1, width=20)
labels_1_txt.grid(column=6, row=11)

papers_1_lbl = Label(tab1, text="Printing paper :")
papers_1_lbl.grid(column=5, row=12)
papers_1_stock = Label(tab1, text="")
papers_1_stock.grid(column=7, row=12)
papers_1_txt = ttk.Spinbox(tab1, from_=0, to=1, width=20)
papers_1_txt.grid(column=6, row=12)

glue_1_lbl = Label(tab1, text="Glue :")
glue_1_lbl.grid(column=5, row=13)
glue_1_stock = Label(tab1, text="")
glue_1_stock.grid(column=7, row=13)
glue_1_txt = ttk.Spinbox(tab1, from_=0, to=1, width=20)
glue_1_txt.grid(column=6, row=13)


def add_status():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    status = status_1_combo.get()
    box1_qty = box1_1_txt.get()
    box2_qty = box2_1_txt.get()
    order_id = order_id_1_txt.get()
    return_id = return_id_1_txt.get()
    datetime_1 = datetime_1_txt.get()
    box1_1_txt.delete(0, "end")
    box2_1_txt.delete(0, "end")
    order_id_1_txt.delete(0, "end")
    return_id_1_txt.delete(0, "end")
    datetime_1_txt.delete(0, "end")

    if 'Prepared' in status and int(box1_qty) > 0:
        box1 = 'Caja Chica'
        box1 = f'"{box1}"'
        box1_stock = SQL_Tools.get_supply_stock(connection, box1)
        box1_stock = box1_stock[0]
        update_box1_stock = int(box1_stock) - int(box1_qty)
        update_box1_stock = f'"{update_box1_stock}"'
        SQL_Tools.update_supply_stock(connection, box1, update_box1_stock)
        box1_1_stock.config(text=f"Box 1 Stock :{update_box1_stock}")

    if 'Prepared' in status and int(box2_qty) > 0:
        box2 = 'Caja Grande'
        box2 = f'"{box2}"'
        box2_stock = SQL_Tools.get_supply_stock(connection, box2)
        box2_stock = box2_stock[0]
        update_box2_stock = int(box2_stock) - int(box2_qty)
        update_box2_stock = f'"{update_box2_stock}"'
        SQL_Tools.update_supply_stock(connection, box2, update_box2_stock)
        box2_1_stock.config(text=f"Box 2 Stock :{update_box2_stock}")

    if int(order_id) > 0:
        SQL_Tools.add_order_status(connection, order_id, datetime_1, status, box1_qty, box2_qty)

    else:
        if 'Received' in status:
            SQL_Tools.add_return_status(connection, return_id, datetime, status, box1_qty, box2_qty)
            product_in_id = SQL_Tools.get_id(connection, 'return_products', 'product_in_id', 'return_id', return_id)
            product_in_id = product_in_id[0]
            product_in_id = f'"{product_in_id}"'
            product_in_qty = SQL_Tools.get_id(connection, 'return_products', 'product_in_qty', 'return_id', return_id)
            product_in_qty = product_in_qty[0]
            product_in_sku = SQL_Tools.get_id(connection, 'products', 'sku', 'id', product_in_id)
            product_in_sku = product_in_sku[0]
            product_in_sku = f'"{product_in_sku}"'
            product_stock = SQL_Tools.get_product_stock(connection, product_in_sku)
            product_stock = product_stock[0]
            update_stock = int(product_stock) + int(product_in_qty)
            update_stock = f'"{update_stock}"'
            SQL_Tools.update_product_stock(connection, product_in_sku, update_stock)
            print("Return completed successfully")
        else:
            SQL_Tools.add_return_status(connection, return_id, datetime, status, box1_qty, box2_qty)

    connection.close()
    print("MySQL connection closed successfully")


def update_supplies():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    labels_1 = labels_1_txt.get()
    papers_1 = papers_1_txt.get()
    glue_1 = glue_1_txt.get()

    if labels_1_txt.index("end") != 0:
        labels = 'Brother Labels'
        labels = f'"{labels}"'
        labels_stock = SQL_Tools.get_supply_stock(connection, labels)
        labels_stock = labels_stock[0]
        update_labels_stock = int(labels_stock) - int(labels_1)
        update_labels_stock = f'"{update_labels_stock}"'
        SQL_Tools.update_supply_stock(connection, labels, str(update_labels_stock))
        labels_1_stock.config(text=f"Brother Labels Stock : :{update_labels_stock}")

    if papers_1_txt.index("end") != 0:
        papers = 'Ream Paper'
        papers = f'"{papers}"'
        papers_stock = SQL_Tools.get_supply_stock(connection, papers)
        papers_stock = papers_stock[0]
        update_papers_stock = int(papers_stock) - int(papers_1)
        update_papers_stock = f'"{update_papers_stock}"'
        SQL_Tools.update_supply_stock(connection, papers, update_papers_stock)
        papers_1_stock.config(text=f"Ream Papers Stock : :{update_papers_stock}")

    if glue_1_txt.index("end") != 0:
        glue = 'Glue'
        glue = f'"{glue}"'
        glue_stock = SQL_Tools.get_supply_stock(connection, glue)
        glue_stock = glue_stock[0]
        update_glue_stock = int(glue_stock) - int(glue_1)
        update_glue_stock = f'"{update_glue_stock}"'
        SQL_Tools.update_supply_stock(connection, glue, update_glue_stock)
        glue_1_stock.config(text=f"Glue Stock : :{update_glue_stock}")

    labels_1_txt.delete(0, "end")
    papers_1_txt.delete(0, "end")
    glue_1_txt.delete(0, "end")
    connection.close()
    print("MySQL connection closed successfully")


def time_1():
    time_now = datetime.now(tz=None)
    datetime_1_txt.insert(0, time_now)


def update_users():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    distribution_center = []
    cursor.execute('SELECT name FROM distribution_center LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        distribution_center.append(row1[0])
    distribution_center_1_txt['values'] = distribution_center
    distribution_center_1_txt.current(1)
    erp_users = []
    cursor.execute('SELECT name FROM user LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        erp_users.append(row1[0])
    user_1_txt['values'] = erp_users
    user_1_txt.current(0)


def start_time():
    time_start = datetime.now(tz=None)
    print(time_start)


def stop_time():
    time_stop = datetime.now(tz=None)
    print(time_stop)


StatusTime = Button(tab1, text="Get TimeTag", command=time_1)
StatusTime.grid(column=7, row=8)

UpdateUsers = Button(tab1, text="Update ", command=update_users)
UpdateUsers.grid(column=7, row=1)

StartTime = Button(tab1, text="Start", command=start_time)
StartTime.grid(column=7, row=2)

StopTime = Button(tab1, text="Stop", command=stop_time)
StopTime.grid(column=8, row=2)
AddStatus = Button(tab1, text="Add Input", command=add_status)
AddStatus.grid(column=6, row=9)

UpdateSupplies = Button(tab1, text="Update Supplies", command=update_supplies)
UpdateSupplies.grid(column=6, row=14)


def status_update():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    tv.delete(*tv.get_children())
    cursor.execute('SELECT * FROM status ORDER BY id DESC LOCK IN SHARE MODE')
    for number, row in enumerate(cursor.fetchall()):
        tv.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    connection.close()
    print("MySQL connection closed")


label = tk.Label(tab2, text="Status", font=("Arial", 12)).grid(row=0, columnspan=1)
cols = ('status_id', 'order_id', 'return_id', 'datetime', 'status', 'box1', 'box2')
tv = ttk.Treeview(tab2, columns=cols, show='headings')
for col in cols:
    tv.heading(col, text=col)
tv.grid(row=1, column=0, columnspan=2)

UpdateStatus = tk.Button(tab2, text="Update", width=15, command=status_update).grid(row=4, column=0)

shipping_name_3_lbl = Label(tab3, text="Shipping Name :")
shipping_name_3_lbl.grid(column=5, row=3)
shipping_name_3_txt = Entry(tab3, width=50)
shipping_name_3_txt.grid(column=6, row=3)

shipping_address_3_lbl = Label(tab3, text="Shipping Address :")
shipping_address_3_lbl.grid(column=5, row=4)
shipping_address_3_txt = Entry(tab3, width=50)
shipping_address_3_txt.grid(column=6, row=4)

shipping_mail_3_lbl = Label(tab3, text="Shipping Mail :")
shipping_mail_3_lbl.grid(column=5, row=5)
shipping_mail_3_txt = Entry(tab3, width=50)
shipping_mail_3_txt.grid(column=6, row=5)

shipping_phone_3_lbl = Label(tab3, text="Shipping Phone :")
shipping_phone_3_lbl.grid(column=5, row=6)
shipping_phone_3_txt = Entry(tab3, width=50)
shipping_phone_3_txt.grid(column=6, row=6)

product_3_lbl = Label(tab3, text="Products ( Enter SKU separated by a space): ")
product_3_lbl.grid(column=5, row=7)
product_3_txt = Entry(tab3, width=100)
product_3_txt.grid(column=6, row=7)

product_qty_3_lbl = Label(tab3, text="Products Quantity ( Separated by a space) : ")
product_qty_3_lbl.grid(column=5, row=8)
product_qty_3_txt = Entry(tab3, width=100)
product_qty_3_txt.grid(column=6, row=8)


product_price_3_lbl = Label(tab3, text="Products Price ( Separated by a space) : ")
product_price_3_lbl.grid(column=5, row=9)
product_price_3_txt = Entry(tab3, width=100)
product_price_3_txt.grid(column=6, row=9)

order_value_3_lbl = Label(tab3, text="Order Value : ")
order_value_3_lbl.grid(column=5, row=10)
order_value_3_txt = Entry(tab3, width=20)
order_value_3_txt.grid(column=6, row=10)

store_id_3_lbl = Label(tab3, text="Store ID : ")
store_id_3_lbl.grid(column=5, row=11)
store_id_3_txt = Entry(tab3, width=20)
store_id_3_txt.grid(column=6, row=11)

store_tag_3_lbl = Label(tab3, text="Store Tag : ")
store_tag_3_lbl.grid(column=5, row=12)
store_tag_3_txt = Entry(tab3, width=20)
store_tag_3_txt.grid(column=6, row=12)

order_tag_3_lbl = Label(tab3, text="Order Tag : ")
order_tag_3_lbl.grid(column=5, row=12)
order_tag_3_txt = Entry(tab3, width=20)
order_tag_3_txt.grid(column=6, row=12)

opl_id_3_lbl = Label(tab3, text="OPL ID : ")
opl_id_3_lbl.grid(column=5, row=13)
opl_id_3_txt = Entry(tab3, width=20)
opl_id_3_txt.grid(column=6, row=13)

datetime_3_lbl = Label(tab3, text="Time Tag : ")
datetime_3_lbl.grid(column=5, row=14)
datetime_3_txt = Entry(tab3, width=20)
datetime_3_txt.grid(column=6, row=14)


def new_order():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()

    shipping_name_3 = shipping_name_3_txt.get()
    shipping_address_3 = shipping_address_3_txt.get()
    shipping_mail_3 = shipping_mail_3_txt.get()
    shipping_phone_3 = shipping_phone_3_txt.get()
    product_3 = product_3_txt.get()
    product_qty_3 = product_qty_3_txt.get()
    product_price_3 = product_price_3_txt.get()
    order_value_3 = order_value_3_txt.get()
    store_id_3 = store_id_3_txt.get()
    opl_id_3 = opl_id_3_txt.get()
    store_tag_3 = store_tag_3_txt.get()
    order_tag_3 = order_tag_3_txt.get()
    datetime_3 = datetime_3_txt.get()
    shipping_name_3_txt.delete(0, "end")
    shipping_address_3_txt.delete(0, "end")
    shipping_mail_3_txt.delete(0, "end")
    shipping_phone_3_txt.delete(0, "end")
    product_3_txt.delete(0, "end")
    product_qty_3_txt.delete(0, "end")
    product_price_3_txt.delete(0, "end")
    order_value_3_txt.delete(0, "end")
    store_id_3_txt.delete(0, "end")
    opl_id_3_txt.delete(0, "end")
    store_tag_3_txt.delete(0, "end")
    order_tag_3.delete(0, "end")
    datetime_3_txt.delete(0, "end")

    shipping_mail_3_s = f'"{shipping_mail_3}"'

    client_id = SQL_Tools.get_id(connection, 'clients', 'id', 'mail', shipping_mail_3_s)
    try:
        if client_id[0] >= 0:
            print(f"Client ID'{client_id[0]}' found in database")
            client_id = client_id[0]
    except TypeError:
        client_id = SQL_Tools.create_client_id(connection, shipping_name_3, shipping_mail_3, shipping_phone_3)
    finally:
        order_id = SQL_Tools.add_order(connection, store_id_3, store_tag_3, shipping_address_3, opl_id_3, order_value_3,
                                       datetime_3, order_tag_3)
        SQL_Tools.add_order_client(connection, order_id, client_id)
        product = product_3.strip().split()
        product_qty = product_qty_3.strip().split()
        product_price = product_price_3.strip().split()
        for x, y, z in zip(product, product_qty, product_price):
            print(x, y)
            x_s = f'"{x}"'
            product_id = SQL_Tools.get_id(connection, 'products', 'id', 'sku', x_s)
            product_stock = SQL_Tools.get_product_stock(connection, x_s)
            product_stock = product_stock[0]
            update_stock = int(product_stock) - int(y)
            update_stock = f'"{update_stock}"'
            SQL_Tools.add_order_products(connection, order_id, product_id[0], y, z)
            SQL_Tools.update_product_stock(connection, x_s, update_stock)

        status_q = "Queue"
        status_null = 0
        SQL_Tools.add_order_status(connection, order_id, datetime_3, status_q, status_null, status_null)
        print("Order imported successfully")
        cursor.close()
        connection.close()
        print("MySQL connection closed successfully")


def time_3():
    time_now = datetime.now(tz=None)
    datetime_3_txt.insert(0, time_now)


OrderTime = Button(tab3, text="Get TimeTag", command=time_3)
OrderTime.grid(column=7, row=14)

NewOrder = Button(tab3, text="Add Order", command=new_order)
NewOrder.grid(column=6, row=15)

order_id_4_lbl = Label(tab4, text="Order ID :")
order_id_4_lbl.grid(column=5, row=3)
order_id_4_txt = Entry(tab4, width=20)
order_id_4_txt.grid(column=6, row=3)

opl_id_4_lbl = Label(tab4, text="OPL ID :")
opl_id_4_lbl.grid(column=5, row=4)
opl_id_4_txt = Entry(tab4, width=20)
opl_id_4_txt.grid(column=6, row=4)

product_out_4_lbl = Label(tab4, text="Product Out  ( SKU Separated by a space) :")
product_out_4_lbl.grid(column=5, row=5)
product_out_4_txt = Entry(tab4, width=20)
product_out_4_txt.grid(column=6, row=5)

product_out_qty_4_lbl = Label(tab4, text="Product Out Quantity  ( Separated by a space)  :")
product_out_qty_4_lbl.grid(column=5, row=6)
product_out_qty_4_txt = Entry(tab4, width=20)
product_out_qty_4_txt.grid(column=6, row=6)

product_in_4_lbl = Label(tab4, text="Product In  ( SKU Separated by a space) : ")
product_in_4_lbl.grid(column=5, row=7)
product_in_4_txt = Entry(tab4, width=20)
product_in_4_txt.grid(column=6, row=7)

product_in_qty_4_lbl = Label(tab4, text="Product Quantity ( Separated by a space) : ")
product_in_qty_4_lbl.grid(column=5, row=8)
product_in_qty_4_txt = Entry(tab4, width=20)
product_in_qty_4_txt.grid(column=6, row=8)

datetime_4_lbl = Label(tab4, text="Time Tag : ")
datetime_4_lbl.grid(column=5, row=9)
datetime_4_txt = Entry(tab4, width=20)
datetime_4_txt.grid(column=6, row=9)


def add_return():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()

    order_id = order_id_4_txt.get()
    opl_id = opl_id_4_txt.get()
    product_out = product_out_4_txt.get()
    product_out_qty = product_out_qty_4_txt.get()
    product_in = product_in_4_txt.get()
    product_in_qty = product_in_qty_4_txt.get()
    datetime_4 = datetime_4_txt.get()
    order_id_4_txt.delete(0, "end")
    opl_id_4_txt.delete(0, "end")
    product_out_4_txt.delete(0, "end")
    product_out_qty_4_txt.delete(0, "end")
    product_in_4_txt.delete(0, "end")
    product_in_qty_4_txt.delete(0, "end")
    datetime_4_txt.delete(0, "end")
    status_q = "Queue"
    status_null = 0
    product_in = product_in.strip().split()
    product_in_qty = product_in_qty.strip().split()
    product_out = product_out.strip().split()
    product_out_qty = product_out_qty.strip().split()
    return_id = SQL_Tools.add_return(connection, order_id, opl_id)
    SQL_Tools.add_return_status(connection, return_id, datetime_4, status_q, status_null, status_null)
    for w, x, y, z in zip(product_in, product_in_qty, product_out, product_out_qty):
        w = f'"{w}"'
        y = f'"{y}"'
        print(w, x)
        print(y, z)
        product_in_id = SQL_Tools.get_id(connection, 'products', 'id', 'sku', w)
        product_out_id = SQL_Tools.get_id(connection, 'products', 'id', 'sku', y)
        SQL_Tools.add_return_products(connection, return_id, product_in_id[0], x,
                                      product_out_id[0], z)
        product_in_qty = product_in_qty[0]
        product_stock = SQL_Tools.get_product_stock(connection, y)
        product_stock = product_stock[0]
        update_stock = int(product_stock) - int(z)
        update_stock = f'"{update_stock}"'
        SQL_Tools.update_product_stock(connection, y, update_stock)

    print("Return imported successfully")
    cursor.close()
    connection.close()
    print("MySQL connection closed successfully")


def time_4():
    time_now = datetime.now(tz=None)
    datetime_4_txt.insert(0, time_now)


ReturnTime = Button(tab4, text="Get TimeTag", command=time_4)
ReturnTime.grid(column=7, row=9)


AddReturn = Button(tab4, text="Add Return", command=add_return)
AddReturn.grid(column=6, row=10)


def returns_update():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    tv2.delete(*tv2.get_children())
    cursor.execute('SELECT * FROM return_products ORDER BY return_id DESC LOCK IN SHARE MODE')
    for number, row in enumerate(cursor.fetchall()):
        tv2.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
    connection.close()
    print("MySQL connection closed")


cols = ('return_id', 'product_in_id', 'product_in_qty', 'product_out_id', 'product_out_qty')
tv2 = ttk.Treeview(tab5, columns=cols, show='headings')
for col in cols:
    tv2.heading(col, text=col)
tv2.grid(row=1, column=0, columnspan=2)

ReturnsUpdate = Button(tab5, text="Update Returns", command=returns_update)
ReturnsUpdate.grid(column=5, row=14)

supplier_6_lbl = Label(tab6, text="Supplier :")
supplier_6_lbl.grid(column=5, row=3)
supplier_6_txt = ttk.Combobox(tab6)
supplier_6_txt.grid(column=6, row=3)

model_6_lbl = Label(tab6, text="Model :")
model_6_lbl.grid(column=5, row=4)
model_6_txt = Entry(tab6, width=20)
model_6_txt.grid(column=6, row=4)

composition_6_lbl = Label(tab6, text="Composition :")
composition_6_lbl.grid(column=5, row=5)
composition_6_txt = Entry(tab6, width=20)
composition_6_txt.grid(column=6, row=5)


size_xs_desc_6_lbl = Label(tab6, text="XS Description : ")
size_xs_desc_6_lbl.grid(column=5, row=6)
size_xs_desc_6_txt = Entry(tab6, width=20)
size_xs_desc_6_txt.grid(column=6, row=6)

size_s_desc_6_lbl = Label(tab6, text="S Description : ")
size_s_desc_6_lbl.grid(column=5, row=7)
size_s_desc_6_txt = Entry(tab6, width=20)
size_s_desc_6_txt.grid(column=6, row=7)

size_m_desc_6_lbl = Label(tab6, text="M Description : ")
size_m_desc_6_lbl.grid(column=5, row=8)
size_m_desc_6_txt = Entry(tab6, width=20)
size_m_desc_6_txt.grid(column=6, row=8)

size_l_desc_6_lbl = Label(tab6, text="L Description : ")
size_l_desc_6_lbl.grid(column=5, row=9)
size_l_desc_6_txt = Entry(tab6, width=20)
size_l_desc_6_txt.grid(column=6, row=9)

size_xl_desc_6_lbl = Label(tab6, text="XL Description : ")
size_xl_desc_6_lbl.grid(column=5, row=10)
size_xl_desc_6_txt = Entry(tab6, width=20)
size_xl_desc_6_txt.grid(column=6, row=10)

size_2x_desc_6_lbl = Label(tab6, text="2X Description : ")
size_2x_desc_6_lbl.grid(column=5, row=11)
size_2x_desc_6_txt = Entry(tab6, width=20)
size_2x_desc_6_txt.grid(column=6, row=11)

size_unique_desc_6_lbl = Label(tab6, text="Unique Description : ")
size_unique_desc_6_lbl.grid(column=5, row=12)
size_unique_desc_6_txt = Entry(tab6, width=20)
size_unique_desc_6_txt.grid(column=6, row=12)


colour_6_lbl = Label(tab6, text="Colour: ")
colour_6_lbl.grid(column=8, row=4)
colour_6_txt = Entry(tab6, width=20)
colour_6_txt.grid(column=9, row=4)

colour_desc_6_lbl = Label(tab6, text="Colour Description : ")
colour_desc_6_lbl.grid(column=8, row=5)
colour_desc_6_txt = Entry(tab6, width=20)
colour_desc_6_txt.grid(column=9, row=5)

distribution_center_6_lbl = Label(tab6, text="Distribution Center :")
distribution_center_6_lbl.grid(column=11, row=3)
distribution_center_6_txt = ttk.Combobox(tab6)
distribution_center_6_txt.grid(column=12, row=3)

supplier_b_6_lbl = Label(tab6, text="Supplier :")
supplier_b_6_lbl.grid(column=11, row=4)
supplier_b_6_txt = ttk.Combobox(tab6)
supplier_b_6_txt.grid(column=12, row=4)

model_b_6_lbl = Label(tab6, text="Model :")
model_b_6_lbl.grid(column=11, row=5)
model_b_6_txt = ttk.Combobox(tab6)
model_b_6_txt.grid(column=12, row=5)

colour_b_6_lbl = Label(tab6, text="Colour: ")
colour_b_6_lbl.grid(column=11, row=6)
colour_b_6_txt = ttk.Combobox(tab6)
colour_b_6_txt.grid(column=12, row=6)


size_xs_6_lbl = Label(tab6, text="XS : ")
size_xs_6_lbl.grid(column=11, row=7)
size_xs_6_txt = Entry(tab6, width=20)
size_xs_6_txt.grid(column=12, row=7)

size_s_6_lbl = Label(tab6, text="S : ")
size_s_6_lbl.grid(column=11, row=8)
size_s_6_txt = Entry(tab6, width=20)
size_s_6_txt.grid(column=12, row=8)

size_m_6_lbl = Label(tab6, text="M :")
size_m_6_lbl.grid(column=11, row=9)
size_m_6_txt = Entry(tab6, width=20)
size_m_6_txt.grid(column=12, row=9)

size_l_6_lbl = Label(tab6, text="L :")
size_l_6_lbl.grid(column=11, row=10)
size_l_6_txt = Entry(tab6, width=20)
size_l_6_txt.grid(column=12, row=10)

size_xl_6_lbl = Label(tab6, text="XL :")
size_xl_6_lbl.grid(column=11, row=11)
size_xl_6_txt = Entry(tab6, width=20)
size_xl_6_txt.grid(column=12, row=11)

size_2x_6_lbl = Label(tab6, text="2X :")
size_2x_6_lbl.grid(column=11, row=12)
size_2x_6_txt = Entry(tab6, width=20)
size_2x_6_txt.grid(column=12, row=12)

size_unique_6_lbl = Label(tab6, text="Unique :")
size_unique_6_lbl.grid(column=11, row=13)
size_unique_6_txt = Entry(tab6, width=20)
size_unique_6_txt.grid(column=12, row=13)

distribution_center_c_6_lbl = Label(tab6, text="Distribution Center :")
distribution_center_c_6_lbl.grid(column=14, row=3)
distribution_center_c_6_txt = ttk.Combobox(tab6)
distribution_center_c_6_txt.grid(column=15, row=3)

model_c_6_lbl = Label(tab6, text="Model :")
model_c_6_lbl.grid(column=14, row=4)
model_c_6_txt = ttk.Combobox(tab6)
model_c_6_txt.grid(column=15, row=4)

colour_c_6_lbl = Label(tab6, text="Colour: ")
colour_c_6_lbl.grid(column=14, row=5)
colour_c_6_txt = ttk.Combobox(tab6)
colour_c_6_txt.grid(column=15, row=5)

size_xs_c_6_lbl = Label(tab6, text="XS : ")
size_xs_c_6_lbl.grid(column=14, row=6)
size_xs_c_6_txt = Entry(tab6, width=20)
size_xs_c_6_txt.grid(column=15, row=6)

size_s_c_6_lbl = Label(tab6, text="S : ")
size_s_c_6_lbl.grid(column=14, row=7)
size_s_c_6_txt = Entry(tab6, width=20)
size_s_c_6_txt.grid(column=15, row=7)

size_m_c_6_lbl = Label(tab6, text="M :")
size_m_c_6_lbl.grid(column=14, row=8)
size_m_c_6_txt = Entry(tab6, width=20)
size_m_c_6_txt.grid(column=15, row=8)

size_l_c_6_lbl = Label(tab6, text="L :")
size_l_c_6_lbl.grid(column=14, row=9)
size_l_c_6_txt = Entry(tab6, width=20)
size_l_c_6_txt.grid(column=15, row=9)

size_xl_c_6_lbl = Label(tab6, text="XL :")
size_xl_c_6_lbl.grid(column=14, row=10)
size_xl_c_6_txt = Entry(tab6, width=20)
size_xl_c_6_txt.grid(column=15, row=10)

size_2x_c_6_lbl = Label(tab6, text="2X :")
size_2x_c_6_lbl.grid(column=14, row=11)
size_2x_c_6_txt = Entry(tab6, width=20)
size_2x_c_6_txt.grid(column=15, row=11)


def update_categories():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    distribution_center = []
    cursor.execute('SELECT name FROM distribution_center LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        distribution_center.append(row1[0])
    distribution_center_6_txt['values'] = distribution_center
    distribution_center_6_txt.current(1)
    distribution_center_c_6_txt['values'] = distribution_center
    distribution_center_c_6_txt.current(1)
    supplier = []
    cursor.execute('SELECT supplier FROM suppliers LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        supplier.append(row1[0])
    supplier_6_txt['values'] = supplier
    supplier_6_txt.current(3)
    supplier_b_6_txt['values'] = supplier
    supplier_b_6_txt.current(3)
    model = []
    cursor.execute('SELECT model FROM products_category LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        model.append(row1[0])
    model_b_6_txt['values'] = model
    model_c_6_txt['values'] = model
    colour = []
    cursor.execute('SELECT colour FROM products_colour LOCK IN SHARE MODE')
    for i, row1 in enumerate(cursor.fetchall()):
        colour.append(row1[0])
    colour_b_6_txt['values'] = colour
    colour_c_6_txt['values'] = colour


def add_category():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    supplier = supplier_6_txt.get()
    model = model_6_txt.get()
    composition = composition_6_txt.get()
    size_xs_desc = size_xs_desc_6_txt.get()
    size_s_desc = size_s_desc_6_txt.get()
    size_m_desc = size_m_desc_6_txt.get()
    size_l_desc = size_l_desc_6_txt.get()
    size_xl_desc = size_xl_desc_6_txt.get()
    size_2x_desc = size_2x_desc_6_txt.get()
    size_unique_desc = size_unique_desc_6_txt.get()

    supplier_id = SQL_Tools.get_id(connection, 'suppliers', 'id', 'supplier', f"'{supplier}'")
    print(supplier_id, supplier, f"'{str(supplier_id[0])}'", supplier_id[0])
    connection.close()
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', f"'{model}'")
    print(category_id)
    print(model, f"'{model}'")
    connection.close()
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    if size_xs_desc_6_txt.index("end") != 0 and size_s_desc_6_txt.index("end") != 0 and \
            size_l_desc_6_txt.index("end") != 0 and size_xl_desc_6_txt.index("end") != 0 and \
            size_2x_desc_6_txt.index("end") != 0:

        try:
            if category_id[0] >= 0:
                print(f"Category ID'{category_id[0]}' found in database")
                category_id = category_id[0]
        except TypeError:
            print(supplier_id[0])
            category_id = SQL_Tools.add_product_category(connection, supplier_id[0], model, f"'{composition}'")
            print(f"Category ID'{category_id}' created")
        finally:
            category_id_s = f'"{category_id}"'

            xs_s = 'XS'
            xs_s = f'"{xs_s}"'
            size_xs_id = SQL_Tools.get_product_size_id(connection, category_id_s, xs_s)
            connection.close()
            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
            try:
                if size_xs_id[0] >= 0:
                    print(f"Size ID'{size_xs_id[0]}' found in database")
            except TypeError:
                size_xs_id = SQL_Tools.add_product_size(connection, category_id, 'XS', size_xs_desc)
                print(f"Size ID'{size_xs_id}' created")
            finally:

                s_s = 'S'
                s_s = f'"{s_s}"'
                size_s_id = SQL_Tools.get_product_size_id(connection, category_id_s, s_s)
                connection.close()
                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
                try:
                    if size_s_id[0] >= 0:
                        print(f"Size ID'{size_s_id[0]}' found in database")
                except TypeError:
                    size_s_id = SQL_Tools.add_product_size(connection, category_id, 'S', size_s_desc)
                    print(f"Size ID'{size_s_id}' created")
                finally:

                    m_s = 'M'
                    m_s = f'"{m_s}"'
                    size_m_id = SQL_Tools.get_product_size_id(connection, category_id_s, m_s)
                    connection.close()
                    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

                    try:
                        if size_m_id[0] >= 0:
                            print(f"Size ID'{size_m_id[0]}' found in database")
                    except TypeError:
                        size_m_id = SQL_Tools.add_product_size(connection, category_id, 'M', size_m_desc)
                        print(f"Size ID'{size_m_id}' created")
                    finally:
                        l_s = 'L'
                        l_s = f'"{l_s}"'
                        size_l_id = SQL_Tools.get_product_size_id(connection, category_id_s, l_s)
                        connection.close()
                        connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                    "ERP_NotFashion")

                        try:
                            if size_l_id[0] >= 0:
                                print(f"Size ID'{size_l_id[0]}' found in database")
                        except TypeError:
                            size_l_id = SQL_Tools.add_product_size(connection, category_id, 'L', size_l_desc)
                            print(f"Size ID'{size_l_id}' created")
                        finally:
                            xl_s = 'XL'
                            xl_s = f'"{xl_s}"'
                            size_xl_id = SQL_Tools.get_product_size_id(connection, category_id_s, xl_s)
                            connection.close()
                            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                        "ERP_NotFashion")

                            try:
                                if size_xl_id[0] >= 0:
                                    print(f"Size ID'{size_xl_id[0]}' found in database")
                            except TypeError:
                                size_xl_id = SQL_Tools.add_product_size(connection, category_id, 'XL', size_xl_desc)
                                print(f"Size ID'{size_xl_id}' created")
                            finally:
                                xxl_s = '2X'
                                xxl_s = f'"{xxl_s}"'
                                size_2x_id = SQL_Tools.get_product_size_id(connection, category_id_s, xxl_s)
                                connection.close()
                                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                            "ERP_NotFashion")

                                try:
                                    if size_2x_id[0] >= 0:
                                        print(f"Size ID'{size_2x_id[0]}' found in database")
                                except TypeError:
                                    size_2x_id = SQL_Tools.add_product_size(connection, category_id, '2X',
                                                                            size_2x_desc)
                                    print(f"Size ID'{size_2x_id}' created")

    else:
        try:
            if category_id[0] >= 0:
                print(f"Category ID'{category_id[0]}' found in database")
                category_id = category_id[0]
        except TypeError:
            category_id = SQL_Tools.add_product_category(connection, supplier_id[0], model, composition)
            print(f"Category ID'{category_id}' created")
        finally:
            category_id_s = f'"{category_id}"'
            unique_s = 'Unique'
            unique_s = f'"{unique_s}"'
            size_unique_id = SQL_Tools.get_product_size_id(connection, category_id_s,
                                                           unique_s)
            connection.close()
            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

            try:
                if size_unique_id[0] >= 0:
                    print(f"Size ID'{size_unique_id[0]}' found in database")
            except TypeError:
                size_unique_id = SQL_Tools.add_product_size(connection, category_id, 'Unique', size_unique_desc)
                print(f"Size ID'{size_unique_id}' created")

    supplier_6_txt.delete(0, "end")
    model_6_txt.delete(0, "end")
    composition_6_txt.delete(0, "end")
    size_xs_6_txt.delete(0, "end")
    size_s_6_txt.delete(0, "end")
    size_m_6_txt.delete(0, "end")
    size_l_6_txt.delete(0, "end")
    size_xl_6_txt.delete(0, "end")
    size_2x_6_txt.delete(0, "end")
    size_unique_6_txt.delete(0, "end")
    size_xs_desc_6_txt.delete(0, "end")
    size_s_desc_6_txt.delete(0, "end")
    size_m_desc_6_txt.delete(0, "end")
    size_l_desc_6_txt.delete(0, "end")
    size_xl_desc_6_txt.delete(0, "end")
    size_2x_desc_6_txt.delete(0, "end")
    size_unique_desc_6_txt.delete(0, "end")
    connection.close()
    print("MySQL session ended successfully")


def add_colour():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    colour = colour_6_txt.get()
    colour_desc = colour_desc_6_txt.get()

    colour_s = f'"{colour}"'
    colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour_s)
    connection.close()
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    try:
        if colour_id[0] >= 0:
            print(f"Colour ID'{colour_id[0]}' found in database")
    except TypeError:
        colour_id = SQL_Tools.add_product_colour(connection, colour, colour_desc)
        print(f"Colour ID'{colour_id}' created")

    colour_6_txt.delete(0, "end")
    colour_desc_6_txt.delete(0, "end")


def add_product():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    model = model_b_6_txt.get()
    colour = colour_b_6_txt.get()
    size_xs = size_xs_6_txt.get()
    size_s = size_s_6_txt.get()
    size_m = size_m_6_txt.get()
    size_l = size_l_6_txt.get()
    size_xl = size_xl_6_txt.get()
    size_2x = size_2x_6_txt.get()
    size_unique = size_unique_6_txt.get()

    sku_xs = model + '-XS-' + colour
    sku_s = model + '-S-' + colour
    sku_m = model + '-M-' + colour
    sku_l = model + '-L-' + colour
    sku_xl = model + '-XL-' + colour
    sku_2x = model + '-2X-' + colour
    sku_unique = model + '-' + colour

    category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', model)
    connection.close()
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

    if size_xs_6_txt.index("end") != 0 and size_s_6_txt.index("end") != 0 and \
            size_l_6_txt.index("end") != 0 and size_xl_6_txt.index("end") != 0 and \
            size_2x_6_txt.index("end") != 0:

        try:
            if category_id[0] >= 0:
                print(f"Category ID'{category_id[0]}' found in database")
                category_id = category_id[0]
        except TypeError:
            print(f"Category ID'{category_id}' created")
        finally:
            category_id_s = f'"{category_id}"'
            colour_s = f'"{colour}"'
            colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour_s)
            connection.close()
            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

            try:
                if colour_id[0] >= 0:
                    print(f"Colour ID'{colour_id[0]}' found in database")
                    colour_id = colour_id[0]
            except TypeError:
                print(f"Colour ID'{colour_id}' created")
            finally:
                xs_s = 'XS'
                xs_s = f'"{xs_s}"'
                size_xs_id = SQL_Tools.get_product_size_id(connection, category_id_s, xs_s)
                connection.close()
                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
                try:
                    if size_xs_id[0] >= 0:
                        print(f"Size ID'{size_xs_id[0]}' found in database")
                        size_xs_id = size_xs_id[0]
                except TypeError:
                    print(f"Size ID'{size_xs_id}' created")
                finally:
                    SQL_Tools.add_product(connection, category_id, sku_xs, size_xs_id, colour_id, size_xs)

                    s_s = 'S'
                    s_s = f'"{s_s}"'
                    size_s_id = SQL_Tools.get_product_size_id(connection, category_id_s, s_s)
                    connection.close()
                    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
                    try:
                        if size_s_id[0] >= 0:
                            print(f"Size ID'{size_s_id[0]}' found in database")
                            size_s_id = size_s_id[0]
                    except TypeError:
                        print(f"Size ID'{size_s_id}' created")
                    finally:
                        SQL_Tools.add_product(connection, category_id, sku_s, size_s_id, colour_id, size_s)

                        m_s = 'M'
                        m_s = f'"{m_s}"'
                        size_m_id = SQL_Tools.get_product_size_id(connection, category_id_s, m_s)
                        connection.close()
                        connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

                        try:
                            if size_m_id[0] >= 0:
                                print(f"Size ID'{size_m_id[0]}' found in database")
                                size_m_id = size_m_id[0]
                        except TypeError:
                            print(f"Size ID'{size_m_id}' created")
                        finally:
                            SQL_Tools.add_product(connection, category_id, sku_m, size_m_id, colour_id, size_m)
                            l_s = 'L'
                            l_s = f'"{l_s}"'
                            size_l_id = SQL_Tools.get_product_size_id(connection, category_id_s, l_s)
                            connection.close()
                            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                        "ERP_NotFashion")

                            try:
                                if size_l_id[0] >= 0:
                                    print(f"Size ID'{size_l_id[0]}' found in database")
                                    size_l_id = size_l_id[0]
                            except TypeError:
                                print(f"Size ID'{size_l_id}' created")
                            finally:
                                SQL_Tools.add_product(connection, category_id, sku_l, size_l_id, colour_id, size_l)
                                xl_s = 'XL'
                                xl_s = f'"{xl_s}"'
                                size_xl_id = SQL_Tools.get_product_size_id(connection, category_id_s, xl_s)
                                connection.close()
                                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                            "ERP_NotFashion")

                                try:
                                    if size_xl_id[0] >= 0:
                                        print(f"Size ID'{size_xl_id[0]}' found in database")
                                        size_xl_id = size_xl_id[0]
                                except TypeError:
                                    print(f"Size ID'{size_xl_id}' created")
                                finally:
                                    SQL_Tools.add_product(connection, category_id, sku_xl, size_xl_id, colour_id,
                                                          size_xl)
                                    xxl_s = '2X'
                                    xxl_s = f'"{xxl_s}"'
                                    size_2x_id = SQL_Tools.get_product_size_id(connection, category_id_s, xxl_s)
                                    connection.close()
                                    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP",
                                                                                "ERP_NotFashion")

                                    try:
                                        if size_2x_id[0] >= 0:
                                            print(f"Size ID'{size_2x_id[0]}' found in database")
                                            size_2x_id = size_2x_id[0]
                                    except TypeError:
                                        print(f"Size ID'{size_2x_id}' created")
                                    finally:

                                        SQL_Tools.add_product(connection, category_id, sku_2x, size_2x_id, colour_id,
                                                              size_2x)

    else:
        try:
            if category_id[0] >= 0:
                print(f"Category ID'{category_id[0]}' found in database")
                category_id = category_id[0]
        except TypeError:
            print(f"Category ID'{category_id}' created")
        finally:
            category_id_s = f'"{category_id}"'
            colour_s = f'"{colour}"'
            colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour_s)
            connection.close()
            connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

            try:
                if colour_id[0] >= 0:
                    print(f"Colour ID'{colour_id[0]}' found in database")
                    colour_id = colour_id[0]
            except TypeError:
                print(f"Colour ID'{colour_id}' created")
            finally:
                unique_s = 'Unique'
                unique_s = f'"{unique_s}"'
                size_unique_id = SQL_Tools.get_product_size_id(connection, category_id_s,
                                                               unique_s)
                connection.close()
                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")

                try:
                    if size_unique_id[0] >= 0:
                        print(f"Size ID'{size_unique_id[0]}' found in database")
                        size_unique_id = size_unique_id[0]
                except TypeError:
                    print(f"Size ID'{size_unique_id}' created")
                finally:

                    SQL_Tools.add_product(connection, category_id, sku_unique, size_unique_id, colour_id, size_unique)

    supplier_6_txt.delete(0, "end")
    model_6_txt.delete(0, "end")
    colour_6_txt.delete(0, "end")
    colour_desc_6_txt.delete(0, "end")
    composition_6_txt.delete(0, "end")
    size_xs_6_txt.delete(0, "end")
    size_s_6_txt.delete(0, "end")
    size_m_6_txt.delete(0, "end")
    size_l_6_txt.delete(0, "end")
    size_xl_6_txt.delete(0, "end")
    size_2x_6_txt.delete(0, "end")
    size_unique_6_txt.delete(0, "end")
    size_xs_desc_6_txt.delete(0, "end")
    size_s_desc_6_txt.delete(0, "end")
    size_m_desc_6_txt.delete(0, "end")
    size_l_desc_6_txt.delete(0, "end")
    size_xl_desc_6_txt.delete(0, "end")
    size_2x_desc_6_txt.delete(0, "end")
    size_unique_desc_6_txt.delete(0, "end")
    connection.close()
    print("MySQL session ended successfully")


def inventory_update():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()

    model = model_c_6_txt.get()
    colour = colour_c_6_txt.get()
    size_xs = size_xs_c_6_txt.get()
    size_s = size_s_c_6_txt.get()
    size_m = size_m_c_6_txt.get()
    size_l = size_l_c_6_txt.get()
    size_xl = size_xl_c_6_txt.get()
    size_2x = size_2x_c_6_txt.get()
    sku_xs = model + '-XS-' + colour
    sku_s = model + '-S-' + colour
    sku_m = model + '-M-' + colour
    sku_l = model + '-L-' + colour
    sku_xl = model + '-XL-' + colour
    sku_2x = model + '-2X-' + colour
    size_xs = f'"{size_xs}"'
    sku_xs = f'"{sku_xs}"'
    size_s = f'"{size_s}"'
    sku_s = f'"{sku_s}"'
    size_m = f'"{size_m}"'
    sku_m = f'"{sku_m}"'
    size_l = f'"{size_l}"'
    sku_l = f'"{sku_l}"'
    size_xl = f'"{size_xl}"'
    sku_xl = f'"{sku_xl}"'
    size_2x = f'"{size_2x}"'
    sku_2x = f'"{sku_2x}"'

    SQL_Tools.update_product_stock(connection, sku_xs, size_xs)
    SQL_Tools.update_product_stock(connection, sku_s, size_s)
    SQL_Tools.update_product_stock(connection, sku_m, size_m)
    SQL_Tools.update_product_stock(connection, sku_l, size_l)
    SQL_Tools.update_product_stock(connection, sku_xl, size_xl)
    SQL_Tools.update_product_stock(connection, sku_2x, size_2x)

    colour_c_6_txt.delete(0, "end")
    model_c_6_txt.delete(0, "end")
    size_xs_c_6_txt.delete(0, "end")
    size_s_c_6_txt.delete(0, "end")
    size_m_c_6_txt.delete(0, "end")
    size_l_c_6_txt.delete(0, "end")
    size_xl_c_6_txt.delete(0, "end")
    size_2x_c_6_txt.delete(0, "end")

    print("Product Updated successfully")
    cursor.close()
    connection.close()
    print("MySQL connection closed successfully")


AddInventory = Button(tab6, text="Update Categories", command=update_categories)
AddInventory.grid(column=6, row=2)

AddInventory = Button(tab6, text="Add Category", command=add_category)
AddInventory.grid(column=6, row=13)

AddInventory = Button(tab6, text="Add Colour", command=add_colour)
AddInventory.grid(column=9, row=6)

AddInventory = Button(tab6, text="Add Product", command=add_product)
AddInventory.grid(column=12, row=14)

UpdateInventory = Button(tab6, text="Update Product stock", command=inventory_update)
UpdateInventory.grid(column=15, row=12)


def inventory_list_update():
    print('ok')


inventory_cols = ('id', 'category_id', 'size_id', 'colour_id', 'sku', 'stock')
tv4 = ttk.Treeview(tab7, columns=inventory_cols, show='headings')
for col in inventory_cols:
    tv4.heading(col, text=col)
tv4.grid(row=5, column=0, columnspan=2)
ProductsUpdate = Button(tab7, text="Update", command=inventory_list_update)
ProductsUpdate.grid(column=1, row=1)

category_8_lbl = Label(tab8, text="Category :")
category_8_lbl.grid(column=1, row=2)
category_8_txt = Entry(tab8, width=20)
category_8_txt.grid(column=2, row=2)

colour_8_lbl = Label(tab8, text="Colour :")
colour_8_lbl.grid(column=1, row=3)
colour_8_txt = Entry(tab8, width=20)
colour_8_txt.grid(column=2, row=3)

size_8_lbl = Label(tab8, text="Size :")
size_8_lbl.grid(column=1, row=4)
size_8_txt = Entry(tab8, width=20)
size_8_txt.grid(column=2, row=4)


def products_update():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    tv3.delete(*tv3.get_children())
    cursor.execute('SELECT * FROM products LOCK IN SHARE MODE')
    for number, row in enumerate(cursor.fetchall()):
        tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    connection.close()
    print("MySQL connection closed")


def products_search():
    category = category_8_txt.get()
    colour = colour_8_txt.get()
    size = size_8_txt.get()

    tv3.delete(*tv3.get_children())
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    cursor = connection.cursor()
    colour = f'"{colour}"'
    size = f'"{size}"'

    if category_8_txt.index("end") > 0 and colour_8_txt.index("end") == 0 and size_8_txt.index("end") == 0:
        category_8_txt.delete(0, "end")
        category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', category)
        category_id = f'"{category_id[0]}"'

        cursor.execute('SELECT * FROM products WHERE category_id=' + category_id + ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") == 0 and colour_8_txt.index("end") > 0 and size_8_txt.index("end") == 0:
        colour_8_txt.delete(0, "end")
        colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour)
        colour_id = f"'{colour_id[0]}'"
        cursor.execute('SELECT * FROM products WHERE colour_id=' + colour_id + ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") == 0 and colour_8_txt.index("end") == 0 and size_8_txt.index("end") > 0:
        size_8_txt.delete(0, "end")
        size_id_lst = []
        cursor.execute('SELECT id FROM products_size WHERE size=' + size + ' LOCK IN SHARE MODE')
        for i, row1 in enumerate(cursor.fetchall()):
            size_id_lst.append(row1[0])
        size_id = ','.join([str(n) for n in size_id_lst])
        cursor.execute('SELECT * FROM products WHERE size_id IN (' + size_id + ') LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") > 0 and colour_8_txt.index("end") > 0 and size_8_txt.index("end") == 0:
        colour_8_txt.delete(0, "end")
        category_8_txt.delete(0, "end")
        category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', category)
        category_id = f'"{category_id[0]}"'
        colour_id_lst = []
        cursor.execute('SELECT id FROM products_colour WHERE colour=' + colour + ' LOCK IN SHARE MODE')
        for i, row1 in enumerate(cursor.fetchall()):
            colour_id_lst.append(row1[0])
        colour_id = ','.join([str(n) for n in colour_id_lst])
        cursor.execute('SELECT * FROM products WHERE colour_id IN (' + colour_id + ') AND category_id=' + category_id +
                       ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") > 0 and colour_8_txt.index("end") == 0 and size_8_txt.index("end") > 0:
        size_8_txt.delete(0, "end")
        category_8_txt.delete(0, "end")
        category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', category)
        category_id = f"'{category_id[0]}'"
        size_id_lst = []
        cursor.execute('SELECT id FROM products_size WHERE size=' + size + ' LOCK IN SHARE MODE')
        for i, row1 in enumerate(cursor.fetchall()):
            size_id_lst.append(row1[0])
        size_id = ','.join([str(n) for n in size_id_lst])
        cursor.execute('SELECT * FROM products WHERE size_id IN (' + size_id + ') AND category_id=' + category_id +
                       ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") == 0 and colour_8_txt.index("end") > 0 and size_8_txt.index("end") > 0:
        colour_8_txt.delete(0, "end")
        size_8_txt.delete(0, "end")
        colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour)
        colour_id = f"'{colour_id[0]}'"
        size_id_lst = []
        cursor.execute('SELECT id FROM products_size WHERE size=' + size + ' LOCK IN SHARE MODE')
        for i, row1 in enumerate(cursor.fetchall()):
            size_id_lst.append(row1[0])
        size_id = ','.join([str(n) for n in size_id_lst])
        cursor.execute('SELECT * FROM products WHERE size_id IN (' + size_id + ') AND colour_id=' + colour_id +
                       ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")

    if category_8_txt.index("end") > 0 and colour_8_txt.index("end") > 0 and size_8_txt.index("end") > 0:
        category_8_txt.delete(0, "end")
        colour_8_txt.delete(0, "end")
        size_8_txt.delete(0, "end")
        colour_id = SQL_Tools.get_id(connection, 'products_colour', 'id', 'colour', colour)
        colour_id = f"'{colour_id[0]}'"
        category_id = SQL_Tools.get_id(connection, 'products_category', 'id', 'model', category)
        category_id = f"'{category_id[0]}'"
        size_id_lst = []
        cursor.execute('SELECT id FROM products_size WHERE size=' + size + ' LOCK IN SHARE MODE')
        for i, row1 in enumerate(cursor.fetchall()):
            size_id_lst.append(row1[0])
        size_id = ','.join([str(n) for n in size_id_lst])
        cursor.execute('SELECT * FROM products WHERE size_id IN (' + size_id + ') AND category_id=' + category_id +
                       'AND colour_id=' + colour_id + ' LOCK IN SHARE MODE')
        for number, row in enumerate(cursor.fetchall()):
            tv3.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        connection.close()
        print("MySQL connection closed")


products_cols = ('id', 'category_id', 'size_id', 'colour_id', 'sku', 'stock')
tv3 = ttk.Treeview(tab8, columns=products_cols, show='headings')
for col in products_cols:
    tv3.heading(col, text=col)
tv3.grid(row=5, column=0, columnspan=2)
ProductsUpdate = Button(tab8, text="Update", command=products_update)
ProductsUpdate.grid(column=1, row=1)
CategorySearch = Button(tab8, text="Search ", command=products_search)
CategorySearch.grid(column=2, row=1)

table_9_lbl = Label(tab9, text="Table :")
table_9_lbl.grid(column=5, row=3)
table_9_txt = Entry(tab9, width=20)
table_9_txt.grid(column=6, row=3)

column1_9_lbl = Label(tab9, text="Column 1 : ")
column1_9_lbl.grid(column=5, row=4)
column1_9_txt = Entry(tab9, width=20)
column1_9_txt.grid(column=6, row=4)

column2_9_lbl = Label(tab9, text="Column 2  : ")
column2_9_lbl.grid(column=5, row=5)
column2_9_txt = Entry(tab9, width=20)
column2_9_txt.grid(column=6, row=5)

search_9_lbl = Label(tab9, text="Search  : ")
search_9_lbl.grid(column=5, row=6)
search_9_txt = Entry(tab9, width=20)
search_9_txt.grid(column=6, row=6)

result_9_lbl = Label(tab9, text="Result  : ")
result_9_lbl.grid(column=6, row=7)


def search_id():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", "ERP_NotFashion")
    table = table_9_txt.get()
    column1 = column1_9_txt.get()
    column2 = column2_9_txt.get()
    search = search_9_txt.get()

    result = SQL_Tools.get_id(connection, table, column1, column2, search)
    try:
        if result[0] >= 0:
            result_9_lbl.config(text=f"ID '{result[0]}' found in  Table '{table}' for '{column2}' = '{search} ")
    except TypeError:
        result_9_lbl.config(text=f"ID  not found in database")
    finally:
        table_9_txt.delete(0, "end")
        column1_9_txt.delete(0, "end")
        column2_9_txt.delete(0, "end")
        search_9_txt.delete(0, "end")

        connection.close()
        print("MySQL connection closed successfully")


SearchID = Button(tab9, text="Search", command=search_id)
SearchID.grid(column=5, row=10)


def build_db():
    import SQL_Tools

    connection = SQL_Tools.create_server_connection("localhost", "ERP", "AdminERP")
    createdb = "CREATE DATABASE ERP_NotFashion"
    SQL_Tools.create_database(connection, createdb)
    connectdb = "USE ERP_NotFashion"
    SQL_Tools.connect_database(connection, connectdb)

    create_suppliers_table = """
    CREATE TABLE  suppliers (
      id INT AUTO_INCREMENT,
      supplier VARCHAR(15) NOT NULL UNIQUE,
      web VARCHAR(30) NOT NULL,
      mail VARCHAR(30) NOT NULL,
      phone INT NOT NULL,
      PRIMARY KEY (id)
      );
     """

    create_supplies_table = """
    CREATE TABLE  supplies (
      id INT AUTO_INCREMENT,
      supplier_id INT NOT NULL, 
      supply VARCHAR(20) NOT NULL UNIQUE,
      stock INT NOT NULL,
      description VARCHAR(30) NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
      );
     """

    create_products_category_table = """
    CREATE TABLE products_category (
      id INT AUTO_INCREMENT,
      supplier_id INT NOT NULL,
      model INT NOT NULL UNIQUE,
      composition VARCHAR(30) NOT NULL ,
      PRIMARY KEY (id),
      FOREIGN KEY (supplier_id) REFERENCES suppliers (id)
      );
     """

    create_products_colour_table = """
    CREATE TABLE products_colour (
      id INT AUTO_INCREMENT,
      colour VARCHAR(20) NOT NULL UNIQUE,
      description VARCHAR(30),
      PRIMARY KEY (id)
      );
     """

    create_products_size_table = """
    CREATE TABLE products_size (
      id INT AUTO_INCREMENT,
      category_id INT NOT NULL,
      size VARCHAR(6) NOT NULL ,
      description VARCHAR(30),
      PRIMARY KEY (id),
      FOREIGN KEY (category_id) REFERENCES products_category (id) 
      );
     """

    create_products_table = """
    CREATE TABLE products (
      id INT AUTO_INCREMENT,
      category_id INT NOT NULL,
      size_id INT NOT NULL,
      colour_id INT NOT NULL,
      sku VARCHAR(40) NOT NULL UNIQUE,
      stock INT NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (category_id) REFERENCES products_category (id),
      FOREIGN KEY (size_id) REFERENCES products_size (id),
      FOREIGN KEY (colour_id) REFERENCES products_colour (id)
      );
     """
    create_distribution_center_table = """
    CREATE TABLE  distribution_center (
      id INT AUTO_INCREMENT,
      name VARCHAR(30) NOT NULL UNIQUE,
      mail VARCHAR(30) NOT NULL,
      web VARCHAR(30) NOT NULL,
      address VARCHAR(50) NOT NULL,
      PRIMARY KEY (id) 
      );
     """

    create_user_table = """
    CREATE TABLE  user (
      id INT AUTO_INCREMENT,
      distribution_center_id INT NULL,
      name VARCHAR(30) NOT NULL UNIQUE,
      mail VARCHAR(30) NOT NULL,
      phone INT NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (distribution_center_id) REFERENCES distribution_center (id)
      );
     """

    create_products_stock = """
    CREATE TABLE  products_stock (
      product_id INT NOT NULL,
      dist_center_id INT NOT NULL,
      stock INT NOT NULL,
      PRIMARY KEY (product_id, dist_center_id),
      FOREIGN KEY (product_id) REFERENCES products (id),
      FOREIGN KEY (dist_center_id) REFERENCES distribution_center (id) 
      );
     """
    create_stores_table = """
    CREATE TABLE  stores (
      id INT AUTO_INCREMENT,
      store VARCHAR(15) NOT NULL UNIQUE,
      mail VARCHAR(30) NOT NULL,
      web VARCHAR(30) NOT NULL,
      address VARCHAR(20) NOT NULL,
      PRIMARY KEY (id) 
      );
     """
    create_opl_table = """
    CREATE TABLE opl (
      id INT AUTO_INCREMENT,
      opl VARCHAR(10) NOT NULL UNIQUE,
      mail VARCHAR(30) NOT NULL,
      web VARCHAR(30) NOT NULL,
      phone INT NOT NULL,
      PRIMARY KEY (id)
      );
     """
    create_orders_table = """
    CREATE TABLE orders (
      id INT NOT NULL AUTO_INCREMENT,
      store_id INT NOT NULL,
      store_tag VARCHAR(30) NOT NULL,
      shipping_address VARCHAR(70) NOT NULL,
      opl_id INT NOT NULL,
      order_value INT NOT NULL,
      order_date DATETIME NOT NULL,
      tags VARCHAR(60) NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (store_id) REFERENCES stores (id),
      FOREIGN KEY (opl_id) REFERENCES opl (id)
      );
     """
    create_order_products_table = """
    CREATE TABLE order_products (
      order_id INT NOT NULL,
      product_id  INT NOT NULL,
      quantity INT NOT NULL,
      value INT NOT NULL,
      PRIMARY KEY (order_id, product_id),
      FOREIGN KEY (order_id) REFERENCES orders (id),
      FOREIGN KEY (product_id) REFERENCES products (id)
      );
     """
    create_inventory_table = """
    CREATE TABLE inventory (
      id INT AUTO_INCREMENT,
      date  DATE NOT NULL,
      supplier_id INT NOT NULL,  
      cost INT NOT NULL,
      import_cost INT,
      PRIMARY KEY (id),
      FOREIGN KEY (supplier_id) REFERENCES  suppliers (id)
      );
     """
    create_inventory_products_table = """
    CREATE TABLE inventory_products (
      distribution_center_id INT NOT NULL,
      inventory_id INT NOT NULL,
      product_id INT NOT NULL,
      quantity INT NOT NULL,
      PRIMARY KEY (distribution_center_id, inventory_id, product_id),
      FOREIGN KEY (distribution_center_id) REFERENCES distribution_center (id),
      FOREIGN KEY (inventory_id) REFERENCES  inventory (id),
      FOREIGN KEY (product_id) REFERENCES products (id)
      );
     """
    create_returns_table = """
    CREATE TABLE returns (
      id INT AUTO_INCREMENT,
      order_id INT NOT NULL,
      opl_id INT NOT NULL,
      PRIMARY KEY (id), 
      FOREIGN KEY (order_id) REFERENCES orders (id),
      FOREIGN KEY (opl_id) REFERENCES opl (id) 
      );
     """
    create_returns_products_table = """
    CREATE TABLE  return_products (
      return_id INT NOT NULL,
      product_in_id INT NOT NULL,
      product_in_qty INT NOT NULL,
      product_out_id INT NOT NULL,
      product_out_qty INT NOT NULL,
      PRIMARY KEY (return_id, product_in_id, product_out_id),
      FOREIGN KEY (return_id) REFERENCES returns (id),
      FOREIGN KEY (product_in_id) REFERENCES products (id),
      FOREIGN KEY (product_out_id) REFERENCES products (id)
      );
     """
    create_clients_table = """
    CREATE TABLE clients (
      id INT AUTO_INCREMENT,
      name  VARCHAR(30) NOT NULL,
      mail VARCHAR(30) NOT NULL UNIQUE,
      phone INT NOT NULL,
      PRIMARY KEY (id)
      );
     """
    create_client_orders_table = """
    CREATE TABLE client_orders (
      client_id INT,
      order_id INT,
      PRIMARY KEY (client_id, order_id),
      FOREIGN KEY (client_id) REFERENCES clients (id),
      FOREIGN KEY (order_id) REFERENCES orders (id)
      );
     """
    create_shopify_table = """
    CREATE TABLE shopify (
      id INT AUTO_INCREMENT,
      date  DATE NOT NULL,
      total_visitors INT NOT NULL,
      total_conversion INT NOT NULL,
      total_pageviews INT NOT NULL,
      total_orders_placed INT NOT NULL,
      PRIMARY KEY (id)
      );
     """
    create_status_table = """
    CREATE TABLE status (
      id INT AUTO_INCREMENT,
      order_id INT,
      return_id INT,
      datetime  DATETIME NOT NULL,
      status VARCHAR(10) NOT NULL,
      box1 INT NOT NULL,
      box2 INT NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (order_id) REFERENCES orders (id),
      FOREIGN KEY (return_id) REFERENCES returns (id)
      );
     """

    create_user_status_table = """
    CREATE TABLE  user_status (
      id INT AUTO_INCREMENT,
      user_id INT NOT NULL,
      distribution_center_id INT NULL,
      status_id INT NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (distribution_center_id) REFERENCES distribution_center (id),
      FOREIGN KEY (user_id) REFERENCES user (id),
      FOREIGN KEY (status_id) REFERENCES status (id)
      );
     """

    SQL_Tools.execute_query(connection, create_suppliers_table)
    SQL_Tools.execute_query(connection, create_supplies_table)
    SQL_Tools.execute_query(connection, create_products_category_table)
    SQL_Tools.execute_query(connection, create_products_colour_table)
    SQL_Tools.execute_query(connection, create_products_size_table)
    SQL_Tools.execute_query(connection, create_products_table)
    SQL_Tools.execute_query(connection, create_distribution_center_table)
    SQL_Tools.execute_query(connection, create_user_table)
    SQL_Tools.execute_query(connection, create_products_stock)
    SQL_Tools.execute_query(connection, create_stores_table)
    SQL_Tools.execute_query(connection, create_opl_table)
    SQL_Tools.execute_query(connection, create_orders_table)
    SQL_Tools.execute_query(connection, create_order_products_table)
    SQL_Tools.execute_query(connection, create_inventory_table)
    SQL_Tools.execute_query(connection, create_inventory_products_table)
    SQL_Tools.execute_query(connection, create_returns_table)
    SQL_Tools.execute_query(connection, create_returns_products_table)
    SQL_Tools.execute_query(connection, create_clients_table)
    SQL_Tools.execute_query(connection, create_client_orders_table)
    SQL_Tools.execute_query(connection, create_shopify_table)
    SQL_Tools.execute_query(connection, create_status_table)
    SQL_Tools.execute_query(connection, create_user_status_table)
    SQL_Tools.add_store(connection, 'Shopify', 'mail@ok.com', 'www.shopify.com', 1234567890)
    SQL_Tools.add_store(connection, 'Falabella', 'mail@ok.com', 'www.falabella.com', 1234567890)
    SQL_Tools.add_store(connection, 'Pruebatelo', 'contacto@pruebatelo.cl', 'www.pruebatelo.cl.com', 1234567890)
    SQL_Tools.add_store(connection, 'Manual', 'contacto@notfashion.cl', 'www.notfashion.cl.com', 1234567890)
    SQL_Tools.add_opl(connection, 'Lodis', 'contacto@lodis.cl', 'www.lodis.cl', 1234567890)
    SQL_Tools.add_opl(connection, 'Shipit', 'contacto@shipit.cl', 'www.shippit.cl', 1234567890)
    SQL_Tools.add_opl(connection, 'Falabella', 'contacto@fallabella.cl', 'www.falabella.cl', 1234567890)
    SQL_Tools.add_opl(connection, 'Ripley', 'contacto@ripley.cl', 'www.ripley.cl', 1234567890)
    SQL_Tools.add_opl(connection, 'Pruebatelo', 'contacto@pruebatelo.cl', 'www.pruebatelo.cl', 1234567890)
    SQL_Tools.add_opl(connection, 'Interno', 'contacto@notfashion.cl', 'www.notfashion.cl', 1234567890)
    SQL_Tools.add_supplier(connection, 'Royal Apparel', 'contact@royalapparel.com', 'www.royalapparel.com', 1234567890)
    SQL_Tools.add_supplier(connection, 'Marcia', 'contact@marcia.cl', 'www.marcia.cl', 1234567890)
    SQL_Tools.add_supplier(connection, 'Cajas Matta', 'contact@cajas.cl', 'www.caajasmatta.cl', 1234567890)
    SQL_Tools.add_supplier(connection, 'Insumos Of', 'contact@.cl', 'www..cl', 1234567890)
    SQL_Tools.add_supply(connection, 3, 'Caja Chica', 5, '12x12x12')
    SQL_Tools.add_supply(connection, 3, 'Caja Grande', 5, '24x24x12')
    SQL_Tools.add_supply(connection, 4, 'Brother Labels', 5, ' ')
    SQL_Tools.add_supply(connection, 4, 'Ream paper', 5, 'Letter')
    SQL_Tools.add_supply(connection, 4, 'Glue', 5, 'Uhu-Stick')
    SQL_Tools.add_distribution_center(connection, 'Santiago', 'cd1@notfashion.cl',
                                      'www.blablabla/qwer1.cl', 'Cueto 715, Santiago, Chile')
    SQL_Tools.add_distribution_center(connection, 'Concepcion', 'cd2@notfashion.cl',
                                      'www.blablabla/qwer1.cl', 'Cueto 715, Concepcion, Chile')
    SQL_Tools.add_user(connection, 1, 'Francisco Castañeda', 'fra.castaneda@gmail.com', 946251220)

    connection.close()
    print("MySQL connection closed successfully")


def backup_db():
    os.popen("mysqldump --defaults-extra-file=MySQL_Host  ERP_NotFashion> ERP_NotFashion_Backup.sql")
    messagebox.showinfo('NotFashion ERP', 'Database Backup Completed Successfully')


def restore_db():
    connection = SQL_Tools.create_server_connection("localhost", "ERP", "AdminERP")
    cursor = connection.cursor()
    SQL_Tools.execute_query(connection, 'CREATE DATABASE ERP_NotFashion')
    SQL_Tools.execute_query(connection, 'USE ERP_NotFashion')
    fd = open('ERP_NotFashion_Backup.sql', 'r')
    sqlfile = fd.read()
    fd.close()
    sqlcommands = sqlfile.split(';')

    for command in sqlcommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print(f"Command skipped':{msg}' ")

    messagebox.showinfo('NotFashion ERP', 'Database Restored Successfully')


def version_erp():
    messagebox.showinfo('NotFashion ERP', 'Beta Version 0.2.2')


def shopify_mass_order():
    connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", 'ERP_NotFashion')

    file = filedialog.askopenfilename()
    shopify_orders = pd.read_csv(file, encoding="utf-8")
    print(list(shopify_orders.columns))
    shopify_orders = shopify_orders[['Shipping Name', 'Shipping Address1', 'Email', 'Shipping Phone', 'Lineitem sku',
                                     'Lineitem quantity', 'Total', 'Name', 'Created at', 'Tags', 'Lineitem price']]
    shopify_paid = shopify_orders[shopify_orders['Total'] > 0]
    store_id = 1
    opl_id = 1
    shopify_paid = shopify_paid.values.tolist()

    for i in shopify_paid:
        connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", 'ERP_NotFashion')
        shipping_name = re.sub(r'\d+', '', str(i[:1][0]))
        print(shipping_name)
        shipping_address = str(i[1:2][0])
        print(shipping_address)
        shipping_mail = str(i[2:3][0])
        print(shipping_mail)
        shipping_phone = re.sub(r'\D', '', (str(i[3:4][0])).replace(" ", ""))
        print(shipping_phone)
        if type(shipping_phone) != int:
            shipping_phone = 0
        order_date = datetime.strptime(str(i[8:9][0]), '%Y-%m-%d %H:%M:%S %z').replace(tzinfo=None)
        print(order_date)
        order_tags = str(i[9:10][0])
        print(f"Order Tag'{order_tags}'")
        store_tag = str(i[7:8][0])
        print(store_tag)
        connection.rollback()
        client_id = SQL_Tools.get_id(connection, 'clients', 'id', 'mail', f"'{shipping_mail}'")

        try:
            if client_id[0] >= 0:
                print(f"Client ID'{client_id[0]}' found in database")
                client_id = client_id[0]
        except TypeError:
            client_id = SQL_Tools.create_client_id(connection, shipping_name, shipping_mail, shipping_phone)

        finally:
            order_id = SQL_Tools.add_order(connection, store_id, str(i[7:8][0]), shipping_address, opl_id, i[6:7][0],
                                           order_date, order_tags)
            SQL_Tools.add_order_client(connection, order_id, client_id)
            order_products = shopify_orders[shopify_orders['Name'] == store_tag]
            order_products = order_products.values.tolist()
            print(order_products)
            for j in order_products:
                connection = SQL_Tools.create_db_connection("localhost", "ERP", "AdminERP", 'ERP_NotFashion')
                product = j[4:5][0]
                product_qty = j[5:6][0]
                product_price = j[10:11][0]
                print(f"Product '{product}' (Quantity {product_qty}) Price  ${product_price} ")
                product_id = SQL_Tools.get_id(connection, 'products', 'id', 'sku', f"'{product}'")
                print(f"Product ID : {product_id[0]}")
                product_stock = SQL_Tools.get_product_stock(connection, f"'{product}'")
                product_stock = product_stock[0]
                update_stock = int(product_stock) - product_qty
                update_stock = f'"{update_stock}"'
                SQL_Tools.add_order_products(connection, order_id, product_id[0], product_qty, product_price)
                SQL_Tools.update_product_stock(connection, f"'{product}'", update_stock)
        status_q = "Queue"
        status_null = 0
        time_now = datetime.now()
        SQL_Tools.add_order_status(connection, order_id, time_now, status_q, status_null, status_null)
        print("Order imported successfully")
        connection.close()
        print('<---------------------------------------------------------------------->')
    print("Orders imported successfully")
    connection.close()
    print("MySQL connection closed successfully")


menu_erp = Menu(window)
main_item = Menu(menu_erp)
main_item.add_command(label='Build Database', command=build_db)
main_item.add_command(label='Backup Database', command=backup_db)
main_item.add_command(label='Restore Database', command=restore_db)
main_item.add_separator()
main_item.add_command(label='Version', command=version_erp)
menu_erp.add_cascade(label='Main', menu=main_item)
operation_menu = Menu(menu_erp)
operation_menu.add_command(label="Shopify Orders Mass Input", command=shopify_mass_order)
menu_erp.add_cascade(label='Operations', menu=operation_menu)

window.config(menu=menu_erp)
window.mainloop()
