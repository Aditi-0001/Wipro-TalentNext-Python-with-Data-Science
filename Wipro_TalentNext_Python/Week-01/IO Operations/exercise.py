# Q.1 Write a program to read the entire content from a txt file and display it to the user. 

file_name = "aditi_sample.txt"  
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


# Q.2 Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter the number of lines to read: "))
filename = "aditi_sample.txt"

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        print(f"\nFirst {n} line(s) from '{filename}':\n")
        for i in range(n):
            print(lines[i], end='')

except FileNotFoundError:
    print(f"File '{filename}' not found.")


# Q.3 Write a program to accept input from user and append it to a txt file.

filename = "text_sample.txt"
user_input = input("Enter the text you want to append to the file: ")

try:
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print(f"Text successfully appended to '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")


# Q.4 Write a program to read contents from a txt file line by line and store each line into a list.

filename = "aditi_sample.txt"
lines_list = []

try:
    with open(filename, 'r') as file:
        for line in file:
            lines_list.append(line.strip())  
    print("Contents of the file as a list:")
    print(lines_list)

except FileNotFoundError:
    print(f"File '{filename}' not found.")


# Q.5 Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

filename = "aditi_sample.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
        print("The longest word in the file is:", longest_word)

except FileNotFoundError:
    print(f"File '{filename}' not found.")


# Q.6 Write a program to count the frequency of a user entered word in a txt file.

filename = "aditi_sample.txt"
search_word = input("Enter the word to search in the file: ").strip()

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.lower().split()
        search_word = search_word.lower()
        frequency = words.count(search_word)
        print(f"The word '{search_word}' appears {frequency} time(s) in the file.")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
