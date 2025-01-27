# W3D2 - Voting.
# Tshauni Brown
# W3 Lab 3 
# Date: 01/26/2025
# Programming Essentials Using Python, SE126.02
#Project Description: Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.


#VARIABLE DICTIONARY: 

#totalProcessed = total processes completed.
#totalVote = total votes.
#nonEliReg = non eligible to register.
#canVoteNotReg = can vote but isnt registered.
#canVoteDidntVote = can vote but did not.
#I = id number of person.
#age = age of possible voter
#registered = checks if registered
#voted = checks if voted


                      
#NOTES: main notes found in program.

#--------------------------------------------
import csv

id = []
age = []
registered = []
voted = []
totalProcessed = 0
totalVote = 0
nonEliReg = 0
canVoteNotReg = 0
canVoteDidntVote = 0
totalRecords = 0
ageReq = 18

with open("w3/voters_202040.csv") as file:  
    data = csv.reader(file)
    for row in data:
        # Append data from each row into lists.
        id.append(row[0])   
        age.append(int(row[1]))   
        registered.append(row[2])       
        voted.append(row[3])             
        # Add each record to the total.
        totalRecords += 1
    for i in range(totalRecords):
        if(registered[i] == "N"):
            nonEliReg += 1
        if(age[i] >= ageReq and registered[i] == "N"):
            canVoteNotReg += 1
        if(age[i] >= ageReq and voted[i] == "N"):
            canVoteDidntVote += 1
        if(voted[i] == "Y"):
            totalVote += 1
    totalProcessed += 1
    
print("Number of individuals not eligible to register: ",nonEliReg) 
print("Number of individuals who are old enough to vote but have not registered: ",canVoteNotReg)
print("Number of individuals who are eligible to vote but did not vote: ",canVoteDidntVote)
print("Number of individuals who did vote: ",totalVote)
print("Number of records processed: ",totalProcessed)