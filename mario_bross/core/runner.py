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
  
  personaje = Personaje(100, 450, 40, 40)
  enemigo = Enemigo(300, 300, 40, 40, velocidad=2)
  pantalla.anadir_entidad(personaje)
  pantalla.anadir_entidad(enemigo)

  piso = Piso([0, 500], 800, 100, color=(34, 139, 34))
  pantalla.anadir_estructura(piso)


  obstaculo1 = Piso([200, 400], 100, 100, color=(139, 69, 19))
  pantalla.anadir_estructura(obstaculo1)

  obstaculo2 = Piso([400, 300], 100, 100, color=(139, 69, 19))
  pantalla.anadir_estructura(obstaculo2)

 ## obstaculo3 = Piso([600, 400], 100, 100, color=(139, 69, 19))
 ## pantalla.anadir_estructura(obstaculo3)


  plataforma1 = Piso([150, 250], 150, 20, color=(169, 169, 169))
  pantalla.anadir_estructura(plataforma1)

  plataforma2 = Piso([500, 200], 150, 20, color=(169, 169, 169))
  pantalla.anadir_estructura(plataforma2)

  plataforma3 = Piso([300, 150],150,20,color=(169, 169, 169))
  pantalla.anadir_estructura(plataforma3)

  limite1=Piso([-10,0], 10, 600, color=(135, 206, 235))
  pantalla.anadir_estructura(limite1)

  limite2=Piso([800,0], 10, 600, color=(135, 206, 235))
  pantalla.anadir_estructura(limite2)

  game.run(pantalla)
