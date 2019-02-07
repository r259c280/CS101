
def ask_user():
    """ asks the user for valid input """
    return False

def get_roman():
    """ Gets roman numeral from user """
    while True:
        value = input("Enter a roman numeral ")
        for ch in value:
            if ch not in "IVX":
                print("Entered invalid char ", ch)
                break
        else:
            return value
    
def roman_2_int(roman):
    """ Converts a roman number into an int """
    total = 0
    for char in roman:
        if char == "I":
            total = total + 1
        elif char == "V":
            total = total + 5
        elif char == "X":
            total = toal + 10
    return 4

def int_2_roman(value):
    """ Converts an integer into a roman numberal """
    return "VII"



playing = True
while playing:

    # Roman numeral process
    roman1 = get_roman()
    roman2 = get_roman()

    roman1_int = roman_2_int(roman1)
    roman2_int = roman_2_int(roman2)

    total = roman1_int + roman2_int

    total_roman = int_2_roman(total)

    print(roman1, " + ", roman2, "=", total_roman)
    print("playing the game")


    
    # Ask user to continue
    playing = ask_user()
print("Thanks for playing")
