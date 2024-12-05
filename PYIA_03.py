produtos = {}

for i in range (5):
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto R$: '))
    produtos [produto] = valor

total = sum(produtos.values())

print('O valor total da compra é de R$', total)