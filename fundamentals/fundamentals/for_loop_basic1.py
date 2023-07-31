# Basic - Print all integers from 0 to 150.
def print0_to_150():
    for i in range(0, 150):
        print(i)

    
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def multipleof_5_to_1k():
    for i in range(0,1000,5):
        print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def dojo_count():
    for i in range(1,100):
        if i % 10 == 0:
            print("Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def oddcount_500000():
    sum = 0
    for i in range(0,500000):
        if i % 2 == 1:
            sum += i
    print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def countdown():
    for i in range(2018,0, -4):
        print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_counter(lowNUm, highNum,mult):
    for i in range(lowNUm, highNum+1):
        if i % mult == 0:
            print(i)








######### function call##############
# print0_to_150()
#works!

# multipleof_5_to_1k()
# works!

# dojo_count()
# works!

# oddcount_500000()
# works!

# countdown()
# works!

# flex_counter(2,9,3)
# works