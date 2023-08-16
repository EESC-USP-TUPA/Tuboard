import numpy as np
import pyqtgraph as pg


def plotar_tabela(data):

    app = pg.mkQApp("Table Widget Example")

    w = pg.TableWidget()
    w.show()
    w.resize(500,500)
    w.setWindowTitle('pyqtgraph example: TableWidget')

    w.setData(data)

    pg.exec()

if __name__ == '__main__':
    plotar_tabela()
