#: 2 3 1
# python lab2_2.py 2 3 1
#Everybody sing a song: la-la la-la la-la!
#: 1 0 0
# python lab2_2.py 1 0 0
# Everybody sing a song:.

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
last='.'
middle=''
if z == 1: 
    last='!'
if x == 1:
    word='la'
elif x>=2:
    word='la'+'-la'*(x-1)
if y == 1:
    middle=' ' + word
elif y>=2:
    nextword= ' '+word
    middle=' '+word+nextword*(y-1)
    

print 'Everybody sing a song:'+middle+last
