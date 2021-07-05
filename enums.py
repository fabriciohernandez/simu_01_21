from enum import Enum


class indicator(Enum):
    NOTHING = 0


class lines(Enum):
    NOLINE = 0
    SINGLELINE = 1
    DOUBLELINE = 2


class modes(Enum):
    NOMODE = 0
    INT_FLOAT = 1
    INT_FLOAT_FLOAT_FLOAT = 1
    INT_INT_INT_INT_INT = 3


class parameters(Enum):
    CONSTANT_EI = 0
    FORCE_X = 1
    FORCE_Y = 2
    FORCE_Z = 3


class sizes(Enum):
    NODES = 0
    ELEMENTS = 1
    DIRICHLET_X = 2
    DIRICHLET_Y = 3
    DIRICHLET_Z = 4
    NEUMANN = 5
