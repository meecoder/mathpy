#pydivision script, asks division problem and checks answer

from random import randint, choice

pre1 = randint(1, 50)
pre2 = randint(1, 50)
n2 = pre1 * pre2
pre = [pre1, pre2]
n1 = choice(pre)

print "divide first number by second number:"
print n2
print n1

ans = input("answer: ")
ansint = int(ans)

if(n1 == pre1):
	global realans
	realans = pre2
else:
	global realans
	realans = pre1
	


 

if (ansint == realans):
	print "Correct!"
else:
	print "Incorrect. The answer is: " 
	print realans
	

