#functions
def beginner_workout():
    pass
def advanced_workout():
    pass
def gym_workout():
    pass

#menu
print("Welcome to the weekly workout generetor: \n 1: Beginner. \n 2: Advanced with race. \n 3: Gym.")

while True:
    choice = int(input("Please select by typing the number: "))
    if choice == 1:
        beginner_workout()
        break
    elif choice == 2:
        advanced_workout()
        break
    elif choice == 3:
        gym_workout()
        break
    else:
        print("Please select a number from 1 to 3!!!")