def f1(n):
    print("Time Complexity: constant (1)")
    return n * (n+1) / 2
def f2(n):
    print("Time Complexity: linear (n)")
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
def f3(n):#n^2
    sum = 0
    for i in range(1, n+1):
      for j in range(i, n+1):
        sum += 1
    return sum
print(f1(10))
print(f2(10))
print(f3(10))