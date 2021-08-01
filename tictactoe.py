import pprint

def drawBoard():
    print(boardData['top-L'] + " | " + boardData['top-M'] + " | " + boardData['top-R'])
    print("------")
    print(boardData['mid-L'] + " | " + boardData['mid-M'] + " | " + boardData['mid-R'])
    print("------")
    print(boardData['bot-L'] + " | " + boardData['bot-M'] + " | " + boardData['bot-R'])

boardData = {'top-L': '', 'top-M': '', 'top-R': '',
             'mid-L': '', 'mid-M': '', 'mid-R': '',
             'bot-L': '', 'bot-M': '', 'bot-R': ''}

drawBoard()



