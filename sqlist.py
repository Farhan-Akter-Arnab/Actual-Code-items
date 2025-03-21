L = [3, 4, 5, 6, 8, 10, 24, 12, 20, 18, 25, 50, 40, 36, 80, 64, 32, 88, 96, 90, 15, 16, 19, 60]
L2 = []
def square(num):
    return num**2
for i in L:
    sq = square(i)
    L2.append(sq)
print("Original list : ", L)
print("List of their squares : ", L2)