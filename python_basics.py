# Strings
# A symbol (Word, nummber etc.)
# For it to be a string you have to use the "" or '' in the definition of the variable 
first_name = "Thierry"
food = "Pizza"
email = "thierry.oesch@icloud.com"
print(first_name)


# Integers
# for Numbers
# only full numbers
age = 17
quantity = 5
number = 30

# float
# there is no limit like in C# 
# no different types of floats 
price = 10.99
exam_result = 5.5
distance = 11.967

# boolean
# Unlikely for prints. More in if/else Statments
# in a if statment it alway prints the "if" it's true. 
# On the other Hand it will print the else statment if the variable is False
is_student = True

# print
variable = "variable"
print("For a Text")

print(f"For a Text and a {variable}.")
print(variable)
print(type(variable))
print("This is for a break in the output\n")

# if/else statment

# normaly if/else statments look like this:
car = "Porsche 918 Spyder"

if car == "Porsche 918 Spyder":
    print("You are right")
else:
    print("You are wrong")

# in a boolean you can do it like this
if is_student: 
    print("\nYou are a Student") # it will print this when the is_student variable is True
else:
    print("You are NOT a student") # it will print this when the is_student variable is False