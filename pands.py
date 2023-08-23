#Pandas
#O Pandas é uma ferramenta que permite a construção de estruturas de dados própria e a manipulação e retirada de dados.
#O principal ponto do Pandas está em sua estrutura de dados, a qual a biblioteca se concentra, que são duas: DataFrame e Series.
#Series é um array unidimensional indexado por um índice (rótulos).
#O DataFrame é dado por um grupo de dados retangulares, também chamados de dados tabulares.
#Nesse formato, cada coluna vai conter um tipo de dado, representado por um índice de colunas e por um índice para cada um de seus rótulos, que são as linhas.


#importando a biblioteca Pandas
import pandas as pd

"""
#O objeto Series é um tipo array unidimensional que se associa a um rótulo denominado index. Criamos a série da seguinte forma:
series_objeto = pd.Series([1,7,9,13,17,99]) #cada elemento da série está associado a um índice, que vai de zero a cinco.
series_objeto
print(series_objeto)

print() #pula linha

#personalizar os índices:
series_objeto2= pd.Series([4, 7, 8, -2], index = ['alfa', 'beta', 'teta', 'gama'])
series_objeto2
print(series_objeto2)

_________________________


"""

#DataFrame
#Tabela retangular é representada pelo DataFrame que pode conter um conjunto
#de colunas preenchidas por rótulos com tipos de dados como : strings, booleanos,
#inteiros, numéricos, entre outros. Existem ainda dois índices, um para os rótulos
#e outro para as colunas. Repare que coluna requisito retorna Verdadeiro (True)
#ou Falso (False), ou seja, ela mostra se determinada disciplina possui ou não requisito para ser cursada.


disciplinas = {'cursos': ['Estatística', 'Economia', 'Cálculo', 'Geometria'],
               'créditos': [90, 60, 90, 40],
               'requisito': [True, False, True, False]}

data = pd.DataFrame(disciplinas)
print(data)


























