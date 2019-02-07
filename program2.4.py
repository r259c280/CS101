import random
while 1:
    pot = 0
    wager = 0
    guessNo = 0
    # asking the pot money in loop
    # til user enters valid pot value
    while 1:
        try:
            pot = int(input("Enter the amount for your pot : "))
            if pot <= 0:
                print(" Enter a positive number! ")
            else:
                break
        except:
            print("Enter a postive number! ")
    # loop will run until the pot is greater than 0
    while pot > 0:
        #asks for a wager
        while 1:
            try:
                wager = int(input(" Enter the amount to wager "))
                if wager <= 0 or wager > pot:
                    print("Stop trying to cheat the system, enter a valid wager amount!")
                else:
                    break
            except:
                print("Stop trying to cheat the system, enter a valid wager amount!")
        #check range of (1-7)
        while 1:
            guessNo = int(input("Enter a number from (1-6) : "))
            if guessNo not in range(1,7):
                print("I'll repeat myself again...Enter a number from 1 to 6")
            else:
                break
        # rolls dice
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        # adding value of die to list
        li = [dice1, dice2, dice3]
        matchedDice = 0
        # counting the number of matched guess no in die rolled
        for i in li:
            if i == guessNo:
                matchedDice=matchedDice+1
        #print the updated value of pot
        if matchedDice == 0:
            print("You have horrible luck, nothing matched.")
            pot = pot - wager
            print("Updated pot value : " + str(pot))
        elif matchedDice == 1:
            print("One is the lonliest number, but you're still a winner!")
            pot = pot + wager
            print("Updated pot value : " + str(pot))
        elif matchedDice == 2:
            print("Two out of three ain't bad!")
            pot = pot + (wager*2)
            print("Updated pot value : " + str(pot))
        elif matchedDice == 3:
            print("Winner winner chicken dinner, all three matched!")
            pot = pot + (wager*3)
            print("Updated pot value : " + str(pot))
    # if pot value empty ask if user wants to play again
    exitStatus = input("Do you want to play again YES/NO? :")
    if exitStatus.lower() == "n" or exitStatus.lower() == "no":
        break
