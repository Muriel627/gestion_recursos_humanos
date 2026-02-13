from python_scripts.data_generator import UniversityDataGenerator
from python_scripts.db_uploader import upload_to_sql

def run_pipeline():
    print("1. Generando datos...")
    gen = UniversityDataGenerator()

    df_empleados = gen.generate_staff(150)
    gen.save_to_csv(df_empleados, 'RRHH_Docentes_Raw.csv')

    df_finanzas = gen.generate_budget_transactions(2000)
    gen.save_to_csv(df_finanzas, 'Finanzas_Presupuesto_Raw.csv')

    upload_to_sql()
    print("---Proceso finalizado---")



if __name__ == '__main__':
    run_pipeline()


