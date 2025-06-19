from mario_bross.core.game import Game
from mario_bross.utils.config import Config

from mario_bross.pantallas.escena1 import Pantalla

from mario_bross.entidades.personaje import Personaje
from mario_bross.entidades.enemigos import Enemigo

from mario_bross.estructuras.piso import Piso

import random

def run_game():
    config = Config()
    game = Game(config)
    
    pantalla = Pantalla()
    
    personaje = Personaje(100, 450, 40, 40)
    enemigo = Enemigo(300, 460, 40, 40, velocidad=2)
    pantalla.add_entity(personaje)
    pantalla.add_entity(enemigo)

    # Ground level
    piso = Piso([0, 500], 800, 100, color=(34, 139, 34))
    pantalla.add_structure(piso)

    # Obstacles
    obstaculo1 = Piso([random.randint(0, 800), 450], 50, 50, color=(139, 69, 19))
    pantalla.add_structure(obstaculo1)

    obstaculo2 = Piso([random.randint(0, 800), 450], 50, 50, color=(139, 69, 19))
    pantalla.add_structure(obstaculo2)

    # Platforms
    plataforma1 = Piso([random.randint(0, 800), 350], 200, 20, color=(169, 169, 169))
    pantalla.add_structure(plataforma1)

    plataforma2 = Piso([500, 300], 200, 20, color=(169, 169, 169))
    pantalla.add_structure(plataforma2)

    plataforma3 = Piso([300, 250], 200, 20, color=(169, 169, 169))
    pantalla.add_structure(plataforma3)

    plataforma4 = Piso([350, 150], 100, 20, color=(169, 169, 169))
    pantalla.add_structure(plataforma4)

    # Decorative elements
    decor1 = Piso([50, 450], 25, 25, color=(0, 100, 0))
    pantalla.add_structure(decor1)

    decor2 = Piso([700, 450], 25, 25, color=(0, 100, 0))
    pantalla.add_structure(decor2)

    # Boundaries
    limite1 = Piso([-10, 0], 10, 600, color=(135, 206, 235))
    pantalla.add_structure(limite1)

    limite2 = Piso([800, 0], 10, 600, color=(135, 206, 235))
    pantalla.add_structure(limite2)

    game.run(pantalla)
