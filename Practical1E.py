class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

def binary_search(players, username):
   k = len(players)
   mid = k // 2
   if players[mid].username == username:
      return players[mid].score
   if mid > 0:
      result = binary_search(players[:mid], username)
      if result:
         return result
   if mid+1 < l:
      result = binary_search(players[mid+1:], username)
      if result:
         return result
   return False
