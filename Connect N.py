class Board:
    def __init__(self, N):
        self.N = N

    array = []
    for x in range(7):
        line = []
        for y in range(6):
            line.append(0)
        array.append(line)

    def print(self):
        for y in reversed(range(6)):
            for x in range(7):
                print(self.array[x][y], end="")
            print()

    def addOne(self, y, player):
        for index, number in enumerate(self.array[y]):
            if(number == 0):
                self.array[y][index] = player
                return True
        return False

    def didSomebodyWin(self):
        count = 0
        for x in range(7):
            oldNumber = 0
            if(count == N):
                return True
            for y in range(6):
                number = self.array[x][y]
                if(number != 0):
                    if(number == oldNumber):
                        count += 1
                    else:
                        oldNumber = number
                        count = 1
                else:
                    break
        count = 0
        for y in range(6):
            oldNumber = 0
            if(count == N):
                return True
            for x in range(7):
                number = self.array[x][y]
                if(number != 0):
                    if(number == oldNumber):
                        count += 1
                    else:
                        oldNumber = number
                        count = 1
                else:
                    break
        count = 0
        for x in range(7):
            y = 0
            oldNumber = 0
            if(count == N):
                print(x, y, 1)
                return True
            for _ in range(x+1):
                number = self.array[x][y]                
                print(x,y)
                if(number != 0):
                    if(number == oldNumber):
                        count += 1
                    else:
                        oldNumber = number
                        count = 1
                y += 1
                x -= 1
                if(y == 6):
                    break
        for _ in range(6):
            y = 0
            x = 6
            oldNumber = 0
            if(count == N):
                print(x, y, 2)
                return True
            for _ in range(x+1):
                number = self.array[x][y]
                if(number != 0):
                    if(number == oldNumber):
                        count += 1
                    else:
                        oldNumber = number
                        count = 1
                y += 1
                if(y == 5):
                    break


def isInputBetweenBoundaries(input):
    if(input <= 7 and input >= 1):
        return True
    return False


def isInputLegal(input):
    try:
        number = int(input)
        if(isInputBetweenBoundaries(number)):
            type(number)
            return number
        else:
            return False
    except:
        return False


def askUserForN():
    N = input(
        "Please pick a number of pieces that need to line up in order for a player to win :")
    output = isInputLegal(N)
    if(output):
        return output
    return askUserForN()


illegalMove = False
gameEnded = False
player = 2

N = askUserForN()
stringN = str(N)
print("You are playing Connect "+stringN+"! The first player to get "+stringN +
      " pieces of the same color vertically, horizontally, or diagonally wins.")
board = Board(N)
while not gameEnded:
    board.print()
    if(illegalMove == True):
        print("Please try again.")
        illegalMove = False
    else:
        if(player == 1):
            player = 2
        else:
            player = 1

    print("Player "+str(player)+"'s turn")
    line = input(
        "Which row would you like to put it?: ")
    if(isInputLegal(line)):
        isSuccesfull = board.addOne(int(line)-1, player)
        if(not isSuccesfull):
            print("The row you are putting in is filled.")
            illegalMove = True
    else:
        print("You can only pick a number from 1 to 7.")
        illegalMove = True

    print()

    gameEnded = board.didSomebodyWin()

print("----------------------------------")
board.print()
print("Congratulations!! Player "+str(player)+" won!!")
