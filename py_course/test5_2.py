"""counts diff chars in first from second"""
def counter(first, second):
    """counts diff chars in first from second"""
    first_str = str(first)
    second_str = str(second)
    result = first_str+second_str
    return result

print counter(12345, 567)
print counter(123321, 12128)
print counter(123, 45)
