import json

global dados

with open('config/idmap.json', 'r') as arquivo:
    dados = json.load(arquivo)

def file_to_byte_array(file_path):
    byte_array = []
    with open(file_path, 'rb') as file:
        byte = file.read(1)
        while byte:
            byte_array.append(ord(byte))
            byte = file.read(1)
    return byte_array

def decodificar_arquivo(file_path):
    bytedump = file_to_byte_array(file_path)
    
    i = 0

    mensagens = []

    while (i < len(bytedump)):
        
        mensagem = {}
        mensagem["tick"] = (bytedump[i + 3] << 24) | (bytedump[i + 2] << 16) |(bytedump[i + 1] << 8) | bytedump[i]
        mensagem["id"] = (bytedump[i + 7] << 8) | bytedump[i + 6]
        mensagem["nome"] = [dicionario["nome"] for dicionario in dados if dicionario['id'] == mensagem["id"]]
        mensagem["dlc"] = (bytedump[i + 5] << 8) | bytedump[i + 4]

        # Talvez isso aqui esteja invertido
        mensagem["dados"] = list(reversed(bytedump[(i + 8) : (i + 16)]))
        mensagens.append(mensagem)
        i = i + 16

    return mensagens