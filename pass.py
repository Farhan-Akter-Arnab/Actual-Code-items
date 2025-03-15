for x in range (25):
    if x % 24 == 0:
        print("∅ front: ", x)
    elif x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        print("freeze")
    elif x % 8 == 0:
        print("Empty Front: ", x)
    elif x % 7 == 0:
        pass
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)