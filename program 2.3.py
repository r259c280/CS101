import random
con = 'Y'
while con == 'Y' or con == 'YES': #continue will allow user to quit by entering N or No
    money_pot = int(input("How much money do you have in pot:"))# taking the money present in the pot

while money_pot <= 0: #loop continues until the user enters a positive value
    money_pot = int(inpout("How much money do you have in pot:"))
while money_pot > 0: #continues until user has money in his pot
    wager = int(input("How much money do you want to wager:"))# taking the wager input from user
sel_num = int(input("Select a number to wager on(1-6):"))# number selected by user
while sel_num <= 0 or sel_num >= 7: #continues until valid number is selected by user
    sel_num = int(input("Select a number to wager on(1-6):"))
dice1 = random.randint(1, 6)# generating the number on dice1
dice2 = random.randint(1, 6)# generating the number on dice2
dice3 = random.randint(1, 6)# generating the number on dice3
win = 0# calculate the winnings of the user
if sel_num == dice1:
    win = win + 1
if sel_num == dice2:
    win = win + 1
if sel_num == dice3:
    win = win + 1
money_pot = money_pot - wager + (wager * win)# money left in pot after each round
print("Money left in the pot-" + str(money_pot)
      if con == input('Do you want to play again: ')# when the money pot is 0, the user is prompted to play again
        (True): #continues until the user inputs a valid input
        if con == 'Y'
        or con == 'N'
        or con == 'YES'
        or con == 'NO':
        break con = input('Do you want to play again: ')
