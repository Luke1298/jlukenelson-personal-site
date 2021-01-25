import collections
from functools import reduce

def combinationWithReplacement(n, r):
    top = [i for i in range(1, n+r) if i>r] + [1, 1]
    bottom = [i for i in range(1,n)] + [1, 1]
    product = lambda z: reduce((lambda x, y: x * y), z)
    return  product(top)//product(bottom)



def getCheckoutPossibilitiesFor(x):
    count = 0
    pos_endings = [i*2 for i in range(1,21)] + [25*2]
    total_ways_to_score = collections.Counter(pos_endings + [i for i in range(1,21)] + [i*3 for i in range(1,21)] + [25])
    pos_endings = list(filter(lambda i: i<=x, pos_endings))
    for ending in pos_endings:
        remainder = x - ending
        if remainder == 0:
            count+=1
        if remainder in total_ways_to_score:
            count+=total_ways_to_score[remainder]
        possible_pairs = [(i, remainder-i) for i in range(1, (remainder//2 + 1))]
        for pair in possible_pairs:
            if (pair[0] in total_ways_to_score) and (pair[1] in total_ways_to_score):
                #combination with replacement
                if pair[0]==pair[1]:
                    #When the two values that we are trying to achieve are the same
                    #then it is possible to double count by just multiplying
                    #6 lends a great example of this -- letting our last throw be D1
                    #we have a remainder of 4 -- one way to get 4 is (2,2)
                    # When we have 2,2 we cannot multiply because that would lend:
                    # (D1, D1)
                    # (S2, D1)
                    # (S2, S2)
                    # (D1, S2) XX BUT WE DONT WANT TO COUNT THIS ONE -- this is where
                    # Combinations with replacement comes it -- it counts this instantly
                    num_to_add = combinationWithReplacement(total_ways_to_score[pair[0]],2)
                else:
                    num_to_add = total_ways_to_score[pair[0]]*total_ways_to_score[pair[1]]

                count+=num_to_add
    return count


if __name__ == '__main__':
    #VERIFY:
    print(getCheckoutPossibilitiesFor(6))
    print(sum([getCheckoutPossibilitiesFor(x) for x in range(171)]))
    #SOLVE:
    print(sum([getCheckoutPossibilitiesFor(x) for x in range(100)]))
