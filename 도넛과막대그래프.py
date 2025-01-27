OUTPUT = 0
INPUT = 1

def solution(edges):
    answer = []

    edges_count = checkNumberOfEdgesPerNode(edges)
    answer = checkAnswer(edges_count)

    return answer
    

def checkNumberOfEdgesPerNode(edges):
    edges_count = {}

    for edge in edges:
        if not edges_count.get(edge[0]):
            edges_count[edge[0]] = [0,0] #[ a번 노드에서 나가는 간선의 수, a번 노드로 들어오는 간선의 수 ]
        
        if not edges_count.get(edge[1]):
            edges_count[edge[1]] = [0,0]

        edges_count[edge[0]][OUTPUT] += 1
        edges_count[edge[1]][INPUT] += 1

    return edges_count 



def checkAnswer(edge_count):

    answer = [0, 0, 0, 0]

    for key, counts in edge_count.items():

        if counts[OUTPUT] >= 2 and counts[INPUT] == 0: #생성된 노드
            answer[0] = key
        
        elif counts[OUTPUT] == 0 and (counts[INPUT] == 1 or counts[INPUT] == 2): #막대 모양 그래프의 맨끝부분 찾기 input이 1이거나 
            answer[2] += 1
        
        elif counts[OUTPUT] >= 2 and counts[INPUT] >= 2: #8자 모양 그래프의 중간 노드 찾기 
            answer[3] += 1
        
    answer[1] = (edge_count[answer[0]][OUTPUT] - answer[2] - answer[3]) #생성된 노드와 연결된 노드 중 막대모양과 8자 모양을  제외하면 남는 노드가 바로 도넛 모양의 개수 

    return answer
