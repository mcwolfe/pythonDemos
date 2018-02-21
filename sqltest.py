from sqlite3 import *


conn = connect('sample7.db')


curs = conn.cursor()

curs.execute('''create table item (id integer primary key, itemno text unique, scancode text, descr text, price real)''')

curs.execute("insert into item values\
            (NULL,0001,32187645,'Milk',2.50)")
curs.execute("insert into item values\
            (NULL,0002,45321876,'Beer',4.50)")
curs.execute("insert into item values\
            (NULL,0003,18764532,'Bread',1.50)")
#conn.commit()


conn2 = connect('sample7.db')
curs2 = conn2.cursor();


curs2.execute("select * from item")
for row in curs2:
	print row
