import pygame
pygame.init()

class Gameloop(object):
	def __init__(self):

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.DARK_GREEN = (0, 200, 0)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 225)
		self.size = (int(1280), int(700))
		self.screen = pygame.display.set_mode(self.size)
		self.Width = 50
		self.Height = self.Width
		self.Margin = 50
		self.MenuSize = 280
		self.ButtonSize_Height = 50
		self.ButtonSize_Width = 100
		self.Add_Character_Button_Height = 100
		self.clock = pygame.time.Clock()
		self.Create_View()

	def Create_View(self):
		self.screen.fill(self.WHITE)
		for column in range(self.size[0]-self.MenuSize):
			for row in range(self.size[1]):
				if row % self.Margin == 0:
					if column % self.Margin == 0:
						pygame.draw.rect(self.screen, self.BLACK, [column, row, self.Height, self.Width], 1)
		pygame.draw.rect(self.screen, self.WHITE, [self.size[0]-self.MenuSize, 0, self.MenuSize, self.size[1]],0)
		self.grid = [[0 for x in range(int((self.size[0]-self.MenuSize)/self.Width))] for y in range(int(self.size[1]/self.Height))]
		pygame.draw.rect(self.screen, self.GREEN, [self.size[0] - (self.MenuSize*8/10), self.Add_Character_Button_Height, (self.MenuSize*6/10), self.ButtonSize_Height], 0)

	def Colour_Square_Blue(self, pos):
		self.Create_View()
		column = pos[0] // (self.Margin)
		row = pos[1] // (self.Margin)
		# Debug prints
		print("Click ", pos, "Grid coordinates: ", row, column)
		pygame.draw.rect(self.screen, self.BLUE, [column * self.Height, row * self.Width, self.Height, self.Width], 0)

	def Flicker_Add_Character_Button(self,hue):
		if hue is "DARK":
			pygame.draw.rect(self.screen, self.DARK_GREEN,
							 [self.size[0] - (self.MenuSize * 8 / 10), self.Add_Character_Button_Height, (self.MenuSize * 6 / 10), self.ButtonSize_Height], 0)
		elif hue is "LIGHT":
			pygame.draw.rect(self.screen, self.GREEN,
							 [self.size[0] - (self.MenuSize * 8 / 10), self.Add_Character_Button_Height, (self.MenuSize * 6 / 10), self.ButtonSize_Height], 0)

	def run(self):

		Finished = False
		while Finished is False:
			# --- Main event loop
			for event in pygame.event.get():  # User did something
				if event.type == pygame.QUIT:  # If user clicked close
					Finished = True  # Flag that we are done so we exit this loop
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if pos[0] < 1000:
						self.Colour_Square_Blue(pos)


			# --- Game logic should go here
			pos = pygame.mouse.get_pos()
			Mouse_x = pos[0]
			Mouse_y = pos[1]

			Add_Character_Button_X0 = self.size[0]-(self.MenuSize*8/10)
			Add_Character_Button_X1 = self.size[0]-(self.MenuSize*8/10) + (self.MenuSize*6/10)
			Add_Character_Button_Y0 = self.Add_Character_Button_Height
			Add_Character_Button_Y1 = self.Add_Character_Button_Height + self.ButtonSize_Height

			if Mouse_x > Add_Character_Button_X0 and Mouse_x < Add_Character_Button_X1 and Mouse_y > Add_Character_Button_Y0 and Mouse_y < Add_Character_Button_Y1:
				self.Flicker_Add_Character_Button("DARK")
			else:
				self.Flicker_Add_Character_Button("LIGHT")

			# --- Drawing code should go here

			pygame.display.flip()
			self.clock.tick(60)

		pygame.quit()

