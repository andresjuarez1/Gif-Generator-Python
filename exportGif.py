import pygame
import sys
import random
import os
import imageio
ruta_dibujos = "C:/Users/Pc/Documents/multimedia_act2/"
ruta_estrella = os.path.join(ruta_dibujos, "bala.png")
ruta_fondo = os.path.join(ruta_dibujos, "guerra.jpg")

pygame.init()
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Lluvia")
color_pantalla = (255, 255, 255)

fondo = pygame.image.load(ruta_fondo)
fondo = pygame.transform.scale(fondo, (ancho, alto))

estrella = pygame.image.load(ruta_estrella)
estrella = pygame.transform.scale(estrella, (20, 20))
estrella_rect = estrella.get_rect()
estrellas = []
for _ in range(100):
    estrella_info = {
        'x': random.randint(0, ancho - estrella_rect.width),
        'y': random.randint(0, alto - estrella_rect.height),  
        'velocidad': 5
    }
    estrellas.append(estrella_info)
# Configuración de salida de la animación
output_filename = "lluvia_de_estrellas2.gif"
grabar_imagen = imageio.get_writer(output_filename, fps=30)
reloj = pygame.time.Clock()
tiempo = 0  # Tiempo transcurrido

while tiempo < 20:  # Solo exporta los primeros 3 segundos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ventana.blit(fondo, (0, 0))  # Dibujar el fondo

    # ventana.fill(color_pantalla)

    for estrella_info in estrellas:
        estrella_info['x'] += estrella_info['velocidad']  # Modificar la posición en x
        if estrella_info['x'] > ancho:
            estrella_info['x'] = 0
            estrella_info['y'] = random.randint(0, alto - estrella_rect.height)
            estrella_info['velocidad'] = 5
        ventana.blit(estrella, (estrella_info['x'], estrella_info['y']))
    pygame.display.flip()
    # Agregar el fotograma actual al escritor de imageio
    grabar_imagen.append_data(pygame.surfarray.array3d(ventana).swapaxes(0, 1))
    tiempo += 1 / 30  # Incrementar el tiempo transcurrido
    reloj.tick(30)
# Cerrar el escritor de imageio
grabar_imagen.close()

pygame.quit()
sys.exit()