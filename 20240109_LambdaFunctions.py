#| cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#| For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#| Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#| Implement car and cdr.

#------------------#
# Define Functions #
#------------------#

#| Definition of the car function to extract first pair element
def car(pair):
    #| Apply lambda function to extract the first element
    return pair(lambda a, b: a)

#| Definition of the cdr function that extracts second pair element
def cdr(pair):
    #| Apply lambda function to extract the second element
    return pair(lambda a, b: b)

#------------------#
# Test Application #
#------------------#

pair_example = cons(3,4)
print(car(pair_example)) 
print(cdr(pair_example))