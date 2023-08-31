no = int(input("Enter pocket number:\n"))

if no < 0:
    print("ERROR: number outside range")
elif no == 0:
    print("The pocket is green")
elif no <= 10:
    if no % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif no <= 18:
    if no % 2 != 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif no <= 28:
    if no % 2 == 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
elif no <= 36:
    if no % 2 != 0:
        print("The pocket is black")
    else:
        print("The pocket is red")
else:
    print("ERROR: number outside range")
