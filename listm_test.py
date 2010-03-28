
import listmcli

print("trying to initialize")
lm = listmcli.listmcli('/Users/tjohnson/.listm/working');
print("trying to print...")
lm.printList(1,-1)

print("trying an add...")
lm.additem("other stuff to do",2)
lm.additem("call crystal",15)
print ("---")
lm.printList(15,-1)
print ("---")
lm.printList(1,-1)
print("and I'm spent")
