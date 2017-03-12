"""counts diff chars in first from second"""
def counter(first, second):
    """counts diff chars in first from second"""
    first_str = str(first)
    second_str = str(second)
    result = 0
    for i in range(len(second_str)):
        if first_str.find(second_str[i:i+1:]) > -1 and second_str[i:i+1:] != '':
            result += 1
            first_str = first_str.replace(second_str[i:i+1:], '')
            second_str = second_str.replace(second_str[i:i+1:], '')
    return result

print counter(12345, 567)
print counter(123321, 12128)
print counter(123, 45)
