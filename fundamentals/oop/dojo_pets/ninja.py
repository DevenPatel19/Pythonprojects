class Ninja:
#     # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self , first_name , last_name , pet , treats , pet_food ) :
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
#     # implement the following methods:
#     # walk() - walks the ninja's pet invoking the pet play() method
#     # feed() - feeds the ninja's pet invoking the pet eat() method
#     # bathe() - cleans the ninja's pet invoking the pet noise() method
    def walk(self):
      self.pet.play()
      return self
    
    def feed(self):
      self.pet.eat()
      return self

    def bathe(self):
      self.pet.noise()
      return self
