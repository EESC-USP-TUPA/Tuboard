import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
from itertools import cycle


import pyqtgraph.examples
#pyqtgraph.examples.run()


cores = ['r', 'g', 'b', 'y', 'c']
cores = cycle(cores)

app = pg.mkQApp("Tuboard")

def plotar_tabela(data):
    w = pg.TableWidget()
    w.show()
    w.resize(500,500)
    w.setWindowTitle('pyqtgraph example: TableWidget')

    w.setData(data)

    pg.exec()

def plotar_grafico_composto(dados):
    win = pg.plot()
    win.resize(1000,600)
    win.setWindowTitle("Gráfico Composto")
    win.addLegend()

    pg.setConfigOptions(antialias=True)


    for i in dados:
        # definindo o eixo x em cada um dos dados, consguimos plotar gráficos com taxas de amostragem diferentes no mesmo gráfico
        p1 = win.plot(y = i.dados, x = i.tempos, pen = next(cores), name= i.nome)

    #p1.multiDataPlot(y = [i.dados for i in dados], x = [i.tempos for i in dados])

    # p1 = win.addPlot(title="hmmmm")
    # p1.multiDataPlot(y = [i.dados for i in dados], x = [i.tempos for i in dados])


def mostrar():
    pg.exec()
