import pandas as pd

import decode
import visualize

# Substitua 'nome_do_arquivo' pelo caminho para o arquivo que você deseja ler
arquivo = 'config/19.bin'
dic = decode.decodificar_arquivo(arquivo)
bytes = decode.file_to_byte_array(arquivo)


"""
Classe usada para manipular o dado recebido em algo que seja legível e entendível

-> Fazer com que a classe receba o valor direto do arquivo e a partir de uma lambda function 
processe os dados 

-> A taxa de amostragem dos dados nem sempre é a mesme, o mesmo vale pro tempo de medida, por 
isso temos que fazer as funções de visualização levando isso em consideração, uma possível 
solução pra isso é fazer um scatter plot quando formos plotar os dados pelo tempo (Ex:. (apps_1, apps2) x tempo)
e podemos usar uma lookup table quando formos plotar um dado por outro
"""
class dado:
    def __init__(self, nome, origem):
        self.nome = nome
        self.origem = origem
        self.dados = []
        self.tempos = []
        self.unidade = ''

    def __getitem__(self, index):
        return self.dados[index] 
    
    def scatter(self):
        return [(self.tempos[i], self.dados[i]) for i in range(len(self.dados))]
    


apps1_bruto = dado("apps1_bruto", dic)
apps1_bruto.dados = [(i["dados"][1] << 8) | (i["dados"][0]) for i in dic if i["id"] == 3]
apps1_bruto.tempos = [(i["tick"]) for i in dic if i["id"] == 3]
apps1_bruto.unidade = "Valor Apps"

apps1_tensao = dado("apps1_tensão", dic)
apps1_tensao.dados = [float((i["dados"][1] << 8) | (i["dados"][0])) * (3.3/4095.0) for i in dic if i["id"] == 3]
apps1_tensao.tempos = [(i["tick"]) for i in dic if i["id"] == 3]
apps1_tensao.unidade = "Tensão (Volts)"

apps2_bruto = dado("apps2_bruto", dic)
apps2_bruto.dados = [(i["dados"][3] << 8) | (i["dados"][2]) for i in dic if i["id"] == 3]
apps2_bruto.tempos = [(i["tick"]) for i in dic if i["id"] == 3]
apps2_bruto.unidade = "Valor Apps"

apps2_tensao = dado("apps2_tensão", dic)
apps2_tensao.dados = [float((i["dados"][3] << 8) | (i["dados"][2])) * (3.3/4095.0) for i in dic if i["id"] == 3]
apps2_tensao.tempos = [(i["tick"]) for i in dic if i["id"] == 3]
apps2_tensao.unidade = "Tensão (Volts)"


#print(bytes)
#print(array_de_bytes)  

visualize.plotar_tabela(dic)
visualize.plotar_grafico_composto([apps1_tensao, apps2_tensao])
visualize.plotar_grafico_composto([apps1_bruto, apps2_bruto])

visualize.mostrar()