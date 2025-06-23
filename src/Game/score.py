# Class to hold level info
class Score():
	def __init__(self, win_function):
		self.__win_function = win_function
		self.__max_level = 10
		self.__level = 0
		self.__score = 0

	def get_score(self):
		return self.__score

	def get_level(self):
		return self.__level

	def score(self, points):
		self.__score += points
		self.check_next_level()

	def check_next_level(self):
		if self.__score > 2*self.__level:
		#if self.__score > 2**self.__level:
			self.__level += 1
			self.check_win_condition()

	def check_win_condition(self):
		if self.__level > self.__max_level:
			self.__win_function()

