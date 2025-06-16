import pygame
from mario_bross.core.loop import Loop
from mario_bross.utils.config import Config
  
class Game:
  def __init__(self, config:Config) -> None:
    self.config = config
    self.loop = Loop()
    self.screen = pygame.display.set_mode((self.config.width, self.config.height))
    pygame.display.set_caption(self.config.title)
    self.clock = pygame.time.Clock()

  def run(self, pantalla):
    while self.loop.running:
      self.screen.fill((135, 206, 235))
      pantalla.handle_events(
        self.loop.get_eventos()
      )
      pantalla.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(self.config.fps)
      