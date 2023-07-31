num1 = 42 #variable declaration, initialize integer
num2 = 2.3 #variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log  data type of fruit variable
print(pizza_toppings[1]) #log value of index 1 of list pizza_toppings
pizza_toppings.append('Mushrooms') # add string 'Mushrooms' to list pizza_toppings
print(person['name']) # log corresponding key pair value from dictionary person
person['name'] = 'George' # assign value of key pair 'name' in dictionary  person
person['eye_color'] = 'blue' #  initialize and assign key pair value of 'eye_color' to 'blue' strings both
print(fruit[2])  # log string from tuple 'fruit'

if num1 > 45: # conditional if 
    print("It's greater") # result if above "if" boolean value is true
else: # if above conditional is true alternate route
    print("It's lower") # result if else  conditional is true

if len(string) < 5: # conditional for value of string length
    print("It's a short word!") #result if boolean value of above conditional is true
elif len(string) > 15: # secondary conditional to check if above is false
    print("It's a long word!") # result if "elif" condition boolean value is true
else: # else conditional is 'catch all' result container
    print("Just right!") # result if all above conditionals are false boolean value

for x in range(5): # for loop iterating to 5
    print(x) # action log of for loop
for x in range(2,5): # parameters for loop limiting range
    print(x) # action log of for loop
for x in range(2,10,3): # parameters for loop limiting range and step
    print(x) # action log of for loop
x = 0 #assign x variable value of int 0
while(x < 5): #while loop  for value of x being less than 5
    print(x) # log value of 'x' variable
    x += 1 # step value of while loop

pizza_toppings.pop() # method to remove last value of list
pizza_toppings.pop(1) # method to remove value of referenced index

print(person) #log of  dictionary
person.pop('eye_color') #method to remove dictionary key-pair value
print(person) # log modified dictionary

for topping in pizza_toppings: # for loop using items in list to iterate
    if topping == 'Pepperoni': # conditional for specific value of iterated list item
        continue # keyword to move to next iteration 
    print('After 1st if statement')  #log result string
    if topping == 'Olives': # conditional for specific value of iterated list item
        break # end loop

def print_hello_ten_times(): # define function
    for num in range(10): # for loop iterating using num variable for range function parameter set to integer 10
        print('Hello')  # log result string

print_hello_ten_times() #call function

def print_hello_x_times(x): #define function with parameter 'x'
    for num in range(x): # for loop iterating using num variable for range function parameter set to value of 'x'
        print('Hello') # result print string 

print_hello_x_times(4) # call function setting parameter x assigned to value integer 4

def print_hello_x_or_ten_times(x = 10): # call previous function setting undefined range value manually to ' x= 10'
    for num in range(x): # for loop using numb variable value in range of x value
        print('Hello') # result print string

print_hello_x_or_ten_times() # call previous defined function with no parameter defined
print_hello_x_or_ten_times(4) # call previous defined function with parameter defined as integer value of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)