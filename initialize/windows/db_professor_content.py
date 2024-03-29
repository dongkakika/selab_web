import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

li = ['<p style="margin-bottom: 0px;"><b>Major</b>: Software Engineering, Software Modeling and Verification<br></p><p style="margin-bottom: 0px;"><b>Affiliation</b>: College of Electronic Information, Chungbuk National University<br></p><p style="margin-bottom: 0px;"><b>E-mail</b>: jehong@chungbuk.ac.kr</p><p style="margin-bottom: 0px;"><b>Contact</b>: +82 43 261 2261<br></p><p style="margin-bottom: 0px;"><b>Office</b>: S4-1, Office No. 320, Computer Science Department<br></p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;"><b>Academic Ability and Work Experience</b><br></p><p style="margin-bottom: 0px;">2020 - Present, the dean of the software department at CBNU</p><p style="margin-bottom: 0px;">2016 - Present, Director of Computer Information Services at CBNU</p><p style="margin-bottom: 0px;">2014 - Present, SSEF member</p><p style="margin-bottom: 0px;">2012 - Present, Director of the Software Engineering Society of the Korean Society of Information Science</p><p style="margin-bottom: 0px;">2011 - Present, Permanent Director of the Korea Small and Medium Business Convergence Society</p><p style="margin-bottom: 0px;">2004 - Present, Adviser of the Korea Defense Research Institute\'s Information Center</p><p style="margin-bottom: 0px;">2004 - Present, Professor of Computer Engineering at CBNU</p><p style="margin-bottom: 0px;">2001 - Doctor of Computer Science, KAIST.</p><p style="margin-bottom: 0px;"><br></p><p style="margin-bottom: 0px;">2010 ~ 2013 - App Center Director of Chungbuk National University</p><p style="margin-bottom: 0px;">2002 ~ 2004 - Director &amp; Senior Consultant, Solution Link Technology Lab</p><p style="margin-bottom: 0px;">2002 ~ 2003 - Committee member preparing national technical guidance and technical cooperation guidance of the Ministry of Science and Technology</p><p style="margin-bottom: 0px;">2001 ~ 2002 - Defense Science Laboratory</p><div><br></div>']

cur.execute('insert into professor (content) values(?)', li)
con.commit()

con.close()
