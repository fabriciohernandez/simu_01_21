from classes import *
from io import TextIOWrapper
from enums import sizes


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
                newElement.setValues(
                    int(vals[0]), None, None,
                    None, int(vals[1]), int(vals[2]),
                    int(vals[3]), int(vals[4].replace('\n', '')), None)

                item_list.append(newElement)
    elif(type == sizes.DIRICHLET_X.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndDirichlet_X\n"):
                stopCondition = True
            if(line != "Dirichlet_X\n" and line != "EndDirichlet_X\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newCondition = condition()
                newCondition.node1 = int(vals[0])
                newCondition.value = float(vals[1].replace('\n', ''))
                item_list.append(newCondition)
    elif(type == sizes.DIRICHLET_Y.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndDirichlet_Y\n"):
                stopCondition = True
            if(line != "Dirichlet_Y\n" and line != "EndDirichlet_Y\n"):
                vals = line.split(" ")
                vals = list(filter(('').__ne__, vals))
                newCondition = condition()
                newCondition.node1 = int(vals[0])
                newCondition.value = float(vals[1].replace('\n', ''))
                item_list.append(newCondition)
    elif(type == sizes.DIRICHLET_Z.value):
        stopCondition = False
        file.readline()
        while(stopCondition == False):
            line = file.readline()
            if(line == "EndDirichlet_Z\n"):
                stopCondition = True
            if(line != "Dirichlet_Z\n" and line != "EndDirichlet_Z\n"):
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
    # Obteniendo EI f_x f_y f_z
    vals = line.split(" ")
    EI = float(vals[0])
    f_x = float(vals[1])
    f_y = float(vals[2])
    f_z = float(vals[3].replace('\n', ''))
    # Obteniendo nnodes,neltos,ndirch_x,ndirch_y,ndirch_z,nneu
    line = file.readline()
    vals = line.split(" ")
    nnodes = int(vals[0])
    neltos = int(vals[1])
    ndirich_x = int(vals[2])
    ndirich_y = int(vals[3])
    ndirich_z = int(vals[4])
    nneu = int(vals[5].replace('\n', ''))
    # Seteando parametros
    m.setParameters(EI, f_x, f_y, f_z)
    m.setSizes(nnodes, neltos, ndirich_x, ndirich_y, ndirich_z, nneu)
    # Obteniendo datos coordenadas
    obtenerDatos(file, m.node_list, sizes.NODES.value)
    # Obteniendo datos Elements
    obtenerDatos(file, m.element_list, sizes.ELEMENTS.value)
    # Obteniendo datos Dirichlet X
    obtenerDatos(file, m.dirichlet_list_X, sizes.DIRICHLET_X.value)
    # Obteniendo datos Dirichlet Y
    obtenerDatos(file, m.dirichlet_list_Y, sizes.DIRICHLET_Y.value)
    # Obteniendo datos Dirichlet Z
    obtenerDatos(file, m.dirichlet_list_Z, sizes.DIRICHLET_Z.value)
    # Obteniendo datos Neumann
    obtenerDatos(file, m.neumann_list, sizes.NEUMANN.value)
    # Cerramos el archivo .dat
    file.close()
    # Corregimos indices de eliminacion
    correctConditions(ndirich_x, m.dirichlet_list_X, m.indices_dirich_X)
    correctConditions(ndirich_y, m.dirichlet_list_Y, m.indices_dirich_Y)
    correctConditions(ndirich_z, m.dirichlet_list_Z, m.indices_dirich_Z)


def findIndex(v: int, s: int, arr: list):
    for i in range(0, s):
        if(arr[i] == v):
            return True
        return False


def writeResult(m: mesh, T: list, filename: str):
    dirich_indices = m.indices_dirich_X
    dirich = m.dirichlet_list_X

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
