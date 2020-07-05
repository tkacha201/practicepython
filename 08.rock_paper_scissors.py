player_1 = input('rock', 'paper', 'scissors')
player_2 = input('rock', 'paper', 'scissors')

if player_1 == player_2:
    print('Draw')
elif player_1 == 'rock' and player_2 == 'paper':
    print('player_2: Win')
elif player_1 == 'scissors' and player_2 == 'rock':
    print()
    