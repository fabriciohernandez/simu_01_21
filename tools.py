from classes import *
from io import TextIOWrapper
from enums import modes, sizes


def obtenerDatos(file: TextIOWrapper, item_list: list, type: int):
    if(type == sizes.NODES.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndCoordinates\n"):
                stopCondition = True
            if(line != "Coordinates\n" and line != "EndCoordinates\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newNode = node()
                newNode.id = int(vals[0])
                newNode.x = float(vals[1])
                newNode.y = float(vals[2])
                newNode.z = float(vals[3].replace('\n', ''))
                item_list.append(newNode)
    elif(type == sizes.ELEMENTS.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndElements\n"):
                stopCondition = True
            if(line != "Elements\n" and line != "EndElements\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newElement = element()
                newElement.setValues(int(vals[0]), None, None, None, int(vals[0]), int(
                    vals[1]), int(vals[2]), int(vals[3]), None, None, None, None, None, None, None)

                item_list.append(newElement)
    elif(type == sizes.DIRICHLET.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndDirichlet\n"):
                stopCondition = True
            if(line != "Dirichlet\n" and line != "EndDirichlet\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newCondition = condition()
                newCondition.node1 = int(vals[0])
                newCondition.value = float(vals[1].replace('\n', ''))
                item_list.append(newCondition)
    elif(type == sizes.NEUMANN.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndNeumann\n"):
                stopCondition = True
            if(line != "Neumann\n" and line != "EndNeumann\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newCondition = condition()
                newCondition.node1 = int(vals[0])
                newCondition.value = float(vals[1].replace('\n', ''))
                item_list.append(newCondition)


def correctConditions(n: int, conditions: list, indices: list):
    for i in range(0, n):
        indices.append(conditions[i].node1)

    for i in range(0, n-1):
        pivot = conditions[i].node1
        for j in range(0, n):
            if(conditions[j].node1 > pivot):
                conditions[j].node1 = conditions[j].node1-1


def leerMallayCondiciones(m: mesh, filename: str):
    filename += ".dat"
    file = open(filename)
    line = file.readline()
    # Obteniendo k y q
    vals = line.split(" ")
    k = float(vals[0])
    q = float(vals[1].replace('\n', ''))
    # Obteniendo nnodes,neltos,ndirch,nneu
    line = file.readline()
    vals = line.split(" ")
    nnodes = int(vals[0])
    neltos = int(vals[1])
    ndirich = int(vals[2])
    nneu = int(vals[3].replace('\n', ''))
    # Seteando parametros
    m.setParameters(k, q)
    m.setSizes(nnodes, neltos, ndirich, nneu)
    # Obteniendo datos coordenadas
    obtenerDatos(file, m.node_list, sizes.NODES.value)
    # Obteniendo datos Elements
    obtenerDatos(file, m.element_list, sizes.ELEMENTS.value)
    # Obteniendo datos Dirichlet
    obtenerDatos(file, m.dirichlet_list, sizes.DIRICHLET.value)
    # Obteniendo datos Neumann
    obtenerDatos(file, m.neumann_list, sizes.NEUMANN.value)
    # Cerramos el archivo .dat
    file.close()
    # Corregimos indices de eliminacion
    correctConditions(ndirich, m.dirichlet_list, m.indices_dirich)


def findIndex(v: int, s: int, arr: list):
    for i in range(0, s):
        if(arr[i] == v):
            return True
        return False


def writeResult(m: mesh, T: list, filename: str):
    dirich_indices = m.indices_dirich
    dirich = m.dirichlet_list

    # Agregamos la extension del archivo
    filename += ".post.res"
    # Escribimos en el archivo
    file = open(filename, 'a')
    file.write("GiD Post Results File 1.0\n")
    file.write(
        "Result \"Temperature\" \"Load Case 1\" 1 Scalar OnNodes\nComponentNames \"T\"\nValues\n")

    #Tpos = 0
    #Dpos = 0
    #n = m.getSize(sizes.NODES.value)
    #nd = m.getSize(sizes.DIRICHLET.value)
    # for i in range(0, n):
    #    if(findIndex(i+1, nd, dirich_indices)):
    #        file.write(i+1 + " " + dirich[Dpos].value + "\n")
    #        Dpos += 1
    #    else:
    #        file.write(i+1 + " " + T[Tpos] + "\n")
    #        Tpos += 1

    file.write("End values\n")

    file.close()
