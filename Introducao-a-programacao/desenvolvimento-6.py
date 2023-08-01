def idade(anoNascimento, anoAtual, nomePessoa):
    idadePessoa = anoAtual - anoNascimento
    if 0 < idadePessoa < 122:
        return print(
            f"""
            Seu nome: {nomePessoa}
            Sua idade: {idadePessoa}
            """
        )
    else:
        raise Exception("Os dados inseridos são inválidos")


while True:
    try:
        anoNascimento = int(input("Digite o ano de seu nascimento: "))
        anoAtual = int(input("Digite o ano atual: "))
        nomePessoa = input("Digite seu nome: ")

        idade(anoNascimento, anoAtual, nomePessoa)
        break
    except Exception as err:
        print(err)
        continue