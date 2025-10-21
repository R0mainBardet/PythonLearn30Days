years = int(input("Enter number of years you have lived "))
years_left_to_live = 100 - years 

second_lived = years * 365 * 24 * 60 * 60 
left_to_live = years_left_to_live * 365 * 24 * 60 * 60 

print("You have lived for ", second_lived, "seconds")
print("You have ", left_to_live, "seconds left to live")