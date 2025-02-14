import mysql.connector

import json



'''
####################################################################
# Código Python para interação com o banco de dados
####################################################################
'''
# Desc: Conexão com o banco de dados a partir da leitura do arquivo database/clinica.conf
# Entrada: None
# Saída: Conexão do banco de dados
def conexaoBD():
    try:
        with open('database/clinica.conf', 'r') as dadosbd: 
            databd = json.load(dadosbd)

        cnx = mysql.connector.connect(user=databd['user'],
                                    password=databd['pass'],
                                    host=databd['host'],
                                    database=databd['database'])
        
        return cnx
    
    except Exception as e:
        print (f"FALHA NA CONEXÃO COM O BANCO: {e}")
    
    


# Desc: Função responsável pelas transações de inserção, atualização e remoção no banco de dados
# Entrada:  1 - STRING com o comando SQL desejado;
#           2 - Tupla com os dados
#           3 - String informando qual o tipo de comando, se INSERT, UPDATE ou DELETE
# Saída: True se tudo ocorreu bem | False se houve alguma falha
def createUpdateDelete(sql:str, tupla:tuple, tipo:str):
    try:
        ##################################
        ###    SEU CÓDIGO AQUI - 1     ###
        ##################################

        return True

    except Exception as e:
        print (f"FALHA NO {tipo} NO BANCO: {e}")
        return False



# Desc: Função responsável pelas consultas (SELECT) no banco de dados
# Entrada:  1 - STRING com o comando SQL SELECT desejado;
#           2 - Tupla com os dados
#           3 - String informando qual o tipo consulta:
#               a) 'fetchall' -> recebo todas as linhas da resposta do SELECT
#               b) 'fetchone' -> recebo apenas a 1ª linha da resposta do SELECT
# Saída: Um dicionario com os dados se tudo ocorreu bem | None, caso tenha ocorrido alguma falha
def read(sql:str, tupla:tuple, tipoRetorno='fetchall'):
    try: 
        conexao = conexaoBD()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(sql, tupla)

        if tipoRetorno == 'fetchone':
            return cursor.fetchone()
        else:
            return cursor.fetchall()
    
    except Exception as e:
        print (f"FALHA NA LEITURA DO BANCO: {e}")
        return None