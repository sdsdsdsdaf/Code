DIVISIOR = 10007

def solution(n, tops):
    answer = 0
    
    right_rhombus = [0] * (n+1)
    left_rhombus = [0] * (n+1) 

    right_rhombus[0] = 0
    left_rhombus[0] = 1

    for i in range(1, n+1):
        right_rhombus[i] =  (right_rhombus[i-1] + left_rhombus[i-1]) % DIVISIOR
        left_rhombus[i] = (right_rhombus[i-1] + right_rhombus[i-1] * tops[i-1] +
                           left_rhombus[i-1] * 2 + left_rhombus[i-1] * tops[i-1]) % DIVISIOR
        
    answer = (right_rhombus[i] + left_rhombus[i]) % DIVISIOR

    return answer 

solution(2, [0,1])