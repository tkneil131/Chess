def collin():
    # Each piece corresponds to a key
    # Each value contains a list of the coordinates [xpos,ypos]
    
    # To access a piece: white['key'] would return [1,2]
    # To acces a coordinate: white['key'][0] or white['key'][1]
    white={
    'wp1':[1,2],
    'wp2':[2,2],
    'wp3':[3,2],
    'wp4':[4,2],
    'wp5':[5,2],
    'wp6':[6,2],
    'wp7':[7,2],
    'wp8':[8,2],
    }

    turn = 0
    
    while turn == 0:
        
        # Get User input for which piece
        UserInputPiece = input('What piece would you like to move: ')
        
        # Input Validation
        while UserInputPiece not in white.keys(): # check if user input is a key in white
            print("Sorry I didn't understand what piece you meant")
            UserInputPiece = input('What piece would you like to move: ')
        
        # Get User input for piece movement
        UserInputPlace = int(input('How many spaces would you like to move: '))
        
        # Input Validation
        while UserInputPlace not in [1,2]: # check if user input is in the list [1,2]
            print('You must enter either 1 or 2')
            UserInputPlace = int(input('How many spaces would you like to move: '))
        
        # Controls for Movement
        if UserInputPlace == 1:
            print('moving 1 space')
            white[UserInputPiece][1] += 1
            print('position of ',UserInputPiece,'=', white[UserInputPiece])
        
        # Due to our input validation we can assume if it's not a 1, then it must be a 2
        else:
            print('moving 2 spaces')
            white[UserInputPiece][1] +=2
            print('position of ',UserInputPiece,'=', white[UserInputPiece])
        
        turn = 1


collin()
