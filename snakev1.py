import pygame
import time
import random

pygame.init()

# Window dimensions
window_width = 800
window_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (128, 128, 128)

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Snake properties
snake_block = 10
snake_speed = 5

# Clock for controlling speed
clock = pygame.time.Clock()

def draw_snake(block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_window, white, [segment[0], segment[1], block, block])

def food_position():
    return round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, \
           round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

def game_loop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x, food_y = food_position()

    while not game_over:

        while game_close:
            game_window.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            msg = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            game_window.blit(msg, [window_width / 6, window_height / 3])
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_window.fill(gray)

        pygame.draw.rect(game_window, green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x, food_y = food_position()
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
