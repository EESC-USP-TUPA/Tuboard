import pandas as pd

import decode
import visualize

# Substitua 'nome_do_arquivo' pelo caminho para o arquivo que você deseja ler
arquivo = '0.bin'
dic = decode.decodificar_arquivo(arquivo)
bytes = decode.file_to_byte_array(arquivo)


"""
Classe usada para manipular o dado recebido em algo que seja legível e entendível

-> Fazer com que a classe receba o valor direto do arquivo e a partir de uma lambda function 
processe os dados 
"""
class dado:
    def __init__(self, nome, origem):
        self.nome = nome
        self.origem = origem
        self.dados = []
        self.tempos = []

    def __getitem__(self, index):
        return self.dados[index] 
    
    def scatter(self):
        return [(self.tempos[i], self.dados[i]) for i in range(len(self.dados))]
    


apps1_bruto = dado("apps1_bruto", dic)
apps1_bruto.dados = [(i["dados"][0] << 8) | (i["dados"][1]) for i in dic if i["id"] == 3]
apps1_bruto.tempos = [(i["tick"]) for i in dic if i["id"] == 3]

apps1_tensao = dado("apps1_tensão", dic)
apps1_tensao.dados = [float((i["dados"][0] << 8) | (i["dados"][1])) * (3.3/4095.0) for i in dic if i["id"] == 3]
apps1_tensao.tempos = [(i["tick"]) for i in dic if i["id"] == 3]

apps2_bruto = dado("apps1_bruto", dic)
apps2_bruto.dados = [(i["dados"][2] << 8) | (i["dados"][3]) for i in dic if i["id"] == 3]
apps2_bruto.tempos = [(i["tick"]) for i in dic if i["id"] == 3]

apps2_tensao = [float(i)* 3.3/4096.0 for i in apps2_bruto]
volante_bruto = [(i["dados"][4] << 8) | (i["dados"][5]) for i in dic if i["id"] == 3]
volante_tensao = [float(i)* 3.3/4096.0 for i in volante_bruto]


#print(bytes)
#print(array_de_bytes)  

#visualize.plotar_tabela([apps1_bruto.tempos, apps1_bruto.dados])
visualize.plotar_grafico_composto([apps1_bruto, apps2_bruto])