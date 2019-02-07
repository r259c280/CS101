str = "this is a sample string"
print(str[5:10])
print(str.capitalize())
if str.endswith('!'):
    print("It does not endw with !")
else:
    print("It ends with !")
  
print("There are ",str.count('n'), " n's")
first_index = str.index(' ')
print("First index of space is",first_index)
print("Second index of space is",str.index(' ',first_index+1))
print("Lower Cased: ",str.lower())
print("Upper Cased: ",str.upper())
print("With leet speak it is : ",str.replace("e", "3"))
print("With title it is : ",str.title())
