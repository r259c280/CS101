def temperature(l):
    """This function divides temperatures into buckets"""    #Docstring
  
    diction = {} #Default dictionary to store buckets

    for i in range(len(l)): #Addding empty lists for the keys
        key = l[i]/10 * 10
        diction[key] = []
      
    for i in range(len(l)): #Filling the buckets with corresponding values
        key = l[i]/10 * 10
        diction[key].append(l[i])
    print (diction) #Result

l=[10, 11,12,14,1,2,10,23,30,45,20,21,22,23, 60,70,90,92] #input list
temperature(l) # function call
