class Drawer():
	def __init__(self, first_draw, loop_draw):
		self.__fist_draw = first_draw
		self.__loop_draw = loop_draw
		self.__draw_fn = self.__run_first_draw

	def draw(self):
		self.__draw_fn()

	def __run_first_draw(self):
		self.__fist_draw(self)
		self.__draw_fn = self.__run_loop_draw

	def __run_loop_draw(self):
		self.__loop_draw(self)

