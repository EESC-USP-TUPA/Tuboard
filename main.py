import pandas as pd

import decode
import visualize

"""
TODO: Testar esse código e decidir como essa bagaça vai ser desenvolvida
"""


# Substitua 'nome_do_arquivo' pelo caminho para o arquivo que você deseja ler
arquivo = 'decode.py'
array_de_bytes = decode.decodificar_arquivo(arquivo)
df = pd.DataFrame(array_de_bytes)

visualize.plotar_tabela(array_de_bytes)