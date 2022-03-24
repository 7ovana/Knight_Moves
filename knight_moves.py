import numpy as np

def kn(start, N):
    if start == 5:
        if N == 0:
            return 1
        return 0
    
    if N==0:
        return 1
    markov = np.array([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]], dtype = object)
    res = np.eye(10, dtype = object)
    while N > 1:
        if N & 1:
            res = res@markov
        markov = markov@markov
        N >>= 1
    return np.sum(res@markov[start])

if __name__ == '__main__':
    print(kn(2,100000))
