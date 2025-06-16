from mario_bross.core.game import Game
from mario_bross.utils.config import Config

from mario_bross.pantallas.escena1 import Pantalla

from mario_bross.entidades.personaje import Personaje
from mario_bross.entidades.enemigos import Enemigo

from mario_bross.estructuras.piso import Piso

def run_game():
  config = Config()
  game = Game(config)
  
  pantalla = Pantalla()
  personaje = Personaje([100, 100], 5)
  enemigo = Enemigo([200, 200], 5, color=(0, 0, 255))
  pantalla.add_entity(personaje)
  pantalla.add_entity(enemigo)

  # Add ground platform
  piso = Piso([0, 500], 800, 100, color=(124, 252, 0))
  pantalla.add_structure(piso)

  # Add obstacles
  obstaculo1 = Piso([200, 400], 100, 100, color=(124, 252, 0))
  pantalla.add_structure(obstaculo1)

  obstaculo2 = Piso([400, 350], 100, 100, color=(124, 252, 0))
  pantalla.add_structure(obstaculo2)

  obstaculo3 = Piso([600, 300], 100, 100, color=(124, 252, 0))
  pantalla.add_structure(obstaculo3)

  # Add floating platforms
  plataforma1 = Piso([150, 250], 150, 20, color=(124, 252, 0))
  pantalla.add_structure(plataforma1)

  plataforma2 = Piso([500, 200], 150, 20, color=(124, 252, 0))
  pantalla.add_structure(plataforma2)

  game.run(pantalla)