#EN- Loop structure: While
#63-Write a program that reads any integer number N and displays on the screen the first N elements of a
# Fibonacci Sequence.
terms = int(input("How many terms do you want to show?"))
first_term = 0
second_term = 1
print(f"{first_term} -> {second_term}", end='')
counter = 3
while counter <= terms:
    third_term = first_term + second_term
    print(f" -> {third_term}", end='')
    first_term = second_term
    second_term = third_term
    counter += 1
