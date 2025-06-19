import pygame
from mario_bross.entidades.entidad import Entidad

class Enemigo(Entidad):
  def __init__(self, x, y, width, height, velocidad=2, color=(150, 75, 0)) -> None:
    super().__init__(x, y, width, height, velocidad, color)

  def accionar(self):
    super().accionar()
    self.mover_derecha()

  def morir(self):
    self.esta_muerto = True

  def _render_(self, screen, camera_y=0):
    displaced_rect = self.rect.copy()
    displaced_rect.y -= camera_y
    pygame.draw.rect(screen, self.color, displaced_rect)