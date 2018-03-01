import pygame
pygame.init()

class GameField(object):
	def __init__(self):
		self.mousePos = (0,0)
		self.currentMousePos = (-1,-1)
		self.old_column = -1
		self.old_row = -1
		self.lmbClick = False
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
		self.SmallText = pygame.font.Font("freesansbold.ttf",20)

	def text_objects(self,text, font):
		textSurface = font.render(text, True, self.BLACK)
		return textSurface, textSurface.get_rect()

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
		self.textSurf, self.textRect = self.text_objects("Add Character", self.SmallText)
		self.textRect.center = (self.size[0] - (self.MenuSize*8/10) + (self.MenuSize*6/10)/2) , (self.Add_Character_Button_Height + (self.ButtonSize_Height/2))
		self.screen.blit(self.textSurf, self.textRect)

	def Update_view(self):
		self.Character_Button()

		if(self.lmbClick):
			self.currentMousePos = self.mousePos
		self.Colour_Square_Blue(self.currentMousePos)


	def Colour_Square_Blue(self, mousePos):

		column = mousePos[0]
		row = mousePos[1]

		column_leftover = column % 50
		column -= column_leftover

		row_leftover = row % 50
		row -= row_leftover

		if (self.old_column < (self.size[0] - self.MenuSize)):
			pygame.draw.rect(self.screen, self.WHITE, [self.old_column, self.old_row, self.Height, self.Width], 0)
			pygame.draw.rect(self.screen, self.BLACK, [self.old_column, self.old_row, self.Height, self.Width], 1)

		if(column < (self.size[0] - self.MenuSize)):
			pygame.draw.rect(self.screen, self.BLUE, [column, row, self.Height, self.Width], 0)

		self.old_column = column
		self.old_row = row


	def Flicker_Add_Character_Button(self,hue):
		if hue is "DARK":
			pygame.draw.rect(self.screen, self.DARK_GREEN,
							 [self.size[0] - (self.MenuSize * 8 / 10), self.Add_Character_Button_Height, (self.MenuSize * 6 / 10), self.ButtonSize_Height], 0)
			self.screen.blit(self.textSurf, self.textRect)
		elif hue is "LIGHT":
			pygame.draw.rect(self.screen, self.GREEN,
							 [self.size[0] - (self.MenuSize * 8 / 10), self.Add_Character_Button_Height, (self.MenuSize * 6 / 10), self.ButtonSize_Height], 0)
			self.screen.blit(self.textSurf, self.textRect)

	def Character_Button(self):

		Mouse_x = self.mousePos[0]
		Mouse_y = self.mousePos[1]

		Add_Character_Button_X0 = self.size[0]-(self.MenuSize*8/10)
		Add_Character_Button_X1 = self.size[0]-(self.MenuSize*8/10) + (self.MenuSize*6/10)
		Add_Character_Button_Y0 = self.Add_Character_Button_Height
		Add_Character_Button_Y1 = self.Add_Character_Button_Height + self.ButtonSize_Height

		if Add_Character_Button_X0 < Mouse_x < Add_Character_Button_X1 and Add_Character_Button_Y0 < Mouse_y < Add_Character_Button_Y1:
			self.Flicker_Add_Character_Button("DARK")
		else:
			self.Flicker_Add_Character_Button("LIGHT")
