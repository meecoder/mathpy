#pyexponent, mathoy sub-app for exponents

from random import randint


n1 = randint(0, 10)
	
n2 = randint(0, 10)
	
print "first number to second number power:"
print n1
print n2
	
ans = input("answer: ")
	
realans = n1 ** n2
	
ansint = int(ans)
	
if (ansint == realans):
	print "Correct!"
else:
	print "Incorrect. The answer is: " 
	print realans
