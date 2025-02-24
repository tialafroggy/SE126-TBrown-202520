

# Tshauni Brown
# Program Name: Airplane Seat Reservation System.
# Week 7 Lab # 6
# Program Prompt: This program allows users to reserve seats in a small airplane, displaying the seat map and allowing the user to select a seat while ensuring the seat is available.

# Function to display the current seating chart.
def displaySeats(seats):
    print("Row\tA\tB\tC\tD")
    for i in range(len(seats)):
        print(f"{i+1}\t", end="")
        for j in range(len(seats[i])):
            print(seats[i][j], end="\t")
        print()

# Function to ask the user if they want to continue or stop.
def continuePrompt():
    choice = input("Would you like to continue reserving seats? (Y/N): ").strip().lower()
    while choice not in ['y', 'n']:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        choice = input("Would you like to continue reserving seats? (Y/N): ").strip().lower()
    return choice

# Initialize a 2D list representing the seats (7 rows, 4 seats per row.)
seats = [["A", "B", "C", "D"] for _ in range(7)]

# Display the initial seat map.
displaySeats(seats)

# Main loop for reserving seats.
reserving = 'y'

while reserving == 'y':
    seatChoice = input("Which seat would you like to reserve? (ex. 1A, 2B, etc.): ").strip().upper()

    # Check if input is in the valid format.
    if len(seatChoice) != 2 and len(seatChoice) != 3:
        print("INVALID SEAT. Please enter a seat like '1A', '2B', etc.")
    else:
        row = int(seatChoice[0]) - 1  # Convert the row number to an index (0-6.)
        seatLetter = seatChoice[1]   # The seat letter (A, B, C, D.)

        # Check if row is valid.
        if row < 0 or row > 6:
            print("INVALID ROW. Please enter a row between 1 and 7.")
        else:
            # Map seat letter to the index in the list.
            seatIndex = {"A": 0, "B": 1, "C": 2, "D": 3}

            # Check if the seat letter is valid.
            if seatLetter not in seatIndex:
                print("INVALID LETTER. Please choose from A, B, C, or D.")
            else:
                # Check if the seat is already taken.
                if seats[row][seatIndex[seatLetter]] == 'X':
                    print(f"Seat {seatChoice} is already taken. Please choose another seat.")
                else:
                    # Assign the seat by marking it as 'X'.
                    seats[row][seatIndex[seatLetter]] = 'X'

                # Display the updated seat map.
                displaySeats(seats)

    # Ask the user if they want to continue or stop.
    reserving = continuePrompt()

print("Seat reservation process is complete, enjoy your flight. :)")
