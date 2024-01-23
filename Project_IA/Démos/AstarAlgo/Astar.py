from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
from timeit import timeit
#calcule de la fonction heurestique h
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2)+abs(y1-y2)
#developper la fonction de A*
def Astar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)#etat finale
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath
if __name__=='__main__':
    m=maze(5,5)# la taille du matrice 
    m.CreateMaze()
    path=Astar(m)
    l=textLabel(m,'A* Path Length',len(path)+1)#le nombre de sommet
    t1=timeit(stmt='Astar(m)',number=1000,globals=globals())#le temps d'execution
    textLabel(m,'A* Time',t1)
    a=agent(m,footprints=True)
    m.tracePath({a:path})
  
    m.run()