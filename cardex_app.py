from prettytable import PrettyTable
import pymysql

"""
1. identificar cada parte de lo que esta en el codigo

"""

"""
connection = pymysql.connect(

esta creando la conexion entre mi programa python con la base de datos
mysql vean que se tiene los datos de conexion host, user, passwrd, el
eschema o la base de datos
"""
connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="cardexdb",
    cursorclass=pymysql.cursors.DictCursor,
)

"""
def getAllClients():
este es un metodo de este archivo que se encarga de traer todos 
los clientes de nuestra tabla cliente, colocarlos en una prettytable
y luego desplegarlos
"""


def getAllClients():
    # con la conexion y sql va a traer todos los datos y los guarda en
    # una variable llamada result
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM cardexdb.client;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        pass
    # crea un objeto pretty table y le genera los encabezados de la tabla
    table = PrettyTable()
    table.field_names = ["Id", "Name", "Age", "Email"]
    # for medio del for saco todos los cliente y los voy ingresando
    # a la pretty table
    for client in result:
        table.add_row([client["id"], client["name"], client["age"], client["email"]])
    # imprimo la prettytable
    print(table)
    # luego limpiamos la tabla
    table.clear()


def addNewClient():
    print("add a new client...")
    name = input("name: ")
    age = int(input("age: "))
    email = input("email: ")
    try:
        with connection.cursor() as cursor:
            sql = f"insert into cardexdb.client(name, age, email) values('{name}', {age}, '{email}');"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
    getAllClients()


def updateClient():
    print("update client...")
    id = int(input("id of client to update: "))
    try:
        with connection.cursor() as cursor:
            sql = f"select * from cardexdb.client where id={id};"
            cursor.execute(sql)
            client = cursor.fetchone()
    finally:
        pass

    update = int(input("update name 0-no 1-yes? "))
    if update == 1:
        print(f"old name: {client['name']}")
        name = input("name: ")
    else:
        name = client["name"]

    update = int(input("update age 0-no 1-yes? "))
    if update == 1:
        print(f"old age: {client['age']}")
        age = int(input("age: "))
    else:
        age = client["age"]

    update = int(input("update email 0-no 1-yes? "))
    if update == 1:
        print(f"old email: {client['email']}")
        email = input("email: ")
    else:
        email = client["email"]

    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE cardexdb.client SET name = '{name}', age = {age}, email = '{email}' WHERE id = {id};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
    getAllClients()


def deleteClient():
    print("delete client...")
    id = int(input("id of client to delete: "))
    try:
        with connection.cursor() as cursor:
            sql = f"delete from cardexdb.client where id={id};"
            cursor.execute(sql)
            connection.commit()
    finally:
        pass
    getAllClients()


while True:
    print("cardex app...")
    print("menu: ")
    print("0 - exit: ")
    print("1 - get all clients: ")
    print("2 - add a new client: ")
    print("3 - update client: ")
    print("4 - delete client: ")
    option = int(input("option: "))

    if option == 0:
        print("exit cardex app...")
        connection.close()
        break
    if option == 1:
        getAllClients()
    if option == 2:
        addNewClient()
    if option == 3:
        updateClient()
    if option == 4:
        deleteClient()
