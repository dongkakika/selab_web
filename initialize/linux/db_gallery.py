import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

file_names = os.listdir('../../media/image/default/')
contents = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'This is a test image.',
    'This is a test gif image.',
    'This is the central library in CBNU.',
    'This is the main entrance image of CBNU.',
    'Find where you want to go with this map !',
    'The autumn sky of Chungju city.',
    'The first picture of the jeju conference at the airport.',
    'Our lab members had a conference and a great time in Jeju.',
    'Our professor appeared in a local article.',
    'This is our department building.',
    '-',
    ]

for i in file_names:
    li = [i[2:-4], "image/default/"+i, contents[int(i[0:2])]]

    cur.execute('insert into gallery (title, img, content) values(?,?,?)', li)
    con.commit()

con.close()
