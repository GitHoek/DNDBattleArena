import pygame
from GameField import GameField
pygame.init()
Map = GameField.GameField()


class Gameloop(object):
	def __init__(self):
		self.i = 0
		self.clock = pygame.time.Clock()

	def run(self):

		Finished = False
		while Finished is False:
			# --- Main event loop
			pos = pygame.mouse.get_pos()
			Map.mousePos = pos
			Map.Create_View()

			for event in pygame.event.get():  # User did something
				if event.type == pygame.QUIT:  # If user clicked close
					Finished = True  # Flag that we are done so we exit this loop
				elif event.type == pygame.MOUSEBUTTONDOWN:
					Map.lmbClick = True
				elif event.type != pygame.MOUSEBUTTONDOWN:
					Map.lmbClick = False

			pygame.display.flip()
			self.clock.tick(60)

		pygame.quit()
