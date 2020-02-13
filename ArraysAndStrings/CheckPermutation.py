def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    char_count = [0] * 128

    for char in string1:
        char_count[ord(char)] += 1
    
    for char in string2:
        index = ord(char)
        if char_count[index] == 0:
            return False
        char_count[index] -= 1
    
    return True
    

if __name__ == '__main__':
    assert not checkPermutation('Saran', 'rasna')
    assert checkPermutation('saran', 'rasna')
    assert not checkPermutation('swathys', 'ssy')
    assert not checkPermutation('dog ', 'god')
    assert not checkPermutation('abc ', 'def')