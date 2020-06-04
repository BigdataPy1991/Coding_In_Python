
import itertools
# def current_game(game):
#     for i in game:
#         if(all((ele)==i[0] for ele in i)):
#             print("Winner")
#         else:
#             print("Play again")
def all_same(l):
    if(l.count(l[0])==len(l) and row[0]!=0):
        print("Winner")

def Wingame(game):
    print(game)
 #Horizantal wins for the game
    for row in game:
        if all_same(row):
            win_flag=True
            play=False
            print("Player {} won the game with horizantal match".format(row[0]))
            return True
#Vertical checks for win
    for col in range(len(game)):
        ver_list = []
        for row in game:
            ver_list.append(row[col])
            print(ver_list)
        if all_same(ver_list):
            win_flag = True
            play = False
            print("Player {} won the game with vertical match".format(ver_list[0]))
            return True
#Diagnoal check for win
    diag=[]
    for row,col in enumerate(range(len(game))):
        diag.append(game[row][col])
        print(diag)
    if all_same(diag):
        win_flag = True
        play = False
        print("Player {} won the game with diagnal match".format(diag[0]))
        return True

    diag=[]
    for row,col in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
        print(diag)
    if  all_same(diag):
        win_flag = True
        play = False
        print("Player {} won the game with diagnal match".format(diag[0]))

# chkList(game)
def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        print("   0, 1, 2")
        if not just_display:
            game_map[row][column] = player
            for index,row in enumerate(game_map):
                print(index,row)
            return game_map
    except Exception as e:
        print("Did u enter the index correctly as in 0,1,2")

play=True
players=[1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    win_flag=False
    game,_ = game_board(game, just_display=True)
    players_choice=itertools.cycle([1,2])
    while not win_flag:
        current_player=next(players_choice)
        print("Current player is 1 {}".format(current_player))
        played=False
        while not played:
            player=int(input("select player ID 1 0r 2 : "))
            row=int(input("Select the row in 0,1,2 : "))
            column=int(input("seletc the column in 0,1,2 : "))
            game = game_board(game, player, row, column)
            Wingame(game)