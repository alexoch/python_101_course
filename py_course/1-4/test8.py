import sys

A = int(sys.argv[1])
B = int(sys.argv[2])
RESULT = 0
for i in range(A, B+1):
    T = str(i)
    if len(T) != 6:
        for j in range(6-len(T)):
            T = '0'+T
    if int(T[0])+int(T[1])+int(T[2]) == int(T[3])+int(T[4])+int(T[5]):
        RESULT = RESULT+1
print RESULT


