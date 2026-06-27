import heapq
def printJobScheduling(arr):
    n = len(arr)
    '''arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit; we will sort the array based on deadline'''
    arr.sort(key=lambda x: x[1])
    result = []; maxHeap = [] # initialize result and maxHeap
    for i in range(n-1, -1, -1): # calculate slots available between two deadlines
        if i == 0: slots_available = arr[i][1]
        else: slots_available = arr[i][1] - arr[i-1][1]
        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))
        '''include the profit of jobs (as priority), deadline and job_id in maxHeap; note that we are pushing negative profit to make it a maxHeap from a minHeap'''
        while slots_available and maxHeap:
            profit, deadline, job_id = heapq.heappop(maxHeap) # get the job with maximum profit
            slots_available -= 1 # decrease the available slots
            result.append([job_id, deadline]) # include the job in the result array
    # sort the result based on deadline and print the job sequence because jobs included might be shuffled
    result.sort(key=lambda x: x[1])
    for job in result:
        print(job[0], end=' ')
    print()
if __name__ == "__main__":
    arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27], ['d', 1, 25], ['e', 3, 15]]
    print("Following is maximum profit sequence of jobs:")
    printJobScheduling(arr)