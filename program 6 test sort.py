import csv
import operator

sample = open('show_channel.csv','r')

csv1 = csv.reader(sample,delmiter=',')

sort = sorted(csv1,key=operator.itemgetter(0))

for eachline in sort:
    print(eachline)
    
