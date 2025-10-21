import math

integer = 5
Float = 3.6
complex = 4 - 3j

string = "Romain"
boolean = True
list = [1, 2, 3, 4, "Romain"]
tuple = (5, 6, 7, 8, "Bardet")
set = {9, 10, 11, 12, "France"}
dictionary = {
    "name" : "Romain",
    "family name" : "Bardet",
    "country" : "France"
}

p1 = 2
p2 = 3
q1 = 10
q2 = 8
d = math.sqrt(((p1 - q1)**2) + ((p2 - q2)**2))

print(d)
d_int = int(d)
print(d_int)
d_string = str(d)
print(d_string)
d_list = list(d_string)
print(d_list)