#! /usr/bin/env python3
a=9
def change():
    global a
    print(a)
    a=100

change()
print(a)
