import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random
import os

fake = Faker('es_ES')
Faker.seed(42)
random.seed(42)

class UniversityDataGenerator:
    def __init__(self):
        self.faculties = ['Ingenieria', 'Medicina', 'Derecho', 'Artes', 'Economia']
        self.departments = ['Recursos Humanos', 'Investigacion', 'Infraestructura', 'Docencia', 'Administracion']

    def generate_staff(self, num_records = 100):
        data = []
        for _ in range(num_records):
            facultad = random.choice(self.faculties) if random.random()>0.05 else None

            sueldo = round(random.uniform(1500, 8000), 2)
            if random.random()<0.03:
                sueldo = sueldo * -1

            record = {
                'ID_Empleado': fake.unique.random_number(digits = 5),
                'Nombre': fake.name(),
                'Email': fake.email(),
                'Facultad': facultad,
                'Fecha_Contratacion': fake.date_between(start_date='-10y', end_date = 'today'),
                'Sueldo_Base': sueldo,
                'Categoria': random.choice(['Titular', 'Adjunto', 'Auxiliar', 'Invitado'])
            }
            data.append(record)
        df = pd.DataFrame(data)

        duplicates = df.sample(n=5)
        df = pd.concat([df, duplicates], ignore_index=True)

        return df

    def generate_budget_transactions(self, num_records = 500):
        data = []
        for _ in range(num_records):
            fecha = fake.date_between(start_date='-2y', end_date='today')
            tipo_gasto = random.choice(['Nomina', 'Equipamiento', 'Software', 'Mantenimiento', 'Viaticos'])
            # investigacion gasta mas equipamiento

            depto = random.choice(self.departments)
            monto = round(random.uniform(100, 5000), 2)

            if depto == 'Investigacion' and tipo_gasto == 'Equipamiento':
                monto = monto * 3

            record = {
                'ID_Transaccion': fake.uuid4(),
                'Departamento': depto,
                'Fecha': fecha,
                'Tipo_Gasto': tipo_gasto,
                'Monto': monto,
                'Descripcion': fake.sentence(nb_words=6),
                'Aprobado': random.choice([True, True, True, False])
            }
            data.append(record)

        df = pd.DataFrame(data)

        mask = df.sample(frac = 0.1).index
        df.loc[mask, 'Fecha'] = df.loc[mask, 'Fecha'].apply(lambda x: x.strftime('%d/%m/%Y'))

        return df

    def save_to_csv(selfself, df, filename):
        cwd = os.getcwd()
        if os.path.basename(cwd) =='python_scripts':
            output_path = os.path.join('..', 'data_raw', filename)
        else:
            output_path = os.path.join('data_raw', filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print("Archivo generado.")

if __name__ == '__main__':
    print("Iniciando generador de datos del Sistema Universitario...")

    generator = UniversityDataGenerator()

    df_staff = generator.generate_staff(num_records = 150)
    generator.save_to_csv(df_staff, 'RRHH_Docentes_Raw.csv')

    df_budget = generator.generate_budget_transactions(num_records = 1000)
    generator.save_to_csv(df_budget, 'Finanzas_Presupuesto_Raw.csv')

    print("Generacion completada con exito.")