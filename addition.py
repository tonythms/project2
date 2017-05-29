# define functions
"""
prgm
"""
def add(x, y):
    if int(x) and int(y):
        return x + y
    else:
        return False

# take input from the user
print "Addition of two numbers"

A = raw_input("Enter first number: ")
B = raw_input("Enter second number: ")

print A, "+", B, "=", add(A, B)
