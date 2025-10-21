a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print('{} + {} = {}'.format(a, b, a + b))
print('%d + %d = %d' %(a, b, a + b))

language = "Python"
c, d, e, f, g, h = language # ne peux pas moins
print(c)
print(d)
print(e)

first_lettre = language[0]
print(first_lettre)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

first_three = language[0:3]
print(first_three) #Pyt
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

