""" super_fibonacci """
def super_fibonacci(num1, num2):
    """ super_fibonacci """
    result = 1
    num1 = int(num1)
    if num1 > num2:
        arr = [1 for x in range(num1+1)]
        for i in range(num1):
            if i < num2:
                arr[i] = 1
            else:
                temp = 0
                for j in range(i-num2, i):
                    temp += arr[j]
                arr[i] = temp
        result = arr[num1-1]
    return result

print super_fibonacci(2, 1)
print super_fibonacci(3, 5)
print super_fibonacci(8, 2)
print super_fibonacci(9, 3)
