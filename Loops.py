###LOOPS###

#for loop:

primes = [2,3,5,7]
for prime in primes:
    print(prime)
#output
'''
2
3
5
7
'''

for A in range(5):
    print(A)
#output
'''
0
1
2
3
4
'''
    
for x in range(1,9):
    print(x)
#output
'''
1
2
3
4
5
6
7
8
'''

for x in range(1,9,2):
    print(x)
#output
'''
1
3
5
7
'''

#while loop:

A = 0
while A > 5:
    print(A)
    A+=1
#output
'''
0
1
2
3
4
'''

#break and continue statements:

b = 50
while True:
    print(b)
    b += 1
    if b >= 55:
        break
#output
'''
50
51
52
53
54
'''

for x in range(25):
    if x % 2 == 0:
        continue
    print(x)
#output
'''
1
3
5
7
9
11
13
15
17
19
21
23
'''

#can we use "else" clause for loops?

X = 0
while (X < 7):
    print(X)
    X += 1
else:
    print("X value reached %d" %(X))
#output
'''
0
1
2
3
4
5
6
X value reached 7
'''

for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail of condition")
#output
'''
1
2
3
4
'''
