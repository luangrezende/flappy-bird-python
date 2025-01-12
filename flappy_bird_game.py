import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()

BG_IMG = pygame.image.load("assets/background-day.png")
BIRD_IMG = pygame.image.load("assets/bluebird-downflap.png")
PIPE_IMG = pygame.image.load("assets/pipe-green.png")
GAME_OVER_IMG = pygame.image.load("assets/gameover.png")

BG_IMG = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (50, 35))
PIPE_IMG = pygame.transform.scale(PIPE_IMG, (80, 500))
GAME_OVER_IMG = pygame.transform.scale(GAME_OVER_IMG, (200, 100))

PIPE_FLIPPED_IMG = pygame.transform.flip(PIPE_IMG, False, True)

class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.gravity = 0.5
        self.lift = -10
        self.velocity = 0

    def draw(self):
        SCREEN.blit(BIRD_IMG, (self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

        if self.y <= 0:
            self.y = 0
            self.velocity = 0

        if self.y >= SCREEN_HEIGHT - BIRD_IMG.get_height():
            self.y = SCREEN_HEIGHT - BIRD_IMG.get_height()
            self.velocity = 0

    def flap(self):
        self.velocity = self.lift

class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap = 150
        self.top = random.randint(100, SCREEN_HEIGHT - 200)
        self.bottom = self.top + self.gap

    def draw(self):
        SCREEN.blit(PIPE_FLIPPED_IMG, (self.x, self.top - PIPE_IMG.get_height()))
        SCREEN.blit(PIPE_IMG, (self.x, self.bottom))

    def update(self):
        self.x -= 5

    def off_screen(self):
        return self.x < -PIPE_IMG.get_width()

def reset_game():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH)]
    return bird, pipes, 0

def main():
    bird, pipes, score = reset_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()

        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))
                score += 1

        for pipe in pipes:
            if (bird.x + BIRD_IMG.get_width() > pipe.x and
                bird.x < pipe.x + PIPE_IMG.get_width() and
                (bird.y < pipe.top or bird.y + BIRD_IMG.get_height() > pipe.bottom)):
                SCREEN.blit(BG_IMG, (0, 0))
                SCREEN.blit(GAME_OVER_IMG, ((SCREEN_WIDTH - GAME_OVER_IMG.get_width()) // 2, (SCREEN_HEIGHT - GAME_OVER_IMG.get_height()) // 2))
                pygame.display.flip()
                pygame.time.delay(1000)
                bird, pipes, score = reset_game()

        SCREEN.blit(BG_IMG, (0, 0))
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
