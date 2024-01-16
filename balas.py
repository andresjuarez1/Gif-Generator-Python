import pygame
import sys
import random
import os
# Obtener la ruta completa del directorio de dibujos
ruta_dibujos = "/home/horacio/Documents/MDD_2024/Dibujos"
# Obtener la ruta completa del archivo de imagen
ruta_estrella = os.path.join(ruta_dibujos, "estrella.png")
# Inicializar Pygame
pygame.init()
# Configuración de la pantalla
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lluvia")
# Definir colores
color_pantalla = (255, 255, 255)
# Cargar imagen de estrellas y escalar
estrella = pygame.image.load(ruta_estrella)
estrella = pygame.transform.scale(estrella, (20, 20))  # Ajusta el tamaño según tus necesidades
# Obtener el rectángulo de la imagen
estrella_rect = estrella.get_rect()
# Lista para almacenar las posiciones y velocidades iniciales de las estrellas
estrellas = []
for _ in range(100):
    estrella_info = {
        'x': random.randint(0, ancho - estrella_rect.width),
        'y': random.randint(0, alto - estrella_rect.height),
        'velocidad': 10
    }
    estrellas.append(estrella_info)
# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Limpiar la pantalla
    ventana.fill(color_pantalla)
    # Actualizar la posición de las estrellas
    for estrella_info in estrellas:
        estrella_info['y'] += estrella_info['velocidad']
        # Si la estrella sale de la pantalla, reiniciar su posición
        if estrella_info['y'] > alto:
            estrella_info['y'] = 0
            estrella_info['x'] = random.randint(0, ancho - estrella_rect.width)
            estrella_info['velocidad'] = 10
        ventana.blit(estrella, (estrella_info['x'], estrella_info['y']))
    # Actualizar la pantalla
    pygame.display.flip()
    # Controlar la velocidad de actualización
    clock.tick(30)