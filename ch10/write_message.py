#! /bin/python3

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I alse love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

