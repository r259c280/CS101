"""
    (1) Prompting user to enter Title for data.
    It is stored in string variable named dataTitle
"""
print("Enter a title for the data:")
dataTitle=input()
print("You entered:",dataTitle)
print()
"""
    (2) Prompting user for the headers of the two columns of a table.
    First header is stored in string variable named header1.
    Second header is stored in string variable named header2.
"""
print("Enter the column 1 header:")
header1=input()
print("You entered:",header1)
print()
print("Enter the column 2 header:")
header2=input()
print("You entered:",header2)
print()


"""
    Now creating two list's named dataString[] and dataInteger[] respectively.
    dataString will store data string 
"""
dataString=[]
dataInteger=[]

while True:
    """
        This while loop runs until user enters -1.
    """
    print("Enter a data point(-1 to stop input):")
    """
        Whatever user enters, it is stored in string variable named dataPoint.
    """
    dataPoint=input()
    if dataPoint=="-1":
        """
            If dataPoint is -1 then we terminate the loop 
        """
        break
    """
        commaCount is integer variable that stores count of commas in string dataPoint.
    """
    commaCount=dataPoint.count(',')
    if commaCount==0:
        """
            If there are 0 commas then an error message is printed.
        """
        print("Error: No comma in string.")
        print("\nEnter a valid data point:")
    elif commaCount>1:
        """
            If there are more then 1 commas then an error message is printed.
        """
        print("Error: Too many commas in input.")
        print("\nEnter a valid data point:")
    else:
        """
            Here using split() function we create a string list named data.
            Mostly it has only two elements one at data[0] and another at data[1].
        """
        data=dataPoint.split(',')
        data[0]=data[0].lstrip() #"""lstrip remove spaces from front os the string"""
        data[1]=data[1].lstrip()
        """
            Now at index 1 i.e data[1] has to be integer, So below
            we check if that is the case or not.
        """
        if data[1].isdigit():
            """
                If data[1] is integer then we print respective data.
                And add the elements into respective list's i.e data[0] into dataString[]
                and data[1] into dataInteger[]
            """
            print("Data string:",data[0])
            print("Data integer:",data[1])
            dataString.append(data[0])
            dataInteger.append(data[1])
        else:
            """
                Here is data[1] is like "nine" then an error message is printed.
            """
            print("Error: Comma not followed by an integer.")
            print("\nEnter a valid data point:")



"""
    Now below just printed data is done.
"""
print(dataTitle.rjust(33))



width1 = 20
print("{:<{width}} | {:<{width}}".format(header1, header2, width=width1))
print("--------------------------------------------------------------")
for i in range(len(dataString)):
    print("{:<{width}} | {:<{width}}".format(dataString[i],dataInteger[i], width=width1))



print("\n\n\n\n____________________Histogram format____________________")
for i in range(len(dataString)):
    print(dataString[i].rjust(20),end=" ")
    val=int(dataInteger[i])
    for j in range(val):
        print("*",end="")
    print()
