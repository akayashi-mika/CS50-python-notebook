
### Making Comments ###

# This is a single lined comment
"""
This is a multiple line comment
"""



name    =   input("What's your name? ")     # Ask the user for their name
# Say hello to user
print(f'hello,  {name}')
print('hello,'  + name)     # The "+" treats all variables as a single arguement
print('hello,', name)       # The "," treats the variables as different arguements



### Named Parameters ###

print('hello, ',    end='')
print(name)

print('hello, ',    end='???')
print(name)

print('hello,', name,   sep='???')



### Escaping Characters ###

print('hello, "friend"')
print('hello, \'friend\'')  # The character \ is an escape character used to nullify the effect of a command



### f-Strings ###

print(f'hello, {name}')



### String Methods ###

name    =   name.strip()         # Remove whitespace from str
print(f'hello, {name}')

name    =   name.capitalize()    # Capitalize the first word of the user's name
print(f'hello, {name}')

name    =   name.title()         # Capitalize each word of the user's name
print(f'hello, {name}')

name = name.strip().title()     # Remove whitespace from str & Capitalize each word of the user's name
print(f'hello, {name}')

name    =   input("What's your name? ").strip().title()     # Ask the user for their name & Remove whitespace from str & Capitalize each word of the user's name
print(f'hello, {name}')

### Split ###