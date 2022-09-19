#Leonardo Eliezer Santos Rodrigues 3°Ano de Informática

#Importando as bibliotecas
import pandas as pd
import numpy as np #Numpy
import pandas as pd #Pandas
import matplotlib.pyplot as plt #Matplotlib
from sklearn.linear_model import LinearRegression #Regressão linear
from sklearn import metrics #Cálculo do erro
import streamlit as st

#Importando a Base de Dados
rioAptos = pd.read_csv('https://raw.githubusercontent.com/mvinoba/notebooks-for-binder/master/dados.csv')

st.title('Preços de apartamentos')#Título do Streamlit
bairro = st.selectbox('Escolha o bairro', rioAptos['bairro'].unique())#Abrindo a base de dados na coluna "bairro" sem repetições nos nomes
df = rioAptos[rioAptos['bairro'] == bairro]#Puxando a coluna "bairro" na base de dados

df_quartos = df['quartos']#Pegando a coluna "quartos" na base de dados
minimo = int(df_quartos.min())#Setando o número minímo de quartos
maximo = int(df_quartos.max())#Setando o número máximo de quartos
quartos = st.slider("Escolha a quantidade de quartos", minimo, maximo, value=minimo)#Fazendo um Slider com o número minímo e máximo de quartos

df_area = df['area']#Pegando a coluna "area" na base de dados
minimo = int(df_area.min())#Setando o número minímo de area
maximo = int(df_area.max())#Setando o número minímo de area
area = st.slider("Escolha a área", minimo, maximo, value=minimo)#Fazendo um Slider com o número minímo e máximo da area

indep = df[['quartos', 'area']].values.reshape(-1, 2) # variável independente
dep = df['preco'].values.flatten() # variavel dependente

rl = LinearRegression()#Pegando Regressao linear
rl.fit(indep, dep)#Coloca a variavel independente e dependente na Regressão linear

x = [[quartos], [area]] # valor para a variável independente
x_arr = np.array(x).reshape(-1, 2)
y_pred = rl.predict(x_arr)#Predição da variavel dependente

st.write(f"Valor estimado: R$ {int(y_pred.flatten()):,.2f}")#Preço de apartamentos
