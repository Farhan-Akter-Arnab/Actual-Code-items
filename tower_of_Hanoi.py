def Hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    Hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    Hanoi(n - 1, auxiliary, destination, source)
    
n = 8
Hanoi(n, 'A', 'C', 'B')