#Question 1
print("Question 1")
input_string = "Python is a case sensitive language"
#part a
print("Part a")
print(len(input_string))
print("\n")

#partb
input_string=input_string[::-1]
print("Part b")
print(input_string)
print("\n")

#partc
print("part c")
input_string=input_string[::-1]
popped=input_string[10:26]
print(popped)
print("\n")

#part d
print("part d")
input_string=input_string.replace("a case sensitive","object oriented")
print(input_string)
print("\n")

#part e
input_string = "Python is a case sensitive language"
print("part e")
print(input_string.index("a"))
print("\n")

#part f
print("part f")
input_string=input_string.replace(" ","")
print(input_string)
print("\n")
#################################################################################
#Question 2
print("Question 2")
name=input("Please enter your name-")
SID=input("Please enter your SID- ")
Dept_name=input("Please enter your department name- ")
CGPA= input("Please enter your CGPA- ")

print('Hey, %s here!\nMy SID is %s\nI am from %s and my CGPA is %s'%(name,SID,Dept_name,CGPA))
#################################################################################
#Question 3
print("Question 3")


a = 56
b = 10

#Part A
print("Part A")
print(" a&b : ", a & b)
print("\n")

#Part B
print("Part B")
print(" a|b : ", a | b)
print("\n")

#Part C
print("Part C")
print(" a^b : ", a ^ b)
print("\n")

#Part D
print("Part D")
# Left shift both a and b with 2 bits.
print("a << 2 : ", a << 2, "\tb << 2 :", b << 2)
print("\n")

#Part E
# Right shift a with 2 bits and b with 4 bits.
print("Part E")
print("a >> 2 : ", a >> 2, "\tb >> 4 :", b >> 4)
###################################################################################
#Question 4
print("Question 4")

# taking input of 3 numbers from the user.
a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

#finding the highest no.
if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c


print(f"Highest no. = {highest_number}")
####################################################################################
#Question 5
print("Question 5")
string_entered= input("Please enter a string -")
string_entered=string_entered.lower()
if "name" in string_entered:
    print("Yes")
else:
    print("No")
####################################################################################
#Question 6
print("Question 6")
side_a=int(input("length of side A- "))
side_b=int(input("length of side B- "))
side_c=int(input("length of side C- "))

print("Is this triangle possible?")
if side_a>side_b+side_c or side_b>side_c+side_a or side_c>side_b+side_a:
    print("No")
else:
    print("Yes")
#####################################################################################
