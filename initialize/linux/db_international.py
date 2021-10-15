import sqlite3
import codecs
import os

# read file
f = codecs.open('db_international.txt', 'r', encoding='UTF8')

# transform file to list
total = []
while True:
    line = f.readline()
    if not line: break
    total.append(line)
f.close()


# db connection
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()


### MAIN ###
for li in total:
    before = li.split('"')

    # people & content
    content = before[0] + '"' + before[1] + '"'
    
    # journals & date
    after = before[2].replace("\n", "").replace("\r", "").split(', ')
    date = after[-1]

    temp = after[1:-1]
    journals = temp[0]
    for idx in range(len(temp)):
        if idx != 0:
            journals = journals + ", " + temp[idx]

    result = [content, journals, date]
    
    cur.execute('insert into international_journal(title, journals, issued_date) values(?,?,?)', result)
    con.commit()


con.close()
