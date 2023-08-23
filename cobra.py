#Criando Nossa Primeira Conexão
#Estabelecer uma conexão com o banco que permitirá que o SQLite3 possa interagir com o banco.

import sqlite3

# Conecte-se ao banco de dados (ele será criado se não existir)
conexao = sqlite3.connect('banco.db') # sqlite3.connect() cria uma conexão com o banco de dados existente no diretório corrente ou o criando de modo implícito, caso o arquivo .db não exista. 
cursor = conexao.cursor() #Para a execução de instruções SQL e a busca dos resultados das consultas se faz necessário o uso de um cursor de banco de dados. A chamada con.cursor() cria um cursor, o objeto retornado representa a conexão com o banco de dados no disco.

# Crie uma tabela se ela não existir
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT UNIQUE, idade INTEGER)')

# Insira ou atualize dados na tabela com o mesmo ID para o mesmo nome
cursor.execute('INSERT OR REPLACE INTO usuarios (id, nome, idade) VALUES ((SELECT id FROM usuarios WHERE nome = ?), ?, ?)', ('Alice', 'Alice', 22))
cursor.execute('INSERT OR REPLACE INTO usuarios (id, nome, idade) VALUES ((SELECT id FROM usuarios WHERE nome = ?), ?, ?)', ('Bob', 'Bob', 25))
cursor.execute('INSERT OR REPLACE INTO usuarios (id, nome, idade) VALUES ((SELECT id FROM usuarios WHERE nome = ?), ?, ?)', ('Johnny', 'Johnny', 21))
cursor.execute('INSERT OR REPLACE INTO usuarios (id, nome, idade) VALUES ((SELECT id FROM usuarios WHERE nome = ?), ?, ?)', ('Felix', 'Felix', 24))

# Salve as alterações
conexao.commit()

# Consulte dados da tabela
cursor.execute('SELECT * FROM usuarios ORDER BY id')
dados = cursor.fetchall()

for linha in dados:
    print(linha)

# Feche a conexão
conexao.close()

