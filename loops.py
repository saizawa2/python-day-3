# 2 kinds of loops 1. While loops 2. For loops
# While loop - you don't know how many times it's going to happen
# For loop - when you know the amount of times
'''
While loop is high risk of creating an infinite loop!
risk of creating an infinite loop
2 ways to avoid the infinite loop:
    1. make a condition that can be False
    2. use the break keyword
'''

borrow_sweater = input("Can I borrow your sweater?")
while borrow_sweater != "Yes":
    borrow_sweater = input("Can I borrow your sweater?")
    if borrow_sweater == "Yes":
        print("Thank you!")
    else: 
        print("oh no")


while True:
    borrow_sweater = input("Can I borrow your sweater?")
    if borrow_sweater == "Yes":
        print("Thank you!")
        break
    else:
        print("oh no")


# Blastoff
# Create a countdown before a spaceship launches
count = 10
while count >= 1:
    print(count)
    count = count - 1
    if count < 1:

print("Blastoff!")



