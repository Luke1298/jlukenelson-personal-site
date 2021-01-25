
import math

p_squares = [i**2 for i in range(1000)]

def find_solutions(p):
    solutions = []
    for ab in range(1, p-1):
        for bc in range(ab, (p-ab)/2):
            if ab**2+bc**2 in p_squares and ab+bc+int(math.sqrt(ab**2+bc**2)) == p:
                solutions.append((ab, bc, int(math.sqrt(ab**2+bc**2))))
    return solutions
    



print max([(i, len(find_solutions(i))) for i in range(1000)], key=lambda x: x[1])