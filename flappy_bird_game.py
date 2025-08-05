import pygame
import sys
import random
import json
import os

def load_config():
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    config_path = os.path.join(base_path, "config.json")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
        print("Configuration loaded from config.json")
        return config

def load_image(filename):
    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(base_path, filename)
    return pygame.image.load(image_path)

def show_preset_menu_gui(screen, config):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (100, 255, 100)
    BLUE = (100, 150, 255)
    RED = (255, 100, 100)
    
    options = [
        {"name": "EASY", "color": GREEN, "key": "1"},
        {"name": "NORMAL", "color": BLUE, "key": "2"},
        {"name": "HARD", "color": RED, "key": "3"}
    ]
    
    selected = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    return options[selected]["key"]
                elif event.key == pygame.K_1:
                    return "1"
                elif event.key == pygame.K_2:
                    return "2"
                elif event.key == pygame.K_3:
                    return "3"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        screen.fill(BLACK)
        
        title_text = font.render("FLAPPY BIRD", True, WHITE)
        title_rect = title_text.get_rect(center=(screen.get_width()//2, 120))
        screen.blit(title_text, title_rect)
        
        start_y = 200
        for i, option in enumerate(options):
            y_pos = start_y + i * 80
            
            if i == selected:
                pygame.draw.rect(screen, option["color"], (100, y_pos - 10, 200, 60), 3)
            
            option_text = font.render(option['name'], True, option["color"])
            option_rect = option_text.get_rect(center=(screen.get_width()//2, y_pos + 15))
            screen.blit(option_text, option_rect)
        
        inst_text = pygame.font.Font(None, 24).render("↑↓ to select, ENTER to play", True, WHITE)
        inst_rect = inst_text.get_rect(center=(screen.get_width()//2, 450))
        screen.blit(inst_text, inst_rect)
        
        pygame.display.flip()
        clock.tick(60)

def apply_preset(preset_choice, config):
    if preset_choice == '1':
        return config['difficulty_presets']['easy']
    elif preset_choice == '2':
        return config['difficulty_presets']['normal']
    else:
        return config['difficulty_presets']['hard']

config = load_config()
display_settings = config["display_settings"]

pygame.init()
SCREEN_WIDTH = display_settings["screen_width"]
SCREEN_HEIGHT = display_settings["screen_height"]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Select Difficulty")

preset_choice = show_preset_menu_gui(screen, config)
game_settings = apply_preset(preset_choice, config)

config["game_settings"] = game_settings

pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
FPS = display_settings["fps"]
clock = pygame.time.Clock()

GRAVITY = game_settings["gravity"]
JUMP_FORCE = game_settings["jump_force"]
PIPE_GAP_Y = game_settings["pipe_gap_y"]
PIPE_GAP_X = game_settings["pipe_gap_x"]
PIPE_SPEED = game_settings["pipe_speed"]

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
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.gravity = GRAVITY
        self.lift = JUMP_FORCE
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
    def __init__(self, x):
        self.x = x
        self.gap = PIPE_GAP_Y
        self.top = random.randint(100, SCREEN_HEIGHT - 200)
        self.bottom = self.top + self.gap

    def draw(self):
        screen.blit(PIPE_FLIPPED_IMG, (self.x, self.top - PIPE_IMG.get_height()))
        screen.blit(PIPE_IMG, (self.x, self.bottom))

    def update(self):
        self.x -= PIPE_SPEED

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
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        bird.update()

        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH + PIPE_GAP_X))
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

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
