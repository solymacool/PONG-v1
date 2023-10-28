import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
GRAVITY = 0.25
BIRD_SPEED = 0
JUMP_AMOUNT = -6
PIPE_WIDTH = 50
PIPE_GAP = 200
PIPE_SPEED = 3
SCORE = 0

# Colors
BLUE = (135, 206, 250)  # Light Blue for background
RED = (255, 0, 0)  # Red for bird
GREEN = (0, 128, 0)  # Dark Green for pipes

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Bird properties
bird_x = 50
bird_y = HEIGHT // 2
bird_width = 20
bird_height = 20

# Pipes list to hold pipe positions
pipes = []

clock = pygame.time.Clock()

def draw():
    screen.fill(BLUE)  # Set background color

    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))  # Upper pipe
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT))  # Lower pipe

    pygame.draw.rect(screen, RED, (bird_x, bird_y, bird_width, bird_height))  # Set bird color

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {SCORE}', True, (255, 255, 255))  # White color for text
    screen.blit(text, (10, 10))

    pygame.display.update()

def check_collision(pipe):
    if (bird_x < pipe[0] + PIPE_WIDTH and bird_x + bird_width > pipe[0] and
            (bird_y < pipe[1] or bird_y + bird_height > pipe[1] + PIPE_GAP)):
        return True
    return False

def main():
    global BIRD_SPEED, bird_y, SCORE

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    BIRD_SPEED = JUMP_AMOUNT

        # Bird physics
        bird_y += BIRD_SPEED
        BIRD_SPEED += GRAVITY

        # Pipe movement
        for pipe in pipes:
            pipe[0] -= PIPE_SPEED

        # Remove off-screen pipes
        if pipes and pipes[0][0] < -PIPE_WIDTH:
            pipes.pop(0)

        # Generate new pipes
        if len(pipes) == 0 or (len(pipes) < 5 and pipes[-1][0] < WIDTH - 300):
            pipes.append([WIDTH, random.randint(100, HEIGHT - PIPE_GAP - 100)])

        # Check for collisions and scoring
        for pipe in pipes:
            if pipe[0] <= bird_x + bird_width <= pipe[0] + PIPE_WIDTH:
                if check_collision(pipe):
                    running = False
                if pipe[0] == bird_x:
                    SCORE += 1

        # Bird out of screen
        if bird_y > HEIGHT - bird_height:
            running = False

        draw()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

