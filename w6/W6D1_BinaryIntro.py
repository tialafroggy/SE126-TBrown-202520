#W6D1 - Searching Algorithms: Binary vs Sequential Search

import csv
libraryNums = []
titles = []
authors = []
genres = []
pages = []

with open("txtFiles/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libraryNums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
print("----------------------------------------------------------------------")

for i in range(0, len(libraryNums)):
    print(f"{libraryNums[i]:5}  {titles[i]:25}  {authors[i]:15}  {genres[i]:20}  {pages[i]:5}")
print("----------------------------------------------------------------------")

#SEQUENTIAL SEARCH: allow a user to search for a specific title.
#titles[] is NOT ordered.

found = []
searchNum = input("Which Library Num. are you looking for? ")
seqCount = 0


for i in range(0, len(libraryNums)):
    seqCount += 1
    if searchNum.lower() in libraryNums[i].lower():
        found.append(i)
print(f"SEARCH ITERATIONS: {seqCount}")
if not found:
    #found list is still empty, meaning no matches to our search term was found.
    print(f"Sorry, your search for {searchNum} was NOT found. :(")
else:
    print(f"Your search for {searchNum} was FOUND! :D")

    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
    print("----------------------------------------------------------------------")
    for i in range(0, len(found)):
        print(f"{libraryNums[found[i]]:5}  {titles[found[i]]:25}  {authors[found[i]]:15}  {genres[found[i]]:20}  {pages[found[i]]:5}")
    print("----------------------------------------------------------------------")


#BINARY SEARCH: must be performed on ORDERED lists (libraryNums)

min = 0
max = len(libraryNums) - 1
mid = int((min + max) / 2)

binCount = 0

while min < max and searchNum != libraryNums[mid]:
    #min < max --> list has not been exhausted of potential values yet.
    #searchNum != libraryNums[mid] --> what we are looking for is not in the mid position.

    if searchNum < libraryNums[mid]:
        #everything after mid point is not possible.
        max = mid - 1
    else:
        #everything before mid point is not possible.
        min = mid + 1

    mid = int((min + max) / 2)
    binCount += 1

print(f"BINARY SEARCH ITERATIONS: {binCount}")

if searchNum == libraryNums[mid]:
    print(f"Your search for {searchNum} was FOUND! :D")
    print(f"{'LIB#':5}  {'TITLE':25}  {'AUTHOR':15}  {'GENRE':20}  {'PAGES':5}")
    print("----------------------------------------------------------------------")
    print(f"{libraryNums[mid]:5}  {titles[mid]:25}  {authors[mid]:15}  {genres[mid]:20}  {pages[mid]:5}")
    print("----------------------------------------------------------------------")
else:
    print(f"Sorry, your search for {searchNum} was NOT found. :(")


