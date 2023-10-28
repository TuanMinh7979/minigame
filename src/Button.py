import math
import pygame
from random import randint, uniform
SCREEN = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
class Button: 
	def __init__(self, win,value):
		self.win=win
		self.font = pygame.font.Font('../graphics/arial-unicode-ms.ttf', 30) 
		self.text_suft= self.font.render("0",True, 'white')
		self.text_rect= self.text_suft.get_rect(midbottom=(SCREEN_WIDTH/ 2, SCREEN_HEIGHT-80))
		self.value=value
		
	def update(self):

		self.text_suft= self.font.render(self.value,True, 'white')
	
	def draw(self):	
		self.win.blit(self.text_suft, (self.text_rect.centerx-60, self.text_rect.centery-15))
		
		pygame.draw.rect(self.win, (255, 255, 255), self.text_rect.inflate(280, 60), 8, 5)

	