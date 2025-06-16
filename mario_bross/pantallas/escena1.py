from mario_bross.entidades.entidad import Entidad 
from mario_bross.entidades.enemigos import Enemigo 
from mario_bross.estructuras.piso import Piso 

class Pantalla: 
  def __init__(self) -> None: 
    self.entidades:list[Entidad] = [] 
    self.estructuras:list[Piso] = [] 

  def manejar_eventos(self, events, keys_pressed): 
    for entidad in self.entidades: 
      entidad.manejar_eventos(events, keys_pressed) 

  def actualizar(self): 
    for entidad in self.entidades: 
    
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

  def draw(self, screen): 
    screen.fill((135, 206, 235)) 
    for estructura in self.estructuras: 
      estructura.dibujar(screen) 
    for entidad in self.entidades: 
      entidad.dibujar(screen) 

  def add_entity(self, entidad): 
    self.entidades.append(entidad) 

  def add_structure(self, estructura): 
    self.estructuras.append(estructura) 