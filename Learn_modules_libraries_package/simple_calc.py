# Mini-calculator

from math_operation import add

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")