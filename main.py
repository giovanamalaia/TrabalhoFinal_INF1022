# Giovana Malaia Pinheiro - 2312080
# Gabriele Sequeira - 2310202


import sys
import os
import shutil
import subprocess
from lexico import ObsActLexer
from sintatico import ObsActParser

PASTA_TESTES = 'testes'
PASTA_SAIDAS = 'saidas'

def rodar_testes():
    if not os.path.exists(PASTA_SAIDAS):
        os.makedirs(PASTA_SAIDAS)

    # funcoes.py para a pasta de saídas para rodar o código gerado
    try:
        shutil.copy('funcoes.py', os.path.join(PASTA_SAIDAS, 'funcoes.py'))
    except FileNotFoundError:
        print("ERRO: Arquivo 'funcoes.py' não encontrado.")
        return

    # inicializa lexer e parser
    lexer = ObsActLexer()
    parser = ObsActParser()

    # todos os arquivos da pasta 'testes'
    if not os.path.exists(PASTA_TESTES):
        print(f"A pasta '{PASTA_TESTES}' não existe. Crie a pasta e coloque os arquivos .obsact lá.")
        return

    arquivos = [f for f in os.listdir(PASTA_TESTES) if f.endswith('.obsact')]
    arquivos.sort() 

    if not arquivos:
        print("Nenhum arquivo .obsact encontrado na pasta de testes.")
        return

    print(f" {len(arquivos)} testes\n")

    for arquivo in arquivos:
        print(f"Processando: {arquivo}")
        
        caminho_entrada = os.path.join(PASTA_TESTES, arquivo)
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(PASTA_SAIDAS, f"{nome_sem_extensao}.py")

        # ler arquivo
        with open(caminho_entrada, 'r') as f:
            data = f.read()

        # compilar
        try:
            tokens = lexer.tokenize(data)
            codigo_python = parser.parse(tokens)

            if codigo_python:
                # salvar o arquivo python 
                with open(caminho_saida, 'w') as f_out:
                    f_out.write(codigo_python)
                
                print(f"Compilado. Gerado: {caminho_saida}")
                
                # executar o código gerado 
                print("Executando resultado:")
                print("-"*30+ "\n")
                resultado = subprocess.run(
                    [sys.executable, f"{nome_sem_extensao}.py"], 
                    cwd=PASTA_SAIDAS, 
                    capture_output=True, 
                    text=True
                )
                
                # print do programa traduzido
                if resultado.stdout:
                    print(resultado.stdout)
                if resultado.stderr:
                    print("Erro na execução do Python gerado:")
                    print(resultado.stderr)
                print("-"*30 + "\n")
            else:
                print(f"Falha na compilação de {arquivo} (Erro Sintático)\n")

        except Exception as e:
            print(f"Erro inesperado: {e}\n")

if __name__ == '__main__':
    rodar_testes()