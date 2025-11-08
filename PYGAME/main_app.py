import pygame

# Init
pygame.init()

# Variable running game
isRun = True

# Membuat display surface object
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_panjang, window_lebar))
pygame.display.set_caption("Gerak Kotak")

# Object game
x = 350
y = 350
lebar = 20
panjang = 20
speed = 10

# FPS
clock = pygame.time.Clock()

while isRun:
    pygame.time.delay(10)
    # User input event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # Ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # Ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    # Ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
        
    # Ke down
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
        
    # Ke up
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    

    # Update tampilan
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))
    pygame.display.update()

    # Batasi ke 60 FPS
    clock.tick(60)

pygame.quit()
