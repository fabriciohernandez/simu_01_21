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
    THERMAL_CONDUCTIVITY = 0
    HEAT_SOURCE = 1


class sizes(Enum):
    NODES = 0
    ELEMENTS = 1
    DIRICHLET = 2
    NEUMANN = 3
