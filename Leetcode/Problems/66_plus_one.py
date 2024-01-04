def plusOne(digits: list[int]) -> list[int]:
    
    num = int("".join(map(str, digits)))
    num += 1
    new_digits = [int(digit) for digit in str(num)]
    print (new_digits)
    
    
    
    
    
    """num = ""
    for ele in digits:
        num += str(ele)

    num = int(num)
    num += 1
    num = str(num)

    new_digits = []
    for ele in num:
        new_digits.append(int(ele))

    return new_digits
"""

bal = plusOne([9])

print (bal)