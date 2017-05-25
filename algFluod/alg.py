import numpy as np

file = open("matrix.txt", mode='r')
N = int(file.read(1))
file.readline()
P = np.zeros((N, N), dtype=int)
T = np.array([[i]*N for i in range(1,N+1)]).transpose()
P_new = np.zeros((N, N), dtype=int)
for i in range(0, N):
    P[i] = np.array([int(x) for x in file.readline().split(" ")])

print(P)
for k in range(-1, N-1):
    for i in range(0, N):
        for j in range(0,N):
            if i == k+1 or j == k+1:
                P_new[i][j] = P[i][j]
            else:
                P_new[i][j] = min(P[i][j],P[i][k+1] + P[k+1][j])
    for i in range(0, N):
        for j in range(0, N):
            if P_new[i][j] != P[i][j]:
                T[i][j] = k+2
        if P_new[i][i] < 0:
            print("Negative cycle")
            break
    print(P_new)
    print(T)
    P = P_new
    P_new = np.zeros((N, N), dtype=int)
