from functools import wraps


CAP = 10000000

def memoize(func):
    memo = {(1,): 1, (89,): 89}

    @wraps(func)
    def memoizer(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoizer


@memoize
def square_digit_chain(n):
    next = sum([int(c)**2 for c in str(n)])
    if not (next == 1 or next == 89):
        return square_digit_chain(next)
    return next


c = 0
for j in range(1, CAP+1):
    if square_digit_chain(j) == 89:
        c+=1

print c
