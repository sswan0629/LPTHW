# %r is for debugging, since it display "raw data". %s is for users to read. 
x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

#print x
#print y

# % r is a formatter character short for repr(). 
print "I said: %r." % x 
print "I also said '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation %hilarious

w = "This is the left side of..."
e = "a string with a right side."

# no space between w and e
print w + e

# a space between w and e
print w, e
