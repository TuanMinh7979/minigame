import pygame


   
class CustomGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
        # Thiết lập màn hình
      
        # Thiết lập màu nền
        self.surf = pygame.Surface((500, 500))
        self.surf.fill((255, 255, 255))   # màu xanh dương
      

        # Tọa độ top-left của CustomGroup
   

    def draw(self):
        # Vẽ màn hình
        # self.screen.fill((0, 0, 255))  # màu xanh dương
        # super().update()
        df.blit(self.surf,(100, 100))
        for sprite in self.sprites():
            df.blit(sprite.image, (sprite.rect.x , sprite.rect.y))
class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface((50, 50))
        self.image.fill("red")  # màu trắng
        self.rect = self.image.get_rect()
        self.rect.center = (0, 300)
# Khởi tạo pygame
pygame.init()
screen_width = 500
screen_height = 600
df = pygame.display.set_mode((screen_width, screen_height))
# Tạo sprite group
sprite_group = CustomGroup()

# Tạo sprite



# Thêm sprite vào group
SimpleSprite(sprite_group)

# Chạy game loop


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ màn hình
    sprite_group.update()
    sprite_group.draw()
    pygame.display.update()


# Kết thúc game
pygame.quit()