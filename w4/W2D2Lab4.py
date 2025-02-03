import random
import csv

# Define where your input and output files are located
input_file = 'got_emails.csv'  # Path to your CSV with employee data
output_file = 'westeros.csv'   # Path to where we will save the output

# Dictionary that links each house to its department and phone extension range
house_to_department = {
    "House Stark": ("Research & Development", (100, 199)),
    "House Targaryen": ("Marketing", (200, 299)),
    "House Tully": ("Human Resources", (300, 399)),
    "House Lannister": ("Accounting", (400, 499)),
    "House Baratheon": ("Sales", (500, 599)),
    "The Night's Watch": ("Auditing", (600, 699))
}

# This list will store all our employee data as lists of lists (index-based)
employees = []

# Read the 'got_emails.csv' file and process each employee's data
with open("txtFiles/got_emails.csv", mode='r') as file:
    reader = csv.reader(file)
    header = next(reader, None)  # Skip the first row (header)
    
    # Process each employee in the CSV
    for row in reader:
        first_name, last_name, age, screen_name, house_allegiance = row
        
        # Create the employee's email by appending '@westeros.net' to their screen name
        email = f"{screen_name}@westeros.net"
        
        # Find the department and phone extension range based on their house allegiance
        department, ext_range = house_to_department.get(house_allegiance, ("Unknown", (0, 0)))
        
        # Generate a random phone extension within the given range
        phone_extension = random.randint(ext_range[0], ext_range[1])
        
        # Store this employee's data as a list in the employees list
        employees.append([first_name, last_name, email, department, phone_extension])

# Function to search for employees by a specific field (first name, last name, email, department, or phone extension)
def search_employee(query, field_index):
    results = []  # This will store any employees that match the search query
    for employee in employees:
        # Search based on the chosen field (case insensitive)
        if field_index == 0 and query.lower() in employee[0].lower():  # First name
            results.append(employee)
        elif field_index == 1 and query.lower() in employee[1].lower():  # Last name
            results.append(employee)
        elif field_index == 2 and query.lower() in employee[2].lower():  # Email
            results.append(employee)
        elif field_index == 3 and query.lower() in employee[3].lower():  # Department
            results.append(employee)
        elif field_index == 4 and query == str(employee[4]):  # Phone Extension
            results.append(employee)
    
    return results

# Function to display employee data in a clean, formatted way
def display_employee_data(employee):
    print(f"{employee[0]:8} {employee[1]:10} {employee[2]:30} {employee[3]:23} {employee[4]:3}")

# Part 1 - Display all employees in the system
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
print(f"------------------------------------------------------------------")
for employee in employees:
    display_employee_data(employee)

# Menu for the user to choose the type of search
run_program = "y"  # Control variable to manage the program loop

while run_program == "y":
    print("\n--- KT'S ENTERPRISE SEARCH MENU ---")
    print("\n--- Secret Message: I wanted to cry tbh. ---")
    print("1. Search by FIRST Name")
    print("2. Search by LAST Name")
    print("3. Search by EMAIL")
    print("4. Search by DEPARTMENT")
    print("5. Search by PHONE EXT.")
    print("6. EXIT")
    
    # Get user input
    choice = input("Please choose an option (1-6): ")
    
    # Handle the user's choice
    if choice == '1':
        search_query = input("Enter FIRST name to search for: ")
        search_results = search_employee(search_query, 0)  # First name is at index 0
        print("\n--- Does it ever get better... ---")
    elif choice == '2':
        search_query = input("Enter LAST name to search for: ")
        search_results = search_employee(search_query, 1)  # Last name is at index 1
        print("\n--- Constantly wanting to pull my hair out.. ---")
    elif choice == '3':
        search_query = input("Enter EMAIL to search for: ")
        search_results = search_employee(search_query, 2)  # Email is at index 2
        print("\n--- Jk.... ---")
    elif choice == '4':
        search_query = input("Enter DEPARTMENT name to search for: ")
        search_results = search_employee(search_query, 3)  # Department is at index 3
        print("\n--- No I'm not.. ._. ---")
    elif choice == '5':
        search_query = input("Enter PHONE EXT. to search for: ")
        search_results = search_employee(search_query, 4)  # Phone extension is at index 4
        print("\n--- I hope my little messages make you giggle. ---")
    elif choice == '6':
        print("EXITTINGGGGGGG! Also, hi! :) Have a good week KT.")
        print("-- Okeh, BYEEEE. ---")
        run_program = "no"  # Set to "no" to exit the loop
        print("\n--- Okeh, BYEEEE. ---")
    else:
        # If the choice is invalid, show an error message.
        print("This is a cAsE sEnSiTiVe program! Please check your spelling.")
        search_results = []  # Set empty list to avoid further processing
    
    # Show the search results if they exist
    if search_results:
        print(f"\nFound {len(search_results)} employee(s) matching your query:")
        for employee in search_results:
            display_employee_data(employee)
    else:
        # No results to show
        print(f"\n INVALID ENTRY! '{search_query}'.")

# Part 3 - Write the updated data to the output CSV file
data_to_write = []  # List to store the employee data in CSV format
for employee in employees:
    data_to_write.append([employee[0], employee[1], employee[2], employee[3], employee[4]])

# Write to the output file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["First Name", "Last Name", "Email", "Department", "Phone Extension"])
    # Write all the employee data
    writer.writerows(data_to_write)

print("\nData has been successfully written to 'westeros.csv'.")
