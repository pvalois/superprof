#!/usr/bin/env python3

# 1. Suite de Fibonacci
def fibo(n):
    L = [1, 1]
    for i in range(2, n):
        L.append(L[i-1] + L[i-2])
    return L[:n]

# 1. Suite de Lucas
def lucas(n):
    L = [2, 1]
    for i in range(2, n):
        L.append(L[i-1] + L[i-2])
    return L[:n]

# 2. Suite de Pell
def pell(n):
    P = [0, 1]
    for i in range(2, n):
        P.append(2*P[i-1] + P[i-2])
    return P[:n]

# 3. Suite de Tribonacci
def tribonacci(n):
    T = [0, 0, 1]
    for i in range(3, n):
        T.append(T[i-1] + T[i-2] + T[i-3])
    return T[:n]

# 4. Suite de Catalan (par formule récursive)
def catalan(n):
    C = [1]
    for i in range(1, n):
        c_i = 0
        for j in range(i):
            c_i += C[j] * C[i-1-j]
        C.append(c_i)
    return C

# 5. Suite de Hofstadter Q
def hofstadter_q(n):
    Q = [None, 1, 1]  # Q(1)=1, Q(2)=1, indexation commençant à 1
    for i in range(3, n+1):
        val = Q[i - Q[i-1]] + Q[i - Q[i-2]]
        Q.append(val)
    return Q[1:]  # enlever l'élément None en début

if __name__ == "__main__":
    n = 20  # nombre de termes à afficher
    
    print(f'{"Fibonacci":<20} :', fibo(n))
    print(f'{"Lucas":<20} :', lucas(n))
    print(f'{"Pell":<20} :', pell(n))
    print(f'{"Tribonacci":<20} :', tribonacci(n))
    print(f'{"Catalan":<20} :', catalan(n))
    print(f'{"Hofstadter Q":<20} :', hofstadter_q(n))

