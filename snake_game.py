import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)


SNAKE_BLOCK = 20            
SNAKE_SPEED = 8             

font = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()

def score_display(score):
    value = score_font.render("Score: " + str(score), True, YELLOW)
    screen.blit(value, [10, 10])

def draw_snake(snake_list):
    
    for i, (x, y) in enumerate(snake_list):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, [x, y, SNAKE_BLOCK, SNAKE_BLOCK])

def draw_food(food_x, food_y):

    cx = food_x + SNAKE_BLOCK // 2
    cy = food_y + SNAKE_BLOCK // 2
    pygame.draw.circle(screen, RED, (cx, cy), SNAKE_BLOCK // 2)

def message(msg, color, y_shift=0):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3 + y_shift])

def new_food(snake_list):
   
    while True:
        fx = random.randrange(0, WIDTH, SNAKE_BLOCK)
        fy = random.randrange(0, HEIGHT, SNAKE_BLOCK)
        if (fx, fy) not in snake_list:
            return fx, fy

def snap_to_grid(v):
    
    return (v // SNAKE_BLOCK) * SNAKE_BLOCK

def game_loop():
    game_over = False
    game_close = False


    x = snap_to_grid(WIDTH // 2)
    y = snap_to_grid(HEIGHT // 2)
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x, food_y = new_food(snake_list)

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            message("💀 You Lost!", RED)
            message("Press C to Play Again or Q to Quit", YELLOW, 40)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change, y_change = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change, y_change = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change, y_change = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change, y_change = 0, SNAKE_BLOCK

    
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        
        x += x_change
        y += y_change

        screen.fill(BLUE)
        draw_food(food_x, food_y)

      
        snake_head = (x, y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

  
        if snake_head in snake_list[:-1]:
            game_close = True

        draw_snake(snake_list)
        score_display(length_of_snake - 1)
        pygame.display.update()

       
        if x == food_x and y == food_y:
            length_of_snake += 1
            food_x, food_y = new_food(snake_list)

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    raise SystemExit

if __name__ == "__main__":
    game_loop()
