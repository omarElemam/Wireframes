class ATM:
	def	__init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name

	def withdraw(self, request):
		print "Welcome to " + self.bank_name
		print "Current balance " + str(self.balance)
		print "============================="

		if request > self.balance:
			print "Can't give all this money !!"
			print "============================="

		elif request < 0:
			print "Check your request plz"
			print "============================="
		
		else:
			while request <= self.balance and self.balance>0:
				if request == 0:
					break
				if request >= 100:
					print "give 100" 
					request = request - 100
					self.balance = self.balance - 100
				elif request >= 50:
					print "give 50"
					request = request - 50
					self.balance = self.balance - 50
				elif request >= 10:
					print "give 10"
					request = request - 10
					self.balance = self.balance - 10
				elif request >= 5:
					print "give 5"
					request = request - 5
					self.balance = self.balance - 5
				else:
					print "give " + str(request)
					self.balance = self.balance - request
					request = 0
			print "============================="
#------------------------------------
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
#------------------------------------

