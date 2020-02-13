
def isUnique(string):
    char_visited = [False] * 128
    for char in string:
        index = ord(char)
        if char_visited[index]:
            return False
        char_visited[index] = True
    return True


if __name__ == '__main__':
    assert not isUnique('Saran')
    assert isUnique('AaBbCc')
    assert not isUnique('abcda')
    assert isUnique('12,34')
    assert not isUnique(' dfgh jkl')