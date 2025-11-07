class Data:
    def __init__(self, value, index, count=0):
        self.value = value
        self.index = index
        self.count = count
def sortByFrequencyAndIndex(arr):
    if arr is None or len(arr) < 2:
        return
    hm = {}
    # Count frequencies and store first occurrence index
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)).count += 1
    values = [*hm.values()]
    values.sort(key=lambda x: (-x.count, x.index))
    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1
if __name__ == "__main__":
    arr = [3, 3, 1, 1, 1, 8, 3, 6, 1, 7, 8, 8]
    print("Original array: ", arr)
    sortByFrequencyAndIndex(arr)
    print("Sorted: ", arr)