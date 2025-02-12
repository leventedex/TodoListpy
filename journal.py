import os
# Define the subdirectory name
subdirectory = "files"

# Get the current directory where the script is running
current_directory = os.getcwd()

# Create the full path for the subdirectory
files_directory = os.path.join(current_directory, subdirectory)

# Check if the subdirectory exists, if not, create it
if not os.path.exists(files_directory):
    os.makedirs(files_directory)

# Define the file name and path
date = input("Enter the date: ")
file_name = date+".txt"
file_path = os.path.join(files_directory, file_name)

mood = input("Enter your mood rated from 1 to 10: ")
journal = input("Enter your journal:\n ")

with open(file_path, 'w') as file:
    file.write(mood + 2 * "\n")
    file.write(journal)
    print(file_path+" Journal saved!")
