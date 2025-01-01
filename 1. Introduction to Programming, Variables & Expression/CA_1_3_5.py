# Course = IT 140 - Introduction to Scripting
# Southern New Hampshire University
# Module 1 - Introduction to Programming, Variables & Expression
# 1.3 Basic Input and output
# Challenge Activity 1.3.5: Read user input and print to output.

# The first line of code provided in the code windows reads an integer value from
# into user_num1.
# The second line of code provided in the code window reads an integer value from
# input into user_num2.
# Complete the program as follows:
# 1. Write a line of code that reads an integer value from input into user_num3.
# 2. Write a print() statement that outputs the product of user_num1, user_num2, 
# user_num3.

user_num1 = int(input())                    # reads user input and stores in user_num1
user_num2 = int(input())                    # reads user input and stores in user_num2
user_num3 = int(input())                    # reads user input and stores in user_num3

# prints the product of user_num1, user_num2, and user_num3 on screen
print(user_num1 * user_num2 * user_num3)
