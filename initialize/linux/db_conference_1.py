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
f = codecs.open('db_conference_1.txt', 'r', encoding='UTF8')

# transform file to list
total = []
while True:
    line = f.readline()
    if not line: break
    total.append(line)
f.close()

### Main ###
for li in total:
    before = li.replace('\n', '').replace('\r', '').replace(", ", ',').split(',')
    
    people = []
    result = []

    lth = len(before)
    for i in range(lth):
        idx = -1*(i+1)
        if idx > -3:
            result.insert(0, before[idx])
        else:
            people.insert(0, before[idx])

    temp = ""
    for p in people:
        if len(p) < 10:
            p += ", "
        else:
            p = '"' + p + '"'
        temp += p

    result.insert(0, temp)

    cur.execute('insert into conference(title, academic_conference, period) values(?,?,?)', result)
    con.commit()

con.close()

    
    
        
