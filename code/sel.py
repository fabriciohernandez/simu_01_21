
from math_tools import *
from enums import parameters, sizes
from classes import element, mesh


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


def assemblyK(e: element, localK: list, K: list):
    index1: e.node1-1
    index2: e.node2-1
    index3: e.node3-1
    index4: e.node4-1

    K[index1][index1] += localK[0][0]
    K[index1][index2] += localK[0][1]
    K[index1][index3] += localK[0][2]
    K[index1][index4] += localK[0][3]

    K[index2][index1] += localK[1][0]
    K[index2][index2] += localK[1][1]
    K[index2][index3] += localK[1][2]
    K[index2][index4] += localK[1][3]

    K[index3][index1] += localK[2][0]
    K[index3][index2] += localK[2][1]
    K[index3][index3] += localK[2][2]
    K[index3][index4] += localK[2][3]

    K[index4][index1] += localK[3][0]
    K[index4][index2] += localK[3][1]
    K[index4][index3] += localK[3][2]
    K[index4][index4] += localK[3][3]


def assemblyb(e: element, localb: list, b: list):
    index1: e.node1-1
    index2: e.node2-1
    index3: e.node3-1
    index4: e.node4-1

    b[index1] += localb[0]
    b[index2] += localb[1]
    b[index3] += localb[2]
    b[index4] += localb[3]


def ensamblaje(m: mesh, localKs: list, localbs: list, k: list, b: list):
    for i in range(0, m.getSize(sizes.ELEMENTS.value)):
        e = m.getElement(i)
        assemblyK(e, localKs[i], k)
        assemblyb(e, localbs[i], b)


def applyNeumann(m: mesh, b: list):
    for i in range(0, len(m.getSize(sizes.NEUMANN.value))):
        c = m.getCondition(i, sizes.NEUMANN.value)
        b[c.node1-1] += c.value


def applyDirichletX(m: mesh, k: list, b: list):
    for i in range(0, m.getSize(sizes.DIRICHLET_X.value)):
        c = m.getCondition(i, sizes.DIRICHLET_X.value)
        index = c.node1-1

        k.remove(k[0]+index)
        k.remove(b[0]+index)

        for row in range(0, len(k)):
            cell = k[row][index]
            k[row].remove(k[row][0]+index)
            b[row] += -1*c.value*cell


def applyDirichletY(m: mesh, k: list, b: list):
    for i in range(0, m.getSize(sizes.DIRICHLET_Y.value)):
        c = m.getCondition(i, sizes.DIRICHLET_Y.value)
        index = c.node1-1

        k.remove(k[0]+index)
        k.remove(b[0]+index)

        for row in range(0, len(k)):
            cell = k[row][index]
            k[row].remove(k[row][0]+index)
            b[row] += -1*c.value*cell


def applyDirichletZ(m: mesh, k: list, b: list):
    for i in range(0, m.getSize(sizes.DIRICHLET_Z.value)):
        c = m.getCondition(i, sizes.DIRICHLET_Z.value)
        index = c.node1-1

        k.remove(k[0]+index)
        k.remove(b[0]+index)

        for row in range(0, len(k)):
            cell = k[row][index]
            k[row].remove(k[row][0]+index)
            b[row] += -1*c.value*cell


def calculate(K: list, b: list, T: list):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    productMatrixVector(Kinv,b,T)
