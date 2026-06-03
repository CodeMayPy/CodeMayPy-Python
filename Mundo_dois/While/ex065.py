#EN- Loop structure: While
# 65- Create a program that reads several integers from the keyboard. At the end of the execution, show the average of
# all the values and which were the highest and lowest values read. The program should ask the user whether or not he
# wants to continue entering values.
response = "Y"
medium = soma = amount = bigger = smaller = 0
while response in "Yy":
    number = int(input("Enter a number:"))
    soma += number
    amount += 1
    if amount == 1:
        bigger = smaller = number
    else:
        if number > bigger:
            bigger = number
        if number < smaller:
            smaller = number
    response = str(input("Do you want to continue?")).upper().strip()[0]
medium = soma / number
print(f"You entered {amount} and the averege is {medium}.")
print(f"The bigger is {bigger} and the smaller is {smaller}.")