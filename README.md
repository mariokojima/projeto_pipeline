# projeto pipeline

Projeto proposto para a disciplina de * COLETA, ARMAZENAMENTO E VISUALIZAÇÃO DE DADOS * 
do mestrado em * COMPUTAÇÃO APLICADA * 
RA 10082703

## Ideia proposta
Um fabricante de garrafinhas de água, lançou um novo produto e gostaria de acompanhar a variação de preços e aceitação do produto em uma rede de market place.

## Execução
Criar uma pipeline totalmente com ferramentas opensource ou de uso gratuito.

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
```
https://min.io/
```
[1 ponto]

- banco de dados postgress 
[1 ponto]

## 4. Processamento
- Utilizando API do Gemini para avaliar comentários
[1 ponto]

## 5. Alertas
- Ao finalizar o processamento de uma pipeline, o sistema enviará um email com o status do processamento 
[1 ponto] 

## 6. Visualização 
- Streamlit para criação de dashboard
```
https://streamlit.io/
```
[1 ponto]

---
## Anotações
link Magalu
```
https://www.magazineluiza.com.br/busca/garrafa+stanley+aerolight+fast+flow/?page=1
```

iniciar projeto
```  
docker-compose up -d
```


parar projeto
```  
docker-compose down
```

Minio : S3 local 
```
http://localhost:9001/buckets/bucket-coleta/browse
```
