def print_menu():
    print(                        "Streaming Service Comparison")
    print("1. Get Price per channel for all services.")
    print("2. Get weighted comparison for user file.")
    print("Q. Quit")

loop=True

while loop: ## While loop will keep going until loop is false.
    print_menu() ##Displays menu
    choice = input("Enter your choice 1, 2, or Q]: ")

    if choice==1:
        print("Option 1 has been selected")
        ## Add csv file to import for all services
        ## Add menu options for that.
    elif choice == 2:
        print("Option 2 has been selected")
        ## Add csv file to import for all services
        ## Add menu options for that.
    elif choice==Q:
        ## Add csv file to import for all services
        ## Add menu options for that.
    else:
        #any integer inputs other than values 1, 2, or Q will print an error message.
        int(input("You must choose a value from 1,2,Q")
