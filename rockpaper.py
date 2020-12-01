playing = True

while playing:
    print('Lets play Bear, Beetle, Beagle!')
    player1 = input('Player 1 Enter your choice: ')
    
    print(player1)
    player2 = input('Player 2 Enter your choice: ')

    if player1 == 'Bear' and player2 == 'Beagle':
        print('Player1s bear beat the beagle and won')
        
    if player1 == 'Beagle' and player2 == 'Bear':
        print('Player2s bear beat the beagle and won')
    
    play_again = input('Would you like to play again?')
    if play_again[0] == 'n':
        playing = False
