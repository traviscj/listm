#!/usr/bin/python
#
# listm, by traviscj.
# listmc - List Manager Client

#### configuration section ####
databaseFile = '/Users/tjohnson/.listm/example'
#### end configuration section ####

import sqlite3, sys, time
conn = sqlite3.connect(databaseFile)

c = conn.cursor()

if len(sys.argv)==1:
	c.execute("select * from items order by list_index")
	for row in c:
		try:
			print "%d: %s"%(row[0],row[3])
		except:
			print row
elif sys.argv[1]=="ls":
	list = 1;
	if len(sys.argv)==3:
		list = sys.argv[2]
	sql = "select * from items WHERE list_index=?"
	c.execute(sql, (list))
	for row in c:
		try:
			print "%d: %s"%(row[0],row[3])
		except:
			print row
elif sys.argv[1]=="add":
# logic for add
	item = sys.argv[2]
	list = 1
	if len(sys.argv)==4:
		list = sys.argv[3]
	print("will add %s to list %d"%(item,list))
	date = time.localtime()
	datestr = "%s-%s-%s"%(date[0],date[1],date[2])
	ins = (list, datestr, item)
	sql = "insert into items values(NULL, ?, ?, ?)"
	c.execute(sql,ins);
	conn.commit()
else:
	pass

c.close()
