# Activity 1: Fizz Buzz
# Write a code in python in which you can get “Fizz Buzz” for all numbers which can be divided by 
# (3, 5, 15). The range should from (1 to 100)


for num in range(1, 101):  
    if num % 15 == 0:        
        print("FizzBuzz")
    elif num % 3 == 0:       
        print("Fizz")
    elif num % 5 == 0:       
        print("Buzz")
    else:
        print(num)          

print('------------------------------------------------------')


# Activity 2: Swap Cases 
# How to swap all uppercase characters to lowercase and vice versa?
text = input("Enter any text: ")
swapped_text = text.swapcase()
print("swapped case:", swapped_text)


print('------------------------------------------------------')


# Activity 3: Swap Numbers 
# Taking input
a = int(input("Enter a number"))
b = int(input("enter a second number"))

temp = a
a = b 
b = temp
print("After swapping a=", a, "b=", b)


print('------------------------------------------------------')


# Activity 4: Fibonacci Series 
# Write a code in python which will give you a Fibonacci series to a number when you enter it.

# Step 1: user enters a number
n = int(input("Enter a number: "))

# Step 2: Initialize the first two Fibonacci numbers
a, b = 0, 1

print("Fibonacci Series up to", n, ":")

# Step 3: Generate Fibonacci numbers up to 'n'
while a <= n:
    print(a, end=" ")
    a, b = b, a + b  # update values


print('------------------------------------------------------')


# Activity 5: Number Guessing Game
# Create a game in which user guesses a random number in python.
import random

print("🎯 Welcome to the Number Guessing Game!")

number = random.randint(1, 50) 
attempts = 5  
while attempts > 0:
    # Get user's guess
    guess = int(input("Guess the number (1 to 50): "))

    # Check if guess is correct
    if guess == number:
        print("🎉 YOU WON! The number was", number)
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    # Subtract one attempt
    attempts -= 1
    print("Attempts left:", attempts)
    print("--------------------")

if attempts == 0:
    print("😞 YOU LOST! The number was", number)


print('------------------------------------------------------')

#  Activity 6: Basic Calculator
# Create a Basic Calculator that can do Addition, Subtraction, Multiplication and Division in Python.
# Basic Calculator in Python

print("🧮 Basic Calculator")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid input! Please select from 1 to 4.")