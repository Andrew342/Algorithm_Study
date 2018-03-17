from stack import Stack

def base_converter(dec_number,base):
    digits="0123456789ABCDEF"

    rem_stack=Stack()
    while dec_number>0:
        rem=dec_number % base
        rem_stack.push(rem)
        dec_number=dec_number //base

    bin_string=""
    while not rem_stack.is_empty():
        bin_string=bin_string+digits[rem_stack.pop()]

    return bin_string


print(base_converter(25,2))
print(base_converter(25,16))
