# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True
    
    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA {}\nOrigin: \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg



#child class instance
class Human(Organism):
    name = "McGuyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"
    inteligence = 100
  # assinged a attribute inguinuity, gave it a message
    def information(self):
        msg ="\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA {}\nOrigin: \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        msg2 ="\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg + msg2

#another child class instance
class Dog(Organism):
    name = "spot"
    species = "canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"
    noise = "bark"
# assinged attribute bite
    def information(self):
        msg ="\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA {}\nOrigin: \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        msg2 = "\nEmits a loud, menacing growl and bites down fiercly on its prey!"
        return msg + msg2

class Bacterium(Organism):
    name = "K"
    species = "Bacterium"
    arms = 0
    legs = 0
    dna = "Sequence C"
    origin = "Mars"
    size = "Microscopic"
#assinged attribute replication
    def information(self):
        msg ="\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA {}\nOrigin: \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        msg2 = "\nThe cells begin to divide and mulitply into two seperate organisms!"
        return msg + msg2

    


if __name__ == "__main__":
        human = Human()
        print(human.information())
        

        dog = Dog()
        print(dog.information())
      

        bacteria = Bacterium()
        print(bacteria.information())
    

        
