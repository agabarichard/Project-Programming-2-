# Simple program to greet the user and calculate birth year
print("Welcome to Computer Science class!")

# Getting user's name
name = input("Please enter your name: ")
print(f"Hello, {name}! Nice to meet you.")

# Getting user's age
try:
    age = int(input("Please enter your age: "))
    birth_year = 2024 - age
    print(f"You were born in the year {birth_year}.")
except ValueError:
    print("Invalid input! Please enter a numeric value for age.")
