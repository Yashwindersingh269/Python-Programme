class Employee:
  def __init__(self,name):
      self.name = name
  def __len__(self):
      i = 0
      for c in self.name:
          i = i+1
      return 0  
  
  def __str__(self):
    return f"The name of the employee is {self.name}" 

  def __repr__(self):
    return f"Employee ('{self.name}')" 