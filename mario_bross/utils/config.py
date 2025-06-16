class Config:
  def __init__(self) -> None:
    self.width = 800
    self.height = 600
    self.title = "Mario Bros"
    self.fps = 60

# Create a singleton instance
config = Config()
