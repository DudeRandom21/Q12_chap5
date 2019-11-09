import random
def gen_test_cases(size, min_int, max_int):
    A = []
    for i in range(size):
        A.append(random.randint(min_int, max_int))
    return A

def findIndices(A):
    run_sum = 0
    curr_i = 0
    curr_j = 0

    curr_max = -100000
    best_i = 0
    best_j = 0

    for index, item in enumerate(A):
        run_sum += item
        curr_j = index + 1
        if run_sum < 0:
            run_sum = 0
            curr_i = index+1
            curr_j = index

        if run_sum > curr_max:
            curr_max = run_sum
            best_j = curr_j
            best_i = curr_i

        # print(run_sum)
        # print((curr_i, curr_j))
        # print((best_i, best_j))
    if curr_max > run_sum:
        return (best_i, best_j)
    else:
        return (curr_i, curr_j)

def n_square(A):
    lst = []
    for (i, j) in ((i, j) for i in range(len(X)) for j in range(len(X))):
        if i <= j:
            lst.append( (sum(A[i:j+1]), (i,j+1)) )
    return max(lst)[1]

def sum_by_index(A, ij):
    return sum(X[ij[0]:ij[1]])

for _ in range(1000):
    X = gen_test_cases(100, -100, 100)
    for item in X:
        if item > 0:
            break
    else:
        continue
    test = findIndices(X)
    good = n_square(X)
    if sum_by_index(X, test) != sum_by_index(X,good):
        print(X)
        print(test)
        print(good)
[-1, -4, -5, 2, -4]
# print(gen_test_cases(8, -5, 20))