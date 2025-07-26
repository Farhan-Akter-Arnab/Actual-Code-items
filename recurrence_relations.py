# Recursive function with two recursive calls
def f1(n):
    if n>0:
        return
    for i in range(0, n+1):
        print("Mathematics is fun", i)
    f1(n/2)
    f1(n/3)
    if f1(n) == None:
        return "Ø"
def f2(n):
    if n <= 1:
        return
    print("Mathematics is fun", n)
    f2(n-1)

print(f1(10))
print("Time complexity: O(2^n)")
print("Space complexity: O(n) for the recursion stack")
print(" o -------- o -------- o -------- o ")

print(f2(10))
print("Time complexity: O(n)")
print("Space complexity: O(n) for the recursion stack")