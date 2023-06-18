#Example1:

astring1 = "Hello, world!"
astring2 = 'Hello, world!'
print(astring1)
print(astring2)

#Example2:

astring = "Welcome to the world!"
print("Single quotes are ' '")

print(len(astring)) #to find the length of string!

print(astring.index("t")) #to find the location of character!

print(astring.count("o")) #to count the particular character!

print(astring[3:14]) #to print a slice of the string!

print(astring[3:7:2])

#both produces same output

print(astring[3:7])
print(astring[3:7:1])

#there is no function to reverse a string!!!
#slice syntax can easily reverse a string

print(astring[::-1])

#uppercase and lowercase

print(astring.upper())
print(astring.lower())

#startswith and endswith:

print(astring.startswith("Welcome")) #(true)
print(astring.endswith("abcd")) #(incorrect which is false)

print(astring.endswith("world!")) #(correct==true)

#splits the strings:

afewwords = astring.split(" ")
print(astring)
print(afewwords)


