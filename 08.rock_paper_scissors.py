print('Starting...')
while True:
    player_1 = input('rock, paper, scissors: ')
    player_2 = input('rock, paper, scissors: ')

    if player_1 == player_2:
        print('Draw')
    elif player_1 == 'rock' and player_2 == 'paper':
        print('player_2: Win')
    elif player_1 == 'scissors' and player_2 == 'rock':
        print('player_2: Win')
    elif player_1 == 'paper' and player_2 == 'scissors':
        print('player_2: Win')
    else:
        print('player_1: Win')

    yes_or_no = input("Play again? y/n")
    if yes_or_no == 'y':
        continue
    elif yes_or_no == 'n':
        break
