# Conditional Statements (if , else , and elif)
# if Statement

time = 20 #20 represents 8pm in the 24 format
if time == 20:
    print("It's time for dinner!")
    
# else Statemet

x = int(input("Enter the value of x : "))
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd") 

# elif Statement

signal = input("Enter the signal colour : ")
if signal == "red":
    print("STOP")
elif signal == "yellow" :
    print("READY")
else :
    print("GO")
    
# Checking Bus Ticket Price
    
age = int(input("Enter your age : "))

if age < 5 :
    print("Ticket is free")
elif age <= 12 :
    print("You get a child discount")
elif age >= 60 :
    print("You get a senior citizen discount")
else :
    print("You pay the full fare")
    
# Comparing two conditions in if statement using logical operations

age = 16
has_student_id = True

if age < 18 and has_student_id :
    print("You are eligible for the student dicount")
else :
    print("You are not eligible for the student dicount")

