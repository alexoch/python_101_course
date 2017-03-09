"""
:10
: python lab3_1.py 10
: 55
: 0
:python lab3_1.py 0
: 0
"""
import sys

X = int(sys.argv[1])
P = 0
C = 1
if X == 0:
    print P
elif X == 1:
    print C
else:
    for count in range(int(X)-1):
        R = C + P
        P = C
        C = R
    print R

