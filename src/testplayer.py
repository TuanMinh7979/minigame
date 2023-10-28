import pygame
import math
from os import walk
import sys
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collistion_sprites):
       
        super().__init__(groups)
        self.import_assets()
        self.frame_idx= 0
        self.status= 'down'
        self.image= self.animations[self.frame_idx]
  
        

        self.rect= self.image.get_rect(center=pos)
        #float based movement
        self.pos= pygame.math.Vector2(self.rect.center)
        self.direction=pygame.math.Vector2()
        self.speed= 200

        # ---Collistion
        self.collision_sprites= collistion_sprites
        self.hitbox= self.rect.inflate(0, -self.rect.height/2) 
    def move(self, dt):
        # MY WAY:
        # if abs(self.direction.x)==1 and abs(self.direction.y)==1 :
        #       self.pos+=self.direction* self.speed*dt  / math.sqrt(2)
        # else: 
        #       self.pos+=self.direction* self.speed*dt  
        # CORRECT WAY:   
        # 	# normalize a vector -> the length of a vector is going to be 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize() 
        # => from [1,1] to [0.7, 0.7] 

        # * x movement + collistion  
        #  x movement: 
        self.pos.x+= self.direction.x * self.speed*dt  
        self.hitbox.centerx= round(self.pos.x)
        self.rect.centerx= round(self.pos.x)
        #  x collistion: 
        self.collistion('ox')


        # * y movement + collistion 
        self.pos.y+=self.direction.y * self.speed* dt
        self.rect.centery= round(self.pos.y)
        self.hitbox.centery= round(self.pos.y)
        #  y collistion: 
        self.collistion('oy')


        # self.pos+=self.direction* self.speed*dt  
        # self.rect.center= (round(self.pos.x), round(self.pos.y))


 

        
     
    def update(self, dt):
    
        self.move(dt)
        self.animate(dt)
        self.restrict()
     
    def import_assets(self):


        self.animations= []

        # print(walk('../graphics/player'))
        
        for i, obj in enumerate(walk('../testplayer')):


            for filename in obj[2]:
               
                    path= obj[0].replace('\\','/')+'/'+filename
        #             # print(path)
        #             key=folder[0].split("\\")[1]          
        #             # print(key)          
                    surf=pygame.image.load(path).convert_alpha()       
                    self.animations.append(surf)
            # print(self.animations)        
        # print(self.animations)  
    def animate(self, dt):
        # * PATTERN: to make move show slow: 
        cur_animation=  self.animations
        # if self.direction.magnitude()!=0:
        self.frame_idx+=10*dt     
        if self.frame_idx>=len(cur_animation) :
            self.frame_idx=0
        self.image= cur_animation[int(self.frame_idx)]

    def collistion(self, direction):
        # pygame.sprite.spritecollide(self,self.collision_sprites, True)
        if direction=='ox':
            for sprite in self.collision_sprites.sprites():
                if sprite.hitbox.colliderect(self.hitbox):
                    
                    if hasattr(sprite, 'name') and sprite.name=='car':
                        print("abc")
                        # pygame.quit()
                        # sys.exit()

                    if self.direction.x>0:
                        self.hitbox.right= sprite.hitbox.left
                        self.rect.centerx= self.hitbox.centerx
                        self.pos.x= self.hitbox.centerx
                    if self.direction.x < 0 : 
                        self.hitbox.left= sprite.hitbox.right
                        self.rect.centerx= self.hitbox.centerx
                        self.pos.x= self.hitbox.centerx

        else :   
            for sprite in self.collision_sprites.sprites():
                if sprite.hitbox.colliderect(self.hitbox):
    
                    if hasattr(sprite, 'name') and sprite.name=='car':
                        print("abc")
                        # pygame.quit()
                        # sys.exit()
                    if self.direction.y>0:
                        self.hitbox.bottom= sprite.hitbox.top
                        self.rect.centery= self.hitbox.centery
                        self.pos.y= self.hitbox.centery
                    if self.direction.y < 0 : 
                        self.hitbox.top= sprite.hitbox.bottom
                        self.rect.centery= self.hitbox.centery
                        self.pos.y= self.hitbox.centery   

    def restrict(self):
        if self.rect.left< 640:
            self.pos.x= 640 +self.rect.width /2
            # self.hitbox.left = 640
            # self.rect.left=640
        if self.rect.right> 2560:
            self.pos.x= 2560-self.rect.width/2    
            # self.hitbox.right= 2560
            # self.rect.right= 2560
        if self.rect.bottom > 3500:

            self.pos.y= 3500- self.rect.height /2    
    
            # self.hitbox.centery= self.rect.centery
        
   
        

