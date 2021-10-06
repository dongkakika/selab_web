import sqlite3
import codecs
import os

### Main ###
con = sqlite3.connect('../../db.sqlite3')
cur = con.cursor()

titles = ['Our Main Research Areas.', 'Dimestions of Software Engineering']
file_names = os.listdir('../../media/image/research/')
contents = ['Embedded SW Design and Validation Technology for MPSoC\nA Study on Source Technology of system SW for Super Mobile Implementation\nContext-based SW reuse\n\nModel-based Low Power Design Techniques for Robot Applications\nEnergy efficiency guarantee techniques of smartphone embedded SW\nCode refactoring techniques to support low power\n\nInteraction Detection Techniques for Safety Critical System\nFault prevention tree-based risk detection and resolution techniques', 'Process\nSoftware Process Model\nSoftware process improvement\nQuantitative Process Management Techniques\n\nTechnology\nSoftware Modeling\nSoftware Validation\nSoftware Adaptation and Application\n\nResources\nHuman Resource Management (P-CMM)\nTraining and mentoring']
left_right_check = [True, False]
idx = 0
for i in titles:
    li = [i, 'image/research/' + file_names[idx], contents[int(file_names[idx][0:1])], left_right_check[idx]]
    idx += 1
    
    cur.execute('insert into research (title, img, content, left_right_check) values(?,?,?,?)', li)
    con.commit()
    
con.close()
