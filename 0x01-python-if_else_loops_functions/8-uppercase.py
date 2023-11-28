#!/usr/bin/python3
def uppercase(str):
    for i in str:
        k = i
        if ord(k) >= 97 and ord(k) <= 122:
            k = chr(ord(i) - 32)
        print("{}".format(k), end="")
    print()
