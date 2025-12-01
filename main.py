import sys
import os
import shutil
import subprocess
from lexico import ObsActLexer
from sintatico import ObsActParser

# Configuração de pastas
PASTA_TESTES = 'testes'
PASTA_SAIDAS = 'saidas'

def rodar_testes():
    # 1. Cria a pasta de saídas se não existir
    if not os.path.exists(PASTA_SAIDAS):
        os.makedirs(PASTA_SAIDAS)

    # 2. Copia o funcoes.py para a pasta de saídas
    # Isso é necessário para que o código gerado consiga importar as funções
    try:
        shutil.copy('funcoes.py', os.path.join(PASTA_SAIDAS, 'funcoes.py'))
    except FileNotFoundError:
        print("ERRO: Arquivo 'funcoes.py' não encontrado.")
        return

    # 3. Inicializa Lexer e Parser
    lexer = ObsActLexer()
    parser = ObsActParser()

    # 4. Lista todos os arquivos da pasta 'testes'
    if not os.path.exists(PASTA_TESTES):
        print(f"A pasta '{PASTA_TESTES}' não existe. Crie a pasta e coloque os arquivos .obsact lá.")
        return

    arquivos = [f for f in os.listdir(PASTA_TESTES) if f.endswith('.obsact')]
    arquivos.sort() # Ordena para rodar testes na ordem

    if not arquivos:
        print("Nenhum arquivo .obsact encontrado na pasta de testes.")
        return

    print(f" {len(arquivos)} testes\n")

    # 5. Loop para processar cada arquivo
    for arquivo in arquivos:
        print(f"Processando: {arquivo}")
        
        caminho_entrada = os.path.join(PASTA_TESTES, arquivo)
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        caminho_saida = os.path.join(PASTA_SAIDAS, f"{nome_sem_extensao}.py")

        # Ler arquivo
        with open(caminho_entrada, 'r') as f:
            data = f.read()

        # Compilar
        try:
            tokens = lexer.tokenize(data)
            codigo_python = parser.parse(tokens)

            if codigo_python:
                # Salvar o arquivo Python gerado
                with open(caminho_saida, 'w') as f_out:
                    f_out.write(codigo_python)
                
                print(f"Compilado. Gerado: {caminho_saida}")
                
                # Executar o código gerado para ver o resultado real
                print("Executando resultado:")
                print("-"*30+ "\n")
                # Chamada de sistema para rodar o python gerado
                resultado = subprocess.run(
                    [sys.executable, f"{nome_sem_extensao}.py"], 
                    cwd=PASTA_SAIDAS, # Muda o diretório de execução para 'saidas'
                    capture_output=True, 
                    text=True
                )
                
                # Mostra o print do programa traduzido
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