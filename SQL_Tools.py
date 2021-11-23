import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def connect_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database changed successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_supply(connection, supplier_id, supply, stock, description):
    cursor = connection.cursor()
    try:
        new_supply = ("INSERT INTO supplies "
                      "(id, supplier_id, supply, stock, description) "
                      "VALUES (%(id)s, %(supplier_id)s, %(supply)s, %(stock)s, %(description)s)")
        supply_id = cursor.lastrowid
        supply = {
            'id': supply_id,
            'supplier_id': supplier_id,
            'supply': supply,
            'stock': stock,
            'description': description,
        }
        cursor.execute(new_supply, supply)
        result = cursor.lastrowid
        connection.commit()
        print("Supply added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_product_category(connection, supplier_id, model, composition):
    cursor = connection.cursor()
    try:
        new_category = ("INSERT INTO products_category "
                        "(id, supplier_id, model, composition) "
                        "VALUES (%(id)s, %(supplier_id)s, %(model)s, %(composition)s)")

        category_id = cursor.lastrowid
        category = {
            'id': category_id,
            'supplier_id': supplier_id,
            'model': model,
            'composition': composition,
        }
        cursor.execute(new_category, category)
        result = cursor.lastrowid
        connection.commit()
        print("Product's Category added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_product_colour(connection,  colour, description):
    cursor = connection.cursor()
    try:
        new_colour = ("INSERT INTO products_colour "
                      "(id,  colour, description) "
                      "VALUES (%(id)s, %(colour)s, %(description)s)")

        colour_id = cursor.lastrowid
        colour = {
            'id': colour_id,
            'colour': colour,
            'description': description
        }
        cursor.execute(new_colour, colour)
        result = cursor.lastrowid
        connection.commit()
        print("Product's Colour added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_product_size(connection, category_id, size, description):
    cursor = connection.cursor()
    try:
        new_size = ("INSERT INTO products_size "
                    "(id,  category_id, size, description) "
                    "VALUES (%(id)s, %(category_id)s, %(size)s, %(description)s)")

        size_id = cursor.lastrowid
        size = {
            'id': size_id,
            'category_id': category_id,
            'size': size,
            'description': description
        }
        cursor.execute(new_size, size)
        result = cursor.lastrowid
        connection.commit()
        print("Product's size added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_product(connection, category_id, sku, size_id, colour_id, stock):
    cursor = connection.cursor()
    try:
        new_product = ("INSERT INTO products "
                       "(id, category_id, sku, size_id, colour_id, stock) "
                       "VALUES (%(id)s, %(category_id)s, %(sku)s, %(size_id)s, %(colour_id)s, %(stock)s)")
        product_id = cursor.lastrowid
        product = {
            'id': product_id,
            'category_id': category_id,
            'sku': sku,
            'size_id': size_id,
            'colour_id': colour_id,
            'stock': stock,
        }
        cursor.execute(new_product, product)
        result = cursor.fetchone()
        connection.commit()
        print("Product added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_store(connection, store, mail, web, address):
    cursor = connection.cursor()
    try:
        new_store = ("INSERT INTO stores "
                     "(id, store, mail, web, address) "
                     "VALUES (%(id)s, %(store)s, %(mail)s, %(web)s, %(address)s)")
        store_id = cursor.lastrowid
        store = {
            'id': store_id,
            'store': store,
            'mail': mail,
            'web': web,
            'address': address,
        }
        cursor.execute(new_store, store)
        connection.commit()
        print("Store added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_opl(connection, opl, mail, web, phone):
    cursor = connection.cursor()
    try:
        new_opl = ("INSERT INTO opl "
                   "(id, opl, mail, web, phone) "
                   "VALUES (%(id)s, %(opl)s, %(mail)s, %(web)s, %(phone)s)")
        opl_id = cursor.lastrowid
        opl = {
            'id': opl_id,
            'opl': opl,
            'mail': mail,
            'web': web,
            'phone': phone,
        }
        cursor.execute(new_opl, opl)
        connection.commit()
        print("OPL added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_distribution_center(connection, name, mail, web, address):
    cursor = connection.cursor()
    try:
        new_distribution_center = ("INSERT INTO distribution_center "
                                   "(id, name, mail, web, address) "
                                   "VALUES (%(id)s, %(name)s, %(mail)s, %(web)s, %(address)s)")
        distribution_center_id = cursor.lastrowid
        distribution_center = {
            'id': distribution_center_id,
            'name': name,
            'mail': mail,
            'web': web,
            'address': address,
        }
        cursor.execute(new_distribution_center, distribution_center)
        connection.commit()
        print("Distribution Center added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_user(connection, distribution_center_id, name, mail, phone):
    cursor = connection.cursor()
    try:
        new_user = ("INSERT INTO user "
                    "(id, distribution_center_id, name, mail, phone) "
                    "VALUES (%(id)s, %(distribution_center_id)s, %(name)s, %(mail)s,%(phone)s)")
        user_id = cursor.lastrowid
        user = {
            'id': user_id,
            'distribution_center_id': distribution_center_id,
            'name' : name,
            'mail': mail,
            'phone': phone,
        }
        cursor.execute(new_user, user)
        connection.commit()
        print("User added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_supplier(connection, supplier, mail, web, phone):
    cursor = connection.cursor()
    try:
        new_supplier = ("INSERT INTO suppliers "
                        "(id, supplier, mail, web, phone) "
                        "VALUES (%(id)s, %(supplier)s, %(mail)s, %(web)s, %(phone)s)")
        supplier_id = cursor.lastrowid
        supplier = {
            'id': supplier_id,
            'supplier': supplier,
            'web': web,
            'mail': mail,
            'phone': phone,
        }
        cursor.execute(new_supplier, supplier)
        connection.commit()
        print("Supplier added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_order(connection, store_id, store_tag, shipping_address, opl_id, order_value, order_date, tags):
    cursor = connection.cursor()
    try:
        new_order = ("INSERT INTO orders "
                     "(id, store_id, store_tag, shipping_address, opl_id, order_value, order_date, tags) "
                     "VALUES (%(id)s, %(store_id)s, %(store_tag)s, %(shipping_address)s, %(opl_id)s, %(order_value)s, "
                     "%(order_date)s, %(tags)s)")
        order_id = cursor.lastrowid
        order = {
            'id': order_id,
            'store_id': store_id,
            'store_tag': store_tag,
            'shipping_address': shipping_address,
            'opl_id': opl_id,
            'order_value': order_value,
            'order_date': order_date,
            'tags': tags
        }
        cursor.execute(new_order, order)
        result = cursor.lastrowid
        connection.commit()
        print(f"Order ID'{result}' successfully created")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_order_products(connection, order_id, product_id, quantity, value):
    cursor = connection.cursor()
    try:
        order_products = ("INSERT INTO order_products "
                          "(order_id, product_id, quantity, value) "
                          "VALUES (%(order_id)s, %(product_id)s, %(quantity)s, %(value)s)")

        products = {
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'value': value
        }
        cursor.execute(order_products, products)
        connection.commit()
        print("Order's Products added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_order_status(connection, order_id, datetime, status, box1, box2):
    cursor = connection.cursor()
    try:
        new_status = ("INSERT INTO status "
                      "(order_id, datetime, status, box1, box2) "
                      "VALUES (%(order_id)s, %(datetime)s, %(status)s, %(box1)s, %(box2)s)")
        status_id = cursor.lastrowid
        status = {
            'id': status_id,
            'order_id': order_id,
            'datetime': datetime,
            'status': status,
            'box1': box1,
            'box2': box2,
        }
        cursor.execute(new_status, status)
        connection.commit()
        print("Order's Status added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_return(connection, order_id, opl_id):
    cursor = connection.cursor()
    try:
        create_return = ("INSERT INTO returns "
                         "(order_id, opl_id) "
                         "VALUES (%(order_id)s, %(opl_id)s)")
        return_id = cursor.lastrowid
        new_return = {
            'id': return_id,
            'order_id': order_id,
            'opl_id': opl_id,
        }
        cursor.execute(create_return, new_return)
        result = cursor.lastrowid
        connection.commit()
        print(f"Return ID'{result}' successfully created")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_return_products(connection, return_id, product_in_id, product_in_qty, product_out_id, product_out_qty):
    cursor = connection.cursor()
    try:
        return_products = ("INSERT INTO return_products "
                           "(return_id, product_in_id, product_in_qty, product_out_id, product_out_qty) "
                           "VALUES (%(return_id)s, %(product_in_id)s, %(product_in_qty)s, %(product_out_id)s,"
                           " %(product_out_qty)s)")

        products = {
            'return_id': return_id,
            'product_in_id': product_in_id,
            'product_in_qty': product_in_qty,
            'product_out_id': product_out_id,
            'product_out_qty': product_out_qty,
        }
        cursor.execute(return_products, products)
        connection.commit()
        print("Return's Products added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def add_return_status(connection, return_id, datetime, status, box1, box2):
    cursor = connection.cursor()
    try:
        new_status = ("INSERT INTO status "
                      "(return_id, datetime, status, box1, box2) "
                      "VALUES ( %(return_id)s, %(datetime)s, %(status)s, %(box1)s, %(box2)s)")
        status_id = cursor.lastrowid
        status = {
            'id': status_id,
            'return_id': return_id,
            'datetime': datetime,
            'status': status,
            'box1': box1,
            'box2': box2,
        }
        cursor.execute(new_status, status)
        connection.commit()
        result = cursor.lastrowid
        print("Order's Status added successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def create_client_id(connection, name, mail, phone):
    cursor = connection.cursor()
    try:
        new_client = ("INSERT INTO clients "
                      "(id, name, mail, phone) "
                      "VALUES (%(id)s, %(name)s, %(mail)s, %(phone)s)")
        client_id = cursor.lastrowid

        client = {
            'id': client_id,
            'name': name,
            'mail': mail,
            'phone': phone,
        }
        cursor.execute(new_client, client)
        result = cursor.lastrowid
        connection.commit()
        print(f"Client ID'{result}'successfully created")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def add_order_client(connection,  order_id, client_id):
    cursor = connection.cursor()
    try:
        order_products = ("INSERT INTO client_orders "
                          "(order_id, client_id) "
                          "VALUES (%(order_id)s, %(client_id)s)")

        products = {
            'order_id': order_id,
            'client_id': client_id,
        }
        cursor.execute(order_products, products)
        connection.commit()
        print("Client's Order added successfully")
    except Error as err:
        print(f"Error: '{err}'")


def get_id(conn, table, column1, column2, search):
    try:
        curs = conn.cursor()
        query = 'SELECT ' + column1 + ' INTO @id FROM ' + table + ' WHERE ' + column2 + '=' + search +\
                ' LOCK IN SHARE MODE'
        curs.execute(query)
        curs.execute("SELECT @id LOCK IN SHARE MODE")
        result = curs.fetchone()
        conn.commit()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def get_product_size_id(conn, category_id, size):
    try:
        curs = conn.cursor()
        query = 'SELECT id INTO @id FROM products_size WHERE category_id=' + category_id + ' AND size=' + size \
                + 'LOCK IN SHARE MODE'
        curs.execute(query)
        curs.execute("SELECT @id LOCK IN SHARE MODE")
        result = curs.fetchone()
        conn.commit()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def get_product_stock(connection, sku):

    try:
        cursor = connection.cursor()
        query = 'SELECT stock INTO @stock FROM products WHERE sku=' + sku
        cursor.execute(query)
        cursor.execute("SELECT @stock")
        result = cursor.fetchone()
        print(f"Current Stock : {result[0]}")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def update_product_stock(connection, sku, stock):
    cursor = connection.cursor()
    try:
        update = 'UPDATE products SET stock=' + stock + ' WHERE sku=' + sku
        cursor.execute(update)
        connection.commit()
        print(f"Product's {sku} stock updated")
    except Error as err:
        print(f"Error: '{err}'")


def get_supply_stock(connection, supply):

    try:
        cursor = connection.cursor()
        query = 'SELECT stock INTO @stock FROM supplies WHERE supply=' + supply
        cursor.execute(query)
        cursor.execute("SELECT @stock")
        result = cursor.fetchone()
        print(f"Current Stock : {result[0]}")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def update_supply_stock(connection, supply, stock):
    cursor = connection.cursor()
    try:
        update = 'UPDATE supplies SET stock=' + stock + ' WHERE supply=' + supply
        cursor.execute(update)
        connection.commit()
        print(f" Supplies {supply} stock updated")
    except Error as err:
        print(f"Error: '{err}'")

