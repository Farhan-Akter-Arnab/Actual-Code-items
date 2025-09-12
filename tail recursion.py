def tail(A,W):
    if (A > W):
        return
    print(A)
    tail(A + 1, W)
a = int(input("Enter the starting number: "))
w = int(input("Enter the ending number: "))
tail(a, w)