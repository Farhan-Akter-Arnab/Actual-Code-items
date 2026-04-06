import heapq
min_heap = []
def min_enqueue(heap, priority, item):
    heapq.heappush(heap, (priority, item))
    print(f"[MinHeap] Inserted: {item} with priority {priority}")
def min_dequeue(heap):
    if len(heap) == 0:
        print("[MinHeap] Heap is empty")
        return None
    priority, item = heapq.heappop(heap)
    print(f"[MinHeap] Removed: {item} with priority {priority}")
    return item
def display_min(heap):
    print("Min Heap contents:")
    for priority, item in heap:
        print(f"Item: {item}, Priority: {priority}")
max_heap = []
def max_enqueue(heap, priority, item):
    heapq.heappush(heap, (-priority, item))
    print(f"[MaxHeap] Inserted: {item} with priority {priority}")
def max_dequeue(heap):
    if len(heap) == 0:
        print("[MaxHeap] Heap is empty")
        return None
    priority, item = heapq.heappop(heap)
    print(f"[MaxHeap] Removed: {item} with priority {-priority}")
    return item
def display_max(heap):
    print("Max Heap contents:")
    for priority, item in heap:
        print(f"Item: {item}, Priority: {-priority}")
min_enqueue(min_heap, 2, "Task B")
min_enqueue(min_heap, 1, "Task A")
min_enqueue(min_heap, 3, "Task C")
display_min(min_heap)
min_dequeue(min_heap)
display_min(min_heap)
max_enqueue(max_heap, 2, "Task B")
max_enqueue(max_heap, 1, "Task A")
max_enqueue(max_heap, 3, "Task C")
display_max(max_heap)
max_dequeue(max_heap)
display_max(max_heap)