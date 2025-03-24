tuplex = ("tuple", False, 3.2, 1)
print(tuplex)
print(len(tuplex))
tuplex = (4, 6, 2, 8, 3, 1, 10)
print(tuplex)
tuplex = tuplex + (24, )
print(tuplex)
tuple1 = (50, 10, 60, 50, 10, 70, 50)
print(tuple1.count(50))
print(tuple1.count(10))
print(tuple1.count(60))
print(tuple1.count(70))
print(tuple1.count(80))
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1, 2, 8, 5, 3, 4, 8, 10, 9)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)
_slice = tuplex[5:8]
print(_slice)
_slice = tuplex[:8]
print(_slice)
_slice = tuplex[8:]
print(_slice)