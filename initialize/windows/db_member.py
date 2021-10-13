import sqlite3
import codecs
import os

# db connection
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

total = [
    ['Nazakat Ali', '<p style="margin-bottom: 0px;"><b>Interests</b></p><p style="margin-bottom: 0px;">System Safety, Cyber-Physical Systems, Hazard Analysis&nbsp;</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">2018 - 2021, Ph.D. Computer Science, CBNU</p><p style="margin-bottom: 0px;">2016 - 2018, M.S. Computer Science, CBNU</p>', 'nazakatali@selab.cbnu.ac.kr', 'image/docter_ali3.png', 1],
    ['Young Jae Kim (김 영 재)', '<p style="margin-bottom: 0px;"><span style="font-weight: 700;">Interests</span></p><p style="margin-bottom: 0px;">Safety Verification, Cyber-Physical Systems<br></p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">2020 - Present, M.S. Computer Science, CBNU<br></p>', 'kyj@selab.cbnu.ac.kr', 'image/master_kyj.jpg', 3],
    ['Manzoor Hussain', '<p style="margin-bottom: 0px;"><span style="font-weight: 700;">Interests</span></p><p style="margin-bottom: 0px;">System Safety, Cyber-Physical Systems, Hazard Analysis, Machine Learning</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">2020 - Present, M.S. Computer Science, CBNU<br></p>', 'hussain@selab.cbnu.ac.kr', 'image/master_manzoor.png', 5],
]

### Main ###
for li in total:
    cur.execute('insert into people(name, content, email, img_upload, delimiter) values(?,?,?,?,?)', li)
    con.commit()

con.close()
