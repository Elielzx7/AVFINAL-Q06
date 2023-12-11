
print("Descubra a média de valores positivos.")
numeros = []
positivo = 0

for i in range(5):
    numero = float(input(f'Digite o {i + 1}° número: '))
    
    if numero > 0:
        positivo += 1
        numeros.append(numero)

soma = sum(numeros)
print(f"{positivo} valores positivos")
print(f"Média dos valores positivos: {soma / positivo}" if positivo > 0 else "Não há valores positivos para calcular a média.")