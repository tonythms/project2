"""prgm"""
def add(a, b):
    """prgm"""
    if int(a) and int(b):
        return a + b
    else:
        return False

# take input from the user
print "Addition of two numbers"

A = raw_input("Enter first number: ")
B = raw_input("Enter second number: ")

print A, "+", B, "=", add(A, B)
