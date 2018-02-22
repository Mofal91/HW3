import os
import csv
import pandas
from collections import Counter


count =0
candidates=[]
percent=[]


f=open("PYPOLLOUTPUT.txt","w")
csvpath=os.path.join('..','Python','electiondata1.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = pandas.read_csv("electiondata1.csv",header=0)
    
    col_c=list(data.Candidate)
    c=Counter(col_c)   
    next(csvreader)
    
    #-----------------------------------------------------------#
    
    for row in csvreader:
            count=count+1
        
    print("total votes:" , count)
    f.write("total Months: "+str(count)+"\n")
    #-----------------------------------------------------------#
    
    for i in range(len(col_c)-1):
        if col_c[i] not in candidates:
            candidates.append(col_c[i])
     #-----------------------------------------------------------#
        
    for key in c.keys():
        value = c[key]
        print(key,'----',value,"---- %",(value/count)*100)
        f.write(str(key)+'----'+str(value)+"---- %"+str((value/count)*100))
    #-----------------------------------------------------------#
    
    mx=max(c)
    print("Winner: ",mx)
    f.write("\n"+"Winner: "+mx)
    f.close()
        
        
    


