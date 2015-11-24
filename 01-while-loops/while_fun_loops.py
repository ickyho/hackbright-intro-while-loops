#i = 0
#while(i <= 20):
#	if (i == 13):
#		print "Hello"
#	else:
#		print i 
#	i += 1 

#i = 0
#while (i <= 100):
#	print i 
#	i += 10 

#i = 0
#while (i <= 10):
#	if (i % 2 == 1):
#		print i
#	i += 1

#i = 10 
#while (i >= 0):
#	if (i == 0):
#		print "blastoff!"
#	else: 
#		print i
#	i -= 1 

#fruits = ["apples", "oranges", "bananas"]
#i = 0
#while (i<len(fruits)):
#	print fruits[i]
#	i += 1 


#def sum_nums(num):
#	sum = 0 
#	i = 0 
#	while (i < num):
#		sum += i
#		i += 1
#	return sum
#
#print sum_nums(3)


#def sum_nums(num):
#	sum = 0 
#	i = 0 
#	while (i <= num):
#		sum += i
#		i += 1
#	return sum
#
#print sum_nums(3)

#def sum_nums2(num):
#	sum = 0 
#	i = 0 
#	if (num < 0):   #if the passed in argument is negative
#		i = num
#		num = 0
#	while (i < num):    #while we haven't iterated to the passed in argument
#		sum += i      #add the value of i to the sum 			
#		i += 1      #iterate i to the next  number
#	return sum
	
#print sum_nums2(-3)



def fizz_buzz(num):
	i = 0
	while (i <= num):
		if (i % 3 ==0 and i % 5 == 0):
			print "fizzbuzz"
		elif (i % 5 ==0):
			print "buzz"
		elif (i % 3 == 0):
			print "fizz"
		else:
			print i
		i += 1
print fizz_buzz(100)