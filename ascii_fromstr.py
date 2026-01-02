def str_ascii(string):
    li = []
    for i in string:
        ascii_value = ord(i)
        li.append(ascii_value)
    return li
def dec_to_bin(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    if len(binary) < 8:
        return "0" + binary
    else:
        return binary
def str_bin(li):
    for i in range(len(li)):
        li[i] = dec_to_bin(li[i])
    return li
input_str = input("Enter a string: ")
ascii_values = str_ascii(input_str); print("ASCII values:", ascii_values)
binary_values = str_bin(ascii_values); print("Binary values:", binary_values)