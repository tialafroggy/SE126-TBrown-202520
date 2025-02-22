
import csv

# Function to display the menu and return the user's choice
def menu():
    print("\nPersonal Library Menu")
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show All Available")
    print("7. Show All On Loan")
    print("8. EXIT")

    # Get user input for the menu choice
    menu_choice = input("Enter your choice [1-8]: ")
    return menu_choice

# Helper function to swap elements in a list by index
def swap(index, list_name):
    """Helper function to swap elements in the list by index."""
    temp = list_name[index]
    list_name[index] = list_name[index + 1]
    list_name[index + 1] = temp

# Load data from CSV into 1D parallel lists
library_numbers = []
titles = []
authors = []
genres = []
page_counts = []
statuses = []

# Open the CSV file and read the data into the lists
with open('txtFiles/book_list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Append each field to its corresponding list
        library_numbers.append(row[0])
        titles.append(row[1])
        authors.append(row[2])
        genres.append(row[3])
        page_counts.append(row[4])
        statuses.append(row[5])

# Main program loop (instead of while True)
is_running = True
while is_running:
    # Display the menu and get the user's choice
    choice = menu()

    # Handle the "Show All Titles" option
    if choice == "1":  # Show All Titles
        # Bubble Sort Titles alphabetically (case-insensitive)
        for i in range(len(titles) - 1):
            for j in range(len(titles) - 1):
                if titles[j].lower() > titles[j + 1].lower():
                    # Swap elements in all lists to keep data consistent
                    swap(j, titles)
                    swap(j, library_numbers)
                    swap(j, authors)
                    swap(j, genres)
                    swap(j, page_counts)
                    swap(j, statuses)
        
        # Display the sorted books
        print(f"{'Library No.':<15}{'Title':<40}{'Author':<30}{'Genre':<20}{'Page Count':<10}{'Status':<10}")
        print("--------------------------------------------------------------------------------------------")
        print('-' * 125)
        for i in range(len(titles)):
            print(f"{library_numbers[i]:<15}{titles[i]:<40}{authors[i]:<30}{genres[i]:<20}{page_counts[i]:<10}{statuses[i]:<10}")
            print("--------------------------------------------------------------------------------------------")

    # Handle the "Search by Title" option
    elif choice == "2":  # Search by Title
        keyword = input("Enter title or keyword: ").lower()  # Make search case-insensitive
        found = False  # Flag to check if any results are found
        for i in range(len(titles)):
            if keyword in titles[i].lower():  # Case-insensitive search
                # Display the book information
                print(f"\nLibrary No. {library_numbers[i]}")
                print(f"Title: {titles[i]}")
                print(f"Author: {authors[i]}")
                print(f"Genre: {genres[i]}")
                print(f"Page Count: {page_counts[i]}")
                print(f"Status: {statuses[i]}")
                found = True  # Mark that at least one result is found
        if not found:
            print("No books found with that title.")  # If no results are found

    # Handle the "Search by Author" option
    elif choice == "3":  # Search by Author
        author = input("Enter author name: ").lower()  # Make search case-insensitive
        found = False  # Flag to check if any results are found
        for i in range(len(authors)):
            if author in authors[i].lower():  # Case-insensitive search
                # Display the book information
                print(f"\nLibrary No. {library_numbers[i]}")
                print(f"Title: {titles[i]}")
                print(f"Author: {authors[i]}")
                print(f"Genre: {genres[i]}")
                print(f"Page Count: {page_counts[i]}")
                print(f"Status: {statuses[i]}")
                found = True  # Mark that at least one result is found
        if not found:
            print("No books found by that author.")  # If no results are found

    # Handle the "Search by Genre" option
    elif choice == "4":  # Search by Genre
        genre = input("Enter genre: ").lower()  # Make search case-insensitive
        found = False  # Flag to check if any results are found
        for i in range(len(genres)):
            if genre in genres[i].lower():  # Case-insensitive search
                # Display the book information
                print(f"\nLibrary No. {library_numbers[i]}")
                print(f"Title: {titles[i]}")
                print(f"Author: {authors[i]}")
                print(f"Genre: {genres[i]}")
                print(f"Page Count: {page_counts[i]}")
                print(f"Status: {statuses[i]}")
                found = True  # Mark that at least one result is found
        if not found:
            print("No books found in that genre.")  # If no results are found

    # Handle the "Search by Library Number" option
    elif choice == "5":  # Search by Library Number
        library_number = input("Enter library number: ")  # Prompt for library number
        if library_number in library_numbers:  # Check if the number exists
            idx = library_numbers.index(library_number)  # Find the index of the matching library number
            # Display the book information
            print(f"\nLibrary No. {library_numbers[idx]}")
            print(f"Title: {titles[idx]}")
            print(f"Author: {authors[idx]}")
            print(f"Genre: {genres[idx]}")
            print(f"Page Count: {page_counts[idx]}")
            print(f"Status: {statuses[idx]}")
        else:
            print("No book found with that library number.")  # If no matching book is found

    # Handle the "Show All Available" option
    elif choice == "6":  # Show All Available
        found = False  # Flag to check if any available books are found
        for i in range(len(statuses)):
            if statuses[i].lower() == "available":  # Check for available status
                # Display the book information
                print(f"\nLibrary No. {library_numbers[i]}")
                print(f"Title: {titles[i]}")
                print(f"Author: {authors[i]}")
                print(f"Genre: {genres[i]}")
                print(f"Page Count: {page_counts[i]}")
                print(f"Status: {statuses[i]}")
                found = True  # Mark that at least one result is found
        if not found:
            print("No available books.")  # If no available books are found

    # Handle the "Show All On Loan" option
    elif choice == "7":  # Show All On Loan
        found = False  # Flag to check if any on-loan books are found
        for i in range(len(statuses)):
            if statuses[i].lower() == "on loan":  # Check for on loan status
                # Display the book information
                print(f"\nLibrary No. {library_numbers[i]}")
                print(f"Title: {titles[i]}")
                print(f"Author: {authors[i]}")
                print(f"Genre: {genres[i]}")
                print(f"Page Count: {page_counts[i]}")
                print(f"Status: {statuses[i]}")
                found = True  # Mark that at least one result is found
        if not found:
            print("No books are currently on loan.")  # If no on-loan books are found

    # Handle the "EXIT" option
    elif choice == "8":  # EXIT
        print("Exiting the program.")  # Exit message
        is_running = False  # Change the flag to stop the loop

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")  # Error message for invalid input
