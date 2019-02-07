import time
import random

#costs
BAL = 200

costs = {"FOOD" : 10, "WAGON" : 45, "MEDICINE" : 15, "WEAPONS" : 40, "LIVING" : 35}

#Paths
PATHS = 3

#amounts
amounts = {"FOOD" : 5, "WAGON SUPPLIES" : 0, "MEDICINE" : 1, "WEAPONS" : 1, "LIVING" : 0}

#party
party = []

def printStr(string):
  for index in range(len(string)):
    print(string[index], end = "")
    time.sleep(0.03)
  
  print("")
  time.sleep(0.4)
  #input()
  
def handler():
  for m in len(members):
    if members.get(m).isDiseased():
      members.get(m).Hp -= 1

def playTurn():
  path = random.randint(0, PATHS + 2)
  print(path)
  
  if path == 0:
    
    printStr("Bandits are attacking...")
    time.sleep(1)
    
    bandits = random.randint(1, 10);
    foodLost = random.randint(1, amounts.get("FOOD")) - amounts.get("WEAPONS")
    
    if foodLost <= 0:
      foodLost = 0
    
    key = amounts.get("FOOD")
    for k in amounts.keys():
      if k == key:
        amounts.items()[k] -= foodLost
        if (amounts.items()[k] <= 0): 
          amounts.items()[k] = 0
    
    printStr("You lost " + str(foodLost) + " food!")
  elif path == 1:
    if len(members) != 0:
      disease = random.randint(1, len(members))
      members.get(disease).setDiseased(True)
    else:
      player.setDiseased(True)
      
    #Add name & info
    printStr("A member has become diseased!")
      
  else:
    printStr("You travel without impairment...")
    
  handler()
    
  input("Next turn...")
    
class Member:
  
  def __init__(self, name):
  
    diseased = False
    dead = False
    Hp = 10
    hunger = 0
    self.name = name
    
  def setDiseased(self, bool):
    diseased = bool
    
  def isDiseased(self):
    return diseased
    
#player
player = Member("Player")
    
printStr("Welcome Traveller...")
printStr("You are about to embark on the most dangerous trek of your life...")
printStr("Get Ready!")
printStr("First, you'll need to buy some supplies...")
input()

print(
  "---------- -------------------- -------------- ------------- ------------" + "\n" +
  "|Food: 10| |Wagon Supplies: 45| |Medicine: 15| |Weapons: 40| |Living: 35|" + "\n" +
  "---------- -------------------- -------------- ------------- ------------")

while True:
  
  printStr("Your current balance is: " + str(BAL))
  choice = input(
    "Enter the supply you want by putting in the title or nothing to end:")
  
  if choice.upper() in costs and BAL > 0:
    BAL -= costs.get(choice.upper())
    key = amounts.get(choice.upper())
    for k in amounts.keys():
      if k == key:
        amounts[k] += 1
  elif choice.upper() == "" or choice.upper() == " ":
    break;
  elif BAL <= 0:
    printStr("Out of money...")
    break;
  else:
    printStr("Didn't quite get that...")
 
printStr("Great, now that you are fully supplied, you can set off on your adventure.")
input()
printStr("But first I'll need to know what kinds of people you'll be travelling with...")

members = {}
key = -1

while True:
  
  key += 1
  
  member = input("Enter the name of the member of your party here or nothing to end:")
  if member != "" and member != " ":
    members[key] = Member(member)
  else:
    break

'''
for x in range(len(members)):
  members.get(x).__init__();
'''

if len(members) < 1:
  printStr("Travelling alone I see... Be careful")
else:
  printStr("A fine party you have there...")
  
printStr("Now you are prepared, I must warn you, this adventure will contain many dangers...")
printStr("Disease, starvation, thieves, and savage indians line the path...")
printStr("Be wary...")
printStr("Good Luck")

turn = 1
TURNS = 5

while turn <= TURNS:
  playTurn()
  
  
  
  
  
  
  
