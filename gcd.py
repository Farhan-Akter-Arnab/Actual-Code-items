n_large = int(input("Enter the largest number: "))
n_small = int(input("Enter the smallest number: "))

while n_small:
    n_store = n_small
    n_small = n_large % n_small
    n_large = n_store
print("HCF is = ", n_large)