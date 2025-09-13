def list_length(list):
    if list == []:
        return 0
    else:
        return 1 + list_length(list[1:])

my_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("Length of the list:", list_length(my_list))