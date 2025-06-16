from mario_bross.entidades.entidad import Entidad
from mario_bross.estructuras.piso import Piso

class Pantalla:
  def __init__(self) -> None:
    self.entidades:list[Entidad] = []
    self.estructuras:list[Piso] = []

  def handle_events(self, events):
    for entidad in self.entidades:
      entidad.handle_events(events)

  def draw(self, screen):
    screen.fill((135, 206, 235))
    for estructura in self.estructuras:
      estructura.draw(screen)

    # Iterando en cada entidad, si está flotando (no tocando al piso), se le bajará
    for entidad in self.entidades:
      if not entidad.colisiona_conjunto(self.estructuras) and not entidad.en_salto:
        entidad.mover_abajo()
      entidad.draw(screen)

  def add_entity(self, entidad):
    self.entidades.append(entidad)
  
  def add_structure(self, estructura):
    self.estructuras.append(estructura)