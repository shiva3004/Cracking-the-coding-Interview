class cat:
  def __init__(self, name):
    self.name = name
    self.order = None
    self.next = None

class dog:
  def __init__(self, name):
    self.name = name
    self.order = None
    self.next = None

class animal_shelter():
  def __init__(self):
    self.cat_list_head = self.cat_list_tail = None
    self.dog_list_head = self.dog_list_tail = None
    self.order = 0
  
  def enqueue(self, animal):
    animal.order = self.order + 1
    self.order += 1
    if type(animal) is cat:
      if self.cat_list_head is None:
        self.cat_list_head = self.cat_list_tail = animal
      else:
        self.cat_list_tail.next = animal
        self.cat_list_tail = animal
    elif type(animal) is dog:
      if self.dog_list_head is None:
        self.dog_list_head = self.dog_list_tail = animal
      else:
        self.dog_list_tail.next = animal
        self.dog_list_tail = animal
    
  def dequeue_any(self):
    if self.cat_list_head is None and self.dog_list_head is None:
      raise Exception('Queue is Empty')
    elif self.cat_list_head is None:
      return self.dequeue_dog
    elif self.dog_list_head is None:
      return self.dequeue_cat
      
    if self.cat_list_head.order < self.dog_list_head.order:
      return self.dequeue_cat()
    return self.dequeue_dog
    
  def dequeue_cat(self):
    if self.cat_list_head is None:
      raise Exception('Cat Queue is Empty')
    animal = self.cat_list_head.name
    self.cat_list_head = self.cat_list_head.next
    return animal
  
  def dequeue_dog(self):
    if self.dog_list_head is None:
      raise Exception('Dog Queue is Empty')
    animal = self.dog_list_head.name
    self.dog_list_head = self.dog_list_head.next
    return animal
    
shelter = animal_shelter()
shelter.enqueue(cat('cat1'))
shelter.enqueue(cat('cat2'))
shelter.enqueue(cat('cat3'))
shelter.enqueue(dog('dog1'))
shelter.enqueue(dog('dog2'))
shelter.enqueue(dog('dog3'))
print (shelter.dequeue_any())
print (shelter.dequeue_dog())
print (shelter.dequeue_cat())
print (shelter.dequeue_any())
  
