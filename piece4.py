#

# The identity operator

a = ["Retention", 3, None]
b = ["Retention", 3, None]
print(a is b)
b = a
print(a is b)

a = "Something"
b = None
print(a is not None, b is None)

# comparsion operator
a = 2
b = 6
print(a == b)
print(a < b)
print(a <= b,a != b,a >= b, a > b)

a = "many paths"
b = "many paths"
print(a is b)
print(a == b)

a = 9
print(0 <= a <= 10)

# membership operator
p = (4, "frog", 9 -33, 9, 2)
phrase = "Wild Swans by Jung Chang"
print(2 in p)
print("j" in phrase)
print("han" in phrase)

# logical operators
five = 5
two = 2
zero = 0
nought = 0
print("five and two", five and two)
print("two and five", two and five)
print("five and zero", five and zero)
print("five or two", five or two)
print("two or five", two or five)
print("zero or five", zero or five)
print("zero or nought",zero or nought)


