def count_spaces(str, start, end):
    '''
    Input: str, a string. start and end: positions within the string.
    Returns count of spaces in str between positions start and end (inclusive)
    '''
    assert (start <= end), 'end must be >= start'
    assert (0 <= start < len(str)), 'start must be within string boundaries'
    assert (0 <= end < len(str)), 'end must be within string boundaries'
    count = 0
    for i in range(start, end+1):
        if str[i] == ' ':
            count += 1

    assert (count >= 0), 'Cannot have a negative count!'
    return count

def main():
    print(count_spaces('this is a test', 2, 8))
    print(count_spaces('this is a test', 2, 15))

if __name__ == '__main__':
    main()
