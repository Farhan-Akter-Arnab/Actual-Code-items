#set operations

my_set = {1,2,3}
print(my_set)

#set of mixed datatypes
my_set = {1.0, "Mathematics", (1,2,3)}
print(my_set)

#set cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)

#we can make set from a list
my_set = set([1,2,3,2])
print(my_set, "\n")

#remove a number from a set
num_set = set([0,1,3,4,5])
print("Original set: ")
print(num_set)
num_set.pop()
print("After removing the first element from the said set: ")
print(num_set, "\n")