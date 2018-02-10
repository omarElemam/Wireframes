def ATM(money , request):
	for e in request:
		if e > money:
			print "please check your request"
		elif e < 0:
			print "please check your request"
		else:
			money = give_cash(e, money)

		print "Current balance : " + str(money) 
		print "_______________________" 

def give_cash(e, money):
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
			print "give " + str(e)
			money = money - e
			e = 0
	print "================"
	return money
	
#---------------------------------------------
money = 500
request = [1000, 227, 10, 900, -10, 50, 100, 140, 113]
ATM(money, request)
#---------------------------------------------
          