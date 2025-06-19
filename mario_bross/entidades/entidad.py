import pygame

class Entidad:
  def __init__(self, x, y, width, height, velocidad=5, color=(255, 255, 255)) -> None:
    self.rect = pygame.Rect(x, y, width, height)
    self.velocidad = velocidad
    self.vel_x = 0
    self.vel_y = 0
    self.en_suelo = False

    self.fuerza_salto = -15
    self.gravedad = 1
    self.color = color

  def manejar_eventos(self, events, keys_pressed):
    pass

  def accionar(self):
    self.vel_y += self.gravedad
    # para que no caiga en picada, limitamos la cantidad maxima de caida
    if self.vel_y > 10:
      self.vel_y = 10


  def _render_(self, screen):
    pass

  def dibujar(self, screen):
    self._render_(screen)

  def mover_derecha(self):
    self.vel_x = self.velocidad
  
  def mover_izquierda(self):
    self.vel_x = -self.velocidad

  def saltar(self):
    if self.en_suelo:
        self.vel_y = self.fuerza_salto
        self.en_suelo = False

  def cambiar_direccion(self):
      self.velocidad *= -1