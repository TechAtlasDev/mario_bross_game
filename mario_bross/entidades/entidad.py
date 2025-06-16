import pygame

class Entidad:
  def __init__(self, x, y, width, height, velocidad=5, color=(255, 255, 255)) -> None:
    # Atributos de posición y tamaño
    self.rect = pygame.Rect(x, y, width, height)

    # Atributos de movimiento
    self.velocidad = velocidad
    self.vel_x = 0
    self.vel_y = 0
    self.en_suelo = False

    # Atributos de física
    self.fuerza_salto = -15
    self.gravedad = 0.8

    # Atributos visuales
    self.color = color

  def manejar_eventos(self, events, keys_pressed):
    """
    Maneja los eventos del teclado. Sobrescribir en las clases hijas.
    """
    pass

  def accionar(self):
    """
    Actualiza el estado de la entidad. Lógica de IA o física básica va aquí.
    """
    # Aplicamos la gravedad por defecto
    self.vel_y += self.gravedad
    if self.vel_y > 10: # Velocidad terminal para no acelerar infinitamente
        self.vel_y = 10
  
  def _render_(self, screen):
    """
    Dibuja la entidad en pantalla. Debe ser implementado por las clases hijas.
    """
    raise NotImplementedError("Debe implementar el metodo _render_")

  def draw(self, screen):
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