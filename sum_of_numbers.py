#!/usr/bin/env python3

# Created By: Amara Tie

# Date: April 8, 2025

# This is a program gets the sum of a number


def main():

    # Ask User for a number
    user_as_string = input("Enter a positive number :")
    print("")

    # Initialize counter
    loop_counter = 0
    sum = 0
    
    # Use a while loop to add all the integers from 0
    try:
        user_as_number = int(user_as_string)
        # Check if the number is positive 
        if user_as_number > 0: 
            while loop_counter < user_as_number:
                print("{} THE TIME OF LOOP.".format(loop_counter))
                loop_counter = loop_counter + 1
                sum = loop_counter + sum
            print("The sum is {}".format(sum))
        else:
            print("Please enter a positive number")
    except Exception:
        print("This is not a number")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
