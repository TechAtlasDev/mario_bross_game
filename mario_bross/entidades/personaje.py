from mario_bross.entidades.entidad import Entidad
import pygame

class Personaje(Entidad):
  def __init__(self, x, y, width, height, velocidad=5, color=(255, 0, 0)) -> None:
    super().__init__(x, y, width, height, velocidad, color)

  def manejar_eventos(self, events, keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
      self.mover_izquierda()
    elif keys_pressed[pygame.K_RIGHT]:
      self.mover_derecha()
    else:
      self.vel_x = 0

    for event in events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
          self.saltar()

  def _render_(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)