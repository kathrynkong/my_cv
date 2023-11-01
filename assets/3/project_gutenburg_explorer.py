import string
from colorama import Fore, Style

# read the file
FILENAME = "A_room_with_a_view.txt"
f = open(FILENAME, "r", encoding='utf-8') # when debugging, it shows "Using open without explicitly specifying an encoding" in the warning, so I googled and added this
text = f.read()

# error handling
try:
    with open(FILENAME, "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# title, author and date
def book_info(text1):
    title1 = ""
    author1 = ""
    release_date1 = ""
    lines = text1.split('\n')  # split the text into lines
    for line in lines:
        if line.startswith("Title:"):
            title1 = line.split(":")[1].strip()
        elif line.startswith("Author:"):
            author1 = line.split(":")[1].strip()
        elif line.startswith("Release date:"):
            release_date1 = line.split(":")[1].strip()
        if title1 and author1 and release_date1:
            break  # quit the cycle after getting the info
    return title1, author1, release_date1

title, author, release_date = book_info(text)
print(f"{Fore.YELLOW}{Style.BRIGHT}Welcome to the '{title}' Exploration!{Style.RESET_ALL}")
print(f"Author: {author}")
print(f"Release Date: {release_date}")

def count_paragraphs(text1):
    paragraph_number = 0
    lines = text1.split('\n')
    last_line = ""  # initialize a variable to store the last line
    for line in lines:
        if line.strip() == "":  # if the line is empty
            if any(char in string.punctuation for char in last_line):  # check if the last line contains at least one punctuation mark to avoid counting headlines as paragraphs
                paragraph_number += 1  # if contains punctuation, it indicate it is a paragraph
        last_line = line  # update the last line
    return paragraph_number  # Return the total number of paragraphs

# split the text into parts with
parts = text.split("\n\nPART ") #\n\n to differentiate from "PART" in content 
parts.pop(0)  # Remove the content before "PART ONE"

# count paragraphs in each part
for i, part in enumerate(parts):
    paragraph_count = count_paragraphs(part)
    print(f"Total number of paragraphs in PART {i + 1}: {paragraph_count}")

print()

print(f"{Fore.BLUE}{Style.BRIGHT}This novel offers a rich tapestry of themes, including feminism, ideology and literary criticism.\nWould you like to explore more about it from a feminist perspective?{Style.RESET_ALL}") #prompt
answer = input("Enter 'Yes' or 'No': ").strip().lower()
if answer == 'yes':
    print(f"{Fore.GREEN}Fantastic!\nSearch for keywords related to feminism, gender, freedom, independence and choice to track the development of the female protagonist.{Style.RESET_ALL}")
    search_term = input("Enter a word or a phrase related to feminism: ").strip().lower()
    print(f"{Fore.RED}Let's see how often your chosen term appears in different parts of the book.{Style.RESET_ALL}")
    for i, part in enumerate(parts):  # count occurrences of the entered word or phrase in each part to check the changes of the female protagonist 
        occurrences = part.lower().count(search_term)
        print(f"Occurrences of '{search_term}' in PART {i + 1}: {occurrences}")
elif answer == 'no':
    print("Okay. Then try any key words or phrases you'd like to explore about the novel.")
    search_terms = input("Enter multiple words or phrases related to any theme, separated by commas: ").strip().lower().split(',')
    for i, part in enumerate(parts):  # count occurrences of the entered words or phrases in each part
            print(f"{Fore.CYAN}In PART {i + 1}:{Style.RESET_ALL}")
            for term in search_terms:
                term = term.strip()  # remove any extra spaces
                occurrences = part.lower().count(term)
                print(f"Occurrences of '{term}': {occurrences}")
    print(f"{Fore.GREEN}Isn't it fascinating to see how your chosen terms evolve throughout the book?{Style.RESET_ALL}")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
    

# close the file
f.close()