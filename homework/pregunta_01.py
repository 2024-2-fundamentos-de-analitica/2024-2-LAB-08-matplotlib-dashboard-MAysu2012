# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
 
    os.makedirs('output', exist_ok=True)
    generar_grafico_envios_por_bodega(cargar_datos())
    generar_grafico_tipo_envio(cargar_datos())
    generar_grafico_calificacion_clientes(cargar_datos())
    generar_grafico_peso_envios(cargar_datos())
    crear_dashboard()

def cargar_datos():
    """Carga la información del archivo CSV"""
    return pd.read_csv('files/input/shipping-data.csv')

def generar_grafico_envios_por_bodega(df):
    plt.figure()
    df.Warehouse_block.value_counts().plot.bar(
        title='Envíos por Bodega', xlabel='Bodega', ylabel='Cantidad', color='tab:blue', fontsize=8
    )
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.savefig('output/envios_bodega.png')

def generar_grafico_tipo_envio(df):
    plt.figure()
    df.Mode_of_Shipment.value_counts().plot.pie(
        title='Método de Envío', wedgeprops={'width': 0.35}, ylabel='',
        colors=['tab:blue', 'tab:orange', 'tab:green']
    )
    plt.savefig('output/metodo_envio.png')

def generar_grafico_calificacion_clientes(df):
    plt.figure()
    resumen = df.groupby('Mode_of_Shipment')['Customer_rating'].agg(['mean', 'min', 'max'])
    plt.barh(y=resumen.index, width=resumen['max'] - 1, left=resumen['min'], height=0.9, color='lightgray', alpha=0.8)
    colores = ['tab:green' if x >= 3 else 'tab:orange' for x in resumen['mean']]
    plt.barh(y=resumen.index, width=resumen['mean'] - 1, left=resumen['min'], height=0.5, color=colores)
    plt.title('Calificación Promedio Clientes')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.savefig('output/calificacion_clientes.png')

def generar_grafico_peso_envios(df):
    plt.figure()
    df.Weight_in_gms.plot.hist(title='Distribución de Peso Envíos', color='tab:orange', edgecolor='white')
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.savefig('output/peso_envios.png')

def crear_dashboard():
    contenido = """<!DOCTYPE html>
    <html>
        <body>
            <h1>Resumen de Envíos</h1>
            <div style='width: 45%; float: left;'>
                <img src='output/envios_bodega.png' alt='Envíos por Bodega'>
                <img src='output/metodo_envio.png' alt='Método de Envío'>
            </div>
            <div style='width: 45%; float: right;'>
                <img src='output/calificacion_clientes.png' alt='Calificación Promedio'>
                <img src='output/peso_envios.png' alt='Distribución de Peso'>
            </div>
        </body>
    </html>"""
    with open("output/index.html", "w") as f:
        f.write(contenido)

pregunta_01()



