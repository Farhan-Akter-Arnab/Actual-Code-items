def calculateprofits(arr, arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]
    return profit
prices = [610, 824, 695, 530, 410, 490, 650, 820]
print("Maximum profit is:", calculateprofits(prices, len(prices)))