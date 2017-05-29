# define functions
"""prgm"""
def add(X, Y):
    if int(X) and int(Y):
        return X + Y
    else:
        return False

# take input from the user
print "Addition of two numbers"

A = raw_input("Enter first number: ")
B = raw_input("Enter second number: ")

print A, "+", B, "=", add(A, B)
