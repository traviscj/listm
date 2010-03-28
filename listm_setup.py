
import sqlite3, os
dbFile = '/Users/tjohnson/.listm/working'
os.unlink(dbFile)
conn = sqlite3.connect(dbFile)
c=conn.cursor()
c.execute("""create table items (
		item_index INTEGER PRIMARY KEY, 
		item_parent_index INTEGER, 
		date TEXT, 
		item TEXT,
		tag TEXT)""")
conn.commit()

c.execute("""insert into items values ( 1,0,'2010-03-05','masterlist','')""")
c.execute("""insert into items values ( 2,1,'2010-03-05','todo list','')""")
c.execute("""insert into items values ( 3,2,'2010-03-05','school todos','')""")
c.execute("""insert into items values ( 4,3,'2010-03-05','esam411-2','')""")
c.execute("""insert into items values ( 5,4,'2010-03-05','final exam','')""")
c.execute("""insert into items values ( 6,3,'2010-03-05','esam420-2','')""")
c.execute("""insert into items values ( 7,6,'2010-03-05','homework 4','')""")
c.execute("""insert into items values ( 8,6,'2010-03-05','final exam','')""")
c.execute("""insert into items values ( 9,3,'2010-03-05','esam421-2','')""")
c.execute("""insert into items values (10,9,'2010-03-05','homework 4','')""")
c.execute("""insert into items values (11,9,'2010-03-05','final exam','')""")
c.execute("""insert into items values (12,3,'2010-03-05','esam448','')""")
c.execute("""insert into items values (13,12,'2010-03-05','show up on tuesday','')""")
c.execute("""insert into items values (14,12,'2010-03-05','mathematician project','')""")
conn.commit()
conn.close()


