import numpy as np
import math
import sequenceHMM as sH
import HMM

def forwardalgorithm_HMM(sh):
    sequence = (sh)
    if sequence.HMM == None:
        raise Exception("Error. HMM is not identified.")

    alpha = [sequence.HMM.C[j][sequence.sequence[0]]*sequence.HMM.Pi[j] for j in range(0, sequence.A)]
    alphaM = [alpha]
    for t in range(1, sequence.T):
        alphat = [sequence.HMM.C[j][sequence.sequence[t]]*sum(sequence.HMM.P[i][j] for i in range(0, sequence.A))*alphaM[t-1][j] for j in range(0, sequence.A)]
        alphaM.extend([alphat])

    return  alphaM

def asd():
    sum(alphaM[sequence.T - 1][j] for j in range(0, sequence.A))

def backwardalgorithm_HMM(sh):
    sequence = (sh)
    if sequence.HMM == None:
        raise Exception("Error. HMM is not identified.")
    beta = 1
    betaM = [beta]
    for t in range(sequence.T-1,0,-1):
        betat = [sum(sequence.HMM.P[i][j]*sequence.HMM.C[j][sequence.sequence[sequence.T-t-1]] for i in range(0, sequence.A))*betaM[sequence.T-t-1][j] for j in range(0, sequence.A)]
        betaM.extend([betat])
    return betaM

a=sH.sequenceHMM()
b=HMM.HMM()
print(b)
a.setHMM(b)
print(a)
print(forwardalgorithm_HMM(a))