def ternary_decimal_conv(number_input):
    '''Convert N base number to a decimal number
    Keyword:
    number_input -- Giving a certain number from any ternary number
    return:
    sum_num -- the sum of each digit of the power of ternary
    '''
    sum_num = 0
    string_user = str(number_input)

    string_user = string_user[::-1]
    for i in range(len(string_user)):
        formula = int(string_user[i]) * 3 ** i
        sum_num += formula
    return 