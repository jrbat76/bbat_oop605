import os 
import turtle 
print(os.getcwd())


# PYTHON VARIBALS, EXPRESSIONS, STATEMENTS, FUNCTIONS

class FirstDay:

	def __init__(self, cash = None, int_rate = None, num_years = None):

		self.cash = cash 			# cash money when time is at one
		self.int_rate = int_rate	# interest rate is at one and takes float
		self.num_years = num_years	# number of years is at one and takes int 


	# Calculating the future value of an investment 
	def getFutureValue(self):
		# future value is given by following: Future Value (FV) = C0 (1 + r) ** n
		future_value = 0

		future_value = self.cash * (1 + self.int_rate) ** self.num_years

		return future_value





ex1 = FirstDay(1000, 1.07, 10)
print('Investing $1000 with 7 percent annual interest rate will return {} after 10 years.'.format(ex1.getFutureValue()))
