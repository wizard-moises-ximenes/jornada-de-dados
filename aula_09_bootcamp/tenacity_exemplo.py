from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_input():
    user_input = input("Digite 'ok' para continuar: ")
    if user_input.lower() != "ok":
        print("Entrada inválida, tentando novamente...")
        raise ValueError("Entrada inválida. Tente novamente.")
    else:
        print("Entrada válida!")


try:
    get_user_input()
except Exception as e:
    print(f"Falha após várias tentativas: {e}")
