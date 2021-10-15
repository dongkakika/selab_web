import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

titles = [
        'Our Main Research Areas',
        '',
        'Reseach & proejct in progress', 
        ]
file_names = os.listdir('../../media/image/research/')
contents = ['<p style="margin-bottom: 0px;">Embedded SW Design and Validation Technology for MPSoC</p><p style="margin-bottom: 0px;">A Study on Source Technology of system SW for Super Mobile Implementation</p><p style="margin-bottom: 0px;">Context-based SW reuse</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">Model-based Low Power Design Techniques for Robot Applications</p><p style="margin-bottom: 0px;">Energy efficiency guarantee techniques of smartphone embedded SW</p><p style="margin-bottom: 0px;">Code refactoring techniques to support low power</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">Interaction Detection Techniques for Safety Critical System</p><p style="margin-bottom: 0px;">Fault prevention tree-based risk detection and resolution techniques</p>',
            '<p style="text-align: right; margin-bottom: 0px;"><b><font color="#104a5a">Dimestions of Software Engineering&nbsp; &nbsp; &nbsp;</font></b><br></p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;"><b>Process</b><span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span><br></p><p style="text-align: right; margin-bottom: 0px;">Software Process Model&nbsp; &nbsp;<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp;&nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Software process improvement&nbsp;&nbsp;<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Quantitative Process Management Techniques<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;"><b>Technology</b><span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Software Modeling<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Software Validation<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Software Adaptation and Application<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;"><br></p><p style="text-align: right; margin-bottom: 0px;"><b>Resources</b><span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Human Resource Management (P-CMM)<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p><p style="text-align: right; margin-bottom: 0px;">Training and mentoring<span style="color: rgb(16, 74, 90); font-weight: 700;">&nbsp; &nbsp; &nbsp;</span></p>',
            '<p style="text-align: left; margin-bottom: 0px;"><b>&nbsp; &nbsp;Energy</b></p><p style="text-align: left; margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; Architecture-Driven Energy Efficient</p><p style="text-align: left; margin-bottom: 0px;">&nbsp; &nbsp; &nbsp; SW Development in Robot Application</p><p style="text-align: left; margin-bottom: 0px;"><br></p><p style="text-align: left; margin-bottom: 0px;">&nbsp;&nbsp;&nbsp;<b>Safety</b></p><p style="text-align: left; margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;&nbsp; Learning-Based Safety Prediction in Cyber-Physical System</p><p style="text-align: left; margin-bottom: 0px;"><br></p><p style="text-align: left; margin-bottom: 0px;">&nbsp;&nbsp;&nbsp;<b>Reuse</b></p><p style="text-align: left; margin-bottom: 0px;">&nbsp; &nbsp;&nbsp;&nbsp; Data Quality-Based Reuse Patterns for&nbsp;</p><p style="text-align: left; margin-bottom: 0px;">&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Big Data Analysis in Medical Domains</p>',
        ]
left_right_check = [False, True, False]
order = [3,2,1]
idx = 0
for i in titles:
    li = [i, 'image/research/' + file_names[idx], contents[int(file_names[idx][0:1])], left_right_check[idx], order[idx]]
    idx += 1
    
    cur.execute('insert into research (title, img, content, left_right_check, order) values(?,?,?,?,?)', li)
    con.commit()
    
con.close()
