print "*" * 10, "Ex 10", "*" * 10

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list: 
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#%r prints the raw representation of what you typed. but %s prints it the way you'd like to see it
x = "\"new line\""
print "Split on %s" % x
print "Split on %r" % x

while True: 
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" %i,