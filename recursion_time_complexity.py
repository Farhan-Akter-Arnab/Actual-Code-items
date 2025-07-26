def prints(n):
    if n<=0:
        return
    print("Mathematics!")
    prints(n/2)
    prints(n/2)
print(prints(8))
print("Done!")