from functools import wraps, reduce

def memoize(func):
    memo = {}

    @wraps(func)
    def memoizer(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoizer


def memoize_two(func):
    memo = {}

    @wraps(func)
    def memoizer(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]
    return memoizer

@memoize
def gen_increasing(d):
    # D is the number of digits
    if d==0:
        return 0
    elif d==1:
        return 10
    elif d==2:
        return 90
    elif d==3:
        return [(i, ((10 - i) * (11-i))//2) for i in range(1, 10)]
    else:
        former_increasing = gen_increasing(d-1)
        still_increasing = lambda lim: sum(map(lambda x: x[1], filter(lambda y: y[0]>=lim, former_increasing)))
        return [(i, still_increasing(i)) for i in range(1,10)]

@memoize_two
def gen_decreasing(d):
    # D is the number of digits
    if d==0:
        return 0
    elif d==1:
        return 10
    elif d==2:
        return 90
    elif d==3:
        return [(i, ((i+1) * (i+2))//2) for i in range(1, 10)]
    else:
        former_decreasing = gen_decreasing(d-1)
        still_decreasing = lambda lim: sum(map(lambda x: x[1], filter(lambda y: y[0]<=lim, former_decreasing))) + 1 ## Add 1 to include the "0"
        return [(i, still_decreasing(i)) for i in range(1,10)]

def gen_non_bouncy(d):
    # D is the number of digits
    if d==0:
        return 0
    if d==1:
        return 9
    elif d==2:
        return 90
    else:
        return sum(map(lambda x: x[1], gen_increasing(d))) + sum(map(lambda x: x[1], gen_decreasing(d))) - 9

def is_bouncy(x):
    digits = [int(d) for d in str(x)]
    s_digist = sorted(digits)
    return digits != sorted(digits) and digits != sorted(digits)[::-1]


def is_increasing(x):
    digits = [int(d) for d in str(x)]
    s_digist = sorted(digits)
    return digits == sorted(digits)

def is_decreasing(x):
    digits = [int(d) for d in str(x)]
    s_digist = sorted(digits)
    return digits == sorted(digits)[::-1]


if __name__ == '__main__':
    #print(sum([gen_non_bouncy(i) for i in range(11)]))
    print(sum([gen_non_bouncy(i) for i in range(101)]))
    #Verification
    # print(gen_non_bouncy(3))
    # print(sum([(not is_bouncy(x)) for x in range(10**2, 10**3)]))
    # print(gen_non_bouncy(4))
    # print(sum([(not is_bouncy(x)) for x in range(10**3, 10**4)]))
    # print(gen_non_bouncy(5))
    # print(sum([(not is_bouncy(x)) for x in range(10**4, 10**5)]))
    # print(gen_non_bouncy(6))
    # print(sum([(not is_bouncy(x)) for x in range(10**5, 10**6)]))
