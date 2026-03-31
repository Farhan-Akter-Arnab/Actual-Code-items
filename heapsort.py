import heapq

def sortArrayInDescendingOrder(arr):
    minHeap = []
    
    for num in arr:
        heapq.heappush(minHeap, num)
    result = []
    
    while minHeap:
        top = heapq.heappop(minHeap)
        result.insert(0, top)
    
    return result

if __name__ == "__main__":
    
    arr = [4, 6, 3, 2, 9]
    result = sortArrayInDescendingOrder(arr)
    
    for num in result:
        print(num, end=" ")
    
    print()