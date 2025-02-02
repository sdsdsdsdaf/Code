""""
핵심 아이디어 현재 라운드까지 뽑은 카드뭉치 중에서 쓸지 버릴지만 판단단!!

1. 처음 시작하는 카드 뭉치에서 N+1을 만든다.
2. 1에서 불가능하다면, 추가적으로 뽑은 카드 중 1개를 사용하여 N+1을 만든다.
3. 2에서 불가능하다면, 추가적으로 뽑은 카드 2개를 이용하여 N+1을 만든다.
4. 3에서 불가능하다면, 다음 라운드로의 진행이 불가능하다.
"""

from collections import deque

def solution(coin, cards):
    answer = simulate(coin,  cards)
    return answer

def get2Card(tmp, card_batch):
    for _ in range(2):
        if not card_batch:
            tmp.add(card_batch.popleft())

def simulate(coin, cards):
    round_num = 1
    n = max(cards)
    handle = set(cards[0:n//3])
    card_batch = deque(cards[n//3:])
    tmp = set()

    while True:
        is_be = False
        get2Card(tmp, card_batch)

        for x in list(handle):
            if n+1-x in handle:
                
                handle.remove(x)
                handle.remove(n+1-x)
                round_num += 1
                is_be = True
            
            elif not(n+1 == sum(tmp)): #1장만으로 가능함
                if n+1-x in (tmp | handle) and coin > 0:
                    
                    handle.remove(x)
                    tmp.remove(n+1-x) #굳이 하지 않아도 상관은 없음
                    coin -= 1
                    round_num += 1
                    is_be = True
            else:
                if n+1 == sum(tmp):
                    coin -= 2
                    round_num += 1
                    is_be = True

        
                
            

        if not card_batch or not is_be:
            break


    return round_num

solution(4,	[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])