#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = input('Please input your height(cm): ')
weight = input('Please input your weight(kg): ')
height = int(height)
weight = int(weight)
print('\nSo your height and weight are %s cm, %s kg' % (height,weight))
height = height/100
#print(height)
#height = float(height)
BMI = weight/(height**2)
print('Your BMI point is %s \n' % (BMI))

if BMI < 18.5:
	print('You\'re too light! ')
elif 18.5 <= BMI < 25:
	print('You\'re weight is normal. ')
elif 25 <= BMI < 28:
	print('You\'re weight is a little high. ')
elif 28 <= BMI < 32:
	print('You got fat ')
else:
	print('You\'re too fat! Need to go on a diet! ')
