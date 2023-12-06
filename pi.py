import decimal

def calc_pi(decimals=1000):
    # Set precision decimal calculations
    decimal.getcontext().prec = decimals + 1

    # Chudnovsky algorithm
    C = 426880 * decimal.Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, decimals):
        M = (K ** 3 - 16 * K) * M // i ** 3 
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C / S
    return str(pi)

# Calculate Pi > specified decimal places
pi_decimals = calc_pi(x)  # Change "x" by number decimal you want
print(pi_decimals)
