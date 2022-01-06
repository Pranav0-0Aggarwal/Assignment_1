#Question 1
print("Question 1")
#Taking input from user and storing it in 3 variables
number_1=int(input("Plz Give an Input for first number- "))
number_2=int(input("Plz Give an Input for second number- "))
number_3=int(input("Plz Give an Input for third number- "))

#Using the formula to calculate the average
average=(number_1+number_2+number_3)/3

#printing the average
print(average)

###########################################################
#Question 2
print("Question 2")
#taking input from user
gross_income=float(input("Enter your gross Income sir-$"))
Num_Dependants=int(input("Enter total number of Dependants-"))

#rounding of tax to pennies
gross_income=round(gross_income,2)

#Defnining some variable some required constant values
std_deduction=10000
dep_deduction=3000
tax=0

#calculating the taxable income
taxable_income=gross_income-std_deduction-dep_deduction*Num_Dependants

#Checking if the taxable income is greater than 0
if taxable_income>0:
    tax=0.20*taxable_income
else :
    tax=0
#printing the tax
print("Your tax = ",tax,sep="$")

############################################################
#Question 3
print("Question 3")
#taking input from user
SID=int(input("SID-"))
Name=input("Name-")
Gender=input("Gender(F,M orU)-")
Course_name=input("Course name-")
Course_name=Course_name.upper()
CGPA=float(input("CGPA-"))

#storing all the collected data into a list
student=[SID,Name,Gender,Course_name,CGPA]

#printing the data to check the program
print(student)

#############################################################
#Question 4
print("Question 4")
#taking input from user
students=[]
print("Plz give marks as Input\n")
for i in range(0,5):
    element=int(input())
    students.append(element)

#sorting the marks of the students
students.sort()

#seperating input from output
print("*************************")

#printing the sorted result
print(*students,sep="\n")

################################################################
#Question 5
print("Question 5")
#making list of colors as specified
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print("Part a")
#Part(a)-Removing 4th elemnt and printing new list
color.pop(3)

print(color)

print("Part b")
color =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part(b)- Removing "Black" and "Pink" from the list
color.remove('Black');color.remove('Pink'); color.insert(3,'Purple')
print(color)

#################################################################
