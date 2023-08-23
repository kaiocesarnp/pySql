#Criar arquivos .CVS

import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João G. Rosa']
Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {
    'Autor': Autor,
    'Livro': Livro,
    'Ano': Ano
    }

#Verificar o tipo de estrutura criada através do comando type
autores = pd.DataFrame(dados)
print(type(autores))

df = pd.DataFrame(autores)
print(df)

#Salvar o DataFrame 'df' em um arquivo CSV chamado "livros_autores.csv".
df.to_csv("livros_autores.csv")

#Adicionando o argumento index_col=0 ao comando podemos visualizar a tabela e seus índices. 
autores = pd.read_csv('livros_autores.csv', index_col = 0)
print(autores)

#Obter detalhes sobre o arquivo
autores.info()

#Retornando somente informações referentes as colunas
colunas = autores.columns
print(colunas)

indice = autores.index
print(indice)
