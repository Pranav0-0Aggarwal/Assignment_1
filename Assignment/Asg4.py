# Question 1
print("Question 1")


def tower_of_hanoi(n, source="A", destination="B", temporary="C"):
    global counter
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}");
        counter = counter + 1
        return
    tower_of_hanoi(n - 1, source, temporary, destination)
    print(f"Move disk {n} from {source} to {temporary}");
    counter = counter + 1
    tower_of_hanoi(n - 1, temporary, source, destination)


inp = int(input("Please enter total number of disks- "))
counter = 0
tower_of_hanoi(inp, "A", "B", "C")
print(f"Total number of steps to be followed is {counter}")
#########################################################################################

# Question 2
print("Question 2")
# input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

# using recursions
print("\nUsing recursions:\n")


def pascal(n, orgnum=n):
    if n == 0:
        return

    pascal(n - 1, orgnum)

    # printing the spaces
    print('  ' * (orgnum - n), end='')

    # first number is always 1
    entry = 1
    for i in range(1, n + 1):
        print(entry, end='   ')

        # using Binomial Coefficient
        entry = entry * (n - i) // i
    print()


pascal(n)

# using iteration
print("\nUsing loops:\n")
for line in range(1, n + 1):

    print('  ' * (n - line), end='')

    x = 1
    for i in range(1, line + 1):
        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")
####################################################################################

# Question 3
print("Question 3")
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))

# ensuring that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    Q, R = divmod(a, b)
    print(f"Questiont:{Q}\nRemainder:{R}")


division()

print('a)')
print(callable(division))

print('b)')
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('c)')
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

print('d)')
s = set(m)
print(s)

print('e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)

print('f)')
m = max(f_s)
print(hash(str(m)))
####################################################################################################

# Question 4
print("Question 4")


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")


# assigning values
student1 = Student("Pranav Aggarwal", 21105095)
print("Object is created")

# printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

# deleting object
del student1
####################################################################################################

# Question 5
print("Question 5")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __del__(self):
        print(f"Employee {self.name} record deleted")


a = Employee("Mehak", 40000)
b = Employee("Ashok", 50000)
c = Employee("Viren", 60000)

# a)
print("Part a")
a.salary = 70000
print(f"The updated salary of the employee {a.name} is {a.salary}")

# b)
print("Part B")
del c
print("Records of Viren are deleted")
##########################################################################################################

# Question 6
print("Question 6")
# Question-6
# George utters a word
word = input("Enter the first word: ")

# Barbie's word
word2 = input("Enter a new meaningful word to test your friendship: ")


def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# test
if count_in_dict(word) != count_in_dict(word2):
    print("The letters aren't exact, friendship is fake!!")


# shopkeeper's input
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()


userinput()
