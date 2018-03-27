#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Christina', 'Terry', 'Murry', 'Rose']
print(classmates[-1])

classmates.append('Siri')
print(classmates[-1])

classmates.insert(1, 'Jack')
print(classmates[1], '&', classmates[-2])

classmates.pop(3)
print(classmates)

classmates[2] = 'Anna'
print(classmates)

L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]

print(L[0][0], L[1][1], L[2][2])

for n in L[2]:
	print('Hello ',n)
# break = end all this roof / continue = end now this roof
	