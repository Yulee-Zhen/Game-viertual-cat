class Cat:
  def __init__(self, name):
      self.name = name
      self.energy = 3
      self.health = 3
      self.mood = 3


  def __str__(self) -> str:   
    return '-' * 25 + '\n'\
    + f'{self.name}'.center(25) + '\n'\
    + '-' * 25 + '\n'\
    + ' Energy'.ljust(8) + ':' + ' 🍗' * self.energy + '\n'\
    + ' Health'.ljust(8) + ':' + ' 🟢' * self.health + '\n'\
    + ' Mood'.ljust(8) + ':' + ' 🧡' * self.mood + '\n'\
    + '-' * 25



if __name__ == '__main__':
  cat = Cat('Aily')
  print(cat)


