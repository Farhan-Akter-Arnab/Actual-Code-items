class MaxHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None] * maxSize
        self.heapSize = 0
    def MaxHeapify(self, i):
        l = self.lChild(i); r = self.rChild(i); largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]: largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]: largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.MaxHeapify(largest)
    def parent(self, i): return (i - 1) // 2
    def lChild(self, i): return 2 * i + 1
    def rChild(self, i): return 2 * i + 2
    def removeMax(self):
        if self.heapSize <= 0: return None
        if self.heapSize == 1: self.heapSize -= 1; return self.arr[0]
        root = self.arr[0]; self.arr[0] = self.arr[self.heapSize - 1]; self.heapSize -= 1; self.MaxHeapify(0)
        return root
    def increaseKey(self, i, newVal):
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]; i = self.parent(i)
    def getMax(self):
        if self.heapSize == 0: return None
        return self.arr[0]
    def curSize(self): return self.heapSize
    def deleteKey(self, i): self.increaseKey(i, float("inf")); self.removeMax()
    def insertKey(self, x):
        if self.heapSize == self.maxSize: print("\nOverflow: Could not insertKey\n"); return
        i = self.heapSize; self.heapSize += 1; self.arr[i] = x
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]; i = self.parent(i)
if __name__ == "__main__":
    h = MaxHeap(15)
    k, i, n = 6, 0, 6
    h.insertKey(1)
    h.insertKey(1)
    h.insertKey(2)
    h.insertKey(3)
    h.insertKey(5)
    h.insertKey(8)
    print("Max value is:", h.getMax())
    print("Current size of heap is:", h.curSize())
    print("Removing max value:", h.removeMax())
    print("Max value is:", h.getMax())
    print("Current size of heap is:", h.curSize())