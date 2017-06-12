"""prgm"""
def add(att1, att2):
    """prgm"""
    sum = int(att1) + int(att2)
    if sum==0:
        return sum 
    elif att1.isdigit and att2.isdigit:
        return sum
        
    else:
        return False

# take input from the user
print "Addition of two numbers"

#A = raw_input("Enter first number: ")
#B = raw_input("Enter second number: ")
A = '45'
B = '56'
print A, "+", B, "=", add(A, B)
