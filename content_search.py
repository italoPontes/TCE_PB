import streamlit as st  # Importa el módulo streamlit para crear aplicaciones web interactivas
import pandas as pd  # Importa el módulo pandas para manipulación y análisis de datos

# Define el nombre del archivo de entrada que contiene los datos
input_file_name = 'cnpj_ug_dados_gov.csv'

# Lee el archivo CSV y lo carga en un DataFrame de pandas
df = pd.read_csv(input_file_name)

# Establece el título de la aplicación web
st.title("TCE PB - Search Tool")

# Crea una entrada de texto en la aplicación web para que el usuario ingrese su búsqueda
text = st.text_input("Digite o que você busca", "Unidade Gestora (UG), CNPJ, ou Descrição.")

# Define una función de búsqueda que verifica si el texto de búsqueda está en alguna de las variables especificadas
def search(text: str = '', variables: list = ()) -> bool:
    text = str(text).lower()  # Convierte el texto de búsqueda a minúsculas
    # Verifica si el texto de búsqueda está en alguno de los campos de variables, también convertidos a minúsculas
    return any(text in str(field).lower() for field in variables)

# Filtra el DataFrame aplicando la función de búsqueda en las columnas especificadas
df = df[df.apply(lambda x: search(text, 
                                  [x['CNPJ'], 
                                  x['cd_Ugestora'], 
                                  x['NOME FANTASIA'], 
                                  x['Cidade']]), axis=1)]

# Muestra el DataFrame filtrado en la aplicación web
st.dataframe(df)
