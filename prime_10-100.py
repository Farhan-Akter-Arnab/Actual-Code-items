def Sieve(m,n):
    prime = [True for i in range(n+1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):
            for i in range(currentNumber * currentNumber, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    prime[0] = False
    prime[1] = False
    for p in range(m, n + 1):
        if prime[p]:
            print(p, end=' , ')
print("\nPrime numbers between 10 and 100 are: ")
Sieve(10, 100)
print("\n")