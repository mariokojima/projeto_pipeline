# projeto_pipeline

## 1. Coleta
- Web Scrapper para baixar preços e avaliações da Magalu
script em python que lê a página do produto, coleta os dados mapeados e salva em arquivo CSV.


## 2. Ingestão 
- Utilizando air flow para orquestrar o fluxo de dados, incluindo a ingestão
- ETL que lê o arquivo CSV, normaliza os dados, remove outliers e grava no banco


# 3.Armazenamento
- Repositório S3 local (minIO)

- banco de dados postgress
docker run -p 5432:5432 -v /Users/mario/Workspaces/MESTRADO_MACKENZIE/COLETA/PROJETO/postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1234 -d postgres

# 4. Processamento
- Utilizando API do Gemini para avaliar comentários

# 5. Visualização 
- Streamlit para criação de dashboard