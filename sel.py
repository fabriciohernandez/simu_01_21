
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


def calculateLocalJ(ind: int, m: mesh):
    el = m.getElement(ind)

    n1 = m.getNode(el.getNode1()-1)
    n2 = m.getNode(el.getNode2()-1)
    n3 = m.getNode(el.getNode3()-1)
    n4 = m.getNode(el.getNode4()-1)

    a = n2.getX()-n1.getX()
    b = n3.getX()-n1.getX()
    c = n4.getX()-n1.getX()
    d = n2.getY()-n1.getY()
    e = n3.getY()-n1.getY()
    f = n4.getY()-n1.getY()
    g = n2.getZ()-n1.getZ()
    h = n3.getZ()-n1.getZ()
    i = n4.getZ()-n1.getZ()

    # Se calcula el determinante de esta matriz utilizando
    # la Regla de Sarrus.
    J = a*e*i+d*h*c+g*b*f-g*e*c-a*h*f-d*b*i

    return J


def createLocalb(element: int, m: mesh):
    b = []
    j = calculateLocalJ(element, m)
    b_i = j/120
    return b


def crearSistemasLocales(m: mesh, localks: list, localbs: list):
    for i in range(m.getSize(sizes.ELEMENTS.value)):
        #localks.append(createLocalk(i, m))
        localbs.append(createLocalb(i, m))

def calculate(K: list, b: list, T: list):
    print("Iniciando calculo de respuesta...\n")
    Kinv = []
    print("Calculo de inversa...\n")
    inverseMatrix(K,Kinv)
    print("Calculo de respuesta...\n")
    productMatrixVector(Kinv,b,T)

