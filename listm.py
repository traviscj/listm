
import sqlite3, sys, time

class listm:
	def __init__(self, dbFile):
		self.dbFile = dbFile
		self.conn = sqlite3.connect(self.dbFile)
		self.c = self.conn.cursor()
	def delitem(self, item_index):
		sql = """ DELETE FROM items
			WHERE item_index=?"""
		self.c.execute(sql, (item_index,))
		self.conn.commit()
	def additem(self, item, parent=1, tags=''):
		date = time.localtime()
		datestr = "%s-%s-%s"%(date[0],date[1],date[2])
		ins = (parent, datestr, item, tags)
		sql = "insert into items values(NULL,?, ?, ?, ?)"
		self.c.execute(sql, ins)
		self.conn.commit()
	def tagitem(self, itemNo, tag):
		sql = """UPDATE items SET tag=? WHERE item_index=?"""
		self.c.execute(sql,(tag,itemNo))
		self.conn.commit()
	def changepar(self,item, toParent):
		sql = """UPDATE items SET item_parent_index=? WHERE item_index=?"""
		self.c.execute(sql,(toParent, item))
		self.conn.commit()
	def itemslist(self, headItem=1, levels=1):
		retList = []
		if levels ==0:
			return []
		param = (headItem, )
		self.c.execute("""
			SELECT * 
			FROM items 
			WHERE item_parent_index=?
			ORDER BY item_parent_index""", param)
		iterList = [i for i in self.c]
		if len(iterList)==0: return []
		for i in iterList:
			retList.append(i)
			#print("trying to descend on item: %s" % (str(i)))
			posToAdd =  self.itemslist(i[0], levels-1)
			#print "WILL APPEND TO RET LIST: %s"%(posToAdd)
			retList+=posToAdd
			#print "NEW RETLIST %s"%(retList)
			#print("pop descent")
		return retList
