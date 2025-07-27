                               # MINI PROJECTS


# Ride on miles

""" 
1. Create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride
    Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to
    travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination
"""

# Program
dist = int(input("How far would you like to travel in miles?"))
if (dist<3):
    print("I suggest Bicycle to your destination")
elif (dist>3 and dist<300):
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")



""" 
2.	Let's assume you are planning to use your python skills to build an App for Mobile.
    You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following
questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918?
"""

#Program
per_day = 0.51 * 24
print("How much does it cost to operate one server per day?")
print("Cost for per day : ",per_day)

per_week = per_day * 7
print("How much does it cost to operate one server per week?")
print("Cost for per week : ",per_week)

per_month = per_day * 30
print("How much does it cost to operate one server per month?")
print("Cost for per month : ",per_month)

days = 918/0.51
print("How much days can I operate one server with $918?")
print("Number of days :",int(days))