#functions 
def running_beginner():
    pass
def running_intermediate():
    pass
#headline
print("Beginner/Intermediate workout selected! Welcome. \n Now select your current status: \n 1: Beginner (I can't run 30') \n 2: Intermediate (I can run 30')")
choice = int(input("Please select you current training status: "))
while True:
    if choice == 1:
        running_beginner()
        break
    elif choice == 2:
        running_intermediate()
        break
    else:
        print("Please select a valid option!!!")