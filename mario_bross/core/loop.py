import pygame

class Loop:
  def __init__(self) -> None:
    self.running = True

  def get_eventos(self):
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        self.running = False

    return pygame.key.get_pressed()