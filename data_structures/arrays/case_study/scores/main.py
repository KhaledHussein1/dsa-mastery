from game_entry import GameEntry
from scoreboard import Scoreboard

board = Scoreboard()

user1 = GameEntry('Khaled', 800)
user2 = GameEntry('James', 23)
user3 = GameEntry('David', 321)
user4 = GameEntry('Lyrssa', 1111)
user5 = GameEntry('Steven', 968)
user6 = GameEntry('Tammy', 234)
user7 = GameEntry('Mary', 754)
user8 = GameEntry('Hunter', 65)
user9 = GameEntry('Levi', 4)
user10 = GameEntry('Ricky', 100)
user11 = GameEntry('Turner', 4050)
user12 = GameEntry('Sandor', 1600)
user13 = GameEntry('Ulga', 200)
user14 = GameEntry('Aika', 40)

users = [user1, user2, user3, user4, 
        user5, user6, user7, user8,
        user9, user10, user11, user12,
        user13, user14]

for user in users:
    board.add(user)

print(board)