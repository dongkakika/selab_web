import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

file_names = os.listdir('../../media/image/default/')

texts = [
    '2010',
    '2015',
    '2015',
    
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
    
    '2011',
    '2012',
    '2012',
    '2014',
    '2014',
    
    '2018',
    '2016',
    '2019',
    
    '2017',
    '2017',
    '-',
    '2018',
    '2019',
    '2019',
    '2021, Thanks for our professor Hong a lot !',
    ]

file_names.sort()

contents = {}
j = 0
for i in file_names:
    contents[i[0:2]] = texts[j] 
    j += 1

for i in file_names:
    li = [i[3:-4], "image/default/"+i, contents[i[0:2]]]

    cur.execute('insert into gallery (title, img, content) values(?, ?, ?)', li)
    con.commit()

con.close()
