def isBetweenBoundaries(input,min,max):
    if(input <= max and input >= min):
        return True
    return False


def isInputLegal(input):
    try:
        number = int(input)
        if(isBetweenBoundaries(number,1,7)):
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
        for x in range(7):
            for y in range(6):
                main = self.array[x][y]
                right = self.lookToDirection(main, x, y, 0, 1, 1)
                if(right):
                    return True
                down = self.lookToDirection(main, x, y, 1, 0, 1)
                if(down):
                    return True
                leftDiag = self.lookToDirection(main, x, y, -1, 1, 1)
                if(leftDiag):
                    return True
                rightDiag = self.lookToDirection(main, x, y, +1, 1, 1)
                if(rightDiag):
                    return True
        return False

    def lookToDirection(self, main, x, y, changeTypeX, changeTypeY, multitude):
        newX = x+changeTypeX*multitude
        newY = y+changeTypeY*multitude
        if(isBetweenBoundaries(newX,0,6) and isBetweenBoundaries(newY,0,5)):
            selected = self.array[newX][newY]
            if(selected != 0 and selected == main):
                if(multitude < self.N-1):
                    return self.lookToDirection(main, x, y, changeTypeX, changeTypeY, multitude+1)
                else:
                    return True
            return False
        return False


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
