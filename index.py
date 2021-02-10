import os
import csv
import re

link = "https://www.google.net"

info = ["one", "two", "three", "four", "five", "six", "seven", "eight"]


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __repr__(self):
        return f"({self.name}, {self.age}, {self.gender})"

with open("img/future.jpeg", "rb") as img:
    with open("img/copy.jpg", "wb") as copy:
        for line in img:
            copy.write(line)

def decorator(callback):
    def add(num1, num2):
        return num1 + num2 + 10

    return add

@decorator
def display():
    print("This is a display function")

print(display(1, 2))


