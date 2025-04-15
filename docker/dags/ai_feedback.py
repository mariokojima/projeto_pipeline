import requests
import psycopg2
import os
import dotenv
import json





def get_prompt(db_params):
    conn = psycopg2.connect(**db_params)    
    cur = conn.cursor()
    sql = """
        SELECT json_agg(row_to_json(r))
        FROM (
        select 
            sum(s.scrappy_price)/count(1) as preco, 
            TO_CHAR(scrappy_data_insert ::date, 'dd/mm/yyyy') as data, 
            case when s.scrappy_title  like '%710%' then '710ml' else '1100ml' end  capacidade
        from scrappy s 
        group by TO_CHAR(scrappy_data_insert ::date, 'dd/mm/yyyy'), case when s.scrappy_title like '%710%' then '710ml' else '1100ml' end
        ) R
    """
    cur.execute(sql)
    rows = cur.fetchall()
    retorno = json.dumps(str(rows[0][0]))
    print(retorno) 

    prompt = """
    ### INSTRUÇÕES ###
    Analise o conteúdo informado no CONTEXTO,levando em consideração a variação do preço do produto ao passar do tempo. Considerar na análise todas as CAPACIDADES presentes no contexto, informando variações percentuais.
    Retorne um objeto JSON. O output deve parecer com {"analise":"O preço do produto subiu 12% entre 11/04/2023 e 14/04/2025","insight":"uma ação promocional poderia trazer um incremento nas vendas para os dias dos pais"}

    
    ### CONTEXTO ###
    """
    

    return f"{prompt} {retorno}"


def ai_request(db_params):
    request_prompt = get_prompt(db_params)
    # print(request_prompt)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={os.getenv("GEMINI_KEY")}"
    headers = {'Content-Type': 'application/json'}
    payload = {
    "contents": [{
        "parts":[{"text": request_prompt}]
        }],
    "generationConfig": { "response_mime_type": "application/json" }
    }

    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    retorno = json.loads(r.content)['candidates'][0]['content']['parts'][0]['text']
    print(retorno)