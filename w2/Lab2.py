# W2D2 - Text File Handling Review w/ filters!
# Tshauni Brown
# W2 Lab 2
# Date: 01/20/2025
# Programming Essentials Using Python, SE126.02
#Project Description: You have been asked to produce a report that lists all the computers in the csv file filehandling.csv


#VARIABLE DICTIONARY: 

# computer_type = # Type 
# manufacturer = # Manufacturer 
# processor_type = # Processor Type 
# ram_gb =  # RAM 
# hdd_size =  # Size of the first hard drive
# num_hdds =  # Number of hard drives 


                      
#NOTES: main notes found in program.
import csv

# Function to process and print computer data
def print_computer_data(csv_filename):
    # Open and read the CSV file
    with open("txtFiles/filehandling.csv") as file:
        reader = csv.reader(file)
        
        print(f"{'Type':5} {'Manufacturer':15} {'Processor Type':15} {'RAM (GB)':10} {'Hard Drive Size':15} {'No. of HDDs':10} {'Size of 2nd HDD':15} {'Operating System':20} {'Operating System 2':20} {'Year of Purchase':15}")
        
        # Skip the header row in the CSV file
        next(reader)
        
        for record in reader:
            # Extract data from the row
            computer_type = record[0]  # Type 
            manufacturer = record[1]   # Manufacturer 
            processor_type = record[2] # Processor Type 
            ram_gb = record[3]         # RAM 
            hdd_size = record[4]       # Size of the first hard drive
            num_hdds = int(record[5])  # Number of hard drives 

            # If there's only 1 HDD
            if num_hdds == 1:
                os = record[6]  # Operating System 
                purchase_year = record[7]  # Year of Purchase
                print(f"{computer_type:5} {manufacturer:15} {processor_type:15} {ram_gb:10} {hdd_size:<5} {num_hdds:10} {'':15} {os:20} {'':20} {purchase_year:15}")
            
            # If there are 2 HDDs
            elif num_hdds == 2:
                hdd2_size = record[6]  # Size of the second hard drive
                os2 = record[7]        # Second Operating System
                purchase_year = record[8]  
                print(f"{computer_type:5} {manufacturer:15} {processor_type:15} {ram_gb:10} {hdd_size:15} {num_hdds:10} {hdd2_size:15} {os2:20} {purchase_year:15}")


# Call the function and pass the CSV filename you want to use
csv_filename = 'txtFiles/filehandling.csv'  
print_computer_data(csv_filename)