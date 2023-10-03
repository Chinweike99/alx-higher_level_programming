#!/usr/bin/python3
for i in range(100):
    number = f"{i:02d}"
    print(number, end="")
    if i != 99:
        print(', ', end='')
