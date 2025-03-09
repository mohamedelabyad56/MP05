import pygame
import random
import sys
import json
from os import path

# ========================
# Configuración inicial
# ========================
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Extensible - Joc Millorat")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 30)

# ========================
# Carga de recursos
# ========================
def load_data():
    global high_score
    if path.exists("highscore.json"):
        with open("highscore.json", 'r') as f:
            high_score = json.load(f)
    else:
        high_score = 0

def save_data():
    with open("highscore.json", 'w') as f:
        json.dump(high_score, f)

# Sonidos y música
pygame.mixer.init()
background_music = pygame.mixer.Sound("background_music.mp3")
collision_sound = pygame.mixer.Sound("collision.wav")
point_sound = pygame.mixer.Sound("point.wav")
move_sound = pygame.mixer.Sound("move.wav")
powerup_sound = pygame.mixer.Sound("powerup.wav")
shoot_sound = pygame.mixer.Sound("laser.wav")

# ========================
# Variables globales
# ========================
load_data()
score = 0
difficulty_level = 1
lives = 3
last_difficulty_update = pygame.time.get_ticks()
spawn_interval = 1500
player_invulnerable = False
invulnerable_timer = 0

# Eventos personalizados
ADD_OBSTACLE = pygame.USEREVENT + 1
ADD_POWERUP = pygame.USEREVENT + 2
ADD_HOMING = pygame.USEREVENT + 3

# ========================
# Clases del juego
# ========================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 7
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        moved = False
        
        # Movimiento
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            moved = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            moved = True
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moved = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moved = True
            
        # Disparo
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        # Efecto de movimiento
        if moved:
            move_sound.play()
        
        # Limites de pantalla
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = random.randint(20, 80)
        height = random.randint(20, 80)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - height)
        self.speed = random.randint(5 + difficulty_level, 10 + difficulty_level)

    def update(self):
        global score
        self.rect.x -= self.speed
        if self.rect.right < 0:
            score += 1
            point_sound.play()
            self.kill()

class HomingObstacle(Obstacle):
    def __init__(self):
        super().__init__()
        self.image.fill(ORANGE)
        self.speed = 4 + difficulty_level

    def update(self):
        self.rect.x -= self.speed
        # Perseguir al jugador verticalmente
        if self.rect.centery < player.rect.centery:
            self.rect.y += 1
        else:
            self.rect.y -= 1
        if self.rect.right < 0:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(10, 100)
        self.rect.y = random.randint(0, HEIGHT - 30)
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

# ========================
# Funciones del juego
# ========================
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def show_menu():
    menu = True
    while menu:
        screen.fill(BLACK)
        draw_text("Joc Millorat", 64, WHITE, WIDTH//2 - 180, HEIGHT//4)
        draw_text("Prem qualsevol tecla per començar", 22, WHITE, WIDTH//2 - 150, HEIGHT//2)
        draw_text(f"Rècord: {high_score}", 22, WHITE, 10, 10)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menu = False

def game_over():
    global high_score
    if score > high_score:
        high_score = score
        save_data()
    
    screen.fill(BLACK)
    draw_text("GAME OVER", 64, RED, WIDTH//2 - 150, HEIGHT//3)
    draw_text(f"Puntuació: {score}", 36, WHITE, WIDTH//2 - 80, HEIGHT//2)
    draw_text("Prem qualsevol tecla per reiniciar", 24, WHITE, WIDTH//2 - 180, HEIGHT*2//3)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def new_game():
    global score, difficulty_level, lives, all_sprites, obstacles, powerups, bullets, player
    score = 0
    difficulty_level = 1
    lives = 3
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    pygame.time.set_timer(ADD_OBSTACLE, 1500)
    pygame.time.set_timer(ADD_POWERUP, 8000)
    pygame.time.set_timer(ADD_HOMING, 10000)

# ========================
# Bucle principal
# ========================
background_music.play(-1)
while True:
    show_menu()
    new_game()
    running = True
    while running:
        clock.tick(FPS)
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_data()
                pygame.quit()
                sys.exit()
            elif event.type == ADD_OBSTACLE:
                obstacle = Obstacle()
                all_sprites.add(obstacle)
                obstacles.add(obstacle)
            elif event.type == ADD_POWERUP:
                powerup = PowerUp()
                all_sprites.add(powerup)
                powerups.add(powerup)
            elif event.type == ADD_HOMING:
                homing = HomingObstacle()
                all_sprites.add(homing)
                obstacles.add(homing)
        
        # Actualizar
        all_sprites.update()
        
        # Colisiones balas-obstáculos
        hits = pygame.sprite.groupcollide(obstacles, bullets, True, True)
        for hit in hits:
            score += 2
        
        # Colisiones jugador-obstáculos
        if pygame.sprite.spritecollide(player, obstacles, True) and not player_invulnerable:
            collision_sound.play()
            lives -= 1
            if lives <= 0:
                running = False
            else:
                player_invulnerable = True
                invulnerable_timer = pygame.time.get_ticks()
                player.rect.center = (100, HEIGHT//2)
        
        # Temporizador invulnerabilidad
        if player_invulnerable:
            now = pygame.time.get_ticks()
            if now - invulnerable_timer > 2000:
                player_invulnerable = False
        
        # Colisiones powerups
        if pygame.sprite.spritecollide(player, powerups, True):
            powerup_sound.play()
            lives += 1
        
        # Dificultad progresiva
        now = pygame.time.get_ticks()
        if now - last_difficulty_update > 15000:
            difficulty_level += 1
            last_difficulty_update = now
            spawn_interval = max(500, 1500 - difficulty_level * 100)
            pygame.time.set_timer(ADD_OBSTACLE, spawn_interval)
        
        # Renderizado
        screen.fill(WHITE)
        all_sprites.draw(screen)
        
        # Interfaz de usuario
        draw_text(f"Puntuació: {score}", 24, BLACK, 10, 10)
        draw_text(f"Vides: {lives}", 24, BLACK, 10, 40)
        draw_text(f"Nivell: {difficulty_level}", 24, BLACK, 10, 70)
        
        # Efecto de invulnerabilidad
        if player_invulnerable:
            pygame.draw.rect(screen, YELLOW, player.rect, 4)
        
        pygame.display.flip()
    
    game_over()