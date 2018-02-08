def ATM(money , request):
	if request > money:
		print "Your Account value is " + str(money)
		print  "Check your request plz"
	elif request < 0 or money < 0:
		print "Check your request plz"
		return
	while request <= money and request>0:
		if request >= 100:
			print "give 100" 
			request =request - 100
		elif request >= 50:
			print "give 50"
			request =request - 50
		elif request >= 10:
			print "give 10"
			request =request - 10
		elif request >= 5:
			print "give 5"
			request =request - 5
		else:
			print "give " + str(request)
			request = 0

ATM(500, 272)