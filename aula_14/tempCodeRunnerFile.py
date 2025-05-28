#pip install sqlachemy pymysql

from sqlalchemy import create_engine

#variaveis de conexão
host = 'localhost'
user = 'root'
pasword = ''
database = 'db_analise'

#funçãopara realizar a conexão com o banco


def conecta_banco():
    try:
        #  url de conexão com o banco
        engine = create_engine(f'mysql+pymysql://{user}:{pasword}@{host}/{database}')

        with engine.connect() as conexao:
            query = "SELECT *FROM vendas2"

            resultado = conexao.execute(text(query))
            if resultado.rowcount > 0:
                for item in resultado:
                    print(item)  #imprime todas as coluna
                    print(item[0], item[1], item[2])
    except Exception as e:
        print (f'Algo deu errado: {e}')