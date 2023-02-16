# Initializing string
ini_string = 'abcdef'
 
# Character to find
c = "b"
# printing initial string and character
print("initial_string : ", ini_string, "\ncharacter_to_find : ", c)
 
# Using Naive Method
res = None
for i in range(0, len(ini_string)):
    if ini_string[i] == c:
        res = i + 1
        break
 
if res == None:
    print("No such character available in string")
else:
    print("Character {} is present at {}".format(c, str(res)))