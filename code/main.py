from sel import *
from tools import *
import classes
import sys


def main():
    filename = sys.argv[1]
    localKs = []
    localbs = []
    k = []
    b = []
    w = []

    print("IMPLEMENTACION DEL METODO DE LOS ELEMENTOS FINITOS - GRUPO 8")
    print("- Alexa's String Manipulation at the Supra-Dome's Visualizer - 3 DIMENSIONES")
    print("- ELEMENTOS TETRAHEDROS")
    print("*********************************************************************************\n")

    # Lectura de datos
    m = classes.mesh()
    leerMallayCondiciones(m, filename)
    print("Datos obtenidos correctamente\n********************")

    # Creacion de sistemas locales
    crearSistemasLocales(m, localKs, localbs)
    print("******************************")

    # Ensamblaje
    zeroes(k, m.getSize(sizes.NODES.value))
    zeroes(b, m.getSize(sizes.NODES.value))
    ensamblaje(m, localKs, localbs, k, b)
    print("******************************")

    # Aplicamos neumann
    applyNeumann(m, b)
    print("******************************")

    # Aplicamos dirichlet
    applyDirichletX(m, k, b)
    applyDirichletY(m, k, b)
    applyDirichletZ(m, k, b)
    print("******************************")

    # Calculo de matrices
    zeroesVector(w, len(b))
    calculate(k, b, w)

    # Escribimos resultados
    writeResult(m, w, filename)


main()
