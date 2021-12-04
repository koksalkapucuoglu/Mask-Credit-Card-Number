
def masking(number, mask):
    str = ''

    for x in number[:-mask]:
        str += '*'

    str += number [-mask:]
    return str

def masking_two_cursor(number, start_num = 1, end_num = 1, char = '*' ):
    if start_num == 0 or end_num == 0 :
        raise "start number or end number must be greater 0"
        
    number_len = len(number)
    mask_len = end_num - start_num + 1
    final_str = number[:start_num-1] + char * mask_len + number[end_num:]
    return final_str[:number_len]
