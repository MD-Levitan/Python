import numpy as np
import math
import sequenceHMM as sH
import HMM

def forwardalgorithm_HMM(sequence):
    if sequence.HMM == None:
        raise Exception("Error. HMM is not identified.")

    alpha = [sequence.HMM.C[j][sequence.sequence[0]]*sequence.HMM.Pi[j] for j in range(0, sequence.A)]
    alphaset = [alpha]
    for t in range(1, sequence.T):
        alphat = [sequence.HMM.C[j][sequence.sequence[t]]*sum(sequence.HMM.P[i][j] for i in range(0, sequence.A))*alphaset[t-1][j] for j in range(0, sequence.A)]
        alphaset.extend([alphat])
    return alphaset

def backwardalgorithm_HMM(sh):
    sequence = (sh)
    if sequence.HMM == None:
        raise Exception("Error. HMM is not identified.")

    beta = [1]*sequence.A
    betaM = [beta]
    for t in range(sequence.T-1, 0, -1):
        betat = [sum(sequence.HMM.P[i][j]*sequence.HMM.C[j][sequence.sequence[sequence.T-t-1]] for i in range(0, sequence.A))*betaM[sequence.T-t-1][j] for j in range(0, sequence.A)]
        betaM.extend([betat])
    betaM.reverse()
    return betaM

def estimationsequenceforward(sequence, alphaset):
    return sum(alphaset[sequence.T - 1][j] for j in range(0, sequence.A))


def estimationsequenceforward_backawrd(sequence, alphaset, betaset):
    estimation = [sum(alphaset[i][j]*betaset[i][j] for j in range(0, sequence.A)) for i in range(0, sequence.T)]
    return estimation

def doubleprobability(sequence, alphaset, betaset):
    """
    Conjoint probability of 2 successful hidden state.
    :param sequence: hidden sequence which we estimate.
    :param alphaset: coefficients from forward algorithm.
    :param betaset: coefficients from backward algorithm.
    :return: KsiSet has 3 dimension: 1-st - for t=1,.., T-1
                                2-nd - for i in A
                                3-d - for j in A.
    """
    ksiset = np.zeros((sequence.T-1, sequence.A, sequence.A))
    P = sequence.HMM.P
    C = sequence.HMM.C
    seq = sequence.sequence
    estimation = estimationsequenceforward(sequence, alphaset)
    for t in range(0, sequence.T-1):
        ksiset[t] = np.array([[alphaset[t][j]*P[i][j]*C[j][seq[t+1]]*betaset[t+1][j]/estimation
                             for i in range(0, sequence.A)] for j in range(0, sequence.A)])
    return ksiset

def marginalprobability(sequence, alphaset, betaset):
    """
    Marginal probability hidden state.
    :param sequence: hidden sequence which we estimate.
    :param alphaset: coefficients from forward algorithm.
    :param betaset: coefficients from backward algorithm.
    :return: gammaSet has 2 dimension: 1-st - for t=1,.., T-1
                                2-nd - for i in A.
    """
    gammaset = np.zeros((sequence.T - 1, sequence.A))
    estimation = estimationsequenceforward(sequence, alphaset)
    gammaset = np.array([[alphaset[t][i]*betaset[t][i]/estimation
                          for t in range(0, sequence.T-1)] for i in range(0, sequence.A)])
    return gammaset

def estimationinitialprobability(sequence):
    """
    Estimation of initial probability(PI), using forward-backward algorithm.
    :param sequence: hidden sequence which we estimate.
    :return: estimated array PI.
    """
    alphaset = forwardalgorithm_HMM(sequence)
    betaset = backwardalgorithm_HMM(sequence)
    gammaset = marginalprobability(sequence, alphaset, betaset)
    return gammaset[0]

def estiamtionmatrixofprobability(sequence):
    """
    Estimation of matrix of probability(P), using forward-backward algorithm.
    :param sequence: hidden sequence which we estimate.
    :return: estimated matrix P.
    """
    alphaset = forwardalgorithm_HMM(sequence)
    betaset = backwardalgorithm_HMM(sequence)
    gammaset = marginalprobability(sequence, alphaset, betaset)
    ksiset = doubleprobability(sequence, alphaset, betaset)
    P = np.array([[sum(ksiset[t][i][j]/ gammaset[t][i] for t in range(0, sequence.T -1))
                   for i in range(0, sequence.A)] for j in range(0, sequence.A)])
    return P

def estiamtiontransitionmatrix(sequence):
    """
    Estimation of transition matrix(C), using forward-backward algorithm.
    :param sequence: hidden sequence which we estimate.
    :return: estimated transition matrix C.
    """
    alphaset = forwardalgorithm_HMM(sequence)
    betaset = backwardalgorithm_HMM(sequence)
    gammaset = marginalprobability(sequence, alphaset, betaset)
    C = np.array([[sum(gammaset[t][i]/gammaset[t][i]
                    for t in range(0, sequence.T -1) if sequence.sequnce[t] == j)
                    for i in range(0, sequence.A)] for j in range(0, sequence.A)])
    return C


a=sH.sequenceHMM()
b=HMM.HMM()
print(b)
a.setHMM(b)
print(a)
alpha = forwardalgorithm_HMM(a)
beta = backwardalgorithm_HMM(a)

print(estimationsequenceforward(a, alpha))
print(estimationsequenceforward_backawrd(a, alpha, beta))
