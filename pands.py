#Pandas
#O Pandas é uma ferramenta que permite a construção de estruturas de dados própria e a manipulação e retirada de dados.
#O principal ponto do Pandas está em sua estrutura de dados, a qual a biblioteca se concentra, que são duas: DataFrame e Series.
#Series é um array unidimensional indexado por um índice (rótulos).
#O DataFrame é dado por um grupo de dados retangulares, também chamados de dados tabulares.
#Nesse formato, cada coluna vai conter um tipo de dado, representado por um índice de colunas e por um índice para cada um de seus rótulos, que são as linhas.
#Em Pandas temos dois tipos de estrutura de dados: as Listas e os DataFrames.


"""
#O objeto Series é um tipo array unidimensional que se associa a um rótulo denominado index. Criamos a série da seguinte forma:

#importando a biblioteca Pandas
import pandas as pd

series_objeto = pd.Series([1,7,9,13,17,99]) #cada elemento da série está associado a um índice, que vai de zero a cinco.
series_objeto
print(series_objeto)

print() #pula linha

#personalizar os índices:

series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])
series_objeto2
print(series_objeto2)

_________________________


#DataFrame
#Tabela retangular é representada pelo DataFrame que pode conter um conjunto
#de colunas preenchidas por rótulos com tipos de dados como : strings, booleanos,
#inteiros, numéricos, entre outros. Existem ainda dois índices, um para os rótulos
#e outro para as colunas. Repare que coluna requisito retorna Verdadeiro (True)
#ou Falso (False), ou seja, ela mostra se determinada disciplina possui ou não requisito para ser cursada.

#importando a biblioteca Pandas
import pandas as pd

disciplinas = {'cursos': ['Estatística', 'Economia', 'Cálculo', 'Geometria'],
               'créditos': [90, 60, 90, 40],
               'requisito': [True, False, True, False]}

data = pd.DataFrame(disciplinas)
print(data)


#A intenção do código apresentado foi mostrar como podemos criar uma estrutura de
#dados do tipo tabular heterogênea bidimensional de dimensões variáveis.
#A estrutura é tabular pois possui forma de tabela, é bidimensional pois possui
#eixos rotulados (linhas e colunas) é heterogênea visto que contêm dados de tipos distintos.
#Neste exemplo a matriz disciplinas contêm dados dos tipos: Strings na coluna [cursos],
#um tipo inteiro em [créditos] e um valor booleano (verdadeiro ou falso) na coluna [requisitos].

_________________________



#Conversão de uma lista em Dataframe
#Projetar uma estrutura de dados tabular que contenha o nome e a população de algumas cidades brasileiras.
#Iniciar com as três primeiras cidades

#importando a biblioteca Pandas
import pandas as pd

nome_cidade = pd.Series(['Maringá', 'Itabira', 'Uberlândia'])
populacao = pd.Series([403.063, 120.904, 699.097])

#dados = pd.DataFrame({"Cidade": nome_cidade, "População": populacao}) #A linha pd.DataFrame transforma as listas em um DataFrame
#print(dados)

#imprimir diretamente:
#print(pd.DataFrame({"Cidade": nome_cidade, "População": populacao}))

#--------

"""
#Transformar a lista de cidades em um dicionário:

#Definir duas listas com as variáveis que recebem nomes de cidades e população
cidades = ['Maringá', 'Itabira', 'Uberlândia', 'Salvador', 'Fortaleza']
populacao = [403.063, 120.904, 699.0973, 2.886698, 2.686612]

#Como transformar listas em dicionários? É bastante simples através do método ZIP ()
#Criar uma variável chamada população_cidades que representará o dicionário com as informações do nome da cidade e de sua população

populacao_cidades = dict(zip(cidades, populacao))
#print(populacao_cidades)
#print(type(populacao_cidades))

#Visualizar as informações de cada cidade individualmente:
print(populacao_cidades['Uberlândia'])

#--------

#Pesquisar se determinada cidade existe ou não no dicionário:
#print('Maringá' in populacao_cidades)
#print('São Carlos' in populacao_cidades)


#Adicionar registros de um DataFrame:
#populacao_cidades['Vitória'] = 365.855
#print(populacao_cidades)

#Deletar registros:
del populacao_cidades['Fortaleza']
print(populacao_cidades)
