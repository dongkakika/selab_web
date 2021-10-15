import sqlite3
import codecs
import os

# function def.
def num_check(input_str):
    return any(char.isdigit() for char in input_str)

# read file
f = codecs.open('db_international_journal.txt', 'r', encoding='UTF8')

# transform file to list
total = []
while True:
    line = f.readline()
    if not line: break
    total.append(line)
f.close()

# delete the first element: '[ 국제논문지 ]'
del total[0]

### Main ###
for li in total:
    before = li.split(',')
    after = []
    for c in before:
        after.append(c.replace("\n", "").replace("\r", ""))

    people = []
    content = []
    journals = []
    date = []
    date.append(after.pop(-1))

    # why to use count: pop() or remove() makes list changed weirdly.
    count = 0
    for i in after:
        count += 1
        if i.find('"') == -1:
            people.append(i)
        else:
            content.append(i)
            break

    lth = len(after)
    while(count != lth):
        journals.append(after[count])
        count += 1

    # db connection
    con = sqlite3.connect('../../db.sqlite3')
    cur = con.cursor()

    # combine data
    temp = ""
    for k in journals:
        temp += k
    journals = temp

    temp = ""
    for k in people:
        temp = temp + k + ', '
    name = temp + content[0]

    result = [name, journals, date[0]]

    cur.execute('insert into international_journal(title, journals, issued_date) values(?,?,?)', result)
    con.commit()
    con.close()
    
    
