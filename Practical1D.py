class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

def insert(leaderboard, player_username, player_score):
   player = Player(player_username, player_score)
   left = 0
   right = len(leaderboard)-1
   if player_score > leaderboard[0].score:
      return player+leaderboard
   if player_score < leaderboard[-1].score:
      return leaderboard+player
   while (left <= right):
      mid = (left + right) // 2
      if (leaderboard[mid].score >= player_score) and (player_score > leaderboard[mid+1].score):
         return leaderboard[:mid+1] + player + leaderboard[mid+1:]
      if (leaderboard[mid].score >= player_score):
         left = mid + 1
      else:
         right = mid - 1
   return leaderboard
