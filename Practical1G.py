import random

def score_list_generator(minvalue, givenvalue, maxvalue):
   lower_score_list = list(range(minvalue, givenvalue))
   score_list = []
   for i in range(0, 5):
      score = random.choice(lower_score_list)
      lower_score_list.pop(lower_score_list.index(score))
      score_list.append(score)
   higher_score_list = list(range(givenvalue+1, maxvalue+1))
   for i in range(0, 5):
      score = random.choice(higher_score_list)
      higher_score_list.pop(higher_score_list.index(score))
      score_list.append(score)
   return score_list

def name_generator():
   name_length = random.choice(range(4, 8))
   name_nums = []
   for i in range(0, name_length):
      name_num = random.choice(range(1, 27))
      name_nums.append(name_num)
   name = chr(64 + name_nums[0])
   for i in range(1, name_length):
      name += chr(96 + name_nums[i])
   return name

class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

   def display(self):
      print(self.username + ' with a score of ' + str(self.score))

score = int(input('Type in the given score : '))
score_list = score_list_generator(0, score, 99999)
score_list.append(score)
players = []
for i in range(0, 11):
   username = name_generator()
   score = random.choice(score_list)
   score_list.pop(score_list.index(score))
   player = Player(username, score)
   players.append(player)
   player.display()
