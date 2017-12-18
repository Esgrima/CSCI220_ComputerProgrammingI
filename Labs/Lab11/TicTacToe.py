def buildBoard():
    gameBoard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    # # Test Feature
    # print(gameBoard)
    return gameBoard


def displayBoard(_gameBoard):
    for row in range(len(_gameBoard)):
        print(' | '.join(_gameBoard[row]))
        print('---------')
# # Test Feature
# displayBoard(buildBoard())


def updateBoard(_gameBoard: list, _spot: int, _character: str):
    if str(_spot) == '1' or str(_spot) == '2' or str(_spot) == '3':
        _gameBoard[0][_gameBoard[0].index(str(_spot))] = _character
    elif str(_spot) == '4' or str(_spot) == '5' or str(_spot) == '6':
        _gameBoard[1][_gameBoard[1].index(str(_spot))] = _character
    elif str(_spot) == '7' or str(_spot) == '8' or str(_spot) == '9':
        _gameBoard[2][_gameBoard[2].index(str(_spot))] = _character
    # _spot has already been filled
    else:
        print('Invalid input!')
    displayBoard(_gameBoard)


# # Test Feature
# updateBoard(buildBoard(), 5, 'X')


def gameStatus(_gameBoard: list, _character: str, _turns: int):
    # vertical
    # winCondition1: _gameBoard[0][0] == _gameBoard[1][0] == _gameBoard[2][0]
    # winCondition2: _gameBoard[0][1] == _gameBoard[1][1] == _gameBoard[2][1]
    # winCondition3: _gameBoard[0][2] == _gameBoard[1][2] == _gameBoard[2][2]
    # horizontal
    # winCondition4: _gameBoard[0][0] == _gameBoard[0][1] == _gameBoard[0][2]
    # winCondition5: _gameBoard[1][0] == _gameBoard[1][1] == _gameBoard[1][2]
    # winCondition6: _gameBoard[2][0] == _gameBoard[2][1] == _gameBoard[2][2]
    # diagonal
    # winCondition1: _gameBoard[0][0] == _gameBoard[1][1] == _gameBoard[2][2]
    # winCondition2: _gameBoard[2][0] == _gameBoard[1][1] == _gameBoard[0][2]

    if _gameBoard[0][0] == _gameBoard[1][0] == _gameBoard[2][0] or \
       _gameBoard[0][1] == _gameBoard[1][1] == _gameBoard[2][1] or \
       _gameBoard[0][2] == _gameBoard[1][2] == _gameBoard[2][2] or \
       _gameBoard[0][0] == _gameBoard[0][1] == _gameBoard[0][2] or \
       _gameBoard[1][0] == _gameBoard[1][1] == _gameBoard[1][2] or \
       _gameBoard[2][0] == _gameBoard[2][1] == _gameBoard[2][2] or \
       _gameBoard[0][0] == _gameBoard[1][1] == _gameBoard[2][2] or \
       _gameBoard[2][0] == _gameBoard[1][1] == _gameBoard[0][2]:
        if _character == 'X':
            return 1
        elif _character == 'O':
            return 2
    # checks for a tie
    elif _turns == 10:
        return -1
    # win condition is not satisfied yet
    else:
        return 0


def runGame():
    print("Welcome to Tic Tac Toe! X Player goes first!")
    # prints the initial board
    displayBoard(buildBoard())
    turns = 1
    # allows gameStatus to initially return 0
    playerCharacter = ''
    # stores the board in a variable to later be overridden
    nextUpdate = buildBoard()
    status = gameStatus(nextUpdate, playerCharacter, turns)
    print()

    while status != -1 and status != 1 and status != 2:
        if turns % 2 != 0:
            playerCharacter = 'X'
        else:
            playerCharacter = 'O'
        playerInput = int(input("{0}-Player, Please enter a position to play: ".format(playerCharacter)))
        updateBoard(nextUpdate, playerInput, playerCharacter)
        status = gameStatus(nextUpdate, playerCharacter, turns)
        turns += 1
    if status == -1:
        print("Stale Mate!")
    elif status == 1:
        print("X Won!")
    else:
        print("O Won!")


runGame()
