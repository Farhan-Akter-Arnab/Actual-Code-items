# Function to find the largest missing element in a sorted list of distinct non-negative integers
def findLargestMissing(nums):
    left, right = 0, len(nums) - 1
    largest_missing = -1  # Initialize the largest missing number

    while left <= right:
        mid = left + (right - left) // 2
        # If the value at mid is equal to its index, search in the right half
        if nums[mid] == mid:
            left = mid + 1
        else:
            # If there's a mismatch, update the largest missing number
            largest_missing = max(largest_missing, nums[mid] - 1)
            # Search in the left half
            right = mid - 1
    # Check for the largest missing number in the gaps between consecutive elements
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 1:
            largest_missing = max(largest_missing, nums[i] - 1)
    return largest_missing

if __name__ == '__main__':
    nums = [0, 1, 2, 6, 9, 11, 15]
    print('The largest missing element is', findLargestMissing(nums))