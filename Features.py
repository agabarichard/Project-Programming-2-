
try:
    fav_number = int(input("What is your favorite number? "))
    
    # Conditional statements to check if even or odd
    if fav_number % 2 == 0:
        print(f"{fav_number} is an even number.")
    else:
        print(f"{fav_number} is an odd number.")
    
    # Chained and nested conditionals
    if fav_number > 10:
        print("That's a big number!")
    elif fav_number < 10:
        print("That's a small number!")
    else:
        print("Your favorite number is exactly 10!")
except ValueError:
    print("Please enter a valid number!")
