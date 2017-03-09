import sys

ORIGINAL_LINE = sys.argv
NEW_LINE = ''
for i in range(len(ORIGINAL_LINE)-1, 0, -1):
    if i == 1:
        NEW_LINE += ORIGINAL_LINE[i]
    else:
        NEW_LINE += ORIGINAL_LINE[i]+' '
print NEW_LINE
