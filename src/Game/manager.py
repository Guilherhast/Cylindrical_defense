# Class to implement start function in pgzero
# AI told me I couldn't do it
class Manager():
	def __init__(self, start, loop, draw):
		self.__start = start
		self.__loop = loop
		self.__draw = draw
		self.__update_fn = self.__run_start

	def update(self, dt):
		self.__update_fn(dt)

	def draw(self):
		self.__draw(self)

	# Will run the start function
	def __run_start(self, dt):
		self.__start(self, dt)
		self.__update_fn = self.__run_loop

	# Will continue the loop
	def __run_loop(self, dt):
		self.__loop(self, dt)

