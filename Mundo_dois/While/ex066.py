# Create a program that reads integers from the keyboard. The program will only stop when the user enters the value 999,
# which is the stopping condition. At the end, show how many numbers were entered and what the sum of them was
# (disregarding the flag).
amount = 0
while True:
    number = int(input('Ender a number (enter 999 to stop):'))
    if number == 999:
        break
    amount += number
print(f"The sum of the numbers is {amount}")
