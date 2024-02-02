import random, time, threading
import numpy as np
import os



def printMaze():
    global pos,facing,maze
    for row in maze:
        for cell in row:
            if cell == 1:
                print("||", end="")
            elif cell == 2:
                if facing==0:
                    print(">>", end="")
                elif facing==1:
                    print("VV", end="")
                elif facing==2:
                    print("<<", end="")
                else:
                    print("^^", end="")
            elif cell == 3:
                print("X", end="")
            else:
                print("  ", end="")
        print("")


def generateMaze(h, w):
    global maze
    maze = np.ones((h, w), dtype=int)

    # Zufälligen Eingang wählen
    entry = (random.randrange(1, h - 2, 2), 1)
    maze[entry] = 0
    maze[entry[0]][0] = 0

    stack = [entry]

    while stack:
        x, y = stack[-1]

        # Nachbarn
        neighbors = [
            (x, y + 2),
            (x, y - 2),
            (x + 2, y),
            (x - 2, y),
        ]

        unvisited_neighbors = [
            (nx, ny) for nx, ny in neighbors
            if 0 < nx < h-1 and 0 <= ny < w and maze[nx, ny] == 1
        ]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[(x + nx) // 2, (y + ny) // 2] = 0
            maze[nx, ny] = 0
            stack.append((nx, ny))
        else:
            stack.pop()       


    # Ausgang generieren
    exit = (random.randint(1, h - 2), w - 1)
    while not(maze[exit[0]][w-2]==0):
        exit = (random.randint(1, h - 2), w - 1)
    maze[exit] = 0
    return entry, maze


# Löscht alle 100ms das Maze und gibt Maze mit aktueller Playerposition aus
def animate():
    global facing, maze
    os.system('cls' if os.name=='nt' else 'clear')
    printMaze()
    time.sleep(0.1)


def turnRight():
    global facing,stop
    facing  = (facing+1)%4
    animate()


def turnLeft():
    global facing, stop
    facing = (facing-1)%4
    animate()



def blocked():
    global facing, stop
    if not stop:
        if facing==0:
            return maze[pos[0],pos[1]+1]==1
        elif facing==1:
            return maze[pos[0]+1,pos[1]]==1
        elif facing==2:
            return maze[pos[0],pos[1]-1]==1
        else:
            return maze[pos[0]-1,pos[1]]==1


def step():
    global pos, facing

    maze[pos] = 0
    if facing==0:
        pos = pos[0],pos[1]+1
    elif facing==1:
        pos = pos[0]+1,pos[1]
    elif facing==2:
        pos = pos[0],pos[1]-1
    else:
        pos = pos[0]-1,pos[1]

    if maze[pos] == 1:
        maze[pos] = 3
        animate()
        print("Autsch! Du gegen eine Wand gelaufen.")
        os._exit(0)
    elif pos[1] == np.shape(maze)[1]-1:
        stop = 1
        maze[pos] = 2
        animate()
        print("Du bist entkommen!")
        os._exit(0)
    else:
        maze[pos] = 2
        animate()


    

def start(func, h, w):
    global pos, facing, maze, stop
    stop = False
    pos = 0,0
    facing = 0
    maze = np.ones((2, 2), dtype=int)
    if h<4 or w<4:
        print("Das Labyrinth muss mindestens 4x4 groß sein")
    if h%2==0:
        h+=1
    if w%2==0:
        w+=1
    entry, maze = generateMaze(h,w)
    pos = (entry[0],0)
    maze[pos] = 2


    # Startet das Programm der Schülerinnen
    func()

