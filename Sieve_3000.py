a = 3000
for num in range(2, a + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        if str(num) == str(num)[::-1]:
            print(num)