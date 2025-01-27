# W3D2 - Text File Handling. Computer Output.
# Tshauni Brown
# W3 Lab 2 Part 2
# Date: 01/26/2025
# Programming Essentials Using Python, SE126.02
#Project Description: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.


#VARIABLE DICTIONARY: 

# computerType = []       # List to store type of computer (Desktop or Laptop)
# manufacturer = []       # List to store manufacturer names
# processor = []          # List to store processor types
# memory = []             # List to store RAM sizes
# diskCapacity = []       # List to store primary disk sizes
# extraDiskCapacity = []  # List to store secondary disk sizes (if applicable)
# diskCount = []          # List to store number of disks
# osVersion = []          # List to store OS version
# manufactureYear = []    # List to store the year the computer was manufactured



                      
#NOTES: main notes found in program.
import csv

# Initialize variables for counting replacements and storing data.
totalRecords = 0
desktopReplace = 0
laptopReplace = 0
osUpgradeCount = 0
computerType = []       
manufacturer = []       
processor = []          
memory = []             
diskCapacity = []       
extraDiskCapacity = []  
diskCount = []          
osVersion = []          
manufactureYear = []    

# Open the CSV file and read the data.
with open("w3/filehandling-1.csv") as file:  # Replace with actual file path.
    data = csv.reader(file)
    for row in data:
        # Append data from each row into lists.
        computerType.append(row[0])   
        manufacturer.append(row[1])    
        processor.append(row[2])       
        memory.append(row[3])         
        diskCapacity.append(row[4])   
        diskCount.append(row[5])      

        # Check if there's a secondary disk and append the data.
        if row[5] == "2":
            extraDiskCapacity.append(row[6])  
            osVersion.append(row[7])         
            manufactureYear.append(int(row[8]))  
        else:
            extraDiskCapacity.append(0)      
            osVersion.append(row[6])         
            manufactureYear.append(int(row[7])) 

        # Record counter.
        totalRecords += 1

# Loop through each record and count desktops and laptops that need replacement.
for i in range(totalRecords):
    
    if manufactureYear[i] <= 16 and computerType[i] == "D":
        desktopReplace += 1
    
    elif manufactureYear[i] <= 16 and computerType[i] == "L":
        laptopReplace += 1

# Calculate the total cost for replacing desktops and laptops.
desktopReplacementCost = desktopReplace * 2000  # Assume each desktop replacement costs $2000.
laptopReplacementCost = laptopReplace * 1500    # Assume each laptop replacement costs $1500.

print(f"New Desktops:   {desktopReplace: ^1}    Cost of New Desktops:   ${desktopReplacementCost: .2f}")
print(f"New Laptops:    {laptopReplace: ^1}    Cost of New Laptops:    ${laptopReplacementCost: .2f}")