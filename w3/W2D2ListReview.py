#W3D2 - List Review - 1 Dimensional Lists and Parallel Lists

#This file uses: class_grades.csv



#--IMPORTS-------------------------------------
import csv
#--FUNCTIONS-----------------------------------

#--------------------MAIN EXECUTING CODE-------------------------------------------------------------

total_records = 0

#create an empty list for every potential field.

firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open("txtFiles/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # for every record in the file, do the following.
        #print(f"{rec[0]}\t{rec[1]}\t{rec[2]}\t{rec[3]}\t{rec[4]}")
        
        #fname = rec[0]
        #lname = rec[1]
        #test1 = rec[2]

        #add the record to its corresponding list (1 list per field.)
        #append --> to add to the end.
        firstName.append(rec[0])
        lastName.append(rec[1])

        test1.append(int(rec[2])) #cast as integer for easier math later.
        test2.append(int(rec[2]))
        test3.append(int(rec[2]))
#disconnect from the file -- all file data is retained bc we are using lists.

#create a new list to hold each students test score average.

avg = []

#process the current student data to find and store each students test score avg to the avg list.

for i in range(0, len(test1)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    avg.append(a)
    #or, you could also: avg.append((test1[i] + test2[i] + test3[i]) / 3)
#basic processing - use the 1D parallel lists to print all data to the console.
print(f"\nINDEX: {'#':3} : {"FIRST":10}  {"LAST":10}  {"T1":4}  {"T2":4}  {"T3":4}  {"AVG":4}")
print("---------------------------------------------------------------------------")

for index in range(0, len(firstName)): # len() --> length of collection, returns # of items.
    #index --> key pf the ;ost. allows access to ONE specific value at a time.
    print(f"INDEX: {index:3} : {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}  {avg[index]:3.2f}")
    
print("---------------------------------------------------------------------------")        

#find the current average of class by preocessing the average list data.
total_avg = 0
for i in range(0, len(avg)):
    total_avg += avg[1] # adds each avg calue to the total_avg variable

#calculate the average
class_avg = total_avg / len(avg)
print(f"\nThe CLASS AVERAGE of these {len(avg)} students is: {class_avg:2f}")