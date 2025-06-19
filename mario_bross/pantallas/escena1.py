from mario_bross.entidades.entidad import Entidad
from mario_bross.entidades.enemigos import Enemigo
from mario_bross.entidades.personaje import Personaje
from mario_bross.estructuras.piso import Piso
from mario_bross.utils.config import Config

class Pantalla:
  def __init__(self) -> None:
    self.entidades:list[Entidad] = []
    self.estructuras:list[Piso] = []
    self.camera_y = 0
    self.config = Config()

  def manejar_eventos(self, events, keys_pressed):
    for entidad in self.entidades:
      entidad.manejar_eventos(events, keys_pressed)

  def actualizar(self):
    personaje = None
    for entidad in self.entidades:
      if isinstance(entidad, Personaje):
        personaje = entidad
      
      entidad.accionar() # el que ejecuta la gravedad
    
      entidad.rect.x += entidad.vel_x
      for estructura in self.estructuras:
        if entidad.rect.colliderect(estructura.crear_rectangulo()):
          if entidad.vel_x > 0:
            entidad.rect.right = estructura.crear_rectangulo().left
            if isinstance(entidad, Enemigo):
              entidad.cambiar_direccion()
          elif entidad.vel_x < 0:
            entidad.rect.left = estructura.crear_rectangulo().right
            if isinstance(entidad, Enemigo):
              entidad.cambiar_direccion()

      entidad.en_suelo = False
      entidad.rect.y += entidad.vel_y
      for estructura in self.estructuras:
        if entidad.rect.colliderect(estructura.crear_rectangulo()):
          if entidad.vel_y > 0:
            entidad.rect.bottom = estructura.crear_rectangulo().top
            entidad.vel_y = 0
            entidad.en_suelo = True
          elif entidad.vel_y < 0:
            entidad.rect.top = estructura.crear_rectangulo().bottom
            entidad.vel_y = 0

    enemigos = [e for e in self.entidades if isinstance(e, Enemigo)]

    if personaje:
      # que la camara siga al personaje cuando suba, si baja que no lo siga
      if personaje.rect.y < self.config.height / 2:
        self.camera_y = personaje.rect.y - self.config.height / 2

      # Colision con enemigos
      for enemigo in enemigos:
        if not enemigo.esta_muerto and personaje.rect.colliderect(enemigo.rect):
          # si el personaje esta cayendo y la colision es por arriba del enemigo
          if personaje.vel_y > 0 and personaje.rect.bottom <= enemigo.rect.top + 10:
            enemigo.morir()
            personaje.vel_y = -10 # rebote
          else:
            personaje.morir()

    # Eliminar enemigos muertos
    self.entidades = [e for e in self.entidades if not e.esta_muerto]


  def draw(self, screen):
    screen.fill((135, 206, 235))
    for estructura in self.estructuras:
      estructura.dibujar(screen, self.camera_y)
    for entidad in self.entidades:
      entidad.dibujar(screen, self.camera_y) 

  def add_entity(self, entidad): 
    self.entidades.append(entidad) 

  def add_structure(self, estructura): 
    self.estructuras.append(estructura) 