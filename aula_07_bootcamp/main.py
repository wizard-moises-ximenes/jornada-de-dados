from etl import (filtrar_produtos_nao_entregues, ler_csv,
                 somar_valores_dos_produtos)

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)
print(f"O valor total dos produtos entregues é: {valor_dos_produtos_entregues}")
