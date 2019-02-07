menu = """
Menu
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - quit
"""

def add(roster):
    jersey = int(input("\n Enter player jersey number: "))
    rating = int(input("\n Enter player rating: "))
    roster[jersey] = rating

    print("\n Player has been added successfully \n")

def remove(roster):
    jersey = int(input("\n Enter player jersey number: "))
    if jersey not in roster.keys():
        print("\n\n No player exists with given jersey number.... \n\n")
    else:
        del roster[jersey]
        print("\n Deleted Successfully \n")
def update_r(roster):
    jersey = int(input("\n Enter player jersey number: "))

    if jersey not in roster.keys():
        print("\n\n No player exists with given jersey number.... \n\n")
    else:
        rating = int(input("\n Enter player rating: "))
        roseter[jersey] = rating
        print("\n Updated Successfully \n")

def output_r(roster):
    rating = int(input("Enter a rating:\n"))
    print("ABOVE " + str(rating) + "\n")
    sorterRoster = sorted(roster.keys())
    for jersey in sortedRoster:
        if roster[jersey] > rating:
            print("\nJersey Number: " + str(jersey) + ", Rating: " + str(roster[jersey]))

def main():
    roster = {}
    i = 1

    for i in range(1, 6):
        jersey = int(input("Enter player " + str(i) + "'s jersey number:\n"))
        rating = int(input("Enter player " + str(i) + "'s rating:\n\n"))
        roster[jersey] = rating
    print(output(roster))

    while True:
        print(menu)
        option = input("Choose an option:\n")
        if option == 'a':
            addPlayer(roster)
        elif option == 'd':
            deletePlayer(roster)
        elif option == 'o':
            print(output(roster))
        elif option == 'u':
            updatePlayer(roster)
        elif option == 'r':
            aboveRating(roster)
        elif option == 'q':
            return False

main()
            
