def ATM(money , request):
	for e in request:
		print "Current balance : " + str(money)
		print "===========================" 
		if e > money:
			print "Check your request plz"
		elif e < 0:
			print "Check your request plz"
		else:
			while e <= money and e>0:
				if e >= 100:
					print "give 100" 
					e = e - 100
					money = money - 100
				elif e >= 50:
					print "give 50"
					e = e - 50
					money = money - 50
				elif e >= 10:
					print "give 10"
					e = e - 10
					money = money - 10
				elif e >= 5:
					print "give 5"
					e = e - 5
					money = money - 5
				else:
					print "give " + str(request)
					money = money - e
					e = 0
	
	print "Current balance : " + str(money) 
	print "===========================" 

money = 500
request = [200, 10, 900, -10, 50, 100, 140, 10]
ATM(money, request)
