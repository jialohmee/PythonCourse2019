import random

class Portfolio():	# create portfolio class
	def __init__(self):
		self.cash = 0.0
		self.stock = {}
		self.mf = {}
		self.bond = {}
		self.transactions = []

	def __str__(self):
		return "cash: $%s\nstocks: %s\nmutual funds: %s\nbonds: %s" % (format(self.cash, '.2f'), 
			{value : key for key, value in self.stock.items()}, 
			{value : key for key, value in self.mf.items()},
			{value : key for key, value in self.bond.items()})
	
	def addCash(self, amount_cash):
		self.cash += float(amount_cash)
		self.transactions.append("Deposited $" + str(format(amount_cash, '.2f')))
		return self.cash

	def buyStock(self, stock, amount_shares):
		if self.cash >= stock.price * amount_shares:
			self.cash -= stock.price * amount_shares
			self.transactions.append("Bought " + str(amount_shares) + 
			" shares of " + str(stock.name) + " at $" + str(format(stock.price, '.2f')) + " per share")
			if stock not in self.stock.keys():
				self.stock[stock.name] = amount_shares
			else:
				self.stock[stock.name] += amount_shares
		else:
			print("You do not have enough cash")

	def buyMutualFund(self, fund, amount_shares):
		if self.cash >= 1 * amount_shares:
			self.cash -= 1 * amount_shares # $1/share for mutual funds
			self.transactions.append("Bought " + str(amount_shares) + " shares of " + str(fund.name))
			if fund not in self.mf.keys():
				self.mf[fund.name] = float(format(amount_shares, '.2f'))
			else:
				self.mf[fund.name] += float(format(amount_shares, '.2f'))
		else:
			print("You do not have enough cash")
		
	def withdrawCash(self, amount_cash):
		if self.cash >= amount_cash:
			self.cash -= float(amount_cash)
			self.transactions.append("Withdrew $" + str(format(amount_cash, '.2f')))
		else:
			print("You do not have enough cash")

	def sellStock(self, stock, amount_shares):
		self.stock[stock.name] -= float(format(amount_shares, '.2f'))
		sale_price = random.uniform(0.5 * stock.price, 1.5 * stock.price)
		self.cash += sale_price * amount_shares
		self.transactions.append("Sold " + str(amount_shares) + " shares of " + str(stock.name) + 
			" at $" + str(format(sale_price, '.2f')) + " per share")

	def sellMutualFund(self, fund, amount_shares):
		self.mf[fund.name] -= float(format(amount_shares, '.2f'))
		sale_price = random.uniform(0.9, 1.2)
		self.cash += sale_price * amount_shares
		self.transactions.append("Sold " + str(amount_shares) + " shares of " + str(fund.name) +
			" at $" + str(format(sale_price, '.2f')) + " per share")

	def history(self):
		for transaction in self.transactions:
			print(transaction)

class Stock(Portfolio):	# create stock subclass
	def __init__(self, name, price):
		self.name = str(name)
		self.price = float(price)

class MutualFund(Portfolio): # create mutual funds subclass
	def __init__(self, name):
		self.name = str(name)

class Bond(Portfolio):
	def __init__(self, name):
		self.name = str(name)


# Should perform the following:
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock("HFH", 20)
portfolio.buyStock(s, 5)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(mf1, 10.3)
portfolio.buyMutualFund(mf2, 2)
print(portfolio)
portfolio.sellMutualFund(mf1, 3)
portfolio.sellStock(s, 1)
portfolio.withdrawCash(50)
portfolio.history()
