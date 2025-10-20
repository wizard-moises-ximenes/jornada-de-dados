is_nome_aluno: bool = False

while not is_nome_aluno is not True:
    nome_aluno = input("Digite sua classe: ")
    if isinstance(nome_aluno, str):
        nome_aluno_maiusculo = nome_aluno.strip().upper()
        print(f"Classe registrada como: {nome_aluno_maiusculo}")
        is_nome_aluno = True
    else:
        print(
            "Você digitou uma classe errada, precisa ser uma string. Tente novamente."
        )
