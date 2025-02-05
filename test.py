from collections import deque

def solution(coin, cards):
    answer = simulate(coin,  cards)
    return answer

def checkEmpty(card_batch):
    return not card_batch

def getCards(draw, card_batch , n =2):

    for _ in range(n):
        if not checkEmpty(card_batch):
            draw.add(card_batch.popleft())
    

def simulate(coin , cards):
    n = max(cards)
    mine = set(cards[:len(cards)//3])
    draw = set()
    card_batch = deque(cards[len(cards)//3:])
    is_be = False
    round_num = 0

    while True:
        round_num += 1
        is_be = False

        if checkEmpty(card_batch):
            break
        getCards(draw, card_batch)

        for x in list(mine): #코인을 한개도 소모하지 않는 경우
            if n+1-x in mine:
                is_be = True

                mine.remove(x)
                mine.remove(n+1-x)
                break

        if is_be:
            continue

        for x in list(mine):
            if n+1-x in draw and coin >= 1:
                is_be = True
                coin -= 1

                mine.remove(x)
                draw.remove(n+1-x)
                break
        if is_be:
            continue

        for x in list(draw):
            if n+1-x in draw and coin >= 2:
                is_be = True
                coin -= 2

                draw.remove(x)
                draw.remove(n+1-x)
                break


        if not is_be:
            break

    return round_num

solution(	2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])