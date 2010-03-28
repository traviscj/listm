#!/usr/bin/python

# listm, by traviscj
# listmcli - a listm client library.

import cmd, sys
from listm import listm

class listm_helper(listm):
	def __init__(self, dbFile):
		listm.__init__(self,dbFile)
	def printList(self, headItem=1,levels=-1):
		itemsToPrint = self.itemslist(headItem,levels)
		for row in itemsToPrint:
			try:
				print "%d: %s"%(row[0],row[3])
			except:
				pass
				print "Weird output. Row is: [%s]" %(row)
	def otherfunc(self):
		pass

class listmcli(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = 'listm> '
		self.listm = listm_helper('/Users/tjohnson/.listm/working')
		self.listm_head = 1
	def do_hello(self, arg):
		print "hello again", arg, "!"
	def help_hello(self):
		print "syntax: hello [message]"
		print " -- prints a hello message"
	
	def do_list(self,arg):
		head = arg.split(" ")[0]
		if head == "": head=self.listm_head
		self.listm.printList(head,-1)
	do_ls = do_list

	def do_remove(self,arg):
		arglist = arg.split(" ")
		for item_to_remove in arglist:
			print "will remove item ", item_to_remove
			print "which returns: ", self.listm.itemslist(item_to_remove)
			self.listm.delitem(item_to_remove)
	do_rm = do_remove

	def do_new(self,arg):
		if arg != "":
			self.listm.additem(arg,self.listm_head)
		else:
			print "please give me a new command, sir!"
	do_n = do_new

	def do_rehead(self,arg):
		new_head = arg.split(" ")[0]
		if new_head == "":
			self.listm_head = 1
		else:
			self.listm_head = new_head
	do_cd = do_rehead
	def do_changepar(self,arg):
		argList = arg.split(" ")
		itemNumber = argList[0]
		itemNewParent = argList[1]
		self.listm.changepar(itemNumber, itemNewParent)
	do_mv = do_changepar
	def do_quit(self,arg):
		sys.exit(1)
	def help_quit(self):
		print "syntax quit"
		print "-- terminates the application"
	do_q = do_quit
	help_q = help_quit

cli = listmcli()
cli.cmdloop()
