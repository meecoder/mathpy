#mathpy, puts together all sub-apps

from random import randint, choice
global realans

def mathpyrun():
	correct = 0
	incorrect = 0
	print("press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, and 5 for exponents.")
	mathtype = input("press number, then press enter:  ")
	mathnum = input("Type how many problems, then press enter:  ")
	mathtypei = int(mathtype)
	i=1
	if(mathtypei == 1):
		while(i <= mathnum):
			n1 = randint(0, 1000)
		
			n2 = randint(0, 1000)
		
			print("add:")
			print(n1)
			print(n2)
		
			ans = input("answer: ")
		
			realans = n1 + n2
		
			ansint = int(ans)
		
			if (ansint == realans):
				print ("Correct!")
				correct += 1
			else:
				print("Incorrect. The answer is:")
				print(realans)
				incorrect += 1
			i += 1
		print("------STATISTICS------")
		print("Correct:")
		print(correct)
		print("  ")
		print("Incorrect:")
		print(incorrect)
		percent = (float(correct) / float(mathnum) * 100.0)
		percent = str(percent)
		print(" ")
		print(percent + '% correct')
	elif(mathtypei == 2):
		while(i <= mathnum):
			n1 = randint(0, 1000)
	
			n2 = randint(0, n1)
	
			print("subtract:")
			print(n1)
			print(n2)
			
			ans = input("answer: ")
			
			realans = n1 - n2
				
			ansint = int(ans)
			
			if (ansint == realans):
				print("Correct!")
				correct += 1
			else:
				print("Incorrect. The answer is:")
				print(realans)
				incorrect += 1
			i += 1
		print("------STATISTICS------")
		print("Correct:")
		print(correct)
		print("  ")
		print("Incorrect:")
		print(incorrect)
		percent = (float(correct) / float(mathnum) * 100.0)
		percent = str(percent)
		print(" ")
		print(percent + '% correct')
	elif(mathtypei == 3):
		while(i <= mathnum):
			n1 = randint(0, 1000)
			
			n2 = randint(0, 99)
			
			print("multiply:")
			print(n1)
			print(n2)
			
			ans = input("answer: ")
			
			realans = n1 * n2
			
			ansint = int(ans)
			
			if (ansint == realans):
				print("Correct!")
				correct += 1
			else:
				print("Incorrect. The answer is: ")
				print(realans)
				incorrect += 1
			i += 1
		print("------STATISTICS------")
		print("Correct:")
		print(correct)
		print("  ")
		print("Incorrect:")
		print(incorrect)
		percent = (float(correct) / float(mathnum) * 100.0)
		percent = str(percent)
		print(" ")
		print(percent + '% correct')
	elif(mathtypei == 4):
		while(i <= mathnum):
	
			pre1 = randint(1, 50)
			pre2 = randint(1, 50)
			n2 = pre1 * pre2
			pre = [pre1, pre2]
			n1 = choice(pre)
			
			print("divide first number by second number:")
			print(n2)
			print(n1)
			
			ans = input("answer: ")
			ansint = int(ans)
			
			if(n1 == pre1):
				realans = pre2
			else:
				realans = pre1
			
			if (ansint == realans):
				print("Correct!")
				correct += 1
			else:
				print("Incorrect. The answer is: " )
				print(realans)
				incorrect += 1
			i += 1
		print("------STATISTICS------")
		print("Correct:")
		print(correct)
		print("  ")
		print("Incorrect:")
		print(incorrect)
		percent = (float(correct) / float(mathnum) * 100.0)
		percent = str(percent)
		print(" ")
		print(percent + '% correct')
	elif(mathtypei == 5):
		while(i <= mathnum):
			n1 = randint(0, 10)
				
			n2 = randint(0, 10)
				
			print("first number to second number power:")
			print(n1)
			print(n2)
				
			ans = input("answer: ")
			
			realans = n1 ** n2
				
			ansint = int(ans)
			
			if (ansint == realans):
				print("Correct!")
				correct += 1
			else:
				print("Incorrect. The answer is: ")
				print(realans)
				incorrect += 1
			i += 1
		print("------STATISTICS------")
		print("Correct:")
		print(correct)
		print("  ")
		print("Incorrect:")
		print(incorrect)
		percent = (float(correct) / float(mathnum) * 100.0)
		percent = str(percent)
		print(" ")
		print(percent + '% correct')
	else:
		print("Please type 1, 2, 3, or 4.")
		mathpyrun()	
mathpyrun()
