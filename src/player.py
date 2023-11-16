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
        self.image= self.animations[self.status][self.frame_idx]
  
        

        self.rect= self.image.get_rect(center=pos)
        #float based movement
        self.pos= pygame.math.Vector2(self.rect.center)
        self.direction=pygame.math.Vector2()
        self.speed= 200

        # ---Collistion
        self.collision_sprites= collistion_sprites
        self.hitbox= self.rect.inflate(0, -self.rect.height/2) 

        self.health= 3

        self.is_shocked=False

        self.line_lst_time_show=0
        self.line_frame_show_cnt=0
        self.line_show_times=0

        


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


 
    def input(self):
        keys = pygame.key.get_pressed()
        
        # horizontal input 
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

        # vertical input 
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
    def update(self, dt):

        _current_time= pygame.time.get_ticks()
        if self.is_shocked: 
            if  _current_time-self.line_lst_time_show>100 and self.line_frame_show_cnt<30 and self.line_show_times<3 : 
        
                self.line_frame_show_cnt+=1


                self.image=pygame.image.load( "../graphics/player/shock/shock.png").convert_alpha()  
                self.rect= self.image.get_rect(center=self.pos)

                #float based movement
       
              
              
            if self.line_frame_show_cnt==30:
                self.image=pygame.image.load( "../graphics/player/up/0.png").convert_alpha()  
                self.rect= self.image.get_rect(center=self.pos)

                self.line_frame_show_cnt=0
                self.line_lst_time_show=_current_time
                self.line_show_times+=1
            elif self.line_show_times==3:
                self.is_shocked=False
                self.line_show_times=0
            
     
        else:
                self.input()
                self.move(dt)
                self.animate(dt)
                self.restrict()
     
    def import_assets(self):


        self.animations= {}
        # print(walk('../graphics/player'))
        for i, folder in enumerate(walk('../graphics/player')):
            # print("folder",i,folder)
            if i==0:
                # i=0 is root folder
                for name in folder[1]:
                    # subfolder name list inside root folder
                    self.animations[name]=[]
            else:
                for filename in folder[2]:
                    # print(filename)
                    path= folder[0].replace('\\','/')+'/'+filename
                    # print(path)
                    key=folder[0].split("\\")[1]          
                    # print(key)          
                    surf=pygame.image.load(path).convert_alpha()       
                    self.animations[key].append(surf)
            # print(self.animations)        
        # print(self.animations)  
    def animate(self, dt):
        # * PATTERN: to make move show slow: 


        cur_animation=  self.animations[self.status]
        if self.direction.magnitude()!=0:
            self.frame_idx+=10*dt     
            if self.frame_idx>=len(cur_animation) :
                self.frame_idx=0
            self.image= cur_animation[int(self.frame_idx)]

    def reset_pos(self):
            self.health= 3
            self.pos=  pygame.math.Vector2(2062, 3274)
            self.hitbox= self.rect.inflate(0, -self.rect.height/2)
            self.is_shocked=False
            self.status= 'up'

    def collistion(self, direction):
       
        # pygame.sprite.spritecollide(self,self.collision_sprites, True)
        if direction=='ox':
            for sprite in self.collision_sprites.sprites():
                if sprite.hitbox.colliderect(self.hitbox):
          
                    if hasattr(sprite, 'name') and sprite.name=='car':
            
                  
                        self.is_shocked=True
                
                        self.health-=1
                       
                        if self.rect.y>2800:
                      
                            self.rect.center= (2062, 3200)
                           
                        elif self.rect.y>2300:
                  
                            self.rect.center=(2062, 2700)
                           
                        elif self.rect.y>1500: 
                       
                            self.rect.center= (2062, 2100)
                        elif self.rect.y>1100: 
                       
                           self.rect.center= (2062, 1500)
                           
                     
                        self.pos= pygame.math.Vector2(self.rect.center)
                        self.hitbox= self.rect.inflate(0, -self.rect.height/2) 
                        if self.health==0:
                            # pygame.quit()
                            # sys.exit()
                         return  
                        return  
           
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
                        
                        self.is_shocked=True
                
                        self.health-=1
                       
                        if self.rect.y>2800:
                       
                            self.rect.center= (2062, 3200)
                           
                        elif self.rect.y>2300:
                         
                            self.rect.center=(2062, 2700)
                           
                        elif self.rect.y>1500: 
                           
                            self.rect.center= (2062, 2100)
                        elif self.rect.y>1100:   
                      
                           self.rect.center= (2062, 1500)
                     
                        self.pos= pygame.math.Vector2(self.rect.center)
                        self.hitbox= self.rect.inflate(0, -self.rect.height/2) 
                        if self.health==0:
                            # pygame.quit()
                            # sys.exit()
                         return    
                        return
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
        
   
        

