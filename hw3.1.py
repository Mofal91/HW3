import os
import csv
import pandas
count =0


f=open("PYPOLLOUTPUT","w")
csvpath=os.path.join('..','RUHW','PyPoll','HW3','electiondata1.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = pandas.read_csv("HW3.csv",header=0)
    col_a=list(data.Revenue)
    col_b=list(data.Date)
    next(csvreader)
    
    #-----------------------------------------------------------#
    
    for row in csvreader:
            count=count+1
        
    print("total votes:" , count)
    f.write("total Months: "+str(count)+"\n")
    
    f.close()

