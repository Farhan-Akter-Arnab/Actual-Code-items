class MaxHeap:
    arr = []
    maxSize = 0
    heapSize = 0
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None] * maxSize
        self.heapSize = 0
    def MaxHeapify(self, i):
        l = self.lchild(i)
        r = self.rchild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)
        def parent(self, i):
            return (i - 1) // 2
        def lchild(self, i):
            return 2 * i + 1
        def rchild(self, i):
            return 2 * i + 2
        def removeMax(self):
            if self.heapSize <= 0:
                return None
            if self.heapSize == 1:
                self.heapSize -= 1
                return self.arr[0]
            root = self.arr[0]
            self.arr[0] = self.arr[self.heapSize - 1]
            self.heapSize -= 1
            self.MaxHeapify(0)
            return root
    def increaseKey(self, i, newVal):
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)
    def getMax(self):
        return self.arr[0]
    def curSize(self):
        return self.heapSize
    def deleteKey(self, i):
        self.increaseKey(i, float("inf"))
        self.removeMax()