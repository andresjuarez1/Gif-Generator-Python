import pygame
import sys
import random
# Inicializar Pygame
pygame.init()
# Configuración de la pantalla
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lluvia")
# Definir colores
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)
estrellas = []
# Crear listas de círculos con posiciones aleatorias
for _ in range(1000):
        x = random.randint(0, ancho)
        y = random.randint(0, alto)
        radio = 2    
        estrellas.append((x, y, radio, color_dibujo))
# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Limpiar la pantalla
    ventana.fill(color_pantalla)
    # Actualizar la posición de las estrellas siguiendo la ruta de las líneas
    for i, estrella in enumerate(estrellas):
        x, y, radio, color_dibujo = estrella
        # Ajustar la posición de los círculos
        y += 2#random.randint(1,10)  # Puedes ajustar la velocidad cambiando este valor
        # Si el círculo llega al final de la pantalla, reiniciar su posición
        if y > alto:
            y = random.randint(0, 0)
            x = random.randint(0, ancho)
        # Actualizar la posición del círculo en la lista
        estrellas[i] = (x, y, radio, color_dibujo)
        # Dibujar el círculo en la nueva posición
        pygame.draw.circle(ventana, color_dibujo, (int(x), int(y)), radio)
    # Actualizar la pantalla
    pygame.display.flip()
    # Controlar la velocidad de actualización
    clock.tick(30)