import sys
import math

x = int(sys.argv[1])
fi = int(sys.argv[2])
syg = int(sys.argv[3])

print (1/(syg*math.sqrt(2*math.pi)))*math.exp(-((x-fi)**2)/2*(syg**2))