def get_value():
    while True:
        try:
            value = int(input("Enter an integer"))
            if value > 0:
                return value
            print("Enter a number > 0")
        except ValueError:
            count = count + 1
            if count >= 3:
                print("Goodbye")
                exit()
            print("Enter a valid number")
while True:
    try:
        file_name = input("Enter the name of the file ==> ")
        fh = open(file_name)

        break
    
    except FileNotFoundError:
        print("Bad file, eneter a real file")
    except IOError:
        print("Could not open that file ")

value =  get_value()

for line in fh:
        try:
            line_value = int(line)
            if line_value >= value:
                print(line_value)
        except ValueError:
            print("Found a bad file line", line)

fh = close()
