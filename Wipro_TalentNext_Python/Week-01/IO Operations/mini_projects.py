""" 
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go 
and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the 
challenge with our python code.

Hints to find the secret message:

1. The number of lines in the file tells you the meeting time.
Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour format. For example,
-If the number of lines is 15, then the meeting time is 3 PM.
-If the number of lines is 10, then the meeting time is 10 AM.

2. The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name.
For example,
-If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
-If the word Park appears for the maximum number of times, then meeting place is Park Street.

Sample input 1:
Sample1.txt

Sample output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times.

Sample input 2:
Sample2.txt

Sample output 2:
Meeting time: 8 PM
Meeting place: Apollo Street
Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. The word Apollo appears for the maximum of 25 times.
"""

# Program
from collections import Counter
filename = "sample1.txt"

def format_time(lines_count):
    return f"{lines_count} AM" if lines_count <= 12 else f"{lines_count - 12} PM"

def find_place(word_list):
    count = Counter(word_list)
    place = count.most_common(1)[0][0]
    return f"{place.capitalize()} Street"

def process_file():
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)

            text = ' '.join(lines).lower()
            words = [''.join(c for c in word if c.isalpha()) for word in text.split()]
            words = [word for word in words if word]

            time = format_time(total_lines)
            place = find_place(words)

            print(f"Meeting time: {time}")
            print(f"Meeting place: {place}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

process_file()
