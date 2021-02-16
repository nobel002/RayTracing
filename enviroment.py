class Enviroment(object):
  def __init__(self, array = []):
    self.array = array
  
  def __add__(self, value):
    self.array.append(value)

  def __radd__(self, value):
      self.array.append(value)