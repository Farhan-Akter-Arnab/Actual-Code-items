numbers1 = [6,8,10]
numbers2 = [12,16,20]
result = map(lambda a, b: a + b, numbers1,numbers2)
print("Addition of two lists")
print(list(result))

nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)