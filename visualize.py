import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore


import pyqtgraph.examples
#pyqtgraph.examples.run()


app = pg.mkQApp("Tuboard")

def plotar_tabela(data):
    w = pg.TableWidget()
    w.show()
    w.resize(500,500)
    w.setWindowTitle('pyqtgraph example: TableWidget')

    w.setData(data)

    pg.exec()

def plotar_grafico_unico(dado):
    win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
    win.resize(1000,600)
    win.setWindowTitle("Gráfico Único")

    pg.setConfigOptions(antialias=True)

    p1 = win.addPlot(title=dado.nome, y=dado.dados, x=dado.tempos)
    pg.exec()

def plotar_grafico_composto(dados):
    win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
    win.resize(1000,600)
    win.setWindowTitle("Gráfico Composto")

    pg.setConfigOptions(antialias=True)

    p1 = win.addPlot(title="hmmmm")
    p1.multiDataPlot(y = [i.dados for i in dados], x = [i.tempos for i in dados])

    pg.exec()


if __name__ == '__main__':
    plotar_tabela()
