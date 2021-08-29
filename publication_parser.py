import sqlite3
import codecs
import os



# reading the text file
f = codecs.open("publication.txt", 'r', encoding='UTF8')
pub = []
while True:
    line = f.readline()
    if not line: break
    pub.append(line)
f.close()

category_list = ['국내논문지', '국제논문지', '국내학술대회', '국제학술대회', '지적재산권', '연구보고서', '기타 학술활동']

def category(l):
    count = 0
    for cate in category_list:
        if cate in l:
            return count
        count += 1
    # a wrong category exists
    return -1

def num_check(input_str):
    return any(char.isdigit() for char in input_str)

def manipulate(l):
    
    before = l.split(',')
    after = []
    for i in before:
        after.append(i.replace("\r", "").replace("\n", ""))

    people = []
    content = []
    org = []
    date = []
    count = 0
    for j in after:
        lth = len(j)
        temp = num_check(j)
        # 1. when people
        if lth < 5 and temp == False:
            people.append(j)
        elif lth > 22:
            content.append(j)
        elif after[-1] == j:
            date.append(j)
        else:
            org.append(j)

    # org processing
    temp = ""
    for k in org:
        temp += k
    org = temp

    temp = ""
    for k in people:
        temp += k

    name = temp + content[0]

    total_list = [name, org, date[0]]

    # db connecting
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    idx = 0
    for wow in cur.execute('select id from journal order by rowid desc limit 1;'):
        idx = wow[0]
        break
    
    cur.execute('insert into journal(title, journals, issued_date) values(?,?,?)', total_list)
    con.commit()
    con.close()
    print(1)
    
    

### main ###
group_check = False
check_category = 0
stop = 0
for line in pub:
    if group_check is False:        
        for c in line:
            if c == '[':
                check_category = category(line)
                group_check = True
                break
    else:
        
        manipulate(line)






hi = " 6호"

