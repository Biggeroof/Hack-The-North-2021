import queue
base, height = 0, 0
visited = []
def search(imageArray, startX, startY, endX, endY):
    #find the base and height of my array
    global base 
    base = len(imageArray)
    global height
    height = len(imageArray[0])
    #initailize the visited array, make it all 1e9, this array also doubles as a distance array
    global visited
    visited = [[1 for x in range(height)] for y in range(base)]
    #start my dfs
    visited[startX][startY] = 0
    return bfs(startX, startY, imageArray, endX, endY)
#   print("{}{}".format(len(visited) , len(visited[0])))
#     for i in visited:
#         print()
#         for y in i:
#             print(y, end="")
def bfs(startX, startY, imageArray, endX, endY):#'1' means white, '0' means black
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = len(imageArray)
    m = len(imageArray[0])
    dis = [[1e9 for x in range(m)] for y in range(n)]
    pre = [[-1 for x in range(m)] for y in range(n)]
    dis[startX][startY] = 0
    q = []
    q.append((startX,startY))
    while(len(q) > 0):
        x, y = q[0][0], q[0][1]
        q.pop(0)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            #if(new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and imageArray[new_x][new_y] == 1 and dis[new_x][new_y] > dis[x][y]+1 and check(new_x, new_y, imageArray)):
            if(new_x >= 0 and new_x < n and new_y >= 0 and new_y < m and imageArray[new_x][new_y] == 1 and dis[new_x][new_y] > dis[x][y]+1) :
                dis[new_x][new_y] = dis[x][y] + 1
                pre[new_x][new_y] = i
                q.append((new_x, new_y))
    
    path_len = dis[endX][endY]
    sequence = ""
    x = endX
    y = endY
    while(x!= startX or y!= startY):
        if(pre[x][y] == 0):
#             print("HERE")
            sequence += "L"
            x = x+1
        elif(pre[x][y] == 1):
            sequence += "L"
            y = y+1
        elif(pre[x][y] == 2):
            sequence += "R"
            x = x-1
        elif(pre[x][y] == 3):
            sequence += "D"
            y = y-1
        else:
            print("Impossible")
            exit()
    
#     print(sequence)
#     print(startX)
#     print(startY)
#     print(endX)
#     print(endY)
    return sequence
            
def check(x, y, imageArray):
    n = len(imageArray)
    m = len(imageArray[0])
    for i in range (max(0, x-2), min(n, x+2)):
        for j in range(max(0, y-2), min(m, y+2)):
            if(imageArray[i][j] == 0):
                return False
    return True