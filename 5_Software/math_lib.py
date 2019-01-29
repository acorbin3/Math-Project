def pow_native(number, exponent):
    """
    TODO - add function overview
    :param number:
    :param exponent:
    :return:
    """
    if exponent == 0:
        return 1
    total = 1
    for i in range(1, exponent + 1):
        total *= number
    return total

def floor(initial):
    return int(initial)
    
def sine():
    print("TODO - Add implementation")
    
def cosine():
    print("TODO - Add implementation")
    
def square_root(x):
    epsilon = 0.01
    left = 0
    right = x
    guess = (right+left)/2.0
    while abs(guess**2 - x) > :
        if guess**2 < x:
            left = guess
        else:
            right = guess
        guess = (right+left)/2.0
    return guess
