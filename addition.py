# define functions
"""
prgm
"""
def add(na, nb):
    if int(na) and int(nb):
        return na + nb
    else:
        return False

# take input from the user
print "Addition of two numbers"

A = raw_input("Enter first number: ")
B = raw_input("Enter second number: ")

print A, "+", B, "=", add(A, B)
