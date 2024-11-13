import pygame
import sys
from random import randint

WIN_SIZE = 900
CELL_SIZE = WIN_SIZE //3
INF = float('inf')
vec2 = pygame.math.Vector2


class TicTacToe:
	def __init__(self, game):
		self.game = game
		self.field_image = self.get_scaled_image(path='/home/erik/repos/pygame/blender/tictactoe/900by900.jpg', res=[WIN_SIZE]*2)
		self.O_image = self.get_scaled_image(path='/home/erik/repos/pygame/blender/tictactoe/O.jpg', res=[CELL_SIZE]*2)
		self.X_image = self.get_scaled_image(path='/home/erik/repos/pygame/blender/tictactoe/x.jpg', res=[CELL_SIZE]*2)
		self.foo_image = self.get_scaled_image(path='/home/erik/repos/pygame/blender/tictactoe/foo.jpg', res=[CELL_SIZE]*2)
		self.game_array = [[INF, INF, INF],
				   [INF, INF, INF],
				   [INF, INF, INF]]
		self.player = randint(0, 2)

	def run_game_process(self):
		current_cell = vec2(pygame.mouse.get_pos()) // CELL_SIZE
		col, row = map(int, current_cell)
		left_click = pygame.mouse.get_pressed()[0]

		if left_click and self.game_array[row][col] == INF:
			self.game_array[row][col] = self.player
			self.player = (self.player + 1) %3

	def draw_objects(self):
		for y, row in enumerate(self.game_array):
			for x, obj in enumerate(row):
				if obj != INF:
					self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)

	def draw(self):
		self.game.screen.blit(self.field_image, (0, 0))
		self.draw_objects()

	@staticmethod
	def get_scaled_image(path, res):
		img = pygame.image.load(path)
		return pygame.transform.smoothscale(img, res)

	def run(self):
		self.draw()
		self.run_game_process()

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode([WIN_SIZE] * 2)
		self.clock = pygame.time.Clock()
		self.tic_tac_toe = TicTacToe(self)

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()	

	def run(self):
		while True:
			self.tic_tac_toe.run()
			self.check_events()
			pygame.display.update()
			self.clock.tick(60)
			

if __name__ == '__main__':
	game = Game()
	game.run()
