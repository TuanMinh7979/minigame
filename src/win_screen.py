import math
import pygame
from random import randint, uniform
from os import walk
SCREEN = SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

pygame.mixer.init()

class WinScreen():
        def __init__(self, win):
            self.win = win
            self.animateIdx= 0
            self.frame_idx= 0
    
            self.animations= []
            self.animations1= []
            self.import_assets()
            # print(self.animations)
         
        def animate(self, dt):
            # * PATTERN: to make move show slow: 
            cur_animation= None
            if self.animateIdx==0:
             cur_animation=  self.animations1
            else: 
             cur_animation= self.animations
            # if self.direction.magnitude()!=0:
            if self.animateIdx==0:
                self.frame_idx+=30*dt   
            else: 
                self.frame_idx+=20*dt         
            if self.frame_idx>=len(cur_animation) :
                if self.animateIdx== 0:
                   self.animateIdx=1
                self.frame_idx=0
            self.image= cur_animation[int(self.frame_idx)]    
        def updateAndDraw(self,dt):
            self.animate(dt)
            self.win.blit(self.image, (0,0))
        def import_assets(self):
            
            # print(enumerate(walk('../other/win_scene/short')))            
            for i, obj in enumerate(walk('../graphics/other/win_scene2/short2')):
                for filename in obj[2]:
                  
                        path= obj[0].replace('\\','/')+'/'+filename
                        surf=pygame.transform.scale(pygame.image.load(path).convert_alpha(),  (SCREEN_WIDTH, SCREEN_HEIGHT))       
                        self.animations.append(surf)
            for i, obj in enumerate(walk('../graphics/other/win_scene2/long')):
                for filename in obj[2]:
                  
                        path= obj[0].replace('\\','/')+'/'+filename
                        surf=pygame.transform.scale(pygame.image.load(path).convert_alpha(),  (SCREEN_WIDTH, SCREEN_HEIGHT))       
                        self.animations1.append(surf)


            
    
		
