"""prgm"""
def add(att1, att2):
    """prgm"""
    if int(att1) and int(att2):
        y1 = att1 + att2
        if int(y1):
            return y1
        else:
            return False
        #return y
    else:
        return False

# take input from the user
print "Addition of two numbers"

#A = raw_input("Enter first number: ")
#B = raw_input("Enter second number: ")
A = 98
B = 104
print A, "+", B, "=", add(A, B)
