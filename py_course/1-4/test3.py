"""

: 10 20 30
: python lab3_1.py 10 20 30
: not triangle
: 1 1 1
: python lab3_1.py 1 1 1
: triangle
: 5.5 5.5 -2
: python lab3_1.py 5.5 5.5 -2
: not triangle
"""
import sys

X = int(float(sys.argv[1]))
Y = int(float(sys.argv[2]))
Z = int(float(sys.argv[3]))

if X <= 0 or Y <= 0 or Z <= 0:
    print 'not triangle'
elif  X+Y <= Z or X+Z <= Y or X+Z <= Y:
    print 'not triangle'
else:
    print 'triangle'
