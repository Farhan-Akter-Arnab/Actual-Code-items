class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
def fractional_knapsack(W, arr):
    arr.sort(key = lambda x: (x.profit / x.weight), reverse = True)
    finalvalue = 0.0
    for item in arr:
        if item.weight <= W:
            finalvalue += item.profit
            W -= item.weight
        else:
            finalvalue += item.profit * W / item.weight
            break
    return finalvalue
# Example usage:
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    max_profit = fractional_knapsack(W, arr)
    if W <= 1000:
        print(f"Maximum profit in Knapsack = {max_profit}")