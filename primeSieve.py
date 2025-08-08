def Sieve_of_Eratosthenes(n):
    prime = [True for i in range(n+1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):
            for i in range(currentNumber * currentNumber, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p, end=' , ')
n = int(input("Enter number to find all prime numbers less than or equal to the number : "))
Sieve_of_Eratosthenes(n)