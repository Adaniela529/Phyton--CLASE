import pandas as pd

import sqlite3

conn=sqlite3.connect('demo.db')

cur=conn.cursor()

def crear_table():
    cur.execute("CREATE TABLE IF NOT EXISTS USER(id INTERGER,USERNAME TEXT,EMAIL TEXT)")
    conn.commit()

def insertar_data():
    for i in range(10000):
        username='user'+str(i)
        usernamev2=f'user{i}'
        email='user'+str(i)+'@gmail.com'
        cur.execute("insert into user values(?,?,?)",(i,usernamev2,email))
        conn.commit()

def mostrar_tabla():
    data=cur.execute("SELECT * FROM USER").fetchall()
    return data


from capamodelo import *
import uuid

def consultar(opcion:int):
    match opcion:
        case 1:
            crear_table()
            print("se ejecuto caso 1")
        case 2:
            insertar_data()
            print("se ejecuto caso 2")
        case 3:
            data=mostrar_tabla()
            print("data =>",data)
            print("se ejecuto caso 3")
        case _:
            print("action por default")

from capalogica import *


message="""
    1)crear tabla
    2)insert data 
    3)ver datos
"""
print(message)
option=int(input("ingrese una opcion"))

consultar(option)

basecsv=pd.read_csv('basecsv.csv')

base_excel=pd.read_excel('base_excel.xlxs')

base_json=pd.read_json('base_json.j.son')






