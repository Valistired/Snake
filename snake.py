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

    first_body = None

    def __init__(self, x_position, y_position, key_up, key_down, key_left, key_right):
        self.x = x_position
        self.y = y_position
        self.key_up = key_up
        self.key_down = key_down
        self.key_left = key_left
        self.key_right = key_right

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))

        if self.first_body is not None:
            self.first_body.draw()

    def tick(self, keys):
        if keys[self.key_up]:
            self.y -= self.speed_y
        elif keys[self.key_down]:
            self.y += self.speed_y
        elif keys[self.key_left]:
            self.x -= self.speed_x
        elif keys[self.key_right]:
            self.x += self.speed_x


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

    def add_snake_part(self):
        if self.first_body is None:
            self.first_body = SnakeBody(random.choice([0, screen_width-self.size]),
                                                                               random.choice([0, screen_height-self.size]))
        else:
            self.first_body.add_snake_part()
    
class SnakeBody:

    # Erik hat gemeint, dass für meine Idee für den Körper am besten als Linked List umgesetzt werden kann

    speed_x = 20
    speed_y = 20
    size = 20
    initial_length = 3

    next_body = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.size, self.size))

        if self.next_body is not None:
            self.next_body.draw()

    def add_snake_part(self):
        if self.next_body is None:
            self.next_body = SnakeBody(random.choice([0, screen_width-self.size]),
                                       random.choice([0, screen_height-self.size]))
        else:
            self.next_body.add_snake_part()

class Food:
    size_x = 20
    size_y = 20

    x = random.choice([0, screen_width-size_x])
    y = random.choice([0, screen_height-size_y])

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))

# -- end game init area --

head = SnakeHead(SnakeHead.speed_x, SnakeHead.speed_y, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
head.add_snake_part()
head.add_snake_part()
head.add_snake_part()

# -- game tick --
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    head.draw()
    
    keys = pygame.key.get_pressed()

    head.tick(keys)


 # -- end game tick --

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
