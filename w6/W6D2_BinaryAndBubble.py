
#---IMPORTS------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------
def display(x, foundList, records):
    '''PARAMETERS:
                x signifier for if we are printing a single record or multiple.

                    when x != "x" it is an index and we have one value, otherwise we have multiple.
                    
                records the length of a list we are going to process through (# of loops/prints)'''
    print(f"{"CLASS":8} {"NAME":10} {"MEANING":20}  {"CULTURE":8}")
    print(f"------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{classType[x]:8}    {name[x]:10}    {meaning[x]:20} {culture[x]:8}")

    elif foundList:
        #printing multiples, based on length stored in "foundList."
        for i in range(0, records):
            print(f"{classType[foundList[i]]:8}    {name[foundList[i]]:10}    {meaning[foundList[i]]:20} {culture[foundList[i]]:8}")
    else:
        #printing full data, based on length stored in "records."
        for i in range(0, records):
            print(f"{classType[i]:8}    {name[i]:10}    {meaning[i]:20} {culture[i]:8}")

def swap(i, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

#---MAIN EXECUTING CODE---------------------------------------------------------------------------------


classType = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open("txtFiles/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        classType.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#disconnected from the file-------------------------------------------------
display("x",0,len(classType)) #practice with function
print(f"------------------------------------------------------")

ans = input("Would you like to enter the search program? [y/n]: ").lower()

#validity and user error trap loop.
while ans != "y" and ans != "n":
    print(f"INVALID ENTRY. TRY AGAIN NOW :(")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

#main searching loop.
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE")
    print("2. Search by NAME")
    print("3. Search by MEANING")
    print("4. EXIT")

    searchType = input("\nHow would you like to search to today? [1-4]: ")

    #using "not in" fpr user validity checks.
    if searchType not in ["1", "2", "3", "4"]:
         print(f"INVALID ENTRY. TRY AGAIN NOW :(")

    elif searchType == "1":
         print(f"You have chosen search by TYPE.")

         search = input("Which type: 'dragon' or 'elf': ").lower()

         if search not in ["dragon", "elf"]:
             #could also be: if search.title() not in classType.
             print(f"INVALID ENTRY. YOU AREN'T READING MY DIRECTIONS.. :(")
         else: 
             found = []
             for i in range(0, len(classType)):
                 if search.lower() == classType[i].lower():
                     found.append(i)

             if not found:
                 print(f"Sorry, your search could not be completed. :(")
             else:
                 print(f"Your search for {search} is COMPLETE! Details found below! :)")
                 display("x", found, len(found))

    elif searchType == "2":

        #ALWAYS SORT BEFORE YOU SEARCH WHEN USING BINARY SEARCH.
        #BUBBLE SORT----------------------------------------

        for i in range(0, len(name) - 1):#outter loop

            print("OUTER LOOP! i = ", i)

            for index in range(0, len(name) - 1):#inner loop.
                print("\t INNER LOOP! k = ", index)
                #below if statement determines the sort.
                #list used is the list being sorted.
                # > is for increasing order, < for decreasing.
                if(name[index] > name[index + 1]):
                    #if above is true, swap places!
                    swap(index, name)
                    #swap all other values.
                    swap(index, classType)
                    swap(index, meaning)
                    swap(index, culture)

        #check your sorting!
        display("x", 0, len(name))

        #BINARY SEARCH
        search = input("Enter the NAME you are looking for: ")

        min = 0
        max = len(name) - 1
        mid = int((min + max) / 2)

        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid -1
            else:
                #search > name[mid]
                min = mid + 1
            mid = int((min + max) / 2)
        if search == name[mid]:
            display(mid, 0, len(name))
        else:
            print(f"\nYour search for {search} came up empty... :[")
    elif searchType == "3":
        print(f"\nYou have chosen to search by MEANING")

        search = input("Which name meaning are you looking for? ").lower()

        found = []

        #allow the program to search for parts of a name like "dragon" or "light"
        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry, we have no names related to the meanning you entered... '{meaning}' :(")
        else:
            display("x", found, len(found))
    elif searchType == "4":
        print("\nYou have chosen to EXIT. Goodbye :)")
        ans = "N"

   