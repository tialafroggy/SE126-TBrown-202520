# Tshauni Brown
# W5 Midterm Part 2
# Date: 02/04/2025
# Programming Essentials Using Python, SE126.02
#Project Description: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file.
                      
#----------------IMPORTS----------------------------------------------------------------
import csv
import random

#----------------FUNCTIONS----------------------------------------------------------------


#----------------MAIN EXECUTING CODE----------------------------------------------------------------

# This list will store all our employee data as lists of lists (index-based)
fName = []
lName = []
email = []
depart = []
ext = []

with open("westeros.csv", mode='r') as csvfile:
    file = csv.reader(csvfile)
    header = next(file, None)  # Skip the first row (header.)
    for rec in file:
        #append the file data into appropriate lists.
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        depart.append(rec[3])
        ext.append(rec[4])

officeNum = []

for i in range(0, len(fName)):
    a = random.randint(100,200)
    officeNum.append(a)  #-----------COME BACK TO!------------

print(f"{"FIRST":10}   {"LAST":10}   {"EMAIL":30}   {"DEPARTMENT":30}   {"EXT.":3}  {"OFFICE #"}")
print("---------------------------------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10}   {lName[i]:10}   {email[i]:30}   {depart[i]:30}   {ext[i]:8} {officeNum[i]:3}")
print("---------------------------------------------------------------------------------------------------------")
print(f"There are {len(fName)} EMPLOYEES in the file.")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":
    print("\n--- BADDIE ENTERPRISE (idk) SEARCH MENU ---")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT")
    
    # Get user input
    search_type = input("Please choose an option (1-3): ")
    if search_type == "1":
         print("\tSEARCH BY EMAIL")
         found = -1 #invalid index number, wil use to check later to see if a student has been found.
        #get search item from user.
         search_name = input("What is the LAST name you are looking for? ")
        #perform search.
         for i in range(0, len(email)):
            #the FOR LOOP allows for the "sequence" part --> from beginning to end!
            if search_name.lower() == email[i].lower():
                #the IF STATEMENT alows for the "search" part.
                found = i #make found the current index, can be used later to display.
        #display results.
         if found != -1:
            #last name has been found! display data:
            print(f"Your search for {search_name} was FOUND!")
            print(f"{"FIRST":10}   {"LAST":10}   {"EMAIL":30}   {"DEPARTMENT":30}   {"EXT.":3}  {"OFFICE #"}")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{fName[found]:10}   {lName[found]:10}   {email[found]:3}   {depart[found]:3}   {ext[found]:8} {officeNum[i]:3}")
         else:
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program! Please check your spelling.")
    elif search_type == "2":
         print("\tSEARCH BY DEPARTMENT")
         found = -1 #invalid index number, wil use to check later to see if a student has been found.
        #get search item from user.
         search_name = input("What is the DEPARTMENT you are looking for? ")
        #perform search.
         for i in range(0, len(depart)):
            #the FOR LOOP allows for the "sequence" part --> from beginning to end!
            if search_name.lower() == depart[i].lower():
                #the IF STATEMENT alows for the "search" part.
                found = i #make found the current index, can be used later to display.
        #display results.
         if found != -1:
            #last name has been found! display data:
            print(f"Your search for {search_name} was FOUND!")
            print(f"{"FIRST":10}   {"LAST":10}   {"EMAIL":30}   {"DEPARTMENT":30}   {"EXT.":3}  {"OFFICE #"}")
            print("---------------------------------------------------------------------------------------------------------")
            print(f"{fName[found]:10}   {lName[found]:10}   {email[found]:3}   {depart[found]:3}   {ext[found]:8} {officeNum[i]}")
         else:
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program! Please check your spelling.")
    elif search_type == "3":
        print("EXITTING")

    else: 
        print("INVALID ENTRY!")
    
    #BUILD A WAY OUT! Allow for the 'loop key var' to be revalued.
    answer = input('\tDo you want to try again? [y/n]: ')

    #USER ERROR TRAP LOOP -- trap the user when they don't follow directions :]
    while answer != "y" and answer != "Y" and answer != "n" and answer != "N":
        print("\t\t***INVALID ENTRY!*** FOLLOW DIRECTIONS BUDDY.")
        #BUILD A WAY OUT! allow for the 'loop key var' to be revalued.
        answer = input("\tWould you like to try again? :] [y/n]: ")

print("\n\nThank you for using my program. Goodbye :]")

#WRITE SOME DATA TO A NEW FILE.
#create and write all of the data to a new text file:
file = open("midterm_choice1.csv", "w")

for i in range(0, len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{depart[i]},{ext[i]},{officeNum[i]}")
file.close()