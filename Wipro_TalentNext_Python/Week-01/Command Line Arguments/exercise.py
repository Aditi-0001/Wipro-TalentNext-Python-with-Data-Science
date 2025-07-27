# Q.1 Write a program to accept two numbers as command line arguments and display their sum.

import sys
if len(sys.argv) != 3:
    print("Usage: python filename.py <num1> <num2>")
else:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        print("Sum:", n1 + n2)
    except ValueError:
        print("Please enter valid integers.")


# Q.2 Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
if len(sys.argv) < 2:
    print("Usage: python filename.py <welcome message>")
else:
    file_name = sys.argv[0]
    msg = " ".join(sys.argv[1:])
    print("File Name:", file_name)
    print("Welcome Message:", msg)


# Q.3 Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python filename.py <num1> <num2> ... <num10>")
else:
    try:
        nums = [int(arg) for arg in sys.argv[1:]]
        prime_sum = sum(n for n in nums if is_prime(n))
        print("Sum of prime numbers:", prime_sum)
    except ValueError:
        print("Please enter valid integers.")