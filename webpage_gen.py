
import listmcli

lm = listmcli.listmcli('/Users/tjohnson/.listm/working');

def listprint():
	for listClass in lm.itemslist(3,1):		## for each class
		name = listClass[3]
		print("<div class='third'><h1> %s </h1><ul>"%name)
		for assignment in lm.itemslist(listClass[0],1): ## for each homework
			problemList = "<ul>"
			for problem in lm.itemslist(assignment[0],1):
				problemStyle = ""
				if "done" in problem[4]:
					problemStyle = "class=\"done\""

				problemList += "<li %s>%s</li>" %(problemStyle, problem[3])
			problemList += "</ul>"
			print("<li>%s %s</li>"%(assignment[3],problemList));
		print("</ul></div>")

print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
		"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">  
		<head>
		<title>travis's GRADUATE todo list</title>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
		<style type="text/css">
		.half {
				width: 49%;
					float: left;
		}
		.third {
				width: 24%;
					float: left;
		}
		h1 {
				text-align: center;
		}
		.done {
				text-decoration: line-through;
		}
		</style>
		</head>
		<body>
		""")
listprint()
print("""</body>
		</html>
		""")
