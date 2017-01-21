import numpy as np


class HMM:
    def __init__(self, N, M, Pi, P, C):
        self.N = N
        self.M = M
        self.Pi = Pi
        self.P = P
        self.C = C

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.P = np.eye(N, dtype=float)
        self.Pi = np.eye(N, 1, dtype=float)
        self.C = np.eye(N, M, dtype=float)

    def __init__(self, name_file="HMM.txt"):
        self.initfromfile(name_file)


    def initfromfile(self, name_file):
        """ Initilization from fyle "name_file"
            First line: N M
            Second line: Pi (transposed)
            Then matrix P (NxN) and C (NxM).
            Elements of Pi, P, C are from [0,1].
        """
        file = open(name_file, mode='r')
        self.N = int(file.read(1))
        file.read(1)
        self.M = int(file.read(1))
        file.readline()
        self.Pi = np.array([float(x) for x in file.readline().split(" ") if not x.isalpha()])
        self.P = np.zeros((self.N, self.N), dtype=float)
        self.C = np.zeros((self.N, self.M), dtype=float)
        for i in range(0, self.N):
            self.P[i] = np.array([float(x) for x in file.readline().split(" ") if not x.isalpha()])

        for i in range(0, self.M):
            self.C[i] = np.array([float(x) for x in file.readline().split(" ") if not x.isalpha()])

    def __str__(self, ):
        return "Pi: "+str(self.Pi)+"\nP: "+str(self.P)+"\nC: "+str(self.C)

    def __getattribute__(self, *args, **kwargs):
        return super().__getattribute__(*args, **kwargs)

A = HMM()
print(A)
