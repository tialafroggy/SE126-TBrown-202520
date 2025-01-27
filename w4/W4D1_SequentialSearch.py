# Tshauni Brown
# W4 DEMO Lab
# Date: 01/27/2025
# Programming Essentials Using Python, SE126.02
#Project Description: We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

# This file is a demo.
                      
#----------------IMPORTS----------------------------------------------------------------
import csv
#----------------FUNCTIONS----------------------------------------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let #"let" value replaces the function call in the main executing code.
#----------------MAIN EXECUTING CODE----------------------------------------------------------------

#create empty lists to hold the file data.

fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("txtFiles/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists.
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#display from file -- can still access the stored data via the lists.



#process the list data to calc an average score for each student. and find a letter grade equivalent.
num_avg = [] #will hold each student's numeric average of test scores.
let_avg = [] #will hold each student's letter average of test scores.

for i in range(0, len(fName)):
    #calculate average of curent student.
    a = (test1[i] + test2[1] + test3[i])/ 3
    #add average to num_avg list
    num_avg.append(a) #can also do: num_avg.append(((test1[i] + test2[1] + test3[i])/ 3))

    l = letter(a) #return value of letter() stored to 1.
    let_avg.append(l) #can also do: let_avg.append(letter(a))

# process the lists to display all student data back to the user.
print(f"{"FIRST":10}   {"LAST":10}   {"T1":3}   {"T2":3}   {"T3":3}  {"# AVG"}   {"L AVG"}")
print("---------------------------------------------------------------------------------------------")
for i in range(0, len(fName)):
    print(f"{fName[i]:10}   {lName[i]:10}   {test1[i]:3}   {test2[i]:3}   {test3[i]:3}  {num_avg[i]:6.2f}   {let_avg[i]}")
print("---------------------------------------------------------------------------------------------")
print(f"There are {len(fName)} students in the file.")


#--------------------------------------------------------------------write a 

print("\n\nWelcome to the Student Search Program!\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":

    #get search type from user.
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE ")
    print("3. EXIT ")
    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
        print("\tSEARCH BY LAST NAME")

        found = -1 #invalid index number, wil use to check later to see if a student has been found.
        #get search item from user.
        search_name = input("What is the LAST name you are looking for? ")
        #perform search.
        for i in range(0, len(lName)):
            #the FOR LOOP allows for the "sequence" part --> from beginning to end!
            if search_name.lower() == lName[i].lower():
                #the IF STATEMENT alows for the "search" part.
                found = i #make found the current index, can be used later to display.
        #display results.
        if found != -1:
            #last name has been found! display data:
            print(f"Your search for {search_name} was FOUND!")
            print(f"{fName[found]:10}   {lName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}  {num_avg[found]:6.2f}   {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program! Please check your spelling.")

    elif search_type == "2":
        print("\tSEARCH BY LETTER GRADE")

        found = [] #creates empty list to gather and store found index values..
        #get search item from user.
        search_grade = input("What is the LETTER GRADE you are looking for? ")
        #perform search.
        for i in range(0, len(let_avg)):
            #the FOR LOOP allows for the "sequence" part --> from beginning to end!
            if search_grade.upper() == let_avg[i]:
                #the IF STATEMENT alows for the "search" part.
                found.append(i)#add the current index (found), can be used later to display.
        #display results.
        if not found:
            print(f"Your search for {search_grade} was *NOT* FOUND!")
            print(f"This is a cAsE sEnSiTiVe program! Please check your spelling.")
        else:
            #last name has been found! display data:
            print(f"Your search for {search_grade} was FOUND!")
            #found is a list with multiple pieces of data - must use a FOR LOOp to see all.
            for i in range(0, len(found)):
             print(f"{fName[found[i]]:10}   {lName[found[i]]:10}   {test1[found[i]]:3}   {test2[found[i]]:3}   {test3[found[i]]:3}  {num_avg[found[i]]:6.2f}   {let_avg[found[i]]}")
           
    elif search_type == "3":
        print("EXITTING")
    else: 
        print("INVALID ENTRY!")
    #build a way out.

