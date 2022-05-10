
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-/?"


while 1:
    pass_len = int(input("How many characters? "))
    pass_count = int(input("How many to generate? "))
    for x in range(0,pass_count):
        password = ""
        for x in range(0,pass_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here's the password:", password)
