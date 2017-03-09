import sys

ORIGINAL_LINE = str(sys.argv[1])
NEW_LINE = ORIGINAL_LINE.replace(' ', '')
REVERT_LINE = NEW_LINE[::-1]
if NEW_LINE.lower() == REVERT_LINE.lower():
    print 'YES'
else:
    print 'NO'

