###LOOPS###

#for loop:

primes = [2,3,5,7]
for prime in primes:
    print(prime)

for A in range(5):
    print(A)
    
for x in range(1,9):
    print(x)

for x in range(1,9,2):
    print(x)

#while loop:

A = 0
while A > 5:
    print(A)
    A+=1

#break and continue statements:

b = 50
while True:
    print(b)
    b += 1
    if b >= 55:
        break


for x in range(25):
    if x % 2 == 0:
        continue
    print(x)

#can we use "else" clause for loops?

X = 0
while (X < 7):
    print(X)
    X += 1
else:
    print("X value reached %d" %(X))


for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail of condition")
    
