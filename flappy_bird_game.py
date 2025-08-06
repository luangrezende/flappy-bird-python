import pygame
import sys
import random
import json
import os

def get_base_path():
    if getattr(sys, 'frozen', False):
        return getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        return os.path.dirname(os.path.abspath(__file__))

def load_config():
    config_path = os.path.join(get_base_path(), "config.json")
    with open(config_path, 'r') as f:
        return json.load(f)

def load_image(filename):
    image_path = os.path.join(get_base_path(), filename)
    return pygame.image.load(image_path)

def calculate_dynamic_difficulty(score):
    config = load_config()
    progression = config["dynamic_difficulty"]["progression_info"]
    
    gravity = progression["bird_gravity"]
    jump_force = progression["bird_jump_force"]
    pipe_gap = progression["pipe_gap_size"]
    
    difficulty_multiplier = score // progression["level_up_every"]
    
    pipe_speed = min(progression["starting_pipe_speed"] + (difficulty_multiplier * 0.3), progression["max_pipe_speed"])
    pipe_frequency = max(progression["starting_pipe_frequency"] - (difficulty_multiplier * 8), progression["min_pipe_frequency"])
    
    return {
        'gravity': gravity,
        'jump_force': jump_force,
        'pipe_gap_y': pipe_gap,
        'pipe_speed': pipe_speed,
        'pipe_frequency': pipe_frequency
    }

config = load_config()
display_settings = config["display_settings"]

pygame.init()
SCREEN_WIDTH = display_settings["screen_width"]
SCREEN_HEIGHT = display_settings["screen_height"]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
FPS = display_settings["fps"]
clock = pygame.time.Clock()

BG_IMG = load_image("assets/background-day.png")
BIRD_IMG = load_image("assets/bluebird-downflap.png")
PIPE_IMG = load_image("assets/pipe-green.png")
GAME_OVER_IMG = load_image("assets/gameover.png")

BG_IMG = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (50, 35))
PIPE_IMG = pygame.transform.scale(PIPE_IMG, (80, 500))
GAME_OVER_IMG = pygame.transform.scale(GAME_OVER_IMG, (200, 100))

PIPE_FLIPPED_IMG = pygame.transform.flip(PIPE_IMG, False, True)

class Bird:
    def __init__(self):
        config = load_config()
        progression = config["dynamic_difficulty"]["progression_info"]
        
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.gravity = progression["bird_gravity"]
        self.lift = progression["bird_jump_force"]
        self.velocity = 0

    def draw(self):
        screen.blit(BIRD_IMG, (self.x, self.y))

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
    def __init__(self, x, difficulty_params):
        self.x = x
        self.gap = difficulty_params['pipe_gap_y']
        self.speed = difficulty_params['pipe_speed']
        self.top = random.randint(100, SCREEN_HEIGHT - 200)
        self.bottom = self.top + self.gap

    def draw(self):
        screen.blit(PIPE_FLIPPED_IMG, (self.x, self.top - PIPE_IMG.get_height()))
        screen.blit(PIPE_IMG, (self.x, self.bottom))

    def update(self):
        self.x -= self.speed

    def off_screen(self):
        return self.x < -PIPE_IMG.get_width()

def reset_game():
    bird = Bird()
    initial_difficulty = calculate_dynamic_difficulty(0)
    pipes = [Pipe(SCREEN_WIDTH, initial_difficulty)]
    return bird, pipes, 0

def main():
    bird, pipes, score = reset_game()
    config = load_config()
    level_up_every = config["dynamic_difficulty"]["progression_info"]["level_up_every"]
    
    font_large = pygame.font.Font(None, 36)
    font_medium = pygame.font.Font(None, 24)
    font_small = pygame.font.Font(None, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bird.flap()

        current_difficulty = calculate_dynamic_difficulty(score)

        bird.update()

        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH + current_difficulty['pipe_frequency'], current_difficulty))
                score += 1

        for pipe in pipes:
            if (bird.x + BIRD_IMG.get_width() > pipe.x and
                bird.x < pipe.x + PIPE_IMG.get_width() and
                (bird.y < pipe.top or bird.y + BIRD_IMG.get_height() > pipe.bottom)):
                screen.blit(BG_IMG, (0, 0))
                screen.blit(GAME_OVER_IMG, ((SCREEN_WIDTH - GAME_OVER_IMG.get_width()) // 2, (SCREEN_HEIGHT - GAME_OVER_IMG.get_height()) // 2))
                pygame.display.flip()
                pygame.time.delay(1000)
                bird, pipes, score = reset_game()

        screen.blit(BG_IMG, (0, 0))
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        score_text = font_large.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        difficulty_level = (score // level_up_every) + 1
        diff_text = font_medium.render(f"Level: {difficulty_level}", True, WHITE)
        screen.blit(diff_text, (10, 50))
        
        speed_text = font_small.render(f"Speed: {current_difficulty['pipe_speed']:.1f}", True, WHITE)
        screen.blit(speed_text, (10, 75))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
