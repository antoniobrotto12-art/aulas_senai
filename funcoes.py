

def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media
# Programa principal (fora da funçao)
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

resultado = calcular_media(n1, n2, n3)

print(f"media final: ", resultado )