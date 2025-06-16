import pygame

class Piso:
  def __init__(self, coordenadas, ancho, alto, color=(255, 255, 255)) -> None:
    self.coordenadas = coordenadas
    self.ancho = ancho
    self.alto = alto
    self.color = color

  def crear_rectangulo(self):
    return pygame.Rect(self.coordenadas[0], self.coordenadas[1], self.ancho, self.alto)

  def dibujar(self, screen):
    rect = self.crear_rectangulo()
    pygame.draw.rect(screen, self.color, rect)
  