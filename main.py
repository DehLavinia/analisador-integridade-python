
import hashlib
import os

PASTA_HASHES = "hashes"

def calcular_hash(arquivo):
    with open(arquivo, "rb") as f:
        dados = f.read()

    return hashlib.sha256(dados).hexdigest()


def verificar_integridade(arquivo):
    hash_atual = calcular_hash(arquivo)

    os.makedirs(PASTA_HASHES, exist_ok=True)

    nome_hash = os.path.basename(arquivo) + ".sha256"
    caminho_hash = os.path.join(PASTA_HASHES, nome_hash)

    if not os.path.exists(caminho_hash):
        with open(caminho_hash, "w") as f:
            f.write(hash_atual)

        print("\nHash original criado com sucesso!")
        print("Arquivo íntegro. Referência registrada.")
        return

    with open(caminho_hash, "r") as f:
        hash_original = f.read().strip()

    if hash_original == hash_atual:
        print("\nArquivo íntegro. Nenhuma alteração detectada.")
    else:
        print("\nAtenção! O arquivo foi alterado.")

    print("\nHash original:")
    print(hash_original)

    print("\nHash atual:")
    print(hash_atual)


opcao = ""

while opcao != "3":
    print("\n====== ANALISADOR DE INTEGRIDADE PYTHON =======")
    print("1 - Verificar arquivo")
    print("2 - Calcular hash")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        arquivo = input("Digite o nome do arquivo: ")

        if not os.path.isfile(arquivo):
            print("\nArquivo não encontrado.")
        else:
            verificar_integridade(arquivo)

    elif opcao == "2":
        arquivo = input("Digite o nome do arquivo: ")

        if not os.path.isfile(arquivo):
            print("\nArquivo não encontrado.")
        else:
            hash_atual = calcular_hash(arquivo)
            print("\nHash SHA-256:")
            print(hash_atual)

    elif opcao == "3":
        print("\nEncerrando programa...")

    else:
        print("\nOpção inválida!")