def quick_sort(players):
    if players == []:
      return []
   left = []
   right = []
   pivot = players[0].score
   for player in players[1:]:
      i = player.score
      if i < pivot:
         left.append(player)
      else:
         right.append(player)
   left = quick_sort(left)
   right = quick_sort(right)
   return right + [players[0]] + left

class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

n = int(input('Type in the number of players : '))
players = []
for i in range(0, n):
   username = input('Type in the name of this player : ')
   score = int(input('Type in the score of this player : '))
   player = Player(username, score)
   players.append(player)

leaderboard = quick_sort(players)
