import pygame
from mario_bross.entidades.entidad import Entidad

class Enemigo(Entidad):
  def __init__(self, coordenadas, velocidad=20, color=(0, 255, 0)) -> None:
    super().__init__(coordenadas, velocidad, color)
    self.radio = 20

  def _render_(self):
    pygame.draw.circle(
      pygame.display.get_surface(),
      self.color,
      self.coordenadas,
      self.radio
    )