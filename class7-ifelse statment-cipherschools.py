age=int(input("input a number"))
if age >= 15:
    print(age)
    print("you are eligible")
# if else statment
age1=int(input("input a number"))
if age>=14:
    print("you are elligible")
else:
    print("sorry you cant play")


#nested if else statment

Winning_number=27
user_input=int(input())

if user_input == Winning_number:
    print("too high")
else:
    if user_input < Winning_number:
        print("two low")
    else:
        print("too high")
                
#Check two conditions at same time

#and,or

name="abc"
age=19
if name == "abc" and age == "19":
    print("condition true")
else:
    print("Condition false")  


#practice question
#if elif else statment 

age = int(input("Enter a number"))
if age==0 or age<0:
    print("you can't watch")
elif 0<age<=3:
    print("Ticket price:free")
elif 3<age<=10:
    print("ticket price:150")
elif 10<age<=60:
    print("ticket price:150")
else:
    print("ticket price:200")                   
                

