import string

def int2roman(number):
    '''
    So yeah, I wanted to use Roman Numerals and found this class online
    '''
    numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL",
        50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    result = ""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

def tagify(value):
    '''
    I would like to create nice URLs and this function does that
    '''
    value = value.lower().replace('/', ' ').replace('&', ' and ')
    value = value.replace('.net', 'dot net').replace(' - ', ' ')
    value = value.replace('f#', 'f sharp')
    value = value.replace('c#', 'c sharp')
    value = value.translate(None, string.punctuation).replace(' ', '-')
    return value.replace('--', '-')