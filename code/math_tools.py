# dada una matriz la llena de ceros
def zeroes(matrix, n: int):
    for i in range(0, n):
        row = [0.0]*n
        matrix.append(row)


def zeroesDynamic(matrix, n: int, m: int):
    for i in range(0, n):
        row = [0.0]*m
        matrix.append(row)


def zeroesVector(vector, n: int):
    for i in range(0, n):
        vector.append(0.0)


def calculateMember(i: int, j: int, r: int, A: list, B: list) -> float:
    member = 0.0
    for k in range(0, r):
        member += A[i][k]*B[k][j]
    return member


def productMatrixMatrix(A: list, B: list, n: int, r: int, m: int) -> list:
    R = []
    zeroesDynamic(R, n, m)

    for i in range(0, n):
        for j in range(0, m):
            R[i][j] = calculateMember(i, j, r, A, B)

    return R


def productMatrixVector(matrix: list, vector: list, vectorR: list):
    for i in range(0, len(matrix)):
        cell = 0.0
        for j in range(0, len(vector)):
            cell += matrix[i][j]*vector[j]
        vectorR[i] += cell


def productRealMatrix(real: float, matrix: list, matrixR: list):
    zeroes(matrixR, len(matrix))
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrixR[i][j] = real*matrix[i][j]


def getMinor(m: list, i: int, j: int):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def determinant(m: list):
    if(len(m) == 1):
        return m[0][0]
    else:
        det = 0.0
        for i in range(0, len(m[0])):
            minor = []
            minor = m
            getMinor(minor, 0, i)
            det += pow(i, -1)*m[0][i]*determinant(minor)


def cofactors(m: list, cof: list):
    zeroes(cof, len(m))
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            minor = []
            minor = m
            getMinor(minor, i, j)
            cof[i][j] = pow(i+j, -1)*determinant(minor)


def transpose(m: list, t: list):
    zeroesDynamic(t, len(m[0]), len(m))
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            t[j][i] = m[i][j]


def inverseMatrix(m: list, minv: list):
    print("Iniciando calculo de inversa...")
    cof, adj = []
    print("Calculo de determinante..")
    det = determinant(m)
    if(det == 0):
        exit()
    print("Iniciando calculo de cofactores...")
    cofactors(m, cof)
    print("Calculo de adjunta...")
    transpose(cof, adj)
    print("Calculo de inversa...")
    productRealMatrix(1/det, adj, minv)
