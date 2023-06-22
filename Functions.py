##FUNCTIONS##

def my_function():
    print("Hello From My Function!")
my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
my_function_with_args("Tanu","a great year!")

def sum_two_numbers(a, b):
        return a + b
x = sum_two_numbers(1,2)
print(x)

#output
'''
Hello From My Function!
Hello, Tanu , From My Function!, I wish you a great year!
3
''
