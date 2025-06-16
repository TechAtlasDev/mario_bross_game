from mario_bross.entidades.entidad import Entidad
import pygame

class Personaje(Entidad):
  def __init__(self, coordenadas, velocidad=20, color=(255, 0, 0)) -> None:
    super().__init__(coordenadas, velocidad, color)
    self.radio = 30

  def handle_events(self, events):
    if events[pygame.K_RIGHT]:
      self.mover_derecha()
    if events[pygame.K_LEFT]:
      self.mover_izquierda()
    if events[pygame.K_UP]:
      self.mover_arriba()
    if events[pygame.K_DOWN]:
      self.mover_abajo()
    if events[pygame.K_SPACE]:
      self.saltar()

  def _render_(self):
    pygame.draw.circle(
      pygame.display.get_surface(),
      self.color,
      self.coordenadas,
      self.radio
    )