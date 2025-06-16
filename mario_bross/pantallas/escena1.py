from mario_bross.entidades.entidad import Entidad
from mario_bross.entidades.enemigos import Enemigo
from mario_bross.estructuras.piso import Piso

class Pantalla:
  def __init__(self) -> None:
    self.entidades:list[Entidad] = []
    self.estructuras:list[Piso] = []

  def handle_events(self, events, keys_pressed):
    for entidad in self.entidades:
      entidad.handle_events(events, keys_pressed)

  def update(self):
    for entidad in self.entidades:
      # 1. Llama a la lógica interna de la entidad (IA del enemigo, gravedad, etc.)
      entidad.update()

      # 2. Mover en eje X y comprobar colisiones horizontales
      entidad.rect.x += entidad.vel_x
      for estructura in self.estructuras:
        if entidad.rect.colliderect(estructura.make()):
          if entidad.vel_x > 0: # Moviéndose a la derecha
            entidad.rect.right = estructura.make().left
            if isinstance(entidad, Enemigo):
              entidad.cambiar_direccion()
          elif entidad.vel_x < 0: # Moviéndose a la izquierda
            entidad.rect.left = estructura.make().right
            if isinstance(entidad, Enemigo):
              entidad.cambiar_direccion()

      # 3. Mover en eje Y y comprobar colisiones verticales
      entidad.en_suelo = False
      entidad.rect.y += entidad.vel_y
      for estructura in self.estructuras:
        if entidad.rect.colliderect(estructura.make()):
          if entidad.vel_y > 0: # Cayendo
            entidad.rect.bottom = estructura.make().top
            entidad.vel_y = 0
            entidad.en_suelo = True
          elif entidad.vel_y < 0: # Saltando
            entidad.rect.top = estructura.make().bottom
            entidad.vel_y = 0

  def draw(self, screen):
    screen.fill((135, 206, 235))
    for estructura in self.estructuras:
      estructura.draw(screen)
    for entidad in self.entidades:
      entidad.draw(screen)

  def add_entity(self, entidad):
    self.entidades.append(entidad)

  def add_structure(self, estructura):
    self.estructuras.append(estructura)