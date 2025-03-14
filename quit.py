def shutdown_programme():
    print(exit)
    exit()
n = int(input("Enter the number upto which do you want to continue: "))
p = int(input("Enter the number where do you want to stop: "))
for i in range(n):
    print(i+1)
    if (i+1) == p:
        command = input("Do you want to shutdown? Enter 'yes' or 'no' ").lower()
        if command == 'no':
            print("By shutting down, you would stop at the point you have commanded")
            for i in range(n):
                print(i+1)
        elif command == 'yes':
            shutdown_programme()
        else:
            print("Wrong input")