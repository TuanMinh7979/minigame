import math
import pygame
from random import randint, uniform
SCREEN = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
class Score: 
	def __init__(self, win, player):
		self.win=win
		self.font = pygame.font.Font('../graphics/arial-unicode-ms.ttf', 50) 
		self.text_suft= self.font.render("0",True, 'white')
		self.text_rect= self.text_suft.get_rect(midbottom=(SCREEN_WIDTH/ 2, SCREEN_HEIGHT-80))
		self.player= player
		self.heart_img= pygame.image.load("../graphics/other/h2real.png").convert_alpha()
		self.heart_surf = pygame.transform.scale(self.heart_img, (30,30))
		self.heart_rect=self.heart_surf.get_rect(center=(self.text_rect.centerx+30, self.text_rect.centery))
	def update(self):
		score_text=  str(self.player.health) 
		self.text_suft= self.font.render(score_text,True, 'white')
	
	def draw(self):	
		self.win.blit(self.text_suft, self.text_rect)
		self.win.blit(self.heart_surf, self.heart_rect)

	