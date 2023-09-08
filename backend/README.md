### Projeto FARM

FastAPI, React e MongoDB


**Comandos para subir o projeto**
```shell
# Certifique-se que o Docker está instalado
# Execute na pasta backend o comando:
make docker-mongo-up

# Depois de subir o Docker e o container mongodb
# Sobe o projeto backend
python run.py

# Após subir o backend suba o frontend.
# Vá até a pasta frontend e execute:
npm run dev
```

**Comandos Database Mongo**
Banco de Dados => (database)
```python
# lista todos os bancos de dados. O mesmo que show databases;
show dbs

# selecionar um database
use <Database>

# Verifica o database selecionado
db

# Cria um banco de dados qualquer. Detalhe: Sö passa a existir após inserção de uma collection
use <NovaDatabase>

# Deletando database
db.dropdatabase()
```

Collections => (tabelas)
```python
# Mostra todas as collections de um database
show collections

# Cria collection
db.createcollection("<Nome da Collection>")

# Lista dados de uma collection
db.nome_collection.find().pretty()  # Saída Formatada
db.nome_collection.find()  # Saída em uma só linha

# Inserir um documento
db.minhacolecao.insertOne( {"nome" : "Dácio", "email" : "dacio@email.com"} )

# Inserir vários documentos
db.minhacolecao.insertMany([{"nome" : "Dácio", "email" : "dacio@email.com"}, {"nome" : "Isaac", "email" : "isaac@email.com"}])

# Atualizar (Sai dacio@email.com e entra dacio.lima@email.com)
db.minhacolecao.update({'email':'dacio@email.com'},{$set:{'email':'dacio.lima@email.com'}})

# Remove um documento(Equivale a uma linha em SQL)
db.dados.remove({"mail": "james@brown.org"})

# Deletando uma collection
db.minhacolecao.drop()
```
