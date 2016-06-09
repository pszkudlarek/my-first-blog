#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as server
from random import random

# Useful links:
# 
# PEP 249 -- Python Database API Specification v2.0:
#     https://www.python.org/dev/peps/pep-0249
# 
# Help for sqlite3 module: 
#     https://docs.python.org/2/library/sqlite3.html
#
# SQLite data types:
#     https://www.sqlite.org/datatype3.html 


def init_database():
    # Open connection to sqlite file dtabase (database will be created if doesent exists)
    con = server.connect("database.db")
    
    # Create cursor()
    cur = con.cursor()
    
    # Crete table()
    sql_crate='''CREATE TABLE produkty(id integer primary key, nazwa text, cena real)'''  
    cur.execute(sql_crate)
        
    # Insert data into table 
    sql_insert='''insert into produkty (id, nazwa , cena) values (?,?,?)'''
    cur.execute(sql_insert, (1,'truskawka', '5.5'))
    
    cur.close()
    con.commit()
    con.close()

if __name__ == '__main__':
#         init_database()
    con = server.connect("database.db")
    cur = con.cursor() 
    cur.execute('select * from produkty')
    for p in cur.fetchmany(10):
        print p
    cur.close()
    con.close()

    
'''
#===============================================================================
1) wypełnij table produkty losowymi wpisami:
- pobież maksymalną wartość id z tabeli produkty
- automatycznie wygneruj następne wartości id (nie w bazie)
- wpisz 1000 rekordów z losowymi nazwami i cenami 
    random.random() 
- napis funkcję która zwróci histogram cen dla danych w tabeli produkty,
    histogram z dziesięcioma przedziałami w postaci:
    
cena-ilość w procentach całości
-------------------------------
1 - 5%      
2 - 5%      
3 - 20%      
4 - 5%      
...
#===============================================================================
'''
    
