# Day 2: 30 Days of python programming
import math

first_name = "Romain"
last_name = "Bardet"
full_name = first_name + " " + last_name
country = "France"
city = "Paris"
age = 210
year = 1815
is_married = True
is_true = False
is_light_on = False
x , y , z = 1, 2, 3

print(type(first_name))
print(type(last_name))
print(type(full_name ))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

print(len(first_name))

num_one = 5
num_two = 4
total = sum([num_one, num_two])
total2 = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
Divide =  num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
r = 30
area_of_circle = math.pi * (r) ** 2
circum_of_circle = 2 * math.pi * r

r_user = float(input("give me radius :"))
area_of_circle_user = math.pi * (r_user) ** 2
circum_of_circle_user = 2 * math.pi * r_user

print(int(area_of_circle))
print(circum_of_circle)
print(area_of_circle_user)
print(circum_of_circle_user)

first_name_user = input("give first name :")
last_name_user = input("give last name :")
country_user = input("give country :")
age_user = int(input("give age :"))

help('keywords')