# Code for determining the number of ways to climb stairs with steps of 1 or 2.
def ways(stairs):
    # Check base case
    if stairs < 0:
        return 0
    
    # If no stairs left, just return 1 as we reach the top
    if stairs == 0:
        return 1
    
    twosteps = 0
    onestep = 0
    
    # We can jump 2 steps only if there are 2 or more stairs left
    if stairs >= 2:
        twosteps = ways(stairs - 2)
    # We can always jump 1 step if there is at least 1 stair left
    onestep = ways(stairs - 1)
    # Return total ways
    return twosteps + onestep

stairs = int(input("Enter the number of stair-steps: "))

print("Number of ways to climb : ", ways(stairs))