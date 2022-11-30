name= "harshit"
age = 24
print("hello {} your age is {}".format(name,age))#python 2

print(f"hello {name} your age is {age}")#python3


a=int(input("No.1 "))
b=int(input("No.2 "))
c=int(input("No.3 "))
avg=(a+b+c)/3
print(f"average of three numbers {avg}")

#different functions of string

s="language"
print(s[2])
print(s[0:2])
print(s[1:])
print(s[:3])

#step argument

s="language"
print(s[0::2])
print(s[0:5:2])

#Practice Excercise
name=input("Enter a name:")
reverse=name[-1::-1]
print(reverse)



