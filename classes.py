from typing import Sized
from enums import *


class item():
    id: int = 0
    x: float = 0
    y: float = 0
    z: float = 0
    node1: int = 0
    node2: int = 0
    node3: int = 0
    node4: int = 0
    value: float = 0

    def setId(self, id: int):
        self.id = id

    def setX(self, x: float):
        self.x = x

    def setY(self, y: float):
        self.y = y

    def setZ(self, z: float):
        self.z = z

    def setNode1(self, node1: int):
        self.node1 = node1

    def setNode2(self, node2: int):
        self.node2 = node2

    def setNode3(self, node3: int):
        self.node3 = node3

    def setNode4(self, node4: int):
        self.node4 = node4


class node(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, value: float):
        self.id = id
        self.x = x
        self.y = y
        self.z = z


class element(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, value: float):
        self.id = id
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4


class condition(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, value: float):
        self.node1 = node1
        self.value = value


class mesh:
    parameters: list = [None, None, None, None]
    sizes: list = [None, None, None, None, None, None]
    node_list: list = []
    element_list: list = []
    indices_dirich_X: list = []
    indices_dirich_Y: list = []
    indices_dirich_Z: list = []
    dirichlet_list_X: list = []
    dirichlet_list_Y: list = []
    dirichlet_list_Z: list = []
    neumann_list: list = []

    def setParameters(self, EI: float, f_x: float, f_y: float, f_z: float):
        self.parameters[parameters.CONSTANT_EI.value] = EI
        self.parameters[parameters.FORCE_X.value] = f_x
        self.parameters[parameters.FORCE_Y.value] = f_y
        self.parameters[parameters.FORCE_Z.value] = f_z

    def setSizes(self, nnodes: int, neltos: int, ndirich_x: int, ndirich_y: int, ndirich_z: int, nneu: int):
        self.sizes[sizes.NODES.value] = nnodes
        self.sizes[sizes.ELEMENTS.value] = neltos
        self.sizes[sizes.DIRICHLET_X.value] = ndirich_x
        self.sizes[sizes.DIRICHLET_Y.value] = ndirich_y
        self.sizes[sizes.DIRICHLET_Z.value] = ndirich_z
        self.sizes[sizes.NEUMANN.value] = nneu

    def getSize(self, s: int) -> int:
        return self.sizes[s]

    def getParameter(self, p: int) -> int:
        return self.parameters[p]

    def createData(self):
        self.node_list = [None]*self.sizes[sizes.NODES.value]
        self.element_list = [None]*self.sizes[sizes.ELEMENTS.value]
        self.indices_dirich_X = [None]*sizes.DIRICHLET_X.value
        self.dirichlet_list_X = [None]*self.sizes[sizes.DIRICHLET_X.value]
        self.neumann_list = [None]*self.sizes[sizes.NEUMANN.value]

    def getNode(self, i: int) -> node:
        return self.node_list[i]

    def getElement(self, i: int) -> element:
        return self.element_list[i]

    def getCondition(self, i: int, type: int):
        if(type == sizes.DIRICHLET_X):
            return self.dirichlet_list_X[i]
        elif(type == sizes.DIRICHLET_Y):
            return self.dirichlet_list_Y[i]
        elif(type == sizes.DIRICHLET_Z):
            return self.dirichlet_list_Z[i]
        else:
            return self.neumann_list[i]
