#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j, listName):
    temp = listName[j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)       #entire list
print(names_list[0])    #first value  
print(names_list)       #last value


# create an empty list for each potential field.
# these MUST remain the same length in order to be parallel.
names = []
riders = []
nums = []
color1 = []
color2 = []


#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "name" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12, # no key name duplicates.
    "age" : 12.5,

}

print(people_dictionary) # entire dictionary.
print(people_dictionary["fname"]) # replaces with value assigned to "fname" key.

dragonDict = {} # empty dictionary t be populated by the file.

#gaining data from a text file 
with open("txtFiles/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0]) 
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])
        color2.append(rec[4])

        if rec[2] == '2':
            color2.append(rec[4])
            colorVar = rec[4]
        else:
            # still need to assign data for this dragon into color2 list so lists remain parallel.
            color2.append("----")
            colorVar = "----"

        #adding data to a dictionary
        dragonDict.update({rec[0] : [rec[1], rec[2], rec[3], colorVar]})



#processing data from collections
#Lists --> standard for i in range().
print(f"{'NAMES':12}   {'RIDERS':30}   {'NUMS':3}   {'COLOR1':8}   {'COLOR2'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"{names[i]:12}   {riders[i]:30}   {nums[i]:3}   {color1[i]:8}   {color2[i]}")
print("-" * 75)


#dictionaries --> for key in dictionary!


for key in dragonDict:
    print(f"{key.upper():15}    {dragonDict[key]}") # this shows us the list data found at each key.
    for value in dragonDict[key]:
        print(f"{key} - {value}", end = "")
    print()
    for i in range(len(dragonDict[key])):
        print(f"{dragonDict[key][i]}", end = "")
    print("-" * 75)


#searching & sorting
#sequential search for multiple return values
search = input("\nEnter the RIDER name you wish to find: ")
found = []

for key in dragonDict:
    if search.lower() in dragonDict[key][0].lower():
        found.append(key) #adds key of found location to the list.

if not found:
    #found list is still empty, no search returned.
    print(f"\nSorry, your search for {search} came up empty. :[\n")
else:
    print(f"\nHere are the results for your search of {search}: ")
    for i in range(len(found)):
        print(f"{found[i].upper():15}   {dragonDict[found[0].upper():15]}   {dragonDict[found[1].upper():15]}   {dragonDict[found[2].upper():15]}   {dragonDict[found[3].upper():15]}")
#BINARY SEARCH requires the sorting of data before searching.
#WE must also ensure the collection is search.

#bubble sort alogorithm - a loop in a loop.
for i in range(len(names) - 1):
    for j in range(len(names) - 1):
        if names[j] > names[j + 1]:
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)

#binary search
search = input("\nEnter the DRAGON NAME you wish to find: ")

min = 0
max = len(names)
mid = int((min + max) / 2)
while min < max and search.lower() != names[mid].lower():
    print(min, max, mid, names[mid])
    if search.lower() < names[mid].lower():
        max = mid -1
    else:
        min = mid + 1
    mid = int((mid + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record #{mid}, see info below:")
    print(f"{names[i]:12}   {riders[i]:30}   {nums[i]:3}   {color1[i]:8}   {color2[i]}\n")
else:
    print(f"Sorry! We could not find your search for {search}.")


#2D lists - lists of lists! 

letters = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"],
    ["M", "N", "O"],
    ["P", "Q", "R"],
    ["S", "T", "U"],
    ["V", "W", "X"],
    ["Y", "Z", "-"],
]

print(letters)  #whole 2d list (you will see multiple []s)
print(letters[0])   #first list nside of 2d letters
print(letters[0][0])    #first value is first list of 2d letters
print(letters[0][len(letters[0]) - 1])  #last value in first list of 2d letters.
