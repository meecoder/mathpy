#pyminus script, asks subtraction problem and checks answer

from random import randint


n1 = randint(0, 1000)

n2 = randint(0, n1)

print "subtract:"
print n1
print n2

ans = input("answer: ")

realans = n1 - n2

ansint = int(ans)

if (ansint == realans):
	print "Correct!"
else:
	print "Incorrect. The answer is: " 
	print realans
