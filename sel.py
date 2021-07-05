
from enums import sizes
from classes import mesh


def createLocalk(element: int, m: mesh):
    print("Implement")


def createLocalb(element: int, m: mesh):
    print("Implement")


def crearSistemasLocales(m: mesh, localks: list, localbs: list):
    for i in range(m.getSize(sizes.ELEMENTS.value)):
        localks.append(createLocalk(i, m))
        localbs.append(createLocalb(i, m))
