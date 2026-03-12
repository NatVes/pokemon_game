# Q1a: Print only the first 5 numbers in this list
import math
print("\nQ1a\n")
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# A1a:
print(x[0:5])
# [2, 5, 4, 87, 34]

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
# A1b:
for num in x:
    if num % 2 == 0:
        print(num)

# 2
# 4
# 34
# 2

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for num in x[0:5]:
    if num % 2 == 0:
        print(num)
#2
#4
#34

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
letters = []
for name in names:
    letters.append(name[0])
print(letters)
#['A', 'L', 'K', 'A', 'T']

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
spaces = []
for name in names:
    spaces.append(name.index(" "))
print(spaces)
#[4, 8, 9, 5, 7]

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initals = []
for name in names:
    space = name.index(" ")
    first = name[0]
    last = name[space+1]
    initals.append(first+last)
print(initals)
#['AT', 'LF', 'KJ', 'AE', 'TT']

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

# A3a:
for lst in list_of_lists:
    if len(lst) == len(set(lst)):
        print(lst)
#['A', 'B', 'C']
#['one', 'Two', 'Three', 'Four']

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
num = int(input("Enter a number greater than 100: "))

while num <= 100:
    num = int(input("Try again. Enter a number greater than 100: "))
print("You have entered:", num)
#Enter a number greater than 100: 20
#Try again. Enter a number greater than 100: 50
#Try again. Enter a number greater than 100: 60
#Try again. Enter a number greater than 100: 70
#Try again. Enter a number greater than 100: 90
#Try again. Enter a number greater than 100: 150
#You have entered: 150

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not prime")
#Enter a number greater than 100: 45
#Try again. Enter a number greater than 100: 50
#Try again. Enter a number greater than 100: 60
#Try again. Enter a number greater than 100: 70
#Try again. Enter a number greater than 100: 80
#Try again. Enter a number greater than 100: 90
#Try again. Enter a number greater than 100: 150
#You have entered: 150
#Not prime