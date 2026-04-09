#functions
def beginner_workout():
    print("Beginner workout selected: ")
def advanced_workout():
    print("Advanced workout selected: ")
def gym_workout():
    print("Gym workout selected: ")

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