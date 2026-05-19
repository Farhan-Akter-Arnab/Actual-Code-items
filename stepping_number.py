def steppingnumber(n):
    if n < 10:
        return True
    prev_digit = n % 10
    n //= 10
    while n > 0:
        current_digit = n % 10
        if abs(current_digit - prev_digit) != 1:
            return False
        prev_digit = current_digit
        n //= 10
    return True
if __name__ == "__main__":
    input_number = int(input("Enter a number: "))
    if steppingnumber(input_number):
        print(f"{input_number} is a stepping number.")
    else:
        print(f"{input_number} is not a stepping number.")