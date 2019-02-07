def ifValidInt(n):
    for ch in n:
        x = ord(ch)       
        if(x < 48 or x > 57):
            return False           
    return True
try:
    n = input('Enter an Integer : \n')
    if(ifValidInt(n)):
        print('Thanx for entering',n)
    else:
        raise Exception('')
except Exception:
    print('You did not enter an integer')
