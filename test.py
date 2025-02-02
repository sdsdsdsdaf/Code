list_a = [1,2,3,4,5,6]
list_b = [1,1,4,4,5,5]
res_arr = [0] * 501

for a in list_a:
    for b in list_b:

        res_arr[a+b] += 1

print(res_arr)

{"denominator": 1, "numerator": 0}


greatest_common_divisor = gcd(win_rate["denominator"], win + draw + defeat)

        lcm = win_rate["denominator"] * (win + draw + defeat) // greatest_common_divisor

        if win_rate["numerator"] * (lcm // win_rate["denominator"]) < win * (lcm //(win + draw + defeat)):
            win_rate["numerator"] = win
            win_rate["denominator"] = draw + defeat + defeat