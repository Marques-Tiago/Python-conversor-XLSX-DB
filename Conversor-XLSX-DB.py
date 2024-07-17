import psycopg2
import pandas
from sqlalchemy import create_engine

db_url = 'postgresql+psycopg2://usuario:senha@localhost:porta/database'
engine = create_engine(db_url)

file_path = 'EXP_dicionario.xlsx'

# Carregar todas as planilhas em um dicionário de DataFrames
sheets_dict = pandas.read_excel(file_path, sheet_name=None)

for sheet_name, df in sheets_dict.items():
    # Opcional: Modificar o nome da planilha para um nome de tabela adequado
    table_name = sheet_name.lower().replace(' ', '_')

    # Importar os dados para a tabela no PostgreSQL
    df.to_sql(table_name, engine, index=False, if_exists='replace', schema='nome-do-schema')

    print(f'Tabela {table_name} criada com sucesso.')
