import itertools

MAX = 501

win = 0
draw = 0
defeat = 0
result_of_dice_roll = [0]*MAX
result_dice_a_table = [0]*MAX
result_dice_b_table = [0]*MAX

def gcd(a, b):

    if a < b:
        a,b = b,a

    while b > 0:
        a, b = b, a % b
    return a

def solution(dice):
    answer = []
    return answer

def calNumberOfCase(result_dice_a_table, result_dice_b_table):
    tmp_win = 0
    tmp_draw = 0
    tmp_defeat = 0
    
    for i in range(MAX):
        if result_dice_a_table[i] == 0:
            continue

        for j in range(MAX):
            if i < j:
                tmp_defeat += result_dice_a_table[i] * result_dice_b_table[j]
            elif i == j:
                tmp_draw += result_dice_a_table[i] * result_dice_b_table[j]
            else:
                tmp_win += result_dice_a_table[i] * result_dice_b_table[j]

    return tmp_win, tmp_draw, tmp_defeat

def rollDice(dice,number_of_roll, result_arr):

    if number_of_roll == 0:
        result_arr = []

    if number_of_roll == len(dice):

        result = sum(result_arr)
        result_of_dice_roll[result] += 1
            
        return True
        

    for num in dice[number_of_roll]:

        result_arr.append(num)
        rollDice(dice, number_of_roll + 1, result_arr)
        result_arr.pop()

def calWinningRate(pick_dice, number_of_dice):

    
    all_dice_index = list(range(number_of_dice))
    win_rate = {"denominator": 1, "numerator": 0}

    for dice_a in pick_dice:
        dice_b = tuple([value for value in all_dice_index if value not in dice_a])

        number_of_roll = 0
        result_of_dice_roll = [0]*501

        rollDice(dice_a, number_of_roll)
        result_dice_a_table = result_of_dice_roll

        del result_of_dice_roll
        result_of_dice_roll = [0] * MAX
        number_of_roll = 0

        rollDice(dice_b, number_of_roll)
        result_dice_b_table = result_of_dice_roll

        win, draw, defeat = calNumberOfCase(result_dice_a_table, result_dice_b_table)
        greatest_common_divisor = gcd(win_rate["denominator"], draw + defeat)

        lcm = win_rate["denominator"] * (draw+defeat) // greatest_common_divisor

        

def simulate(dice):
    number_of_dice = len(dice)
    pick_dice = itertools.combinations(range(number_of_dice), number_of_dice//2)

    calWinningRate(pick_dice, number_of_dice)



simulate([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])