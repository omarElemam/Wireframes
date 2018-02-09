def ATM(money , request):
	print "Current balance : " + str(money)
	if request > money:
		print  "Check your request plz"
		print "Current balance : " + str(money)
		return
	elif request < 0:
		print "Check your request plz"
		return
	while request <= money and request>0:
		if request >= 100:
			print "give 100" 
			request = request - 100
			money = money - 100
		elif request >= 50:
			print "give 50"
			request = request - 50
			money = money - 50
		elif request >= 10:
			print "give 10"
			request = request - 10
			money = money - 10
		elif request >= 5:
			print "give 5"
			request = request - 5
			money = money - 5
		else:
			print "give " + str(request)
			money = money - request
			request = 0

	
	print "Current balance : " + str(money) 

ATM(500, 600)