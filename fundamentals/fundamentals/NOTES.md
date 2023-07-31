# Primitive data types

These are the basic building blocks of a language. Most languages have these in common:

Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
is_hungry = True
has_freckles = Falsecopy
Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35 # storing an int
weight = 160.57 # storing a floatcopy
Strings - literal text
name = "Joe Blue"copy
Composite types
These are collections composed of the above primitive types.

Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])  # output: Bruce
dog[1] = 'dachshund' # ERROR: cannot be modified ('tuple' object does not support item assignment)copy
Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])  # output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas) # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas) # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas) # output: ['Francis', 'Oliver']
copy
Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods here.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack' # updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)

## output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

w = new_person.pop('weight') # removes the specified key and returns the value
print(w)  # output: 160.2
print(new_person)

## output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}

copy
Common Functions
If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:

print(type(2.63))  # output: <class 'float'>
print(type(new_person))  # output: <class 'dict'>copy
For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:

print(len(new_person))  # output: 4 (the number of key-value pairs)
print(len('Coding Dojo')) # output: 11
