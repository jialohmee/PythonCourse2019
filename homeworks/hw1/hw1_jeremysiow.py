import random

class Portfolio():	# create portfolio class
	def __init__(self):
		self.cash = 0.0
		self.stock = {}
		self.mf = {}
		self.transactions = []

	def __str__(self):
		return "cash: %s \nstock: %s \nmutual funds: %s" % (format(self.cash, '.2f'), self.stock.items(), 
			self.mf.items())
	
	def addCash(self, amount_cash):
		self.cash += float(amount_cash)
		self.transactions.append("Deposited $" + str(format(amount_cash, '.2f')))
		return self.cash

	def buyStock(self, stock, amount_shares):
		if stock not in self.stock.keys():
			self.stock[stock.name] = amount_shares
		else:
			self.stock[stock.name] += amount_shares
		self.cash -= stock.price * amount_shares
		self.transactions.append("Bought " + str(amount_shares) + 
			" shares of " + str(stock.name) + " at $" + str(format(stock.price, '.2f')) + " per share")

	def buyMutualFund(self, fund, amount_shares):
		if fund not in self.mf.keys():
			self.mf[fund.name] = amount_shares
		else:
			self.mf[fund.name] += amount_shares
		self.cash -= float(1) * amount_shares # $1/share for mutual funds
		self.transactions.append("Bought " + str(amount_shares) + " shares of " + str(fund.name))

	def withdrawCash(self, amount_cash):
		self.cash -= float(amount_cash)
		self.transactions.append("Withdrew $" + str(format(amount_cash, '.2f')))

	def sellStock(self, stock, amount_shares):
		self.stock[stock.name] -= amount_shares
		sale_price = random.uniform(0.5 * stock.price, 1.5 * stock.price)
		self.cash += sale_price * amount_shares
		self.transactions.append("Sold " + str(amount_shares) + " shares of " + str(stock.name) + 
			" at $" + str(format(sale_price, '.2f')) + " per share")

	def sellMutualFund(self, fund, amount_shares):
		self.mf[fund.name] -= amount_shares
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
portfolio.sellStock(s, 1)
portfolio.sellMutualFund(mf1, 3)
portfolio.withdrawCash(50)
portfolio.history()
print(portfolio)
