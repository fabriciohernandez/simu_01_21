from sel import *
from tools import *
import classes
import math_tools
import sys


def main():
    filename = "proyecto_test"
    localKs = []
    localbs = []
    k = []
    b = []
    w = []

    print("IMPLEMENTACION DEL METODO DE LOS ELEMENTOS FINITOS - GRUPO 8")
    print("- Alexa's String Manipulation at the Supra-Dome's Visualizer - 3 DIMENSIONES")
    print("- ELEMENTOS TETRAHEDROS")
    print("*********************************************************************************\n")

    m = classes.mesh()
    leerMallayCondiciones(m, filename)
    print("Datos obtenidos correctamente\n********************")

    # crearSistemasLocales(m, localKs, localbs)
    # print("******************************")

    # Escribimos resultados
    # writeResult(m, w, filename)


main()
