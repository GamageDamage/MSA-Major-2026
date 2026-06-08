'''# Print Hello World
print("Hello World")

#create a variable to store my name
first_name = "Evin"

#create a variable for the last name
last_name = "Gamage"

#write a python statement to display "My full name is firstname lastname"
print("My full name is",first_name,last_name,sep=' ')

print(f"My full name is {first_name} {last_name}")

age = 16
weight = 150.5
half_age = age/2

#print(f"My full name is {first_name} {last_name}\nI am {age} years old.\nI weigh {weight} lbs")


#get and print the data type for age, weight, and half-weight

print("\n")
print(type(age))
print(type(weight))
print(type(half_age))


#write 3 statements using string interpitation to print descriptive for the data types
v=str(type(age))
x=v.replace("<class \'",'')
v=x.replace("\'>",'')
print(f"Variable age is an {v}")

v=str(type(weight))
x=v.replace("<class \'",'')
v=x.replace("\'>",'')
print(f"Variable weight is an {v}")

v=str(type(half_age))
x=v.replace("<class \'",'')
v=x.replace("\'>",'')
print(f"Variable half age is an {v}")'''


