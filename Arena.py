import random as rd
class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2
    def battle(self):
        while self.bbot1.is_alive() and self.bbot2.is_alive():
            # if speed is the same randomly determine who goes first
            who_first = rd.randint(0,1)
            #begin battle round
            if self.bbot1.speed < self.bbot2.speed:
              print(self.bbot1.name + " goes first!")
              self.bbot1_first()
            elif(self.bbot2.speed > self.bbot1.speed):
              print(self.bbot2.name + " goes first!")
              self.bbot2_first()
            else:
              if(who_first == 0):
                print(self.bbot1.name + " goes first!")
                self.bbot1_first()
              else:
                print(self.bbot2.name + " goes first!")
                self.bbot2_first()
        if self.bbot1.is_alive():
            print(self.bbot1.name + " is the winner!")
        else:
            print(self.bbot2.name + " is the winner!")
    
    def bbot1_first(self):
        self.bbot1.action(self.bbot2)
        self.bbot2.action(self.bbot1)
        self.bbot1.get_stats()
        print("--------------------")
        self.bbot2.get_stats()
        input("\nPress enter for next round")
    def bbot2_first(self):
        self.bbot2.action(self.bbot1)
        self.bbot1.action(self.bbot2)
        self.bbot1.get_stats()
        print("--------------------")
        self.bbot2.get_stats()
        input("\nPress enter for next round")

#paste Battle Bot Code for one of the students make sure the class name is different
# the one here is just the default! 
"""MAKE SURE TO REPLACE THIS WITH CAMPER'S CODE"""
class BattleBot:
  def __init__(self, name):
    self.name = name;
    self.health = 100.0;
    self.base_armor = 10.0;
    self.base_damage = 10.0;
    self.speed = 10.0;
  def get_stats(self):
    print(self.name)
    print("Health: " + str(self.health))
    print("Speed: " + str(self.speed))
    print("Attack: " + str(self.base_damage))
    print("Defence: " + str(self.base_armor))
  def is_alive(self):
    if self.health <= 0:
      return False
    else:  
      return True
  def attack(self, opponent):
    damage_dealt = self.base_damage-(self.base_damage * (opponent.base_armor/20))
    opponent.take_damage(damage_dealt)
  def take_damage(self, damage_dealt):
    self.health -= damage_dealt
  def build_armor(self):
    self.base_armor += 2
    self.base_damage -= 1
    self.speed -= 1
  def build_speed(self):
    self.speed += 2
    self.base_damage -= 1
    self.base_armor -= 1
  def build_attack(self):
    self.base_damage += 2
    self.base_armor -= 1
    self.speed -= 1
  def action(self, opponent):
    r_m = rd.randint(0, 100)
    if(r_m <= 20):
      self.build_armor()
    elif(r_m <= 40):
      self.build_attack()
    elif(r_m <= 60):
      self.build_speed()
    elif(r_m <= 90):
      self.attack(opponent)
    else:
      print(self.name + " glitched out!")
  
#paste Battle Bot Code for one of the students make sure the class name is different

#declare both Bots for each student here
bot1 = BattleBot("James")
bot2 = BattleBot("Raptor")
arena = Arena(bot1, bot2)
arena.battle()
