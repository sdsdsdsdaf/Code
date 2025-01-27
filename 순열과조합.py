#1. 재귀를 이용한 구현 - 원소를 하나씩 뽑아서 수열을 구성하고 출력

#1-1재귀이용
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()


    generate([], used)


#1-2 반복문 이용
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

#1-3 제너레이터 이용
def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next

#2-1 (조합) 재귀이용
def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

#2-2 제너레이터 이용
def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

                import itertools
""""
    pool = ['A', 'B', 'C']
    import itertools
    pool = ['A', 'B', 'C']
    print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
    print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
    print(list(map(''.join, itertools.combinations(pool,2)))) # 2개의 원소로 수열 만들기

"""


for arr in permutations_2([1,2,3,4], 3):
    print(arr)