# #Variables
# FavouriteNumber = 52000
# print(f"My favourate number:{FavouriteNumber}")

# #String
# greeting = "Hello, PLP Academy"
# print(greeting)

# is_python_boring = True
# is_python_fun = False
# print(f"Is Python fun?{is_python_fun}")
# print(f"Is Python boring{is_python_boring}")

# #Control_Flow
# temperature = 30
# if temperature > 25:
#     print("Its hot outside! Wear shorts. ")
# elif temperature > 15:
#     print("Its warm, Bring a light jacket. ")
# else: 
#     print("brrrr, Its cold. ")     

# #Loops for emxample
# for i in range(5):
#     print(f"This is loop iteration {i}")

# #While loop example
# countdown = 5
# while countdown > 0:
#     print(f"Countdown: {countdown}")
#     countdown -= 1
# print("Blast off!")

#Defining a function
# def greet(name):
#     return f"Hellow, {name}"

# #Using the function
# print(greet("Azola"))
# print(greet("amy"))

#list example
# fruits = ["apple","bananas","cherry"]
# print(f"My favourate fruit if {fruits[0]}")

# #Dictionary example
# contacts = {
#     "Azola": "078-697",
#     "Bob": "078-586"
# }
# print(F"Alice's phone number is {contacts['Azola']}")

#Using the built-in math module
import  math

#Using a function from the math module
result = math.sqrt(8)
print(f"The suqare root of 8 is {result}")

#Creating and using your own module
# Save this code in a file named my_module.py
def greet(name):
    return f"Hello, {name}"

#Now in your main script, you can import and use it
import Day2

print(Day2.greet("Gcina"))