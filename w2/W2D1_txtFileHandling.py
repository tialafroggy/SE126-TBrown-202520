#W2D1 - Text File Handling - Introduction

# Step 1: Import the csv (comma separated value) library.

import csv

total_records = 0 #total number of records (rows) in the file.

#connecting to the fie's path - switch \ to /
#-----------connected to file----------------------

print(f"{'NAME':10}{'NUM':3} {'COLOR'}")
print("----------------------------------")
with open("txtFiles\simple.csv") as csvfile:
    #indent 1 level!


    #allow processor to read the file data.
    file = csv.reader(csvfile)

    #loop through every record(row) in the file.
    for record in file:

        #add +1 to total_records.
        total_records += 1

        #print(record) #the list view of each record (row.) 

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:5}\t{number:3}\t{color.title()}")
print("----------------------------------")
#-----------disconnected from the file-----------------------
print(f"\nTOTAL RECORDS: {total_records}")