import pygame
from pygame.locals import *

# 게임 화면 크기
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 480

# 패들 크기
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 15

# 공 크기
BALL_SIZE = 10

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("1인용 핑퐁 게임")
    clock = pygame.time.Clock()

    # 패들 초기 위치
    player_paddle_pos = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

    # 공 초기 위치 및 속도
    ball_pos = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_vel = [3, 3]

    ## 게임 상태 변수
    game_over = False
    score = 0
    play_count = 3


#    while True:
    while not game_over: ##
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        if play_count > 0: ##
            # 키 입력 처리
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                player_paddle_pos.move_ip(-5, 0)
            if keys[K_RIGHT]:
                player_paddle_pos.move_ip(5, 0)

            # 패들 이동 범위 제한
            if player_paddle_pos.left < 0:
                player_paddle_pos.left = 0
            if player_paddle_pos.right > SCREEN_WIDTH:
                player_paddle_pos.right = SCREEN_WIDTH

            # 공 이동
            ball_pos.move_ip(ball_vel[0], ball_vel[1])

            # 벽 충돌 체크
            if ball_pos.left < 0 or ball_pos.right > SCREEN_WIDTH:
                ball_vel[0] = -ball_vel[0]
            #if ball_pos.top < 0 or ball_pos.bottom > SCREEN_HEIGHT:
            if ball_pos.top < 0 :    
                ball_vel[1] = -ball_vel[1]

            # 패들과 충돌 체크
            if ball_pos.colliderect(player_paddle_pos):
                ball_vel[1] = -ball_vel[1]
                score += 10 ##

            ## 게임 종료 조건 체크
            if ball_pos.bottom >= SCREEN_HEIGHT:
                play_count -= 1
                if play_count > 0:
                    ball_pos = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
                    ball_vel = [3, 3]
                    pygame.time.delay(1000)  # 1초 딜레이
                else:
                    game_over = True   

            # 화면 그리기
            screen.fill(BLACK)
            pygame.draw.rect(screen, WHITE, player_paddle_pos)
            pygame.draw.ellipse(screen, WHITE, ball_pos)
            #pygame.draw.aaline(screen, WHITE, (0, SCREEN_HEIGHT // 2), (SCREEN_WIDTH, SCREEN_HEIGHT // 2))

            ## 점수 표시
            font = pygame.font.Font(None, 36)
            score_text = font.render("Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))

            ## 플레이 기회 표시
            play_count_text = font.render("Play Count: " + str(play_count), True, WHITE)
            screen.blit(play_count_text, (10, 50))

            pygame.display.flip()
            clock.tick(60)

    ## 게임 종료 메시지 출력
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # 2초 딜레이

    pygame.quit()

if __name__ == "__main__":
    main()