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
    text = font.render(f'Score: {SCORE}', True, (255, 255, 255))  # Update score display
    screen.blit(text, (10, 10))

    pygame.display.update()

def check_collision(pipe):
    if (bird_x < pipe[0] + PIPE_WIDTH and bird_x + bird_width > pipe[0] and
            (bird_y < pipe[1] or bird_y + bird_height > pipe[1] + PIPE_GAP)):
        return True
    return False

def game_over_screen():
    screen.fill((0, 0, 0))  # Black background for game over screen

    font = pygame.font.Font(None, 36)
    text = font.render('Game Over', True, (255, 255, 255))  # Display game over text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(text, text_rect)

    final_score_text = font.render(f'Your Final Score: {SCORE}', True, (255, 255, 255))  # Display final score
    final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
    screen.blit(final_score_text, final_score_rect)

    pygame.display.update()

def main():
    global BIRD_SPEED, bird_y, SCORE

    running = True
    passed_pipe = False  # Flag to check if bird has passed a pipe
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over and event.type == pygame.KEYDOWN:
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
            passed_pipe = False  # Reset the flag when the pipe goes off the screen

        # Generate new pipes
        if len(pipes) == 0 or (len(pipes) < 5 and pipes[-1][0] < WIDTH - 300):
            pipes.append([WIDTH, random.randint(100, HEIGHT - PIPE_GAP - 100)])

        # Check for passing through pipes and scoring
        for pipe in pipes:
            if not passed_pipe and pipe[0] < bird_x:
                passed_pipe = True
                SCORE += 1

            if check_collision(pipe):
                game_over = True

        # Bird out of screen
        if bird_y > HEIGHT - bird_height:
            game_over = True

        draw()
        clock.tick(60)

        if game_over:
            break

    while game_over:
        game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


