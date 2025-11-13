# -------------------------------------------
# Exercise 0: Comments Practice
# -------------------------------------------
# In this exercise, you'll practice writing clear, helpful comments
# to explain Python code.
#
# Good comments should:
# - Explain WHAT the code does (not just repeat it)
# - Be clear and concise
# - Help someone else understand your code
#
# Below you'll find several code snippets.
# Add comments to explain what each section does.
# -------------------------------------------

# -------------------------------------------
# Task 1: Shopping Cart
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Shopping Cart\n"
      + "-------------------------------------------")

# Add comments to explain this code:

cart = ["apple", "bread", "milk", "eggs"]               #Creates list [cart] with 4 set strings
total_items = len(cart)                                 #Creates new variable (total_items) assigned to the number of items in (cart)

print(f"You have {total_items} items in your cart")     #Outputs sentence containing the length of list (cart)

for item in cart:                                       #Following code is executed for every item in list (cart)
    print(f"- {item}")                                      #Outputs each item in list (cart) in a neat way

# -------------------------------------------
# Task 2: Grade Calculator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Grade Calculator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

score = int(input("Enter your test score: "))           #Creates variable (score) assigned to the integer given by the user

if score >= 70:                                         #Checks if (score) is greater than or equal to 70
    grade = "Pass"                                          #If previous check was True, variable (grade) is created and assigned to the string, "Pass"
else:                                                   #If previous check was false, execute this code instead
    grade = "Fail"                                          #Create variable (grade) and assignes it to the string, "Fail"

print(f"Your grade: {grade}")                           #Outputs a sentence including the variable (grade)

# -------------------------------------------
# Task 3: Password Validator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Password Validator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

password = input("Create a password: ")                 #Creates variable (password) assigned to the user's input
        
is_long = len(password) >= 8                            #Checks if (password) length is greater than or equal to 8 characters and assigns boolean (is_long) in reference
has_upper = password != password.lower()                #Checks if (password) has any uppercase characters and assigns boolean (has_upper) in reference
has_lower = password != password.upper()                #Checks if (password) has any lowercase characters and assigns boolean (has_lower) in reference

is_valid = is_long and has_upper and has_lower          #Creates (is_valid) based on the state of previous 3 variables, (is_long), (has_upper) and (has_lower)

if is_valid:                                            #Executes following code if (is_valid) is True
    print("Password accepted!")                             #Outputs following string
else:                                                   #Executes if previous condition is not met
    print("Password rejected. Must be 8+ characters with upper and lowercase letters.") #Outputs following string

# -------------------------------------------
# Task 4: Even Number Counter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Even Number Counter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

numbers = [12, 7, 18, 5, 22, 9, 14]                     #Creates [numbers] list
even_count = 0                                          #creates (even_count)

for num in numbers:                                     #Repeats for every item in list (numbers)
    if num % 2 == 0:                                        #Checks if the number is even by checking if the remainder when divided by 2 is 0
        even_count = even_count + 1                             #If previous condition is met, add 1 to (even_count)

print(f"There are {even_count} even numbers in the list")   #Outputs sentence displaying (even_count)

# -------------------------------------------
# Task 5: Student Records
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Student Records\n"
      + "-------------------------------------------")

# Add comments to explain this code:

student = {                                                 #Creates dictionary {student} with keys and values set
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78, 88]
}

average = sum(student["grades"]) / len(student["grades"])   #Creates (average) assigned to the sum of the students grades divided by the total amount of grade values
average = round(average, 2)                                 #Rounds (average) to 2 decimal places

print(f"Student: {student['name']}")                        #Outputs student name in a neat way
print(f"Age: {student['age']}")                             #Outputs student age in a neat way
print(f"Average grade: {average}")                          #Outputs (average) in a neat way

# -------------------------------------------
# Task 6: Countdown Timer
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Countdown Timer\n"
      + "-------------------------------------------")

# Add comments to explain this code:

countdown = 5                                               #Creates (countdown) assigned to 5

while countdown > 0:                                        #Repeats while (countdown) is greater than 0
    print(countdown)                                            #Outputs (countdown)
    countdown = countdown - 1                                   #Lowers the value of (countdown) by 1

print("Blast off!")                                         #Executes after breaking out of the loop, outputs following string

# -------------------------------------------
# Task 7: Menu Formatter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Menu Formatter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

menu_items = ["burger", "pizza", "salad", "pasta"]          #Creates [menu_items] list with assigned values
counter = 1                                                 #Creates (counter) assigned to 1

for item in menu_items:                                     #Loops for every item in [menu_items]
    formatted_item = item.upper()                               #Creates (formatted_item) assigned to the item called and makes the whole string uppercase
    print(f"{counter}. {formatted_item}")                       #Outputs (counter) and (formatted_item) in a neat way
    counter = counter + 1                                       #Increases (counter) by 1

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've added comments to all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
