import pygame
from mario_bross.entidades.entidad import Entidad

class Enemigo(Entidad):
  def __init__(self, x, y, width, height, velocidad=2, color=(150, 75, 0)) -> None:
    super().__init__(x, y, width, height, velocidad, color)

  def update(self):
    super().update()
    self.mover_derecha()

  def _render_(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)