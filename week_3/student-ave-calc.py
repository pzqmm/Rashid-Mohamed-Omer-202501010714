choice = "y"

# Loop to repeat the program if the user chooses 'y'
while choice == "y":

    # Ask the user to enter three quiz marks
    quiz_1 = int(input("Enter Quiz 1 mark: "))
    quiz_2 = int(input("Enter Quiz 2 mark: "))
    quiz_3 = int(input("Enter Quiz 3 mark: "))

    # Calculate the average mark
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Check if the average is 50 or above to determine pass or fail
    if average >= 50:
        print("Student passes")
    else:
        print("Student fails")

    # Allow another student's marks to be entered
    choice = input("Continue? Select Y/N: ")

print("Program Ended")