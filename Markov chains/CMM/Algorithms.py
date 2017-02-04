import numpy as np
import CMM
import sequenceCMM
import random

def MLEalgorithm(sequence):
    """
    Algorithm that calculates maximum likehood estimation of one-step transition matrix.
    :param sequence: sequence of elements in range (0, A). Can be instance of sequenceCMM class, but if not, then it
    will be transformed in such instance.
    :return: Maximum likehood estimation of one-step transition matrix - it's a matrix of size AxA.
    """
    np.seterr(divide='ignore', invalid='ignore')
    if not isinstance(sequence, sequenceCMM.sequenceCMM):
        sequence = sequenceCMM.sequenceCMM(sequence)
    n = np.array([list(sequence.sequence)[:-1].count(x) for x in range(0, sequence.A)])
    n.shape = (sequence.A, 1)
    P = np.array([[transition(sequence, i, j) for j in range(0, sequence.A)] for i in range(0, sequence.A)])
    P = P/n
    for i in range(0, sequence.A):
        if n[i] == 0:
            eye = np.eye(sequence.A, 1, i)
            eye.shape = sequence.A
            P[i] = eye
    return P

def transition(sequence, i, j):
    return sum([1 for t in range(0, sequence.T-1) if sequence.sequence[t] == i and sequence.sequence[t+1] == j])

def choosenumber(array):
    csprng = random.SystemRandom()
    random_double = csprng.randint(0, 1000) / 1000
    arraywithnum = list(zip([x for x in range(0, len(array))], array))
    for counter in range(0, len(array)):
        if random_double <= sum(x[1] for x in arraywithnum[:counter+1]) \
                or (1 <= random_double and 1 <= sum(x[1] for x in arraywithnum[:counter+1])):
            return arraywithnum[counter][0]

def generateCMM(Pi, P, T):
    """
    Generate Markov Chain, using one-step transition matrix P and initial matrix Pi.
    :param P: one-step transition matrix.
    :param Pi: initial matrix.
    :param T: length of sequence.
    :return: sequence CMM.
    """
    initial_val = choosenumber(Pi)
    counter = choosenumber(P[initial_val])
    sequence = [initial_val, counter]
    for i in range(0, T-2):
        counter = choosenumber(P[counter])
        sequence.append(counter)
    return sequence

def bootstrap(sequence, M=1000):
    """
    Bootstrap algorithm which calculates one-step transition matrix, using bootstrap sequences, that is generated, using
    MLE of one-step transition matrix.
    :param sequence: sequence of elements in range (0, A). Can be instance of sequenceCMM class, but if not, then it
    will be transformed in such instance.
    :return: one-step transition matrix.
    """
    Pi_mle = np.array([0.2, 0.6, 0.2])
    P_mle = MLEalgorithm(sequence)
    randominstance = random.SystemRandom()
    bootstraps = [generateCMM(Pi_mle, P_mle, randominstance.randint(50, 256)) for x in range(0, M)]
    bootstrappedP = [MLEalgorithm(x) for x in bootstraps]
    averageP = sum(bootstrappedP)/M
    return averageP


cmm = CMM.CMM()
print(cmm)
sequence = generateCMM(cmm.Pi, cmm.P, 5)
print(sequence)
print(MLEalgorithm(sequence))
# a = bootstrap(sequence)
# print(a)