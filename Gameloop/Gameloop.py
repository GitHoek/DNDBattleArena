import pygame
pygame.init()

class Gameloop(object):
	def __init__(self):

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 225)
		self.size = (640, 480)
		self.screen = pygame.display.set_mode(self.size)
		self.Width = 50
		self.Height = self.Width
		self.Margin = 50
		self.clock = pygame.time.Clock()
		self.Create_Grid_Clean()


	def Create_Grid_Clean(self):
		self.screen.fill(self.WHITE)
		for column in range(self.size[0]):
			for row in range(self.size[1]):
				if row % self.Margin == 0:
					if column % self.Margin == 0:
						pygame.draw.rect(self.screen, self.BLACK, [column, row, self.Height, self.Width], 1)

		self.grid = [[0 for x in range(int(self.size[0]/self.Width))] for y in range(int(self.size[1]/self.Height))]

	def run(self):

		Finished = False
		while Finished is False:
			# --- Main event loop
			for event in pygame.event.get():  # User did something
				if event.type == pygame.QUIT:  # If user clicked close
					Finished = True  # Flag that we are done so we exit this loop
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.Create_Grid_Clean()
					column = pos[0] // (self.Margin)
					row = pos[1] // (self.Margin)
					# Debug prints
					print("Click ", pos, "Grid coordinates: ", row, column)
					pygame.draw.rect(self.screen, self.BLUE, [column*self.Height, row*self.Width, self.Height, self.Width], 0)

			# --- Game logic should go here
			pos = pygame.mouse.get_pos()
			x = pos[0]
			y = pos[1]

			# --- Drawing code should go here

			pygame.display.flip()
			self.clock.tick(60)

		pygame.quit()

