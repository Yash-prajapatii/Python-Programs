##CONDITIONS##

x = 5
print(x == 5)
print(x == 4)
print(x < 6)

#Boolean operators:

name = "Ankur"
age = 23
if name== "Ankur" and age == 23:
    print("Your name is Ankur, and you are also 23 years old.")

if name == "Ankur" or name == "Anil":
    print("Your name is either Ankur or Anil.")

#The "in" operator:

name = "GG"
if name in["GG","VK","Steve"]:
    print("Your name is either GG or VK or Steve.")

# "if" statement using code blocks:
'''
statement = False
statement2 = True
if statement is True:
    pass
elif statement2 is True:
    pass
else:
    pass
'''

#Example:

x = 5
if x == 5:
    print("x equals five!")
else:
    print("x does not equal to five.")

#The "is" operator:

x = [11,22,33]
y = [11,22,33]
print(x == y)
print(x is y)

#The "not" operator:

print(not False)
print((not False) == (False))
