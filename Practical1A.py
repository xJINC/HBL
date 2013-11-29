class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

n = int(input('Enter number of players: '))
players = []
for i in range(0, n):
   username = input('Please enter name of player: ')
   score = int(input('Please enter score of player: '))
   player = Player(username, score)
   players.append(player)
