from functools import wraps, reduce
import numpy as np


def memoize(func):
    memo = {}

    @wraps(func)
    def memoizer(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoizer

@memoize
def solve(d):
    # D is the number of digits
    if d==1:
        return 1
    elif d==2:
        return 1
    else:
        if (d%3 == 0):
            return solve(d-2) + solve(d-1)
        else:
            if (d//3)%2==1:
                return solve(d-2) + solve(d-1) + 1
            else:
                return solve(d-2) + solve(d-1) - 1

def make_number_island_size(x):
    t = 0
    while t<len(x):
        size=0
        while t<len(x) and x[t]:
            size+=1
            t+=1
        if size<3 and size>0:
            return False
        t+=1
    #print(x)
    return True


def gen_all_possible(line_size):
    i = np.array(np.indices(line_size * (2,))).reshape(line_size, -1)
    i = i[:, np.argsort(i.sum(0)[::-1], kind='mergesort')].T[::-1]
    return i


if __name__ == '__main__':
    #Verify
    for i in range(1, 15):
        print("N: {} - Predicted: {} - Actual: {}".format(i, solve(i), sum(np.apply_along_axis(make_number_island_size, 1, gen_all_possible(i)))))
    #From problem 115
    print("N:29, Predicted: {} - Actual: {}".format(solve(29), "673135"))
    print("N:30, Predicted: {} - Actual: {}".format(solve(30), "1089155"))
    print("N:50, Predicted: {}".format(solve(50)))
    pass
