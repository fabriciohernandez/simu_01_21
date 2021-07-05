
from enums import sizes
from classes import mesh

def showMatrix(K: list):
    for i in range(0, len(K[0])):
        print("[\t")
        for j in range(0, len(K)):
            print(K[i][j])
            print("\t")
        print("]\n")

def showKs(Ks: list):
    for i in range(0, len(Ks)):
        print("K del elemento ")
        print(i + 1)
        print(":\n")
        showMatrix(Ks[i])
        print("*************************************\n")

def showVector(b: list):
    print("[\t")
    for i in range(0, len(b)):
        print(b[i])
        print("\t")
    print("]\n")

def showbs(bs: list):
    for i in range(0, len(bs)):
        print("b del elemento ")
        print(i + 1)
        print(":\n")
        showVector(bs[i])
        print("*************************************\n")


def createLocalk(element: int, m: mesh):
    print("Implement")


def createLocalb(element: int, m: mesh):
    print("Implement")


def crearSistemasLocales(m: mesh, localks: list, localbs: list):
    for i in range(m.getSize(sizes.ELEMENTS.value)):
        localks.append(createLocalk(i, m))
        localbs.append(createLocalb(i, m))

def calculate(K: list, b: list, T: list):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    productMatrixVector(Kinv,b,T)

