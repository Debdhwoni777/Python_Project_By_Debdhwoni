import pygame
import random

# Initialize Pygame
pygame.init() 

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200
BIRD_X = 100
GRAVITY = 0.6
FLAP_STRENGTH = -10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill((255, 0, 0))

clock = pygame.time.Clock()

def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - height - PIPE_GAP)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= 5
    if pipes[0].x < -PIPE_WIDTH:
        pipes = pipes[2:]
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(bird, pipes):
    if bird.y > SCREEN_HEIGHT or bird.y < 0:
        return True
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True
    return False

def main():
    bird = pygame.Rect(BIRD_X, SCREEN_HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT)
    bird_movement = 0
    pipes = []
    pipe_timer = 0
    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = FLAP_STRENGTH

        bird_movement += GRAVITY
        bird.y += bird_movement

        if pipe_timer == 0:
            pipes.extend(create_pipe())
        pipe_timer = (pipe_timer + 1) % 90

        pipes = move_pipes(pipes)

        if pipes and pipes[0].x == BIRD_X:
            score += 1

        screen.fill(WHITE)
        screen.blit(bird_img, bird)
        draw_pipes(pipes)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        if check_collision(bird, pipes):
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
