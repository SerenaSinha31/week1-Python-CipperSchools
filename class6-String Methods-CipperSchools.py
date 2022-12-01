
name = "Harshit"
length = len(name)
print(length)

print(name.lower())
print(name.upper())
print(name.title())

print(name.count("h"))

#Excerise question

n=input()
r=input()
print(f'count the e in the sentence ={r.count("e")}')

na,char=input("Enter comma separated name and character:").split(",")
print(f"length of the name is{(len(na))}")
print(f"character count:{na.lower()}")
print(f"character count:{na.lower().count(char.lower())}")

#replace and find method

st="She is beautiful and she is good dancer"
print(st.replace("is","was,2"))

#center method

name="harshit"
name.center(9,"*")


#practice Question

name=input("Enter a name")
print(name.center(len(name)+8,"*"))

