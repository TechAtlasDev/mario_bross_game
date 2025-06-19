from mario_bross.entidades.entidad import Entidad
import pygame

class Personaje(Entidad):
  def __init__(self, x, y, width, height, velocidad=5, color=(255, 0, 0)) -> None:
    super().__init__(x, y, width, height, velocidad, color)
    self.start_x = x
    self.start_y = y

  def morir(self):
    self.rect.x = self.start_x
    self.rect.y = self.start_y
    self.vel_x = 0
    self.vel_y = 0

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

  def _render_(self, screen, camera_y=0):
    displaced_rect = self.rect.copy()
    displaced_rect.y -= camera_y
    pygame.draw.rect(screen, self.color, displaced_rect)