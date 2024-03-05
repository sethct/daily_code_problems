#| Implement integer exponentiation. That is, implement the pow(x, y) function,
#| where x and y are integers and returns x^y.
#| Do this faster than the naive method of repeated multiplication.

#------------------#
# Define Functions #
#------------------#

def pow(x, y):
    #| Base cases
    if y == 0:
        return 1
    elif y < 0:
        #| Handle negative powers by converting them to positive
        #| and inverting the result, assuming integer division.
        return 1 / pow(x, -y)
    
    #| Recursive cases
    if y % 2 == 0:
        #| If y is even, x^y = (x^(y/2))^2
        return pow(x, y // 2) ** 2
    else:
        #| If y is odd, x^y = x * (x^((y-1)/2))^2
        return x * pow(x, (y - 1) // 2) ** 2

#------------------#
# Test Application #
#------------------#

print(pow(2, 10))  # 1024
print(pow(3, 5))   # 243
