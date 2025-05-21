import pandas as pd

livros = ['Literatura Brasileira', 'Literatura Estrangeira', 'Ciências', 'Matemática', 'História']
quantidade_livros = [12, 9, 18, 14, 20]
quantidade_emprestados = [4, 2, 7, 5, 6]

estoque = pd.Series(quantidade_livros, index=livros)
emprestados = pd.Series(quantidade_emprestados, index=livros)

livros.loc["Filosofia"] = None
print("\nEstoque com um valor nulo ():")
print("Livros Disponíveis para empréstimo: ")

print("Estoque livros disponíveis para empréstimo: ")
pritn(estoque - emprestados)