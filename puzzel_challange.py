def solution(diffs, times, limit):
    return binSearch(diffs, times, limit)

def linearSearch(diffs, times, limit):
    
    result = -1

    for level in range(1, limit + 1):
        total = totalTime(diffs, times, level)
        result = level

        if total <= limit:
            break

    return result


def binSearch(diffs, times, limit):
    left = 1
    right = max(diffs)
    mid = (left+right)//2
    result = mid
    
    while left <= right:
        total = totalTime(diffs, times, mid)

        if total > limit:
            left = mid + 1
            

        if total < limit:
            right = mid - 1
            result = mid

        if total == limit:
            return mid

        mid = (left+right) // 2

    answer = result
    return answer

def totalTime(diffs, times, level):
    prev_time = 0
    total = 0

    for i in range(len(diffs)):
        total += stage_time(diffs[i], prev_time, times[i], level)
        prev_time = times[i]

    return total

def stage_time(diffs, prev_time, time_cur, level):
    time = -1
    if 0 <= diffs <= level:
        time = time_cur
    elif diffs > level:
        time = (time_cur+prev_time) * (diffs-level) + time_cur
    else:
        pass
    return time
