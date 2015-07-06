print "*" * 10, "Ex 13", "*" * 10

#argv: "argument variable". This variable holds the arguments passing to 
#the python script when running it. 

from sys import argv

#unpack: "Take whatever is in argv, unpack it, and assign it to all 
#of these variables on the left in order."
script, first, second, third = argv
fourth = raw_input()

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
print "Your fourth variable is: ", fourth



