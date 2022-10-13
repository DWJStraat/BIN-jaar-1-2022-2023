print("Reboot the computer and try to connect.")
answer1= input("Did that fix the problem?")
if answer1 == "No":
    print("Reboot the router and try to connect.")
    answer2 = input("Did that fix the problem?")
    if answer2 == "No": 
        print("Make sure the cables between the router and modem are plugged in firmly.")     
        answer3 = input("Did that fix the problem?")
        if answer3 == "No":
            print("Move the router to a new location.")
            answer4 = input("Did that fix the problem?")
            if answer4 == "No":
                print('Get a new router.')