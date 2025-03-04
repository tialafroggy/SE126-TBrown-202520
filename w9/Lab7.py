# Tshauni Brown
# Program Name: Dictionary Search and Add.
# Week 9 Lab # 7
# Program Prompt: Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu.

import csv

# Function to load words from CSV into a dictionary.
def loadWords(file_name):
    wordDict = {}
    with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header.
            for row in reader:
                word = row[0].strip()  # Word (no conversion to lowercase).
                definition = row[1].strip()  # Definition.
                wordDict[word] = definition
   
    return wordDict

# Function to save new word and definition to CSV.
def save_word_to_csv(file_name, word, definition):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([word, definition])

# Main execution starts here.
file_name = 'txtFiles/words.csv'
#------------MAIN CODE-------------------------------------------------------------------.
# Load the dictionary from CSV file.
programmingDict = loadWords(file_name)

# Welcome message.
print("Welcome to my personal Programming Dictionary!")

# Display the current dictionary.
if programmingDict:
    print("\nHere are where the words and their definitions currently stored:")
    for word, definition in programmingDict.items():
        print(f"{word}: {definition}")
else:
    print("\nLooks like your dictionary is EMPTY. Let's add some words!")

# Interactive menu for the user to interact with the dictionary.
userChoice = ""

while userChoice != '4':
    print("\nMy Programming Dictionary Menu:")
    print("1. Show ALL words")
    print("2. Search for A word")
    print("3. ADD a word")
    print("4. EXIT")
    
    userChoice = input("What would you like to do today? (1-4): ").strip()

    if userChoice == '1':
        # Show all words and their definitions.
        if programmingDict:
            print("\nHere are all the words and definitions in your dictionary:")
            for word, definition in programmingDict.items():
                print(f"{word}: {definition}")
        else:
            print("\nYour dictionary is still EMPTY. Try adding a word!")

    elif userChoice == '2':
        # Search for a word in the dictionary.
        word = input("Please enter the word you're looking for Madam Katie: ").strip()
        if word in programmingDict:
            print(f"\nGUESS WHAT? Found it! Here's the definition of '{word}':")
            print(f"{word}: {programmingDict[word]}")
        else:
            print(f"\nUH OH, we don't have '{word}' in your dictionary yet. Would you like to add it Katie?")

    elif userChoice == '3':
        # Add a new word to the dictionary.
        word = input("What's the new word you'd like to add? ").strip()
        if word in programmingDict:
            print(f"\nSORRY! The word '{word}' already exists in your dictionary. Try updating its definition instead.")
        else:
            definition = input(f"Please enter the definition for '{word}': ").strip()
            programmingDict[word] = definition
            # Save the new word and definition to the CSV file.
            save_word_to_csv(file_name, word, definition)
            print(f"\nWOOHOOOOOOOOOOO! The word '{word}' has been added to your dictionary.")

    elif userChoice == '4':
        # Exit the program.
        print("\nThanks for using my Dictionary. Goodbye and happy coding! Have a great week Katie.")

    else:
        print("\nOops! READ CAREFULLY, AND CHOOSE A VALID OPTION.")