#EN- Loop structure: While
#64-Create a program that reads several integers from the keyboard. The program will only stop when the user enters the
# value 999, which is the stopping condition. At the end, show how many numbers were entered and what the sum of them
# was (disregarding the flag).
number = counter = amount = 0
number = int(input("Enter an integer [999 to stop]:"))
while number != 999:
    amount += number
    counter += 1
    number = int(input("Enter an integer [999 to stop]:"))
print(f"You enter {number} numbers and the sum between them is {amount} ")