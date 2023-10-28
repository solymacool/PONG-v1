import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_SIZE = 10
WHITE = (255, 255, 255)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle positions
paddle_a_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle_b_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_velocity_x = random.choice((1, -1)) * 5
ball_velocity_y = random.choice((1, -1)) * 5

# Score
score_a = 0
score_b = 0



# Font for displaying the score
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a_y -= 5
    if keys[pygame.K_s]:
        paddle_a_y += 5
    if keys[pygame.K_UP]:
        paddle_b_y -= 5
    if keys[pygame.K_DOWN]:
        paddle_b_y += 5

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_velocity_y = -ball_velocity_y

    # Ball out of bounds
    if ball_x <= 0:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_velocity_x = -ball_velocity_x
        score_b += 1
    elif ball_x >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_velocity_x = -ball_velocity_x
        score_a += 1

    # Ball collision with paddles
    if (
        paddle_a_y < ball_y < paddle_a_y + PADDLE_HEIGHT
        and ball_x < PADDLE_WIDTH
        or paddle_b_y < ball_y < paddle_b_y + PADDLE_HEIGHT
        and ball_x > WIDTH - PADDLE_WIDTH - BALL_SIZE
    ):
        ball_velocity_x = -ball_velocity_x

    # Fill the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(
        screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    )
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Display the score
    score_display = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 36, 10))















    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
