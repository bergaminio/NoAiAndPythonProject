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


#Typecasting
    #Explicit, that means you convertet the variable manually
age = 21
gpa = 0
#when you convert a nummber into a bool it will always be True exept if it is 0
gpa = bool(gpa)
print(gpa)

name = ""
student = True

student = str(student)
print(student)
# a str will always be True exept if there is nothing in it
name = bool(name)
print(name)

    #Implicit, Automatic

#X becomes a float automatically
x = 2
y = 2.2
x = x / y
print(x)

#Input
#name = input("What is you name? ")
#age = int(input("What is your age? "))

#age = age + 1

#print(f"Your name is {name}")
#print(f"You are {age} years old")

#exercise for input 
#mad libs

#adjektive1 = input("\nEnter an adjektive: ")
#noun = input("Enter a noun: ")
#adjektive2 = input("Enter a second adjektive: ")
#verb = input("Enter a verb: ")
#adjektive3 = input("Enter a third adjektive: ")


#print(f"\nTody I went to a {adjektive1} school")
#print(f"In one of the classrooms I saw a {noun}")
#print(f"The {noun} was {adjektive2} and {verb}")
#print(f"It was {adjektive3}")


#area clac
#length = float(input("\nEnter the length of a cube: "))
#width = float(input("Enter the width of a cube: "))
#heigth = float(input("Enter the height of a cube: "))

#volume = length * width
#print(f"\n{volume}cm3")

#shopping cart
item =  input("\nWhat item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"\nYou have bought {quantity} x {item}/s")
print(f"Your total is: {round(total, 2)} Fr.") #with rounding

#Math
#addition
friends = 0

friends = friends + 1 #or
friends += 5
#subbtraktion
friends -= 1
#multiply
friends *= 2
#dividion (is a float)
friends /= 2  
# to the power of
friends **= 2
#remainder
remainerder = friends % 6

print (remainerder)
print(friends)