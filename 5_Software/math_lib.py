def pow_native(number, exponent):
    """
    TODO - add function overview
    :param number:
    :param exponent:
    :return:
    """
    if exponent == 0:
        return 1
    total = 0
    for i in range(0,exponent+1):
        total += number
    return total
