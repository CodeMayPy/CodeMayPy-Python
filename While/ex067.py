# Write a program that displays the multiplication table of several numbers, one at a time, for each value entered by
# the user. The program will stop when the requested number is negative.
while True:
    number = int(input("What number do you want to see the multiplication of?"))
    if number < 0:
        break
    for counter in range (1,11):
        print(f'{number} X {counter} = {number * counter}')
