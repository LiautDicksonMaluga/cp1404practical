# numbers = []
# how_many_times = 5
# for i in range(how_many_times):
#     add_numbers = int(input("Number: "))
#     numbers.append(add_numbers)
# print("The first number is", numbers[0])
# print("The last number is", numbers[-1])
# print("The smallest number is", min(numbers))
# print("The largest number is", max(numbers))
# average = sum(numbers) / len(numbers)
# print("The average of the numbers is", average)

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("What is your name: ")
while name not in usernames:
    print("Access denied")
    name = input("What is your name: ")
if name in usernames:
    print("Access Granted")