## Class to manage game controls
class Controller():
	def __init__(self, game, keyboard, actions = {}, post_update = None):
		self.__post_update = post_update
		self.__game = game
		self.__keyboard = keyboard
		self.__actions = actions

	### Update the game using controller actions
	def update(self, dt):
		#### Execute actions based on keyboard input
		for key in self.__actions.keys():
			if self.__keyboard[key]:
				self.__actions[key](self.__game, dt)
		#### Run post update function
		self.__run_post_update(dt)

	### Run the post update function if it exists
	def __run_post_update(self, dt):
		if self.__post_update is not None:
			self.__post_update(self.__game, dt)

