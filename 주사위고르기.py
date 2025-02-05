import itertools

MAX = 501

win = 0
draw = 0
defeat = 0
result_dice_a_table = [0]*MAX
result_dice_b_table = [0]*MAX


def solution(dice):
    answer = simulate(dice)
    return answer

def gcd(a, b):

    if a < b:
        a,b = b,a

    while b > 0:
        a, b = b, a % b
    return a

def calNumberOfCase(result_dice_a_table, result_dice_b_table):
    win = 0
    draw = 0
    defeat = 0
    
    for i in range(MAX):
        if result_dice_a_table[i] == 0:
            continue

        win += result_dice_a_table[i] * sum(result_dice_b_table[0:i])
        draw += result_dice_a_table[i] * result_dice_b_table [i]
        defeat += result_dice_a_table[i] * sum(result_dice_b_table[i+1 : MAX])
        
    return win, draw, defeat

def rollDice(dice_index,number_of_roll, dice):
    global result_arr

    if number_of_roll == 0:
        result_arr = []

    if number_of_roll == len(dice_index):

        result = sum(result_arr)
        result_of_dice_roll[result] += 1
            
        return True
        

    for num in dice[dice_index[number_of_roll]]:

        result_arr.append(num)
        rollDice(dice_index, number_of_roll + 1, dice)
        result_arr.pop()

def calWinningRate(pick_dice, number_of_dice, dice):

    
    all_dice_index = list(range(number_of_dice))
    win_rate = {"denominator": 1, "numerator": 0}
    result = ()
    global result_of_dice_roll

    for dice_a in pick_dice:
        dice_b = tuple([value for value in all_dice_index if value not in dice_a])

        number_of_roll = 0
        result_of_dice_roll = [0]*MAX

        rollDice(dice_a, number_of_roll, dice)
        result_dice_a_table = result_of_dice_roll

        result_of_dice_roll = [0] * MAX
        number_of_roll = 0

        rollDice(dice_b, number_of_roll, dice)
        result_dice_b_table = result_of_dice_roll

        win, draw, defeat = calNumberOfCase(result_dice_a_table, result_dice_b_table)

        greatest_common_divisor = gcd(win_rate["denominator"], win + draw + defeat)

        lcm = win_rate["denominator"] * (win + draw + defeat) // greatest_common_divisor

        if win_rate["numerator"] * (lcm // win_rate["denominator"]) < win * (lcm //(win + draw + defeat)):

            greatest_common_divisor = gcd(win, win + draw + defeat)

            win_rate["numerator"] = win // greatest_common_divisor
            win_rate["denominator"] = (draw + defeat + win) // greatest_common_divisor

            result = dice_a

    return result

        

def simulate(dice):

    number_of_dice = len(dice)
    pick_dice = itertools.combinations(range(number_of_dice), number_of_dice//2)
    
    result = list(calWinningRate(pick_dice, number_of_dice, dice))
    for i in range(len(result)):
        result[i] += 1

    return result


print(simulate([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))