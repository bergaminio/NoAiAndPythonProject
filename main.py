# This is a simple Python program
print("I LOVE SUSHI!")
print("Its really good for you and tastes amazing!")

#Variables
Name = "Sushi" # String variable
print(f"i like {Name}")
price = 12# Integer variable
print(f"the price of sushi is {price} dollars")
float_price = 12.99 # Float variable
print(f"the price of sushi is {float_price} dollars")
in_stock = True # Boolean variable
print(f"Is sushi in stock? {in_stock}")
if in_stock:
    print("Yay! I can buy sushi!")
else:
    print("Oh no! I can't buy sushi.")
#arithmetic operations
#// integer division rounds down to the nearest whole number
print(f"the price of sushi divided by 2 is {price // 2} dollars")
# % modulus operator /remainder
print(f"the price of sushi divided by 5 leaves a remainder of {price % 5} dollars")
#augmented assignment operator
price = price + 2 # Full operation
price += 2 # price = price + 2# short hand operation
print(f"the new price of sushi is {price} dollars")


#type conversion
print(type(Name))# Output: <class 'str'>
price_float = int(price) 
print(price_float)# Output: 16

#user input
favorite_sushi = str
favorite_sushi = input("enter your favorite sushi: ")
print(f"your favorite sushi is {favorite_sushi}")