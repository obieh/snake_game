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

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Snake properties
snake_block = 10
snake_speed = 15

# Clock for controlling speed
clock = pygame.time.Clock()

# Fonts for text display
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def draw_snake(block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(game_window, white, [segment[0], segment[1], block, block])

def food_position():
    return round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0, \
           round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

def show_score(score, level):
    score_text = score_font.render("Score: " + str(score), True, white)
    level_text = score_font.render("Level: " + str(level), True, white)
    game_window.blit(score_text, [0, 0])
    game_window.blit(level_text, [0, 30])

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

    # Initialize score and level
    score = 0
    level = 1

    while not game_over:

        while game_close:
            game_window.fill(white)
            msg = font_style.render(f"You Lost! Score: {score}, Level: {level}. Press Q-Quit or C-Play Again", True, red)
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
        game_window.fill(black)

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
        show_score(score, level)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x, food_y = food_position()
            snake_length += 1
            score += 10

            # Increase level and speed for every 50 points
            if score % 50 == 0:
                level += 1
                snake_speed += 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
