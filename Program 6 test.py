##CS 101
##Program 6
##Ryan Charles
##rwcxp2@mail.umkc.edu
##
##PROBLEM:           Been asked to create a TV Streaming services list.
##                   
##                   
##                   
##           
##ALGORITHM:  
##                1. Create importing classes
##                2. Create Menus
##                3. Define services
##
##ERROR HANDLING:    None.
##
##OTHER COMMENTS:    None.  
##
############################################################################
import csv
Q = quit
def main():
    choice ='True'
    while choice =='True':
        print("                         Streaming Service Comparison")
        print("1. Get Price per channel for all services.")
        print("2. Get weighted comparison for user file.")
        print("Q. Quit")

        choice = input ("")

        if choice == "1":
            print("Getting Price per channel for all services.")
            with open('providers.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                        print(line[0])
                        print(line[2])
                        
        elif choice == "2":
            usercsv = int(input("Enter the name of user csv "))
            print(usercsv)
        elif choice == "Q":
            print("Exiting program")
        else:
            print("I don't understand your choice.")
main()
