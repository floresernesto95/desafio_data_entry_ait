from datetime import datetime
import pandas as pd
import glob

class Procesador:
    @staticmethod
    def convertir_excel(df, supplier_name):
        # Asigna el nombre del proveedor a la variable 'supplier_name'.
        supplier_name = supplier_name

        # Obtiene la fecha actual en formato día-mes-año.
        today_date = datetime.now().strftime('%d-%m-%Y')

        # Define la ruta al directorio donde se guardará el archivo Excel.
        path = r'resources/processed'

        # Crea el nombre del archivo, incluyendo la ruta, el nombre del proveedor y la fecha.
        filename = f"{path}/{supplier_name}_{today_date}.xlsx"

        # Guarda el DataFrame 'df' en un archivo Excel, sin incluir el índice.
        df.to_excel(filename, index=False)

    @staticmethod
    def iniciar():
        # AutoRepuestos Express.
        # Lee el archivo Excel, omitiendo las cabeceras predeterminadas.
        df_auto_repuestos = pd.read_excel(
            r'resources/unprocessed/AutoRepuestos Express.xlsx',
            header=None
        )

        # Omite las primeras 10 filas que no forman parte de los datos útiles.
        df_auto_repuestos = df_auto_repuestos.iloc[10:]

        # Establece la primera fila útil como cabecera.
        header = df_auto_repuestos.iloc[0]
        df_auto_repuestos = df_auto_repuestos[2:]
        df_auto_repuestos.columns = header

        # Reinicia el índice del DataFrame y elimina el nombre de las columnas.
        df_auto_repuestos.reset_index(drop=True, inplace=True)
        df_auto_repuestos.columns.name = None

        # Renombra algunas columnas para estandarizar los nombres.
        df_auto_repuestos.rename(columns={'CODIGO PROVEEDOR': 'CODIGO', 'PRECIO DE LISTA': 'PRECIO'}, inplace=True)

        # Filtra las columnas necesarias y corta la descripción a 100 caracteres.
        df_auto_repuestos = df_auto_repuestos[['CODIGO', 'DESCRIPCION', 'MARCA', 'PRECIO']]
        df_auto_repuestos['DESCRIPCION'] = df_auto_repuestos['DESCRIPCION'].str.slice(0, 100)
        df_auto_repuestos['PRECIO'] = df_auto_repuestos['PRECIO'].map(lambda x: f"{x:.2f}")

        # Convierte el DataFrame a Excel.
        Procesador.convertir_excel(df_auto_repuestos, 'AutoRepuestos Express')

        # AutoFix
        # Obtiene todos los archivos Excel que coinciden con el patrón de nombre.
        path = r'resources/unprocessed/'
        all_files = glob.glob(path + "AutoFix Repuestos*.xlsx")

        df_list_auto_fix = []

        # Lee cada archivo y cada hoja dentro del archivo.
        for filename in all_files:
            xls = pd.ExcelFile(filename)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                df['MARCA'] = sheet_name
                df_list_auto_fix.append(df)

        # Estandarización de nombres de columnas y corte de descripciones.
        for i, df in enumerate(df_list_auto_fix):
            df_list_auto_fix[i].rename(columns={'DESCR': 'DESCRIPCION'}, inplace=True)
            df_list_auto_fix[i] = df[['CODIGO', 'DESCRIPCION', 'MARCA', 'PRECIO']]

        # Concatenación de todos los DataFrames.
        df_auto_fix = pd.concat(df_list_auto_fix, ignore_index=True)
        df_auto_fix['DESCRIPCION'] = df_auto_fix['DESCRIPCION'].str.slice(0, 100)
        df_auto_fix['PRECIO'] = df_auto_fix['PRECIO'].map(lambda x: f"{x:.2f}")

        # Conversión a Excel.
        Procesador.convertir_excel(df_auto_fix, 'AutoFix')

        # Mundo RepCar
        # Lectura y procesamiento de datos desde CSV.
        df_rep_car = pd.read_csv(
            r'resources/unprocessed/AutoRepuestos Express Lista de Precios.csv',
            delimiter=';'
        )

        # Combinación de descripciones y estandarización de nombres de columnas.
        # Filtrado, corte de descripciones y conversión de precios.
        df_rep_car['DESCRIPCION'] = df_rep_car['Descripcion'] + " - " + df_rep_car['Rubro']
        df_rep_car.rename(columns={'Marca': 'MARCA', 'Cod. Articulo': 'CODIGO', 'Importe': 'PRECIO'}, inplace=True)
        df_rep_car = df_rep_car[['CODIGO', 'DESCRIPCION', 'MARCA', 'PRECIO']]
        df_rep_car['DESCRIPCION'] = df_rep_car['DESCRIPCION'].str.slice(0, 100)
        df_rep_car['PRECIO'] = df_rep_car['PRECIO'].map(lambda x: f"{x:.2f}")

        # Conversión del DataFrame final a Excel.
        Procesador.convertir_excel(df_rep_car, 'Mundo RepCar')





