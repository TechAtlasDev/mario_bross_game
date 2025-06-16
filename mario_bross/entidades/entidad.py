import pygame

class Entidad:
  def __init__(self, coordenadas, velocidad=20, color=(255, 255, 255)) -> None:
    self.coordenadas = coordenadas
    self.velocidad = velocidad
    self.unidades_salto = 30
    self.en_salto = False
    self.unidades_locales = self.unidades_salto
    self.color = color

  def handle_events(self, events):
    """
    Maneja los eventos del teclado, por defecto no hace nada
    """
    pass

  def draw(self, screen):
    if self.en_salto:
      self.mover_arriba()
      self.unidades_locales -= 1
    if self.unidades_locales <= 0:
      self.en_salto = False
      self.unidades_locales = self.unidades_salto
    self._render_()
  
  def _render_(self):
    raise NotImplementedError("Debe implementar el metodo _render_")

  def mover_derecha(self):
    self.coordenadas[0] += self.velocidad
  
  def mover_izquierda(self):
    self.coordenadas[0] -= self.velocidad

  def mover_arriba(self):
    self.coordenadas[1] -= self.velocidad

  def mover_abajo(self):
    self.coordenadas[1] += self.velocidad

  def saltar(self):
    print (f"En salto: {self.en_salto}")
    if self.en_salto == False:
      self.en_salto = True

  def make(self):
    return pygame.Rect(self.coordenadas[0], self.coordenadas[1], self.radio, self.radio)
  
  def colisiona_con(self, estructura):
    return self.make().colliderect(estructura.make())

  def colisiona_conjunto(self, estructuras):
    result = False
    for estructura in estructuras:
      if self.colisiona_con(estructura):
        result = True
        break
    return result