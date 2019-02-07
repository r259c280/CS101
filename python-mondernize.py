import sys

#Define function for printf

def printf(format, *args):

    #Define function

    sys.stdout.write(format % args)

   

#Define list 1

mylist = []

#Define list 2

mylist1 = []

#Loop until length

for x in range(5):

       

    #Receive value

    xi = input('Enter player: %d, jersey number: %d ' %x)

    #Add value

    mylist.append(xi)

    #Receive value

    yi = input('Enter player: %d, rating: %d '%x)

    #Add value

    mylist1.append(yi)

#Display message

print('ROSTER')

#print list of items

for i,j in zip(mylist, mylist1):

            #Display result

            printf("Jersey number: %d, Rating: %d \n" , i,j)

#Loop infinite

while(1):

    #Display message

    print('a - Add Player \n')

    #Display message

    print('d - Remove Player \n')

    #Display message

    print('u - Update Player rating \n')

    #Display message

    print('r - Output Players above a rating \n')

    #Display message

    print('o - Output roster \n')

    #Display message

    print('q - Quit \n')

    #Display message

    print('Enter your choice')

    #Store choice from user

    c = raw_input("Enter a choice :")

    #If choice is to quit

    if(c=='q'):

        #Break from loop

        break;

    if(c=='o'):

        #Display message

        print('ROSTER')

       

        #print list of items

        for i,j in zip(mylist, mylist1):

            #Display result

            printf("Jersey number: %d, Rating: %d \n" , i,j)
