def urlify(char_list, str_length):
    num_of_spaces = 0
    for i in range(str_length):
        if char_list[i] == ' ':
            num_of_spaces += 1

    total_length = str_length + num_of_spaces * 2
    for i in range(str_length-1, -1, -1):
        total_length -= 1
        if char_list[i] == ' ':
            char_list[total_length] = '0' 
            char_list[total_length - 1] = '2' 
            char_list[total_length - 2] = '%' 
            total_length -= 2
        else:
            char_list[total_length] = char_list[i]
    return char_list

def validate_urlify(string, true_length):
    # RHS of the comparison is the easiest and probably the pythonic way to do this problem
    # Implemented urlify just to do it in place as thats what the author expects us to understand 
    return ''.join(urlify(list(string), true_length)) == test.strip().replace(' ', '%20')


if __name__ == '__main__':
    test = 'saran sas tt    '
    assert validate_urlify(test, 12)
    test = 'saran'
    assert validate_urlify(test, 5)