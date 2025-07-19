print("\n")
def OnTime(n):
    iteration = 0
    for i in range(1, n+1):
        iteration += 1
    print("When n is ", n, ", Iterations = ", iteration)
OnTime(3 * 10* 8)
OnTime(6 * 10* 24)
OnTime(10 * (10 * 2))
print("\n With every 'n' the time taken and iterations will increase linearly.")