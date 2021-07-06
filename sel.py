
from enums import sizes
from classes import mesh


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
