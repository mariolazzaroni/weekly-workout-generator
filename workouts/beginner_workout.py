#functions 
def running_beginner():
    week = input("Is this your first week of training? (y/n) ")
    while True:
        if week == "y" or "Y":
            days_xweek = int(input("How many days you can train per week? "))
            hours_xweek = int(input("How many hours you can train per week? "))
            next_week_hours = hours_xweek + 0.10* hours_xweek
            hours_xtraining = next_week_hours / days_xweek
            print("Next week you have to train for ", days_xweek, " days, each training long ", hours_xtraining, " hours")
            break
        elif week == "n" or "N":
            i = 0
            while i < 2:
                workout = []
                workout_stats = int(input("Type Days and hours x week: "))
                workout.append(workout_stats)
                
                
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