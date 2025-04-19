class pair_elements:
    def twoSum(self, nums, target):
        # Create an Empty Dictionary
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter sum for which you want to make this search: "))
print("index1 = %d, index2 = %d" % pair_elements().twoSum((8, 10, 16, 20, 24, 30, 32, 40, 48, 50, 56, 60, 64, 70, 72, 80, 88, 90, 96, 100), value))