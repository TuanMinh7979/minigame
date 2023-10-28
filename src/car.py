import pygame
from os import walk
from random import choice
class Car(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.name='car'
        for folder_name,subfolder, img_list in walk("../graphics/cars"):
            car_name= choice(img_list)
            
        self.image= pygame.image.load("../graphics/cars/"+'green.png').convert_alpha()
        self.rect=self.image.get_rect(center= pos) 

        #float based movement
        self.pos= pygame.math.Vector2(self.rect.center)

        if pos[0] < 200:
            self.direction= pygame.math.Vector2(1,0)
        else: 
            self.direction= pygame.math.Vector2(-1,0) 
            self.image= pygame.transform.flip(self.image, True, False)  


        # self.direction= pygame.math.Vector2(1,0)
        self.speed = 150

        #collision
        self.hitbox= self.rect.inflate(0, -self.rect.height/2)

    def update(self, dt):
        #
        self.pos+=self.direction* self.speed*dt  
        self.hitbox.center=(round(self.pos.x), round(self.pos.y))  
        self.rect.center=(round(self.pos.x), round(self.pos.y))  
        if not -200 < self.rect.x<3400 : 
            # range in (0->3200)
            self.kill() 


