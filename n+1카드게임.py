""""
핵심 아이디어 현재 라운드까지 뽑은 카드뭉치 중에서 쓸지 버릴지만 판단단!!

1. 처음 시작하는 카드 뭉치에서 N+1을 만든다.
2. 1에서 불가능하다면, 추가적으로 뽑은 카드 중 1개를 사용하여 N+1을 만든다.
3. 2에서 불가능하다면, 추가적으로 뽑은 카드 2개를 이용하여 N+1을 만든다.
4. 3에서 불가능하다면, 다음 라운드로의 진행이 불가능하다.

링크: https://tech.kakao.com/posts/610
"""

from collections import deque

def solution(coin, cards):
    answer = simulate(coin,  cards)
    return answer

def get2Card(tmp, card_batch):

    for _ in range(2):
        if  card_batch:
            tmp.add(card_batch.popleft())
    
    
def checkEmpty(arr):
    if arr:
       return False
    else:
       return True

def simulate(coin, cards):
    round_num = 0
    n = max(cards)
    handle = set(cards[0:n//3])
    card_batch = deque(cards[n//3:])
    tmp = set()
    
    while True:
        is_be = False
        round_num += 1
        
        if checkEmpty(card_batch): #카드를 가져오기 전에 카드 뭉치가 비었는지 확인 -> 더 가져올 카드가 없으면 게임 종료료
            break

        get2Card(tmp, card_batch)

        for x in list(handle):
            if n+1 - x in handle:
                is_be = True

                handle.remove(x)
                handle.remove(n+1-x)
                break


        if is_be:
            continue

        for x in list(handle):
            if n+1 -x in tmp and coin >= 1:
                is_be = True

                handle.remove(x)
                tmp.remove(n+1-x)
                coin -= 1
                break

        if is_be:
            continue

        for x in list(tmp):
            if n+1 -x in tmp and coin >= 2:
                is_be = True

                tmp.remove(x)
                tmp.remove(n+1-x)
                coin -= 2
                break

        if is_be:
            continue
        else:
            break
        
    
    return round_num



print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))