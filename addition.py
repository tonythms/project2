"""prgm"""
def add(att1, att2):
    """prgm"""
    if int(att1) and int(att2):
        return att1 + att2
    else:
        return False

# take input from the user
print "Addition of two numbers"

#A = raw_input("Enter first number: ")
#B = raw_input("Enter second number: ")
A = 98
B = 104
print A, "+", B, "=", add(A, B)
