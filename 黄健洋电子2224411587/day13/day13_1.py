import random
import time
class Cell:
    def __init__(self, x: int, y:int) -> None:
        self.condition=0
        self.x=0
        self.y=0

def Show(n:int, m:int):
    global space
    print('5s 迭代次数为', ans_step)
    for i in range(n):
        for j in range(m):
            if space[i][j].condition==1:
                print('*',end='')
            else:
                print(' ',end='')
        print()
    print('_________________over_______________')
    print('\033[H')

def Universe(n:int, m:int):
    global space
    space=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            space[i][j]=Cell(i, j)
    Show(n, m)

def Seed(n:int, m:int):
    global space
    for i in range(n*m//4):
        while True:
            x=random.randint(0,n-1)
            y=random.randint(0,m-1)
            if space[x][y].condition==0:
                space[x][y].condition=1
                break
    Show(n, m)

def Judge(x:int, y:int, n:int, m:int) ->bool:
    if x<0 or y<0:
        return False
    if x==n or y==m:
        return False
    if space[x][y].condition==0:
        return False
    return True
def Neighbors(n:int, m:int):
    count=[[0 for _ in range(m)]for _ in range(n)]
    move=[[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,1],[-1,-1]]
    for i in range(n):
        for j in range(m):
            for k in move:
                if Judge(i+k[0],j+k[1],n,m):
                    count[i][j]+=1
    return count
def Alive(n:int, m:int):
    global space
    count=Neighbors(n, m)
    for i in range(n):
        for j in range(m):
            if space[i][j].condition==1:
                if count[i][j]==2 or count[i][j]==3:
                    pass
                else:
                    space[i][j].condition=0
            elif space[i][j].condition==0:
                if count[i][j]==3:
                    space[i][j].condition=1
    Show(n,m)

def Step():
    global ans_step
    start=time.perf_counter()
    ans=1
    while True:
        ans+=1
        Alive(15, 80)
        end=time.perf_counter()
        if end-start>5:
            start=time.perf_counter()
            print(ans)
            ans_step=ans
            ans=0

space=[]
ans_step=0
if __name__=='__main__':
    Universe(15, 80)
    Seed(15, 80)
    Step()