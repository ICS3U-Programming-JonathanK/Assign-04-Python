#!/usr/bin/env python3

# Created by: Jonathan
# Created on: May 25, 2021
# The program will prompt the user to input a positive integer. 
# It will then print the multiplication table of that number
# with the numbers 0 to 10 and a division table if the user wants it.

def main():
    # initialize the counter
    counter = 0


# get the user number as a string
user_number_string = input("Display multiplication table of? ")

try:
    user_number_int = int(user_number_string)
except ValueError:
    print("")
    print("Please enter a valid number")

else:
    if (user_number_int < 0):
        print("")
        print("{} is not a positive number". format(user_number_int))
    else:
        # Iterate 10 times from i = 1 to 10
        for counter in range(1, 13):
            print(user_number_int, 'x', counter, '=', user_number_int*counter)

        # get the user number as a string
        next_question = input("Would you like to divide the number as well?"
                              "Type 'yes' or 'no': ")
        try:
            # get the user number as a string
            next_question_string = str(next_question)
        except UnboundLocalError:
            print("")

        if(next_question == 'yes'):
            # Iterate 10 times from i = 1 to 10
            for counter in range(1, 13):
                print(user_number_int, '÷', counter, '=',
                      "{:.2f}". format(user_number_int/counter))
        elif (next_question == 'no'):
            print("")
            print("Very well")
        else:
            print("")
            print("Since the input isn't yes, I'll assume it means no")

finally:
    print("")
    print("Thank you for your input")


if __name__ == "__main__":
    main()
