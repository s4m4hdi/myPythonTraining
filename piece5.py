#!/usr/bin/env python3

# control flow statements

x = 1
lines = 90

# if statement example
if x:
	print("x is nonzero")
	
if lines < 1000:
	print("small")
elif lines < 10000:
	print("medium")
else:
	print("large")

#while statement example
x = 0	
while True:
	print("x=",x)
	if x:
		break
	else: x = x + 1

print("end while")

# for in loop
for country in ['Denmark', 'Finland', 'Norway', 'Sweden']:
	print(country)
	
countries = ['Denmark', 'Finland', 'Norway', 'Sweden']
for country in countries:
	print(country)
	
# exception handling
s = input("enter an integer: ")
try:
	i = int(s)
	print("valid integer entered:",i)
except ValueError as err:
	print(err)