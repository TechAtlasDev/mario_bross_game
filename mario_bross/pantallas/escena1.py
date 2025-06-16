from mario_bross.entidades.entidad import Entidad  # Importa la clase base Entidad
from mario_bross.entidades.enemigos import Enemigo  # Importa la clase Enemigo para comprobar tipos
from mario_bross.estructuras.piso import Piso  # Importa la clase Piso para las estructuras del nivel

class Pantalla:  # Define la clase Pantalla que representa un nivel o escena del juego
  def __init__(self) -> None:  # Constructor de la clase
    self.entidades:list[Entidad] = []  # Lista para almacenar todas las entidades (jugador, enemigos, etc.)
    self.estructuras:list[Piso] = []  # Lista para almacenar todas las estructuras físicas (pisos, paredes, etc.)

  def handle_events(self, events, keys_pressed):  # Método para manejar eventos de entrada
    for entidad in self.entidades:  # Itera sobre cada entidad en la pantalla
      entidad.handle_events(events, keys_pressed)  # Delega el manejo de eventos a cada entidad

  def update(self):  # Método para actualizar el estado del juego en cada frame
    for entidad in self.entidades:  # Itera sobre cada entidad en la pantalla
      # 1. Llama a la lógica interna de la entidad (IA del enemigo, gravedad, etc.)
      entidad.update()  # Actualiza la lógica interna de la entidad

      # 2. Mover en eje X y comprobar colisiones horizontales
      entidad.rect.x += entidad.vel_x  # Aplica la velocidad horizontal a la posición de la entidad
      for estructura in self.estructuras:  # Comprueba colisiones con cada estructura
        if entidad.rect.colliderect(estructura.make()):  # Si hay colisión con la estructura
          if entidad.vel_x > 0:  # Si la entidad se mueve hacia la derecha
            entidad.rect.right = estructura.make().left  # Ajusta la posición para evitar superposición
            if isinstance(entidad, Enemigo):  # Si es un enemigo
              entidad.cambiar_direccion()  # Cambia la dirección del enemigo al chocar
          elif entidad.vel_x < 0:  # Si la entidad se mueve hacia la izquierda
            entidad.rect.left = estructura.make().right  # Ajusta la posición para evitar superposición
            if isinstance(entidad, Enemigo):  # Si es un enemigo
              entidad.cambiar_direccion()  # Cambia la dirección del enemigo al chocar

      # 3. Mover en eje Y y comprobar colisiones verticales
      entidad.en_suelo = False  # Reinicia el estado de contacto con el suelo
      entidad.rect.y += entidad.vel_y  # Aplica la velocidad vertical a la posición de la entidad
      for estructura in self.estructuras:  # Comprueba colisiones con cada estructura
        if entidad.rect.colliderect(estructura.make()):  # Si hay colisión con la estructura
          if entidad.vel_y > 0:  # Si la entidad está cayendo
            entidad.rect.bottom = estructura.make().top  # Ajusta la posición al tope de la estructura
            entidad.vel_y = 0  # Detiene la caída
            entidad.en_suelo = True  # Marca que la entidad está en contacto con el suelo
          elif entidad.vel_y < 0:  # Si la entidad está saltando (movimiento hacia arriba)
            entidad.rect.top = estructura.make().bottom  # Ajusta la posición al fondo de la estructura
            entidad.vel_y = 0  # Detiene el salto

  def draw(self, screen):  # Método para dibujar todos los elementos en pantalla
    screen.fill((135, 206, 235))  # Rellena el fondo con color celeste (cielo)
    for estructura in self.estructuras:  # Itera sobre cada estructura
      estructura.draw(screen)  # Dibuja la estructura en la pantalla
    for entidad in self.entidades:  # Itera sobre cada entidad
      entidad.draw(screen)  # Dibuja la entidad en la pantalla

  def add_entity(self, entidad):  # Método para añadir una entidad a la pantalla
    self.entidades.append(entidad)  # Agrega la entidad a la lista de entidades

  def add_structure(self, estructura):  # Método para añadir una estructura a la pantalla
    self.estructuras.append(estructura)  # Agrega la estructura a la lista de estructuras