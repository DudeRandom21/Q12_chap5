import random
def gen_test_cases(size, min_int, max_int):
    A = []
    for i in range(size):
        A.append(random.randint(min_int, max_int))
    return A

def findIndices(A):
    diff = 0
    i = 0
    j = 0
    sumit = 0
    for k in range(1, len(A)):
        if diff + A[k] >= 0:
            j = k
            diff = 0
            sumit = sumit + A[k] + diff
        else:
            diff = diff + A[k]
    diff = 0
    for k in range(0, j):
        if diff + A[k] <= 0:
            i = k+1
            diff = 0
            sumit = sumit - diff - A[k]
        else:
             diff = diff + A[k]
    return (i, j)

def n_square(A):
    lst = []
    for (i, j) in ((i, j) for i in range(len(X)) for j in range(len(X))):
        if i <= j:
            lst.append( (sum(A[i:j+1]), (i,j)) )
    return max(lst)[1]

def sum_by_index(A, ij):
    return sum(X[ij[0]:ij[1]])

# for _ in range(100):
#     X = gen_test_cases(5, -5, 5)
#     test = findIndices(X)
#     good = n_square(X)
#     if sum_by_index(X, test) != sum_by_index(X,good):
#         print(X)
#         print(test)
#         print(good)
#[-1, -4, -5, 2, -4]
print(gen_test_cases(8, -5, 20))