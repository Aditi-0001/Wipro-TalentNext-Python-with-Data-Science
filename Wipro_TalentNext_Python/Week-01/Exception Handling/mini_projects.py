                               # MINI PROJECTS


# Purchase

"""
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:

1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.

Note:

Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.

Sample input 1:

Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5

Sample output 1:

Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:

Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup, Free
(blank line)
Discount 80

Sample output 2:

Enter the file name: Purchase-1
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405
"""

# Program
def main():
    try:
        filename = input("Enter the file name: ").strip()
        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, 'r') as file:
            lines = file.readlines()

        purchased_items = 0
        free_items = 0
        total_amount = 0
        discount = 0
        discount_found = False

        for line in lines:
            line = line.strip()
            if not line:
                continue  

            if "Discount" in line:
                try:
                    discount = int(line.split()[-1])
                    discount_found = True
                except ValueError:
                    print("Invalid discount value.")
                    return

            elif "Free" in line:
                free_items += 1

            else:
                parts = line.split()
                if len(parts) < 2:
                    continue 
                try:
                    price = int(parts[-1])
                    total_amount += price
                    purchased_items += 1
                except ValueError:
                    print(f"Invalid price found in line: '{line}'")
                    return

        final_amount = total_amount - discount

        print(f"No of items purchased: {purchased_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
