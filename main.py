import pygame
import random
import os

# Pygame'i başlat
pygame.init()

# Ekran boyutları
screen_width, screen_height = 800, 600
WIDTH, HEIGHT = screen_width, screen_height

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("igdir")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Arkaplan resmi
bg = pygame.image.load("igdir.jpg")
original_image = pygame.transform.scale(bg, (screen_width, screen_height))
resized_image = pygame.transform.scale(bg, (screen_width, screen_height))

# Hoca resimlerini yükle
images_path = "resimler/"
files = os.listdir(images_path)
images = [pygame.image.load(images_path + x) for x in files]

# Kuş ayarları
class Bird:
    def __init__(self):
        self.image = pygame.transform.scale(random.choice(images), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.x_speed = random.choice([-5, 5])
        self.y_speed = random.choice([-5, 5])

    def move(self):
        # Kuşu hareket ettir
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Kenara çarpınca yön değiştir
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.x_speed = -self.x_speed
        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.y_speed = -self.y_speed

    def increase_speed(self, increment=1):
        # X ve Y hızlarını artır
        if self.x_speed > 0:
            self.x_speed += increment
        else:
            self.x_speed -= increment
        if self.y_speed > 0:
            self.y_speed += increment
        else:
            self.y_speed -= increment

# Kuşlar listesi
birds = [Bird()]

# Puan ve font ayarları
score = 0
click_count = 0
font = pygame.font.Font(None, 36)

# Ana oyun döngüsü
running = True
while running:
    screen.fill(WHITE)
    screen.blit(resized_image, (0, 0))

    # Kuşları ekranda göster ve hareket ettir
    for bird in birds:
        bird.move()
        screen.blit(bird.image, bird.rect)

    # Fare tıklaması kontrolü
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            resized_image = pygame.transform.scale(original_image, (screen_width, screen_height))
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1
            hit_bird = None
            for bird in birds:
                if bird.rect.collidepoint(event.pos):
                    hit_bird = bird
                    score += 1
                    break
            if hit_bird:
                birds.remove(hit_bird)  # Vurulan kuşu kaldır
                birds.append(Bird())  # Yeni bir kuş ekle
            else:
                score -= 10

    # Her 10 tıklamada yeni bir kuş ekle ve tüm kuşların hızını artır
    if click_count >= 10:
        birds.append(Bird())
        for bird in birds:
            bird.increase_speed(2)  # Tüm kuşların hızını artır
        click_count = 0

    # Skor gösterimi
    score_text = font.render(f"Puan: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
