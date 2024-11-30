n = int(input("Quantos itens você deseja listar? "))

itens = []

for i in range(n):
    item = input(f"Digite o item {i+1}: ")
    itens.append(item)

itens.sort()

print("\nItens em ordem alfabética:")
for item in itens:
    print(item)
