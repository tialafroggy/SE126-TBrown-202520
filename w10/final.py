# Tshauni Brown
# W10 Final Part 3
# Date: 03/09/2025
# Programming Essentials Using Python, SE126.02
# Project Description: This program lets you know the attendence of a student for the day. You can search by their first name, room number, and age. It will then give you the full information of the student. Their first AND last name, the date, the time of entry, the room number, their age, AND whether they were on time, tardy, or missing.

# Course Questions and Answers:
# Q. How did you arrive at your Final Project Program idea?
# A. Honestly...I had no clue what my project would be about. The deadline was getting closer, and I still had nothing. I asked my friends if they had an idea for me, and an attendance list popped up.
# Q. How did you approach building this program?
# A. Honestly, I didn't want to do too much. I wanted to hit every requirement without going over what I needed to do. I honestly wanted to do only what I had to do.
# Q. What did you do to test your program?
# A. Well to check if my program was realistic enough, I had my friends run through it and tell me if this would be something they'd use if they were given the chance.
# Q. What was the hardest part about building this program?
# A. The hardest part was keeping up with what I already did vs. what I didn't do.
# Q. What was the most enjoyable or fun part about building this program?
# A. The most enjoyable part was seeing different parts of the program work after having problems in between. It was very rewarding.
# Q. If you could go back and change something about the program or your approach to building it, what would you change?
# A. I would add a search by last name, lol. Honestly-- I got tired mid way through and decided to only search by first name since they all had their own unique names. (Generated names btw.)

import csv

# function to display the menu.
def menu():
    print("\nWelcome to my Attendance Search Program!")
    print("Please select an option from the menu below!")
    print("1. Search by student's FIRST NAME.")
    print("2. Search by ROOM NUMBER.")
    print("3. Search by AGE.")
    print("4. Exit")

    menu_choice = input("Enter your choice [1-4]: ")
    return menu_choice

# function to check if the student is on time, tardy, or missing.
def checkAttendance(time):
    if time == "":
        return "Missing"
    else:
        # time is in the format "HH:MM".
        hour, minute = map(int, time.split(":"))
        # check if the student is On Time (before or at 8:30.)
        if hour < 8 or (hour == 8 and minute <= 30):
            return "On Time"
        else:
            return "Tardy"

# function to print student details, including attendance status.
def print_studentDetails(dataFile, index):
    name = f"{dataFile[index][0]} {dataFile[index][1]}"
    age = f"{dataFile[index][2]}"
    date = f"{dataFile[index][3]}"
    time = f"{dataFile[index][4]}"  # time of arrival.
    room = f"{dataFile[index][5]}"
    attendanceStatus = checkAttendance(time)
    
    print(f"\n{'NAME':20} {'AGE':3} {'DATE':12} {'TIME':5} {'ROOM':3} {'STATUS'}")
    print("-------------------------------------------------------------")
    print(f"{name:20} {age:3} {date} {time:5} {room:3} {attendanceStatus}")
    print("-------------------------------------------------------------")

# function to perform a sequential search on the list based on the provided key (name, room, or age.)
def sequentialSearch(dataFile, key, key_index):
    for i in range(len(dataFile)):
        if dataFile[i][key_index].lower() == key.lower():
            return i  # return the index where the match is found.
    return -1  # return -1 if no match is found.

# read the CSV file into a 2D list.
dataFile = []

# read the file.
filename = "txtFiles/final.csv"
with open(filename) as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        dataFile.append(rec)

ans = "y"
while ans.lower() == "y":
    choice = menu()

    if choice == "1":  # search by NAME.
        print("\n~Search by FIRST NAME~")

        searchName = input("What is the first name of the student you are looking for? : ").strip()
        index = sequentialSearch(dataFile, searchName, 0)  # searching by first name (column 0.)

        if index != -1:
            print(f"\nYour search for {searchName} was FOUND! Here are the details:")
            print_studentDetails(dataFile, index)
        else:
            print(f"\nNO STUDENT NAMED {searchName} WAS FOUND ON THE ATTENDANCE LIST.")

    elif choice == "2":  # search by ROOM NUMBER.
        print("\n~Search by ROOM NUMBER~")

        searchRoom = input("What is the room number you are looking for? : ").strip()
        index = sequentialSearch(dataFile, searchRoom, 5)  # searching by room number (column 5.)

        if index != -1:
            print(f"\nYour search for Room {searchRoom} was FOUND! Here are the details:")
            print_studentDetails(dataFile, index)
        else:
            print(f"\nNO STUDENT FOUND IN ROOM {searchRoom} AT THIS TIME..")

    elif choice == "3":  # search by AGE.
        print("\n~Search by AGE~")

        searchAge = input("What is the age of the student you're looking for? ").strip()
        index = sequentialSearch(dataFile, searchAge, 2)  # searching by age (column 2.)

        if index != -1:
            print(f"\nYour search for age {searchAge} was FOUND! Here are the details:")
            print_studentDetails(dataFile, index)
        else:
            print(f"\NO STUDENT FOUND WITH SUCH AGE: {searchAge}.")

    elif choice == "4":  # exit the program.
        print("\nThank you for using my Attendance Search Program!")
        print("Goodbye!(IT'S FINALLY OVER. I CAN BREATHEEEE.)")
        ans = "n"  # exit the loop by changing ans to something that will break the loop.

    else:
        print("***!INAVLID INPUT!*** Please enter a number between 1-4.")

print("\nEXITTINGGGGGGGGGGGGG FOR THE LAST TIME.")
