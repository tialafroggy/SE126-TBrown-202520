#----------------INTRODUCTIONS----------------------------------------------------

# Tshauni Brown
# W1 Lab
# Date: 01/11/2025
# Programming Essentials Using Python, SE126.02
#Project Description: You will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.
#VARIABLE DICTIONARY: 
#  people = people in the room
#  maxCap = what the room can hold.
#  response = user input
#  attendees = people attending.
                      
#NOTES: main notes found in program.

#----------------FUNCTIONS----------------------------------------------------------------
from os import system, name
import random

def clear():# Clears the screen :)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def difference(people, maxCap):
    '''Here, the function will calculate the difference between the amount of people present, and the max capacity of the room.'''
    return people - maxCap

def decision(response):
    '''If the response is not valid, this will play...'''
    while response != 'y' and response != 'n':
        response= input("Please enter a valid response: ").lower()
    return response

#------------------MAIN PROGRAM CODE-----------------------------------------------
clear()

print("Welcome to the Meeting Attendance Checker :D!")
# Welcomes you and sets response to 'y' (yes).
response = 'y'

# Places you into a loop which will play if you decide to create a meeting room.
while response == 'y':
    meetingName = input("What is the meeting room name? ")
    capacityRoom = int(input("What is the room's capacity? "))
    attendees = int(input("How many people are attending? "))

    diff = difference(attendees, capacityRoom)

    if diff > 0:
        print(f"The meeting '{meetingName}' has too many attendees by {diff}. {diff} people need to be removed immediately to meet fire code..")
# too many
    elif diff < 0:
        print(f"The meeting '{meetingName} has space for {-diff} more person(s). {-diff} can be added to continue to meet fire code..")
# enough and can add more.
    else: 
        print(f"Your meeting {meetingName} is completely full. Full place, huh?")
# perfect.
    
    response = input("Would you like to make another meeting? (y/n): ")
    response = decision(response)
# another meeting and calls the function to check your response.

print("Thank you for using the Meeting Attendance Checker. Bye bye Katie!")


