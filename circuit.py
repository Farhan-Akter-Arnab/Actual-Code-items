def circuit(a,b,c):
    m1 = a & b
    m2 = b ^ c
    m3 = b & c
    m4 = m2 & m3
    return m1 | m4
A = int(input("Enter the numerical value of A: "))
B = int(input("Enter the numerical value of B: "))
C = int(input("Enter the numerical value of C: "))
print(circuit(A,B,C))