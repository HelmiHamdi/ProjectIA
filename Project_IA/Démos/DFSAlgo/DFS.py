
from pyamaze import maze,agent,textLabel
from timeit import timeit
def dfs(m):
 
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    
    while len(frontier)>0:
        currCell=frontier.pop()
     
        if currCell==(1,1):
            break
    
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
             
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
 
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath

   

if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze()
    path=dfs(m)
    textLabel(m,'node number : ',len(path)+1)
    t1=timeit(stmt='dfs(m)',number=1000,globals=globals())
    textLabel(m,'dfs Time',t1)
    a=agent(m,footprints=True)
    m.tracePath({a:path})
    
    m.run()

   
