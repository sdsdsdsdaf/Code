ROW = 0
COL = 1
MAX_ROW = 101
MAX_COL = 101
MIN_ROW = 1
MIN_COL = 1

def getMaxLenInMatrix(matrix):
    max_len = -1
    
    for col in matrix:
        max_len = len(col) if max_len < len(col) else max_len

    return max_len 

def getTotalCollision(points, routes):

    robot_routes = []
    result = 0

    for route in routes:
        robot_routes.append(findCourse(points, route))
    
    for time in range(getMaxLenInMatrix(robot_routes)):
        result += countNumberOfCollisionInSametime(robot_routes, time)

    return result

def countNumberOfCollisionInSametime(routes, time):
    collison_points = []
    same_time_postion = []
    
    for i in range(len(routes)):
        if len(routes[i]) > time:
            same_time_postion.append(routes[i][time])
 

    for i, position in enumerate(same_time_postion):
        same_time_postion.pop(i)
        
        if position in same_time_postion and not position in collison_points:
            collison_points.append(position)

        same_time_postion.insert(i, position) #원상복귀


    return len(collison_points)

def findCourse(points, route_per_robot):
    result = [points[route_per_robot[0] - 1]] #처음 노드 저장

    for i in range(len(route_per_robot) - 1):
        points_start = points[route_per_robot[i] - 1]
        points_end = points[route_per_robot[i+1] - 1]

        result.extend(findShortestPathBetweenTwoPoints(points_start, points_end))

    return result

def findShortestPathBetweenTwoPoints(points_start, points_end): #이 경우에는 장애물이 없으므로 bfs 대신 맨해튼 거리(그리드)를 이용할 수 있다.
    
    route = []
    move_row = points_end[ROW] - points_start[ROW]
    move_col = points_end[COL] - points_start[COL]
    
    new_row = points_start[ROW]
    new_col = points_start[COL]

    for i in range(1, abs(move_row)+1): #R좌표 먼저 움직임
        
        new_row = points_start[ROW] +  i * ( 1 if move_row >=0  else -1)
        route.append([new_row, new_col])
        

    for i in range(1, abs(move_col)+1):

        new_col = points_start[COL] + i * (1 if move_col >= 0 else -1)
        route.append([new_row, new_col])

    return route


def solution(points, routes):
    answer = getTotalCollision(points, routes)
    return answer

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [4, 2], [4, 3]]
print(solution(points, routes))

