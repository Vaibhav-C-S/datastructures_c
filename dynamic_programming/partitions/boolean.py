MOD = 1000000007

def evaluate_expression(i, j, is_true, exp, memo):
    if i > j:
        return 0
    
    if i == j:
        if is_true:
            return 1 if exp[i] == 'T' else 0
        else:
            return 1 if exp[i] == 'F' else 0
    
    if memo[i][j][is_true] != -1:
        return memo[i][j][is_true]
    
    ways = 0
    for ind in range(i + 1, j, 2):
        l_t = evaluate_expression(i, ind - 1, 1, exp, memo)
        l_f = evaluate_expression(i, ind - 1, 0, exp, memo)
        r_t = evaluate_expression(ind + 1, j, 1, exp, memo)
        r_f = evaluate_expression(ind + 1, j, 0, exp, memo)

        if exp[ind] == '&':
            if is_true:
                ways = (ways + l_t * r_t) % MOD
            else:
                ways = (ways + l_f * r_t + l_t * r_f + l_f * r_f) % MOD
        elif exp[ind] == '|':
            if is_true:
                ways = (ways + l_f * r_t + l_t * r_f + l_t * r_t) % MOD
            else:
                ways = (ways + l_f * r_f) % MOD
        else:  # XOR operator
            if is_true:
                ways = (ways + l_f * r_t + l_t * r_f) % MOD
            else:
                ways = (ways + l_f * r_f + l_t * r_t) % MOD
    
    memo[i][j][is_true] = ways
    return ways

def evaluate_exp(exp):
    n = len(exp)
    memo = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    return evaluate_expression(0, n - 1, 1, exp, memo)

exp = "F|T^F"
ways = evaluate_exp(exp)
print("The total number of ways:", ways)
