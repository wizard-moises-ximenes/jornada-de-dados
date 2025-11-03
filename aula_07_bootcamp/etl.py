import csv

path_arquivo = "vendas.csv"


def ler_csv(nome_arquivo: str) -> list[dict]:
    """Função que lê um arquivo CSV e retorna uma lista de dicionários.

    Args:
        nome_arquivo (str): Nome do arquivo CSV.

    Returns:
        list[dict]: Lista de dicionários com os dados do arquivo CSV.
    """
    lista: list[dict] = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_nao_entregues(
    lista: list[dict],
) -> list[dict]:
    """Função que filtra os produtos entregues = True"""
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("Entregues") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados


def somar_valores_dos_produtos(
    lista_com_produtos_filtrados: list[dict],
) -> int:
    """Função que soma os valores dos produtos"""
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("Venda", 0))
    return valor_total
