#functions 
def running_beginner():
    week = input("Is this your first week of training? (y/n) ")
    while True:
        if week == "y" or "Y":
            workout_stats = []
            days_xweek = int(input("How many days you can train per week? "))
            hours_xweek = int(input("How many hours you can train per week? "))
            workout_stats.append(days_xweek, hours_xweek)
            hours_xday = workout_stats[1] / workout_stats[2]
            
            break
        elif week == "n" or "N":
            break
        else:
            print("Please select a valid option!!!")
    

def running_intermediate():
    pass
#headline
print("Beginner/Intermediate workout selected! Welcome. \n Can you run 30'?")
choice = input("Please select you current training status by typing y o n ")
while True:
    if choice == "y" or "Y":
        running_beginner()
        break
    elif choice == "n" or "N":
        running_intermediate()
        break
    else:
        print("Please select a valid option!!!")