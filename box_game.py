import sys, pygame
import random
pygame.init()

clock = pygame.time.Clock()
title_font = pygame.font.Font(None , 40)
score_font = pygame.font.Font(None , 30)
score_font_A = pygame.font.Font(None , 30)

size = width, height = 620, 640
speed = [0, 0]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
red = (255 , 0 , 0)
cell_size = 23
class Food():
    def __init__(self):
        self.position = pygame.Vector2(random.randint(0,23), random.randint(0,23))

        self.score = 0
        self.score_A = 0

    def game_over(self):
        gameover = title_font.render(str('GAME OVER Player Red Win'), True, (0, 255, 0))
        screen.blit(gameover, (70, 272))
    def game_over_B(self):
        gameover = title_font.render(str('GAME OVER Player Blue Win'), True, (0, 255, 255))
        screen.blit(gameover, (70, 272))


    def food_draw(self):

        food_surface = pygame.Rect((self.position.x * 23, self.position.y * 23, 23, 23 ))
        pygame.draw.rect(screen, red, food_surface , 0 , 15)

    def collition_food(self):

        self.position = pygame.Vector2(random.randint(0, cell_size - 1), random.randint(0, cell_size - 1))

        self.score = self.score + 1

    def collition2_food(self):

        self.position = pygame.Vector2(random.randint(0, cell_size - 1), random.randint(0, cell_size - 1))


        self.score_A = self.score_A + 1

class Ball():
    def __init__(self):
        self.position1 = pygame.Vector2(random.randint(0,23), random.randint(0,23))
        self.position2 = pygame.Vector2(random.randint(0, 23), random.randint(0, 23))
    def ball_1(self):
        ball_surface = pygame.Rect( self.position1.x*23 , self.position1.y*23 , 23 , 23)
        pygame.draw.rect(screen , (0 ,255 ,0) , ball_surface )


    def ball_2(self):


        ball1_surface = pygame.Rect(self.position2.x*23, self.position2.y*23  ,23 ,23)
        pygame.draw.rect(screen, (0 , 0 , 255), ball1_surface)




food = Food()
ball = Ball()
ball_UPDATE = pygame.USEREVENT
pygame.time.set_timer(ball_UPDATE , 50)
while True:
    if food.score >= 10:
        food.game_over()
    if food.score_A >= 10:
        food.game_over_B()
    if  ball.position1.x    == food.position.x and ball.position1.y == food.position.y:
        food.collition_food()
    if  ball.position2.x    == food.position.x and ball.position2.y == food.position.y:
        food.collition2_food()
    for event in pygame.event.get():
        if event.type == ball_UPDATE:
            pygame.display.update()


        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        ball.position1.y -= 1
    if keys[pygame.K_s]:
        ball.position1.y += 1
    if keys[pygame.K_a]:
        ball.position1.x -= 1
    if keys[pygame.K_d]:
        ball.position1.x += 1

    if keys[pygame.K_UP]:
        ball.position2.y -= 1
    if keys[pygame.K_DOWN]:
        ball.position2.y += 1
    if keys[pygame.K_LEFT]:
        ball.position2.x -= 1
    if keys[pygame.K_RIGHT]:
        ball.position2.x += 1

    screen.fill(black)

    score_surface = title_font.render(str(food.score), True, red)
    screen.blit(score_surface, (25, 570))

    score_surface_A = title_font.render(str(food.score_A), True, (0,0,255))
    screen.blit(score_surface_A, (570, 570))



    food.food_draw()
    ball.ball_1()
    ball.ball_2()

    clock.tick(60)
