def iterateDictionary(some_list):
    for item in some_list:
        for key, value in item.items():
            print(f"{key} - {value}")


# Example list of dictionaries
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# iterateDictionary(students)


def iterateDictionary2(key_name, some_list):
    for item in some_list:
        for key_name, value in item.items():
            print(f"{key_name} - {value}")


iterateDictionary2('first_name', students)

# iterateDictionary2('last_name', students)
