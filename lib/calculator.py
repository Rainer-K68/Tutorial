class Calculator:
  def __init__(self):
    print("Base Calcularor")

  def add(self,a,b):
    return a + b
  
  def sub(self,a,b):
    return a -b
  
  def mul(self, a,b):
    return a * b
  
  def div(self, a,b):
    return a/b

  def operators(self):
    ops = { '+' : self.add,
      '-': self.sub,
      '*': self.mul,
      '/': self.div
      }
    return ops