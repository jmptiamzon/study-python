import pprint, random

boardData = {'1': '', '2': '', '3': '',
             '4': '', '5': '', '6': '',
             '7': '', '8': '', '9': ''}

def drawBoard():
    print(boardData['1'] + " | " + boardData['2'] + " | " + boardData['3'])
    print("------")
    print(boardData['4'] + " | " + boardData['5'] + " | " + boardData['6'])
    print("------")
    print(boardData['7'] + " | " + boardData['8'] + " | " + boardData['9'])

def startGame():
    print('Spots\n1.top-L\n2.top-M\n3.top-R\n4.mid-L\n5.mid-M\n6.mid-R\n7.bot-L\n8.bot-M\n9.bot-R')

    boardDataCopy = boardData.copy()
    userPawn = ''
    choice = ''
    #choose pawn
    while userPawn not in ['X', 'O']:
        print('Choose your pawn [X / O]: ')
        userPawn = input()
        
    while not all(boardData[key] for key in boardData.keys()):
        #player choice
        choice = ''

        while choice not in boardDataCopy.keys():
            choice = input()
            if choice in boardDataCopy.keys():
                boardData[choice] = userPawn
        
        print('\nYour move')
        drawBoard()
        del boardDataCopy[choice]


        #computer choice
        computerPawn = 'X' if userPawn != 'X' else 'O'
        
        if boardDataCopy:
            randomKey = random.choice(list(boardDataCopy.keys()))
            boardData[randomKey] = computerPawn
            del boardDataCopy[randomKey]

        print('\nComputer move')
        drawBoard()


def checkWinner():
    print('')


drawBoard()
startGame()