# Enter your code here. Read input from STDIN. Print output to STDOUT
import os

n = int(input())
phonebook = dict()

for i in range(0, n):
    name, number = str(input()).split(' ')
    phonebook[name] = number

for j in range(0, n):
    name = input()
    if name in phonebook:
        print("{}={}".format(name, phonebook[name]))
    else:
        print('Not found')
