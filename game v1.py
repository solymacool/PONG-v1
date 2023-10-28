import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
GRAVITY = 0.5
BOUNCE_FACTOR = -0.7
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Initialize ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 0

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Apply gravity
    ball_speed_y += GRAVITY

    # Check for collisions with the screen boundaries
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x *= -1

    if ball_y - BALL_RADIUS < 0:
        ball_speed_y *= BOUNCE_FACTOR
        ball_y = BALL_RADIUS

    if ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y *= BOUNCE_FACTOR
        ball_y = HEIGHT - BALL_RADIUS

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
