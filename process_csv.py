# prompt: Criar um script que lerá um arquivo CSV e gravará os dados em um banco de dados postgres

import psycopg2
import pandas as pd
import os

def load_csv_to_postgres(csv_file_path, db_params):

    try:
        # lê o csv e joga num dataframe
        df = pd.read_csv(csv_file_path, encoding='utf-8')

        # conexão com o banco
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

 
        # insere os dados no db
        for index, row in df.iterrows():

            title = ''
            price = 0
            nota = None
            votos = None

            # Normalização dos dados
            title = row['title']
            price = row['price'].replace('R$ ', '').replace(',', '.').strip()
            price = float(price)
            loja = row['store']
            if pd.isna(row['review']) == True:
                nota = 'Null'
                votos = 'Null'   
            else:
                nota = str(row['review']).split(' (')[0].replace(')', '')
                votos = str(row['review']).split(' (')[1].replace(')', '')
            

            
            insert_query = f"""
                 INSERT INTO scrappy (scrappy_title,scrappy_price,scrappy_nota,scrappy_votos,scrappy_loja)
                 VALUES (
            """
            insert_query = insert_query + f"'{title}',{price},{nota},{votos},'{loja}');"

            cur.execute(insert_query)

        # Commit changes and close connection
        conn.commit()
        cur.close()
        conn.close()
        print(f"Leitura de '{csv_file_path}' realizada com sucesso.")
        print(f"Normalização dos dados realizada com sucesso.")
        print(f"Carga realizada com sucesso na tabela 'scrappy'.")

    except psycopg2.Error as e:
        print(f"PostgreSQL error: {e}")
    except FileNotFoundError:
        print(f"Error: file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Database connection parameters
    db_params = {
        'host': 'localhost',  # Replace with your PostgreSQL host
        'database': 'postgres', # Replace with your database name
        'user': 'postgres',     # Replace with your database username
        'password': '1234'  # Replace with your database password
    }
    conn = psycopg2.connect(**db_params)    
    cur = conn.cursor()

    cur.execute('SELECT * FROM produtos ORDER BY produto_id')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    

    # Replace with the actual path of your CSV file
    csv_file_path = 'scrap_result.csv' 

    # Check if file exists
    if not os.path.exists(csv_file_path):
        print('ERRO: ARQUIVO NÃO EXISTE')
    else:
        # Load data into the database
        load_csv_to_postgres(csv_file_path, db_params)
