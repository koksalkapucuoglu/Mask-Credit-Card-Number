#solution 1
CREDIT_CART_NUMBER = '1234123412341234'

length_credit_card_number = len(CREDIT_CART_NUMBER)

mask = length_credit_card_number - 4 

show_credit_card_number = CREDIT_CART_NUMBER[mask:]

print('*' * mask + show_credit_card_number)

#solution 2
import internal_api

print(internal_api.masking('1234123412341234', 4))

#solution 3

str = '1234123412341234'
final_str = str[-4:].rjust(len(str), '*')
print(final_str)


#solution 4

print(internal_api.masking_two_cursor('1234123412341234', 2, 18, '#'))

#solution 5

import re
str = '1234123412341234'
final_str = re.sub('[0-9]', '*', str[:-4]) + str[-4:]
print(final_str)