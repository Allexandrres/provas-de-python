email_cadastrado = "usuario@example.com"
senha_cadastrada = "senha123"

email = ""
senha = ""

while email != email_cadastrado or senha != senha_cadastrada:
    email = "usuario@example.com"  
    senha = "senha123"  

    if email != email_cadastrado or senha != senha_cadastrada:
        print("Email ou senha incorretos. Tente novamente.")

print("Login bem-sucedido!")