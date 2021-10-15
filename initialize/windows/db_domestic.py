import sqlite3
import codecs
import os

# function def.
def num_check(input_str):
    return any(char.isdigit() for char in input_str)

# read file
f = codecs.open('db_domestic.txt', 'r', encoding='UTF8')

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

### Main ###
for li in total:
    
    before = li.split(',')
    after = []
    for c in before:
        # delete unnecessary character
        after.append(c.replace("\n", "").replace("\r", ""))

    people = []
    content = []
    journals = []
    date = ""
    for i in after:
        lth = len(i)
        check = num_check(i)
        if lth < 7 and check == False: # if it's less than 7, it's a name
            people.append(i)
        elif lth > 22:                 # content is always more than 22
            content.append(i)
        elif after[-1] == i:          # last element is always 'date'
            date = i
        else:
            journals.append(i)        # and something rest is 'journals'

    date = date[1:len(date)]
    
    temp = ""
    for k in journals:
        temp += k
    journals = temp

    temp = ""
    for k in people:
        temp = temp + k + ", "
    name = temp + content[0]

    result = [name, journals, date]

    cur.execute('insert into domestic_journal(title, journals, issued_date) values(?,?,?)', result)
    con.commit()

con.close()    
