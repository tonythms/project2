"""prgm"""
def add(att1, att2):
    """prgm"""
    if ((att1 + att2) % 10) - att2 == 0:
        return False
    else:
        return att1 + att2

# take input from the user
print "Addition of two numbers"

#A = raw_input("Enter first number: ")
#B = raw_input("Enter second number: ")
A = 98
B = 104
print A, "+", B, "=", add(A, B)
