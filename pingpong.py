import pygame
from pygame.locals import *

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 15
BALL_SIZE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1인용 핑퐁 게임")
    clock = pygame.time.Clock()

    paddle_pos = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_pos = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_vel = [3, 3]

    return screen, clock, paddle_pos, ball_pos, ball_vel

def handle_paddle_movement(paddle_pos):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle_pos.move_ip(-5, 0)
    if keys[K_RIGHT]:
        paddle_pos.move_ip(5, 0)
    if paddle_pos.left < 0:
        paddle_pos.left = 0
    if paddle_pos.right > SCREEN_WIDTH:
        paddle_pos.right = SCREEN_WIDTH

def handle_ball_movement(ball_pos, ball_vel, paddle_pos):
    ball_pos.move_ip(ball_vel[0], ball_vel[1])
    if ball_pos.left < 0 or ball_pos.right > SCREEN_WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_pos.top < 0:
        ball_vel[1] = -ball_vel[1]
    if ball_pos.colliderect(paddle_pos):
        ball_vel[1] = -ball_vel[1]
    if ball_pos.bottom >= SCREEN_HEIGHT:
        return True
    return False

def draw_screen(screen, paddle_pos, ball_pos):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_pos)
    pygame.draw.ellipse(screen, WHITE, ball_pos)
    pygame.display.flip()

def game_over_screen(screen):
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

def main():
    screen, clock, paddle_pos, ball_pos, ball_vel = initialize_game()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        handle_paddle_movement(paddle_pos)
        game_over = handle_ball_movement(ball_pos, ball_vel, paddle_pos)
        draw_screen(screen, paddle_pos, ball_pos)
        clock.tick(60)

    game_over_screen(screen)
    pygame.quit()

if __name__ == "__main__":
    main()
