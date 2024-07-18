import streamlit as st
import pandas as pd

input_file_name = '../data/cnpj_ug_dados_gov.csv'

df = pd.read_csv(input_file_name)

st.title("TCE PB - Search Tool")

text = st.text_input("Digite o que você busca", "Unidade Gestora (UG), CNPJ, ou Descrição.")

def search(text: str = '',
           variables: list = ()) -> bool:
    text = str(text).lower()
    return any(text in str(field).lower() for field in variables)

df = df[df.apply(lambda x: search(text,
                                  [x['CNPJ'],
                                  x['cd_Ugestora'],
                                  x['NOME FANTASIA'],
                                  x['Cidade']]), axis=1)]

st.dataframe(df)
