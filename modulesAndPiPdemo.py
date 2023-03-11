import usefulTools  #imported my useful tools file
from object import Cars
from object import smartphone
print(usefulTools.rollDice(6))   #this function is defined on usefulTools

car1 = Cars("Toyota", "Fortuner", "red", 2500000)
car2 = Cars("Mercedes", "S-Class", "JetBlack", 12500000)
print (car2.model)

smartphone1=smartphone("Apple", "iPhone 14 pro max","A16 Bionic", "pacific blue", "48mp triple",)
print(smartphone1.color)
