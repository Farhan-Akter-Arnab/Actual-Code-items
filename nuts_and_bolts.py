from typing import List
def partition(arr: List[str], low: int, high: int, pivot: str) -> int:
    i = low; j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]; i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]; j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
def matchPairs (nuts: List[str], bolts: List[str], low: int, high: int) -> None:
    if (low < high):
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])
        matchPairs(nuts, bolts, low, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, high)
if __name__ == "__main__":
    nuts = ['@', '#', '$', '%', '^', '&']; n = len(nuts)
    bolts = ['$', '%', '&', '^', '@', '#']
    matchPairs(nuts, bolts, 0, n - 1)
    print("Matched nuts and bolts are : ")
    for i in range(n):
        print(nuts[i], bolts[i])