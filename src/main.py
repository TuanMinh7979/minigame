import pygame, sys
from settings import *
from player import Player
from car import Car
from random import choice
from sprite import SimpleSprite
from sprite import LongSprite
from Button import Button
from Score import Score
from win_screen import WinScreen
class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset=pygame.math.Vector2(0,0)
        self.bg= pygame.image.load('../graphics/main/map.png').convert()
        self.fg= pygame.image.load('../graphics/main/overlay.png').convert_alpha()
       
    def customize_draw(self):

        #change offset:
        self.offset.x= player.rect.centerx-WINDOW_WIDTH/2
        self.offset.y= player.rect.centery-WINDOW_HEIGHT/2
        # self.offset.x= -600/2
        # self.offset.y= -300/2
 
        #draw bg 
        display_surface.blit(self.bg,-self.offset)
        # instead of drawing the sprite image, draw a green rect
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            # size=sprite.rect.size
            # surf= pygame.Surface(size)
            # surf.fill('blue')
            new_sprite_offset_pos= sprite.rect.topleft-self.offset
            # new_sprite_offset_pos= sprite.rect.topleft
            # print(".....",sprite.rect)
            # print(offset_pos)
            display_surface.blit(sprite.image, new_sprite_offset_pos)
        #draw fg    
        display_surface.blit(self.fg,-self.offset)    

                



pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('EasyGame')
logo = pygame.image.load('../graphics/icon.png')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

#create groups
# all_sprites= pygame.sprite.Group()
all_sprites= AllSprites()
obstacle_sprites= pygame.sprite.Group()
player=Player((2062, 3274),all_sprites, obstacle_sprites )
car=Car((600,200), all_sprites)


#timer
car_timer= pygame.event.custom_type()
pygame.time.set_timer(car_timer, 80)
# game loop
#
car_pos_list=[]

#sprite


for file_name, pos_list in SIMPLE_OBJECTS.items():
    path=f'../graphics/objects/simple/{file_name}.png'
    suft= pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        SimpleSprite(suft, pos, [all_sprites,obstacle_sprites])

for file_name, pos_list in LONG_OBJECTS.items():
    path=f'../graphics/objects/long/{file_name}.png'
    suft= pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        LongSprite(suft, pos,  [all_sprites,obstacle_sprites])

# font 
font= pygame.font.Font("../graphics/arial-unicode-ms.ttf", 50)
win_surf = font.render("Thắng", True, 'White')
win_rect= win_surf.get_rect(center= (WINDOW_WIDTH/2, 226))

lose_surf = font.render("Thua Rồi Bạn Ơi!", True, 'White')
lose_rect= lose_surf.get_rect(center= (WINDOW_WIDTH/2, 226))

score= Score(display_surface, player)
newGame_button = Button(display_surface, "Chơi mới")
tryAgain_button = Button(display_surface, "Chơi lại")
# *win screen
win_scene= WinScreen(display_surface)
start_game= True

# * lose screen
lose_scene_image=pygame.transform.scale(pygame.image.load("../graphics/other/thua.jpg").convert_alpha(),  (WINDOW_WIDTH, WINDOW_HEIGHT))
while True:
	
    # event loop 

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            mouse_x, mouse_y = pygame.mouse.get_pos()
 

            # Kiểm tra xem điểm chuột có nằm trong hình chữ nhật của nút không
            if newGame_button.text_rect.x-120 < mouse_x < newGame_button.text_rect.x + 180  and newGame_button.text_rect.y < mouse_y < newGame_button.text_rect.y + 60:
                start_game=True
                player.reset_pos()
                win_scene.animateIdx=0
                for sprite in all_sprites:
                    # Kiểm tra nếu đối tượng là một instance của lớp Car
                    if isinstance(sprite, Car):
                        # Xóa đối tượng Car
                        sprite.kill()

         
    

              
          
            if tryAgain_button.text_rect.x-120 < mouse_x < tryAgain_button.text_rect.x + 180  and tryAgain_button.text_rect.y < mouse_y < tryAgain_button.text_rect.y + 60:
                start_game=True
                player.reset_pos()
                win_scene.animateIdx=0
                for sprite in all_sprites:
                    # Kiểm tra nếu đối tượng là một instance của lớp Car
                    if isinstance(sprite, Car):
                        # Xóa đối tượng Car
                        sprite.kill()
        

    
           
     
           

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==car_timer:
         

            random_pos= choice(CAR_START_POSITIONS) 
            if random_pos not in car_pos_list:
                car_pos_list.append(random_pos)
                new_pos=(random_pos[0],random_pos[1])
                Car(random_pos,[all_sprites, obstacle_sprites])
            if len(car_pos_list)>5:
                del car_pos_list[0]    
    # delta time 
    dt = clock.tick() / 1000	

# draw bg
    display_surface.fill("blue")
    if player.health==0:
        display_surface.blit(lose_scene_image, (0,0))
        start_game=False
        display_surface.blit(lose_surf, lose_rect)     
        tryAgain_button.update()   
        tryAgain_button.draw() 


    elif  player.pos.y >= 1180 and start_game== True:
        display_surface.fill("black")
        all_sprites.update(dt)	
        # all_sprites.draw(display_surface)
        all_sprites.customize_draw()
        score.update()
        score.draw()
    else: 
        display_surface.fill("blue")
        
        win_scene.updateAndDraw(dt)
        start_game=False
        display_surface.blit(win_surf, win_rect)     
        newGame_button.update()   
        newGame_button.draw()   
    pygame.display.update()
