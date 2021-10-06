import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

titles = ['Our Main Research Areas.', '']
file_names = os.listdir('../../media/image/research/')
contents = ['<p style="margin-bottom: 0px;">Embedded SW Design and Validation Technology for MPSoC</p><p style="margin-bottom: 0px;">A Study on Source Technology of system SW for Super Mobile Implementation</p><p style="margin-bottom: 0px;">Context-based SW reuse</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">Model-based Low Power Design Techniques for Robot Applications</p><p style="margin-bottom: 0px;">Energy efficiency guarantee techniques of smartphone embedded SW</p><p style="margin-bottom: 0px;">Code refactoring techniques to support low power</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">Interaction Detection Techniques for Safety Critical System</p><p style="margin-bottom: 0px;">Fault prevention tree-based risk detection and resolution techniques</p>', '<p style="text-align: right; margin-bottom: 0px;"><b><font color="#104a5a">Dimestions of Software Engineering</font></b><br></p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;">Process<br></p><p style="text-align: right; margin-bottom: 0px;">Software Process Model</p><p style="text-align: right; margin-bottom: 0px;">Software process improvement</p><p style="text-align: right; margin-bottom: 0px;">Quantitative Process Management Techniques</p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;">Technology</p><p style="text-align: right; margin-bottom: 0px;">Software Modeling</p><p style="text-align: right; margin-bottom: 0px;">Software Validation</p><p style="text-align: right; margin-bottom: 0px;">Software Adaptation and Application</p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;">Resources</p><p style="text-align: right; margin-bottom: 0px;">Human Resource Management (P-CMM)</p><p style="text-align: right; margin-bottom: 0px;">Training and mentoring</p>']
left_right_check = [False, True]
idx = 0
for i in titles:
    li = [i, 'image/research/' + file_names[idx], contents[int(file_names[idx][0:1])], left_right_check[idx]]
    idx += 1
    
    cur.execute('insert into research (title, img, content, left_right_check) values(?,?,?,?)', li)
    con.commit()
    
con.close()
