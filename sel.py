
from math_tools import *
from enums import parameters, sizes
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


def calculateLocalJ(ind: int, m: mesh):
    el = m.getElement(ind)

    n1 = m.getNode(el.node1-1)
    n2 = m.getNode(el.node2-1)
    n3 = m.getNode(el.node3-1)
    n4 = m.getNode(el.node4-1)

    a = n2.x-n1.x
    b = n3.x-n1.x
    c = n4.x-n1.x
    d = n2.y-n1.y
    e = n3.y-n1.y
    f = n4.y-n1.y
    g = n2.z-n1.z
    h = n3.z-n1.z
    i = n4.z-n1.z

    # Se calcula el determinante de esta matriz utilizando
    # la Regla de Sarrus.
    J = a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i

    return J


def createLocalb(element: int, m: mesh) -> list:
    b = []
    f = [m.getParameter(parameters.FORCE_X.value),
         m.getParameter(parameters.FORCE_Y.value),
         m.getParameter(parameters.FORCE_Z.value)]
    j = calculateLocalJ(element, m)
    tau = [59, -1, -1, -1, 4, 4, 4, 4, 4, 4]
    t = [[tau, 0, 0], [0, tau, 0], [0, 0, tau]]

    res = []
    for i in range(0, len(t)):
        aux = []
        for j in range(0, len(f)):
            if(t[i][j] != 0):
                for k in t[i][j]:
                    aux.append(f[i]*k)
        res.append(aux)

    b_i = []
    for i in res:
        aux = []
        for k in i:
            aux.append((j/120)*k)
        b_i.append(aux)

    return b_i


def crearSistemasLocales(m: mesh, localks: list, localbs: list):
    for i in range(m.getSize(sizes.ELEMENTS.value)):
        #localks.append(createLocalk(i, m))
        localbs.append(createLocalb(i, m))


def calculate(K: list, b: list, T: list):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    # inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    # productMatrixVector(Kinv,b,T)
