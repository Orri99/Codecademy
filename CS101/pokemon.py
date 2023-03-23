import math
import time
import random

class Pokemon:
  def __init__(self, name, p_type, weakness, move1, move2, level, hp, attack, defence, sp_attack, sp_defence, speed):
    self.name = name
    self.type = p_type
    self.weak = weakness
    self.level = level
    self.max_hp = hp
    self.hp = hp
    self.stats = [attack, defence, sp_attack, sp_defence, speed, 100, 100]
    self.moves = [move1, move2]
    self.fainted = False

  def __repr__(self):
    return "{} an level {} {} type pokémon!".format(self.name,self.level,self.type)

  def faint(self):
    if self.hp <= 0:
      self.fainted = True
      print("{} fainted!".format(self.name))

  def use_move(self, target, selected_move):
    mod = 1
    stab = 1
    index = 0
    for move in self.moves:
      if selected_move in move.name:
        using = move
      else:
        index += 1

    print("{} used {}".format(self.name,using.name))
    
    if using.type in target.weak:
      mod = 2
    if using.type in self.type:
      stab = 1.5

    if using.attack:
      damage = (((((2*self.level)/5)*using.power*(self.stats[0]/target.stats[1]))/50)+2)*stab*mod
      target.hp -= damage
      if mod == 2:
        print("It's super effective!")
      if target.hp <= 0:
        target.faint()
      else:
        print("{} has {}% HP remaining".format(target.name,math.floor(100*target.hp/target.max_hp)))

    if using.sp_attack:
      damage = (((((2*self.level)/5)*using.power*math.floor(self.stats[2]/target.stats[3]))/50)+2)*stab*mod
      target.hp -= damage
      if mod == 2:
        print("It's super effective!")
      if target.hp <= 0:
        target.faint()
      else:
        print("{} has {}% HP remaining".format(target.name,math.floor(100*target.hp/target.max_hp)))

    stat_names = ["attack", "defence", "sp. attack", "sp. defence", "speed", "accuracy", "evasion"]
    if using.debuff_target[0]:
      for i in range(0,6):
        if using.debuff_target[i+1]:
          target.stats[i] = math.floor(target.stats[i]*0.66)
          print("{}'s {} fell.".format(target.name,stat_names[i]))
    
    if using.debuff_user[0]:
      for i in range(0,6):
        if using.debuff_user[i+1]:
          self.stats[i] = math.floor(self.stats[i]*0.66)
          print("{}'s {} fell.".format(self.name,stat_names[i]))

    if using.buff_target[0]:
      for i in range(0,6):
        if using.buff_target[i+1]:
          target.stats[i] = math.floor(target.stats[i]*1.5)
          print("{}'s {} rose.".format(target.name,stat_names[i]))

    if using.buff_user[0]:
      for i in range(0,6):
        if using.buff_user[i+1]:
          self.stats[i] = math.floor(self.stats[i]*1.5)
          print("{}'s {} rose.".format(self.name,stat_names[i]))

class Move:
  def __init__(self, name, power, accuracy, m_type, attack, sp_attack, debuff_target=[0,0,0,0,0,0,0,0], buff_user=[0,0,0,0,0,0,0,0],debuff_user=[0,0,0,0,0,0,0,0], buff_target=[0,0,0,0,0,0,0,0]):
    self.name = name
    self.power = power
    self.accuracy = accuracy
    self.type = m_type
    self.attack = attack
    self.sp_attack = sp_attack
    self.buff_user = buff_user
    self.debuff_user = debuff_user
    self.buff_target = buff_target
    self.debuff_target = debuff_target

class Trainer:
  def __init__(self, name, pokemon):
    self.name = name
    self.pokemon = pokemon 

  def __repr__(self):
    return "A trainer by the name of {} and their pokemon {}.".format(self.name,self.pokemon.name)

tackle = Move("Tackle", 40, 100, "Normal", True, False)    
scratch = Move("Scratch", 40, 100, "Normal", True, False)
growl = Move("Growl", 0, 100, "Normal", False, False, [1,1,0,0,0,0,0])
tail_whip = Move("Tail whip", 0, 100, "Normal", False, False, [1,0,1,0,0,0,0])
water_gun = Move("Water gun", 40, 100, "Water", False, True)

bulbasaur = Pokemon("Bulbasaur", "Grass", ["Fire", "Ice", "Poison", "Flying", "Bug"], tackle, growl, 5, 24, 16, 14, 16, 13, 14)

