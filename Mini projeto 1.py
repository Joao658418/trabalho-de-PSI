# Mini Projeto 1 - Gerador de Siglas

# 1. Pedir ao utilizador uma frase
frase = input("Digite uma frase: ")

# 2. Separar a frase em palavras
palavras = frase.split()

# 3. Criar uma variável para guardar a sigla
sigla = ""

# 4. Percorrer cada palavra
for palavra in palavras:
    # Pegar a primeira letra de cada palavra
    sigla += palavra[0].upper()

# 5. Mostrar o resultado
print("Sigla gerada:", sigla)


