import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados
car_data = pd.read_csv('vehicles_us.csv')

# Título do dashboard
st.title('Dashboard de Anúncios de Carros Usados')

# Layout em colunas para botões
col1, col2, col3 = st.columns(3)

# 1. Histograma da quilometragem
with col1:
    if st.button('📊 Histograma - Odometer'):
        st.subheader('Distribuição da Quilometragem (Odometer)')
        fig1 = px.histogram(car_data, x="odometer", nbins=30, title='Distribuição da quilometragem')
        st.plotly_chart(fig1, use_container_width=True)

# 2. Gráfico de dispersão: preço x ano
with col2:
    if st.button('💵 Dispersão - Preço x Ano'):
        st.subheader('Relação entre Preço e Ano do Carro')
        fig2 = px.scatter(car_data, x='model_year', y='price',
                          color='condition', title='Preço x Ano por Condição')
        st.plotly_chart(fig2, use_container_width=True)

# 3. Gráfico de pizza
with col3:
    if st.button('🥧 Pizza - Tipo de Transmissão'):
        st.subheader('Proporção de Tipos de Transmissão')
        transmission_counts = car_data['transmission'].value_counts().reset_index()
        transmission_counts.columns = ['transmission', 'count']
        fig3 = px.pie(transmission_counts, values='count', names='transmission', 
                      title='Distribuição dos Tipos de Transmissão')
        st.plotly_chart(fig3, use_container_width=True)

# Rodapé
st.markdown("---")
st.caption("Feito por Matheus Moura - com dados de veículos dos EUA")