charmander = Pokemon("Charmander", "Fire", ["Water", "Rock", "Ground"], scratch, growl, 5, 23, 16, 13, 14, 14, 16)

squirtle = Pokemon("Squirtle", "Water", ["Grass", "Electric"], tackle, tail_whip, 5, 24, 16, 16, 14, 14, 13)

#squirtle.moves.append(water_gun)

print("Hello there! Welcome to the world of Pokémon!")
time.sleep(1)
print("My name is Oak! People call me the Pokémon Professor! ")
time.sleep(1)
print("This world is inhabited by creatures called Pokémon! ")
time.sleep(1)
print("For some people, Pokémon are pets. Others use them for fights.")
time.sleep(1)
print("Myself...I study Pokémon as a profession.")
time.sleep(1)
player_name = input("First, what is your name? ")
time.sleep(0.5)
print("Right! So your name is {}!".format(player_name))
time.sleep(1)
print("This is my grandson. He's been your rival since you were a baby.")
time.sleep(2)
rival_name = input("...Erm, what is his name again? ")
time.sleep(0.5)
print("That's right! I remember now! His name is {}!".format(rival_name))
time.sleep(1)
print("{}! Your very own Pokémon legend is about to unfold!".format(player_name))
time.sleep(1)
print("A world of dreams and adventures with Pokémon awaits!")
time.sleep(0.5)
print("Lets go!")
time.sleep(1.5)
print("But before you start your journey you'll need a Pokémon to accompany you.")
time.sleep(1)
select = True
player_choise = input("Which Pokémon would you like to take along with you, Bulbasaur, Charmander or Squirtle? ")
while select:
  if player_choise.capitalize() == "Bulbasaur":
    print("So you have chosen Bulbasaur.")
    player = Trainer(player_name,bulbasaur)
    rival = Trainer(rival_name,charmander)
    select = False
  elif player_choise.capitalize() == "Charmander":
    print("So you have chosen Charmander.")
    player = Trainer(player_name,charmander)
    rival = Trainer(rival_name,squirtle)
    select = False
  elif player_choise.capitalize() == "Squirtle":
    print("So you have chosen Squirtle.")
    player = Trainer(player_name,squirtle)
    rival = Trainer(rival_name,bulbasaur)
    select = False
  else:
    print("That was not one of the options...")
    time.sleep(1)
    player_choise = input("Which pokémon would you like to take along with you, Bulbasaur, Charmander or Squirtle? ")

time.sleep(1)
print("I can see they like you already! Now go, your adventure awaits!")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Rival {} wants to battle!".format(rival.name))
time.sleep(1)
print("Rival {} sent out {}".format(rival.name,rival.pokemon.name))
time.sleep(1)
print("Go, {}!".format(player.pokemon.name))
time.sleep(1)

while player.pokemon.fainted == False and rival.pokemon.fainted == False:

  num_moves = len(player.pokemon.moves)
  list_of_moves = ""
  for i in range(0,num_moves):
    if i == 0:
      list_of_moves += player.pokemon.moves[i].name
    elif i == num_moves-1:
      list_of_moves = list_of_moves + " or " + player.pokemon.moves[i].name
    else:
      list_of_moves = list_of_moves + ", " + player.pokemon.moves[i].name

  select = True
  while select:
    print("Which move will {} use?".format(player.pokemon.name))
    time.sleep(1)
    choise = input(list_of_moves + "? ")
    using = ""
    index = 0
    for move in player.pokemon.moves:
      if choise.capitalize() in move.name:
        using = choise.capitalize()
        select = False
      else:
        index += 1

    if using == "":
      print("That was not one of the options...")
      time.sleep(1)

  rival_choise = random.randint(0,len(rival.pokemon.moves)-1)
    
  if rival.pokemon.stats[4] > player.pokemon.stats[4]:
    rival.pokemon.use_move(player.pokemon, rival.pokemon.moves[rival_choise].name)
    time.sleep(2)
    if player.pokemon.fainted == False:
      player.pokemon.use_move(rival.pokemon, using)
  else:
    player.pokemon.use_move(rival.pokemon, using)
    if rival.pokemon.fainted == False:
      rival.pokemon.use_move(player.pokemon, rival.pokemon.moves[rival_choise].name)

if rival.pokemon.fainted:
  print("Defeated rival {}!".format(rival.name))
elif player.pokemon.fainted:
  print("{} is out of usable Pokémon.".format(player.name))
  print("{} blacked out...".format(player.name))