def itemPrice(barcode):
    li = []
    
    # Iterate through each barcode to find the maximum digit
    for i in barcode:
        n = ord(i)
        maxi = 0
        
        # Find the maximum digit in the barcode number
        while n > 0:
            if n % 10 > maxi:
                maxi = n % 10
            n = n // 10
        
        # Append the maximum digit to the list
        li.append(maxi)
    
    print("The maximum digits from the barcodes are: ", li)
    return sum(li)

# Driver code
inp = input("Enter the barcodes: ")
price = itemPrice(inp)
print("The total price of the items is: ", price)