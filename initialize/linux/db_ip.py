import sqlite3
import codecs
import os

# db connection
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

# function def.
def num_check(input_str):
    return any(char.isdigit() for char in input_str)

# read file
f = codecs.open('db_ip.txt', 'r', encoding='UTF8')

# transform file to list
total = []
while True:
    line = f.readline()
    if not line: break
    total.append(line)
f.close()

### Main ###
for li in total:
    result = li.replace('\n', '').replace('\r', '').replace(", ", ',').split(',')    

    cur.execute('insert into ip(title, type, number, date) values(?,?,?,?)', result)
    con.commit()

con.close()
