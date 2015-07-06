print "*" * 10, "Ex 8", "*" * 10
formatter = "%r %r %r %r"
print formatter %(1, 2, 3,4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
"I had one.", 
"I had two.", 
"I didn't have three.", 
"I had four.")