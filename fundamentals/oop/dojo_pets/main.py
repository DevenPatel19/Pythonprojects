from ninja import *
from pets import *

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.

black_ninja = Ninja('Ryu', 'Hyabusa', 'Cat', ['Noodle' , 'Rice'] , 'Milk' )

black_ninja.feed()
black_ninja.walk()
black_ninja.bathe()

print(black_ninja.pet.name)

Cleo = Cat('Cleo', 'Calico', ['Rams', 'Scratch', 'Defend'], 'Meow meow meow')
Cleo.noise()

Lando = Cat('Snoop', 'Orange Boy', ['Charge', 'Heal', 'Attack'], 'Squeak')
Lando.noise()