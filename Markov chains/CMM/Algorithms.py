import numpy as np
import CMM
import sequenceCMM
import random
import sys



def MLEalgorithm(sequence):
    sequencewithoutlast = list(sequence)[:-1]
    n = [sequencewithoutlast.count(x) for x in sequence]
    P = np.arange([[transition(sequence, i, j) for i in range(0, sequence.a)] for j in range(0, sequence.A)])
    P = P/n
    for i in range(0, sequence.A):
        if n[i] == 0:
            P[i] = np.eye(sequence.A, 1, i)
    return P

def generateCMM(A, P, Pi, T=0):
    """
    Generate Markov Chain, using one-step transition matrix P and initial matrix Pi.
    :param A: (0,..,A) - set of values.
    :param P: one-step transition matrix.
    :param Pi: initial matrix.
    :param T: length of generated sequence.
    :return: list(sequence CMM)
    """
    csprng = random.SystemRandom()
    random_int = csprng.randint(0, sys.maxint)

def transition(sequence, i, j):
    return sum([1 for t in sequence.T-1 if sequence[t] == i and sequence[t+1] == j])

def bootstrap(sequence):
    #Maximum likehood estimation of transition matrix
    P_mle = MLEalgorithm(sequence)
