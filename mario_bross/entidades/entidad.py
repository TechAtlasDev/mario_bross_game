import pygame

class Entidad:
  def __init__(self, x, y, width, height, velocidad=5, color=(255, 255, 255)) -> None:
    self.rect = pygame.Rect(x, y, width, height)
    self.velocidad = velocidad
    self.vel_x = 0
    self.vel_y = 0
    self.en_suelo = False

    self.fuerza_salto = -20
    self.gravedad = 0.8
    self.color = color
    self.esta_muerto = False

  def manejar_eventos(self, events, keys_pressed):
    """
    Maneja los eventos del teclado. Sobrescribir en las clases hijas.
    """
    pass

  def accionar(self):
    """
    Actualiza el estado de la entidad. Lógica de IA o física básica va aquí.
    """
    self.vel_y += self.gravedad
    # para que no caiga en picada, limitamos la cantidad maxima de caida
    if self.vel_y > 10:
      self.vel_y = 10


  def _render_(self, screen, camera_y=0):
    """
    Dibuja la entidad en pantalla. Debe ser implementado por las clases hijas.
    """
    raise NotImplementedError("Debe implementar el metodo _render_")

  def dibujar(self, screen, camera_y=0):
    self._render_(screen, camera_y)

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