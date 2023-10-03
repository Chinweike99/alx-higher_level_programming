#!/usr/bin/python3
eAscci = ord('q')
jAscci = ord('e')

for ascci_value in range(97, 123):
    if ascci_value != eAscci and ascci_value != jAscci:
        print(chr(ascci_value), end = "")
