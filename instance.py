class Instance:
	def __init__(self, initial_money=1000, initial_coin=0, fee=0.001):
		self.money=initial_money
		self.coin=initial_coin
		self.fee=fee
		self.price=0
		self.netWorth=self.money
	def buy(self, amount, price):
		if(amount<=self.money and amount>0):
			self.coin+=amount*(1-self.fee)/price
			self.money-=amount
			self.price=price
			self.netWorth=self.money+self.coin*self.price
	def sell(self, amount, price):
		if(amount<=self.coin and amount>0):
			self.money+=amount*(1-self.fee)*price
			self.coin-=amount
			self.price=price
			self.netWorth=self.money+self.coin*self.price
	def getNetWorth(self, price):
		return self.money+self.coin*price
	def updateNetWorth(self, price):
		self.netWorth = self.money+self.coin*price
	def show(self):
		print("Money: " + str(self.money))
		print("Coin: " + str(self.coin))
		print("Total value: " + str(self.netWorth))
