import sys

ORIGINAL_LINE = sys.argv[1]
for i in range(int(len(ORIGINAL_LINE)/2)):
    if '()' in ORIGINAL_LINE:
        ORIGINAL_LINE = ORIGINAL_LINE.replace('()', '', 1)
    else:
        break
if len(ORIGINAL_LINE) == 0:
    print 'YES'
else:
    print 'NO'
