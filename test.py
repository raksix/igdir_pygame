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

bg = pygame.image.load("igdir.jpg")
original_image = pygame.transform.scale(bg, (screen_width, screen_height))
resized_image = pygame.transform.scale(bg, (screen_width, screen_height))

hocalar_path = "hocalar/"

files = os.listdir(hocalar_path)


images = []

for x in files:
    images.append(pygame.image.load(hocalar_path + x))

# Kuş ayarları


bird_image = images[0]  # Kuş resmini ekleyin
bird_image = pygame.transform.scale(bird_image, (100, 100))
bird_rect = bird_image.get_rect()

# Kuş hızı ve başlangıç konumu
bird_speed = 5
bird_rect.x = random.randint(0, WIDTH - bird_rect.width)
bird_rect.y = random.randint(0, HEIGHT - bird_rect.height)

birds = []

birds.append(bird_rect)

# Puan ve font ayarları
score = 0
click_count = 0

font = pygame.font.Font(None, 36)


# Ana oyun döngüsü
running = True
while running:
    screen.fill(WHITE)

    screen.blit(resized_image, (0, 0))

    # Kuşu ekranda göster
    screen.blit(bird_image, bird_rect)

    # Kuşun hareketi
    bird_rect.x += bird_speed
    if bird_rect.x > WIDTH or bird_rect.x < 0:
        bird_speed = -bird_speed
        for bird in birds: 
            bird.y = random.randint(0, HEIGHT - bird_rect.height)
        print(WIDTH)

    # Fare tıklaması kontrolü
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode(
                (screen_width, screen_height), pygame.RESIZABLE
            )
            # Resmi yeni pencere boyutuna göre yeniden ölçekle
            resized_image = pygame.transform.scale(
                original_image, (screen_width, screen_height)
            )
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_count += 1
            if bird_rect.collidepoint(event.pos):
                score += 1
                bird_image = random.choice(images)  # Kuş resmini ekleyin
                bird_image = pygame.transform.scale(bird_image, (100, 100))
                
                for bird in birds:
                    bird = bird_image.get_rect()
                    bird.x = random.randint(0, WIDTH - bird_rect.width)
                    bird.y = random.randint(0, HEIGHT - bird_rect.height)
                  
            else:
                score -= 10

    # Skor gösterimi
    score_text = font.render(f"Puan: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
