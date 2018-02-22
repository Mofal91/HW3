#Mohamed Faliq
#pyBank
import os
import csv
import pandas

count = 0
total=0
x=1
Delta=[]
averageTotal=0

f=open("HW3OUTPUT.txt","w")
csvpath=os.path.join('..','python','HW3.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data = pandas.read_csv("HW3.csv",header=0)
    col_a=list(data.Revenue)
    col_b=list(data.Date)
    next(csvreader)
  #-----------------------------------------#
    for row in csvreader:
            count=count+1
        
    print("total Months:" , count)
    f.write("total Months: "+str(count)+"\n")
 #------------------------------------------

    for i in range(len(col_a)):
            total+=col_a[i]
    print("Total Revenue:$",total)
    f.write("Total Revenue:$"+str(total)+"\n")
#-------------------------------------------

    for j in range(len(col_a)-1):
    
            delta1=(col_a[j+1]-(col_a[j]))
            Delta.append(delta1)
            averageTotal+=Delta[j]
            a= (averageTotal)/(count-1)
            
    print("average Change over whole year: ","$",a)
    f.write("average Change over the whole year: "+"$"+str(a)+"\n")
    
    mx=max(Delta)
    mn=min(Delta)
    mx1=Delta.index(mx)
    mn1=Delta.index(mn)
    print("Month of Greatest increase:",col_b[mx1+1],"$", mx)
    f.write("Month of Greatest increase: "+str(col_b[mx1+1]+"----$"+ str(mx))+"\n")
    print("Month of Greatest Decrease: ",col_b[mn1+1],"$", mn)
    f.write("Month of Greatest Decrease: "+ str(col_b[mn1+1])+"----$"+ str(mn))
    
#-------------------------------------------
f.close()

        
