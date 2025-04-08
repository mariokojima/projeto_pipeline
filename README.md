# projeto pipeline

Projeto proposto para a disciplina de * COLETA, ARMAZENAMENTO E VISUALIZAÇÃO DE DADOS * 
do mestrado em * COMPUTAÇÃO APLICADA * 
RA 10082703

## Ideia proposta
Um fabricante de garrafinhas de água, lançou um novo produto e gostaria de acompanhar a variação de preços e aceitação do produto em uma rede de market place.

## 1. Coleta
- Web Scrapper para baixar preços e avaliações da Magalu
script em python que lê a página do produto, coleta os dados mapeados e salva em arquivo CSV.
```scrapy runspider scrappy.py -O scrap_result.csv```
[1 ponto]


## 2. Ingestão 
- Utilizando air flow para orquestrar o fluxo de dados, incluindo a ingestão
[1 ponto]
- ETL que lê o arquivo CSV, normaliza os dados, remove outliers e grava no banco
[1 ponto]
- Dados prórios 
[1 ponto]


## 3.Armazenamento
- Repositório S3 local (minIO)
[1 ponto]

- banco de dados postgress
```docker run -p 5432:5432 -v /Users/mario/Workspaces/MESTRADO_MACKENZIE/COLETA/PROJETO/postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres```
[1 ponto]

## 4. Processamento
- Utilizando API do Gemini para avaliar comentários
[1 ponto]

## 5. Visualização 
- Streamlit para criação de dashboard
[1 ponto]