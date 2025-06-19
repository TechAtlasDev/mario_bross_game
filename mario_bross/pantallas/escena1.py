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

    # --- APARTADO DE LAS ENTIDADES ---
    for entidad in self.entidades: 
      entidad.accionar() # el que ejecuta la gravedad o lo mueve a los costados
    
      entidad.rect.x += entidad.vel_x 

      # En el caso de que choque algo de costados
      for estructura in self.estructuras: 
        if entidad.rect.colliderect(estructura.crear_rectangulo()): 

          # Derecha
          if entidad.vel_x > 0: 
            entidad.rect.right = estructura.crear_rectangulo().left 
            if isinstance(entidad, Enemigo): 
              entidad.cambiar_direccion() 

          # Izquierda
          elif entidad.vel_x < 0: 
            entidad.rect.left = estructura.crear_rectangulo().right 
            if isinstance(entidad, Enemigo): 
              entidad.cambiar_direccion() 

    
      entidad.rect.y += entidad.vel_y 

      # En el caso de que choque algo de abajo
      for estructura in self.estructuras: 
        if entidad.rect.colliderect(estructura.crear_rectangulo()): 

          # Abajo (osea cayendo)
          if entidad.vel_y > 0: 
            entidad.rect.bottom = estructura.crear_rectangulo().top 
            entidad.vel_y = 0 
            entidad.en_suelo = True 

          # Abajo (osea subiendo)
          elif entidad.vel_y < 0: 
            entidad.rect.top = estructura.crear_rectangulo().bottom 
            entidad.vel_y = 0 
    # --- TERMINANDO EL AAPRTADO DE LAS ENTIDADES ---

  def draw(self, screen): 
    screen.fill((135, 206, 235)) 
    for estructura in self.estructuras: 
      estructura.dibujar(screen) 
    for entidad in self.entidades: 
      entidad.dibujar(screen) 

  def anadir_entidad(self, entidad): 
    self.entidades.append(entidad) 

  def anadir_estructura(self, estructura): 
    self.estructuras.append(estructura) 