day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
       "Sunday"]
no = int(input("Enter a number between 1 and 7\n"))
if no <0 or no >7:
    print("ERROR: Not a number between 1 and 7")
else:
    print(day[no-1])