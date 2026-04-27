# def minha_funcao():
#     print("Essa é minha funçao")
#     local = "so pode ser utilizada na funcao"
    

# minha_funcao()
# # print(local)
# print(geral)

nome = "Tonho" # Global

def saudacao():
    sobrenome = "python" # local
    print(f"olá, {nome} {sobrenome}")

saudacao()

def somar(n1, n2): # n1 e n2 sao parametros
    print(f"A soma é {n1 + n2}")

somar(7, 47) # são argumentos