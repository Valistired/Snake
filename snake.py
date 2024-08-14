import random
import pygame
import sys
#plswork
pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

# -- game init area --

class SnakeHead:

    x = screen_width/2
    y = screen_height/2
    speed_x = 20
    speed_y = 20
    size = 20

    def __init__():
        Placeholder

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))

    def eating(self, Food):
        return self.x + self.size >= Food.x and \
                   self.x <= Food.x + Food.size and \
                   self.y + self.size >= Food.y and \
                   self.y <= Food.y + Food.size

    def collides_with_self(self, SnakeBody):
        return self.x + self.size >= SnakeBody.x and \
                   self.x <= SnakeBody.x + SnakeBody.size and \
                   self.y + self.size >= SnakeBody.y and \
                   self.y <= SnakeBody.y + SnakeBody.size
    
class SnakeBody:

    x = position_to_head_x
    y = position_to_head_y
    position_to_head_x = x - SnakeHead.x # nochmal überlegen
    position_to_head_y = y - SnakeHead.y # nochmal überlegen
    speed_x = 20
    speed_y = 20
    size = 20
    initial_length = 3

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.size, self.size)) 


class Food:

    x = random.choice(0, screen_width-size_x)
    y = random.choice(0, screen_height-size_y)
    size_x = 20
    size_y = 20

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))

# -- end game init area --

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))



 # -- end game tick --

    pygame.display.flip()
    pygame.time.Clock().tick(1)

pygame.quit()
sys.exit()
