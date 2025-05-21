import pandas as pd 

# Criando uma lista de quantidades em estoque para diferentes produtos

produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera']
quantidade_estoque = [15, 30, 20, 10, 25]


estoque = pd.Series(quantidade_estoque, index=produtos)


print("\nSérie Estoque de Produtos:")
print(estoque)
print("\nQuantidade de notebooks em estoque:")
print(estoque['Notebook'])

print("\nEstoque de Notebook e Câmera:")
print(estoque[['Notebook', 'Câmera']].values)

print("\nProdutos com estoque abaixo de 20 unidades:")
print(estoque[estoque < 20])

print("\nAumentando o estoque em 5 unidades para todos os produtos:")
print(estoque + 5)

estoque.loc['Headphone'] = None
print("\nEstoque com um valor nulo (Headphone):")
print(estoque)

precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

print("\nValor total do estoque por produto (preço * quantidade):")
print(precos * estoque)

