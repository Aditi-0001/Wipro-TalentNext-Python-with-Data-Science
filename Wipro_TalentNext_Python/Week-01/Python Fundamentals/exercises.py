# Q.1 Write a program to check if a given number is Positive, Negative or Zero.
def check_number(n):
    if (n>0):
        print("positive")
    elif (n<0):
        print("negative")
    else :
        print("zero")

n = int(input("Enter n:"))
check_number(n)


# Q.2 Write a program to check if a given number is odd or even.
def even_odd(n):
    if (n%2==0):
        print("even")
    else :
        print("odd")

n = int(input("Enter n:"))
even_odd(n)


# Q.3 Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
def if_same_digit(m,n):
    if (m%10 == n%10):
        print("true")
    else :
        print("false")

m = int(input("Enter m:"))
n = int(input("Enter n:"))
if_same_digit(m,n)


# Q.4 Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11,1):
    print(i,end="\t")


# Q.5 Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(24,58,2):
    print(i)


# Q.6 Write a program to check if a given number is prime or not.
def check_prime(n):
    flag = 0
    for i in range(2,int(n/2)):
        if (n%i==0):
            flag = 1
    if(flag==0):
        print("prime")
    else:
        print("not prime")

n = int(input("Enter n:"))
check_prime(n)


# Q.7 Write a program to print prime numbers between 10 and 99.
def check_prime(n):
    flag = 0
    for i in range(2,int(n/2)):
        if (n%i==0):
            flag = 1
    if(flag==0):
        return True
    else:
        return False

for n in range(9,100):
    if (check_prime(n)):
        print(n,end=" ")


# Q8. Write a program to print the sum of all the digits of a given number.
def sum_of_digits(n):
    Sum = 0
    while(n!=0):
        rem = n%10
        Sum += rem
        n //= 10
    print(Sum)

n=int(input("Enter n:"))
sum_of_digits(n)


# Q.9 Write a program to reverse a given number and print.
def reverse_num(n):
    Sum = 0
    i=0
    while(n!=0):
        rem = n%10
        Sum = Sum*10 + rem
        n //= 10
        i=i+1
    print(Sum)

n=int(input("Enter n:"))
reverse_num(n)


# Q.10 Write a program to find if the given number is palindrome or not.
def reverse_num(n):
    Sum = 0
    i=0
    while(n!=0):
        rem = n%10
        Sum = Sum*10 + rem
        n //= 10
        i=i+1
    return Sum

n=int(input("Enter n:"))
if (n==reverse_num(n)):
    print("Palindrome")
else:
    print("Not Palindrome")