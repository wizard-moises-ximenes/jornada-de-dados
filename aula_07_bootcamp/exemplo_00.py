valor_1 = 10
valor_2 = 20


def soma(valor_1_para_somar: float, valor_2_para_somar: float = 10) -> float:
    """Função que realiza a soma de dois valores.

    Args:
        valor_1_para_somar (float): Primeiro valor.
        valor_2_para_somar (float): Segundo valor.

    Returns:
        float: Resultado da soma dos dois valores.
    """
    valor_3 = valor_1_para_somar + valor_2_para_somar
    return valor_3


valor_3 = soma(valor_1)
print(valor_3)
