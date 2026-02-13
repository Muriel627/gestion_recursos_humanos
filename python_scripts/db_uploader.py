import pandas as pd
from sqlalchemy import create_engine
import os

def upload_to_sql():
    connection_string = "mssql+pyodbc://LAPTOP-IMRL5HBS/UniversidadDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
    engine = create_engine(connection_string)

    print("Iniciando carga a SQL Server...")

    # cargar docentes
    df_docentes = pd.read_csv(os.path.join('data_raw', 'RRHH_Docentes_Raw.csv'))
    df_docentes.to_sql('Staging_Docentes', con=engine, if_exists='replace', index=False)
    print("Tabla Staging_Docentes cargada.")

    # cargar presupuesto
    df_presupuesto = pd.read_csv(os.path.join('data_raw', 'Finanzas_Presupuesto_Raw.csv'))
    df_presupuesto.to_sql('Staging_Presupuesto', con=engine, if_exists='replace', index=False)
    print("Tabla Staging_Presupuesto cargada.")


if __name__ == "__main__":
    upload_to_sql()