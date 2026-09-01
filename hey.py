age = input("enter string")
i = 0
bool =True
while i < len(age):
    if age[i] != age[-(i + 1)]:
        bool = False
if bool:
    print("yes")
else:
    print("not")


#2
age = input("enter string")
i = 0
c =1
while i < len(age):
    if age[i] == ' ':
       c = c+1
 print(c)
 #3
age = input("enter string")
str=age[0]
i = 1
while i < len(age):
    if age[i] == ' ':
      str += age[i-1]
 print(str)