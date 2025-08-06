work = input("Enter the name to the file: ")#Prompt user for file name and place it into variable 'work'

try:
    file = open(work, 'r')
    text = file.read()
    print(text)
except FileNotFoundError:
    print(f"Error: The file '{work}' does not exist.")