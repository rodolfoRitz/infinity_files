email_cadastrado = "nome@gmail.com"
senha_cadastrada = "123"

while True:
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if email == email_cadastrado and senha == senha_cadastrada:
        print("Login bem-sucedido!")
        break
    else:
        print("Email ou senha incorretos. Tente novamente.")
