# W2D2 - Text File Handling Review w/ filters!

# Program Prompt:





# Variable Dictionary:
import csv




#-----------------------IMPORTS-------------------------------
def difference(people, maxCap):
    '''This function is passed 2 values and returns the difference between them.'''
    diff = maxCap - people
    return diff

#----------------------FUNCTIONS-----------------------------



#-------------------MAIN EXECUTING CODE----------------------


# Initialize needed counting variables.
totalRec = 0
roomsOver = 0


#--------connected to file-----------------------------------
print(f"{'NAME':20}  {'  MAX':5}  {'  PPL':5}  {'  OVER':5}") #-----------------FIELD HEADERS for display.-------------
print("------------------------------------------------")
with open("txtFiles/classLab2.csv") as csvfile:
    # we must indent one level while "connected to the file."

    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (text file!)

        #assign each field data value to a friendly var name.
        name = rec[0]
        max = int(rec[1]) #all text data read as a string, so cast as a num!
        ppl = int(rec[2]) #all text data read as a string, so cast as a num!


        #call the difference() to find people over/under capacity.
        remaining = difference(ppl, max)

        #count and display roooms that are over capacity (remaining is negative.)
        if remaining < 0:
            roomsOver += 1
            print(f"{name:20}  {max:5}  {ppl:5}  {remaining * -1:5}")
        #add +1 to totalRec.
        totalRec += 1



#--------connected to file-----------------------------------
#display final data (counting vars)
print(f"\nRooms currently OVER CAPACITY: {roomsOver}")
print(f"Total rooms in file: {totalRec}\n\n")