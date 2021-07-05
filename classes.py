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
    node5: int = 0
    node6: int = 0
    node7: int = 0
    node8: int = 0
    node9: int = 0
    node10: int = 0
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

    def setNode5(self, node5: int):
        self.node5 = node5

    def setNode6(self, node6: int):
        self.node6 = node6

    def setNode7(self, node7: int):
        self.node7 = node7

    def setNode8(self, node8: int):
        self.node8 = node8

    def setNode9(self, node9: int):
        self.node9 = node9

    def setNode10(self, node10: int):
        self.node10 = node10


class node(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, node5: int, node6: int, node7: int, node8: int, node9: int, node10: int, value: float):
        self.id = id
        self.x = x
        self.y = y
        self.z = z


class element(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, node5: int, node6: int, node7: int, node8: int, node9: int, node10: int, value: float):
        self.id = id
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4
        self.node5 = node5
        self.node6 = node6
        self.node7 = node7
        self.node8 = node8
        self.node9 = node9
        self.node10 = node10


class condition(item):
    def setValues(self, id: int, x: float, y: float, z: float, node1: int, node2: int, node3: int, node4: int, node5: int, node6: int, node7: int, node8: int, node9: int, node10: int, value: float):
        self.node1 = node1
        self.value = value


class mesh:
    parameters: list = [None, None]
    sizes: list = [None, None, None, None]
    node_list: list = []
    element_list: list = []
    indices_dirich: list = []
    dirichlet_list: list = []
    neumann_list: list = []

    def setParameters(self, k: float, q: float):
        self.parameters[parameters.THERMAL_CONDUCTIVITY.value] = k
        self.parameters[parameters.HEAT_SOURCE.value] = q

    def setSizes(self, nnodes: int, neltos: int, ndirich: int, nneu: int):
        self.sizes[sizes.NODES.value] = nnodes
        self.sizes[sizes.ELEMENTS.value] = neltos
        self.sizes[sizes.DIRICHLET.value] = ndirich
        self.sizes[sizes.NEUMANN.value] = nneu

    def getSize(self, s: int) -> int:
        return self.sizes[s]

    def getParameter(self, p: int) -> int:
        return self.parameters[p]

    def createData(self):
        self.node_list = [None]*self.sizes[sizes.NODES.value]
        self.element_list = [None]*self.sizes[sizes.ELEMENTS.value]
        self.indices_dirich = [None]*sizes.DIRICHLET.value
        self.dirichlet_list = [None]*self.sizes[sizes.DIRICHLET.value]
        self.neumann_list = [None]*self.sizes[sizes.NEUMANN.value]

    def getNode(self, i: int) -> node:
        return self.node_list[i]

    def getElement(self, i: int) -> element:
        return self.element_list[i]

    def getCondition(self, i: int, type: int):
        if(type == sizes.DIRICHLET):
            return self.dirichlet_list[i]
        else:
            return self.neumann_list[i]
