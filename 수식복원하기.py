def solution(expressions):
    answer = []
    math_exp_list = []
    math_exp_list_X = []
    X_list = []
    
    for expression in expressions:
        math_exp_list.append(expression.split())

    max_digit_in_expres = findMaxDigit(math_exp_list)
    possible_digit_scale_list = findCorrectDigitScale(math_exp_list, max_digit_in_expres) 
    X_list = findX(math_exp_list, possible_digit_scale_list)

    for math_exp in math_exp_list:
        if "X" in math_exp:
            math_exp_list_X.append(math_exp)

    for i, math_exp in enumerate(math_exp_list_X):
        math_exp[-1] = X_list[i]
        answer.append(' '.join(math_exp))


    return answer

def findX(math_exp_list, possible_digit_scale_list):
    math_exp_list_X = []
    result = []

    for math_exp in math_exp_list:
        if "X" in math_exp:
            math_exp_list_X.append(math_exp)

    for math_exp_x in math_exp_list_X:
        possible_x_set = set()
        
        for possible_digit_scale in possible_digit_scale_list:
            possible_x_set.add(calculateResult(possible_digit_scale, math_exp_x))

        if len(possible_x_set) == 1:
            result.append(possible_x_set.pop())

        else:
            result.append("?")

    return result
        

def calculateResult(N, math_exp_x):

    if math_exp_x[1] == "+":
        return decimalToN_DigitScale(N, nDigitToDecimal(N, math_exp_x[0]) + nDigitToDecimal(N, math_exp_x[2]))
    elif math_exp_x[1] == "-":
        return decimalToN_DigitScale(N, nDigitToDecimal(N, math_exp_x[0]) - nDigitToDecimal(N, math_exp_x[2]))
    else:
        print("It`s wrong")

def decimalToN_DigitScale(N,digits):

    if type(digits) == type("string"):
        temp = []
        for digit in digits:
            temp.append(int(digit))

        digits = temp[:]
        number = 0
        for digit in digits:
            number = number*10 + digit
    else:
        number = digits

    result = str()

    if number == 0:
        result += '0'
        return result

    while number > 0:
        result += str(number%N)
        number = number//N

    result = result[::-1]

    return result


def findCorrectDigitScale(math_exp_list, min_digit_scale):

    math_exp_list_non_X = []
    possible_digit_scale_list = []

    for math_exp in math_exp_list:
        if not "X" in math_exp:
            math_exp_list_non_X.append(math_exp)

    for N in range(min_digit_scale+1, 10):
        if calculate_N_digitScale(N, math_exp_list_non_X):
            possible_digit_scale_list.append(N)

    return possible_digit_scale_list
        
def calculate_N_digitScale(N, math_exp_non_X_list):

    for math_exp_non_x in math_exp_non_X_list:
        if math_exp_non_x[1] == "+":
            if (
                nDigitToDecimal(N, math_exp_non_x[0]) + nDigitToDecimal(N, math_exp_non_x[2])
                != nDigitToDecimal(N, math_exp_non_x[4])
                ):
                return False
        
        if math_exp_non_x[1] == "-":
            if (
                nDigitToDecimal(N, math_exp_non_x[0]) - nDigitToDecimal(N, math_exp_non_x[2])
                != nDigitToDecimal(N, math_exp_non_x[4])
                ):
                return False
            
    
    return True




def nDigitToDecimal(N, digits):
    result = 0

    if type(digits) == type("string"):
        temp = []
        for digit in digits:
            temp.append(int(digit))

        digits = temp[:]

    for digit in digits:
        result = result * N +digit

    return result

def findMaxDigit(expression_list):
    digit_set = set()
    digit_set.add(1) #2진법부터 시작이기에 1까지는 가능
    for exp in expression_list:
        for digits in exp[0:5:2]: #숫자부분만 뽑기
            for digit in digits:
                if digits == 'X':
                    continue
                
                digit_set.add(int(digit))

    return max(digit_set)

      