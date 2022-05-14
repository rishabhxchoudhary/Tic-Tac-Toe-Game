class TicTacToe:
    def __init__(self):
        self.grid = [[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' '],]
    def printgrid(self):
        print("   y→",1,"  ",2,"  ",3)
        for i in range(3):
            if i==0: print("x",end="")
            elif i==1: print("↓", end="")
            else: print(" ",end="")
            print("",i+1,self.grid[i])

    def check(self,x):
        for i in range(3):
            if self.grid[i]==[x,x,x]: return True
        if [self.grid[0][0],self.grid[1][0],self.grid[2][0]]==[x,x,x]: return True
        if [self.grid[0][1],self.grid[1][1],self.grid[2][1]]==[x,x,x]: return True
        if [self.grid[0][2],self.grid[1][2],self.grid[2][2]]==[x,x,x]: return True
        if [self.grid[0][0],self.grid[1][1],self.grid[2][2]]==[x,x,x]: return True
        if [self.grid[0][2],self.grid[1][1],self.grid[2][0]]==[x,x,x]: return True
        return False

    def place(self,x,y,c):
        if self.grid[x-1][y-1]==" ":
            self.grid[x-1][y-1]=c
        else:
            print("Invalid input. Try again.")
            x,y = map(int,input("Enter x and y for "+c+" : ").split())
            self.place(x,y,c)

    def start(self):
        choice=0
        chance=0
        self.printgrid()
        while chance<9:
            if choice&1:
                x,y = map(int,input("Enter x and y for O : ").split())
                self.place(x,y,'O')
                if self.check('O'):
                    self.printgrid()
                    print("O WON")
                    break
                else:
                    self.printgrid()
                    choice+=1
                    chance+=1
            else:
                x,y = map(int,input("Enter x and y for X : ").split())
                self.place(x,y,'X')
                if self.check('X'):
                    self.printgrid()
                    print("X WON")
                    break
                else:
                    self.printgrid()
                    choice+=1
                    chance+=1
        if chance==9:
            print("Draw")
game = TicTacToe().start()
