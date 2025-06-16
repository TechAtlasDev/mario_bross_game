import pygame
from mario_bross.utils.config import Config

class Game:
  def __init__(self, config:Config) -> None:
    pygame.init()
    self.config = config
    self.screen = pygame.display.set_mode((self.config.width, self.config.height))
    pygame.display.set_caption(self.config.title)
    self.clock = pygame.time.Clock()
    self.running = True

  def run(self, pantalla):
    while self.running:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          self.running = False
      
      keys_pressed = pygame.key.get_pressed()
      pantalla.handle_events(events, keys_pressed)

      pantalla.update()

      pantalla.draw(self.screen)
      pygame.display.flip()

      self.clock.tick(self.config.fps)
    
    pygame.quit()
      