#mathpy, puts together all sub-apps

from random import randint

def mathpyrun():
	print "press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division."
	mathtype = input("press number, then press enter:  ")
	mathtypei = int(mathtype)
	
	if(mathtypei == 1):
		n1 = randint(0, 1000)
	
		n2 = randint(0, 1000)
	
		print "add:"
		print n1
		print n2
	
		ans = input("answer: ")
	
		realans = n1 + n2
	
		ansint = int(ans)
	
		if (ansint == realans):
			print "Correct!"
		else:
			print "Incorrect. The answer is: " 
			print realans
	elif(mathtypei == 2):
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
	elif(mathtypei == 3):
	
		n1 = randint(0, 1000)
		
		n2 = randint(0, 99)
		
		print "multiply:"
		print n1
		print n2
		
		ans = input("answer: ")
		
		realans = n1 * n2
		
		ansint = int(ans)
		
		if (ansint == realans):
			print "Correct!"
		else:
			print "Incorrect. The answer is: " 
			print realans
	elif(mathtypei == 4):
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
	else:
		print "Please type 1, 2, 3, or 4."
		mathpyrun()			

mathpyrun()
