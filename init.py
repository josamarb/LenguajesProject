from Gramatica.Produccion import Produccion
from Gramatica.Gramatica import Gramatica
from LR.LRcero import LRcero

if __name__ == '__main__':
    producciones = [Produccion("E","E+ni"),Produccion("E","ni")]
    G = Gramatica(["E"],["+","ni"],Produccion("E","E+ni"),producciones)

    lr = LRcero(G)

    caa = "casas"

    print(caa.split("c"))

    cerraduras = lr.cerraduras
    print(len(cerraduras))
    for c in cerraduras:
        print(c.estado)
        print("Accion"+str(c.getActions()))
        print("IR_A" + str(c.getIra()))
        print("Reduccion "+str(c.getReduccion()))
        for i in c.prod:
            print(i.getNoTerminal()+" -> "+i.getProduccion())
        print("----------------------------------------------")
