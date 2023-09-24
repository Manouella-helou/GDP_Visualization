import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.read_csv('gdp_1960_2020.csv')
st.title('GDP Visualizations')
#plot the GDP in Asia line chart with a selecting country feature 
st.subheader('GDP in Asia')
#to add the selecting country feature
selected_countries_asia=st.multiselect('Select Country:',df.query("state=='Asia'")['country'].unique())
df_filtered_asia=df[df['country'].isin(selected_countries_asia)&(df['state']=='Asia')]

fig_asia=px.line(df_filtered_asia,x="year",y="gdp",color="country", title="GDP in Asia")
st.plotly_chart(fig_asia)
#plot the GDP in Oceania with a country check box feature and a year slider feature
st.subheader('GDP in Oceania')
#to add the slider feature
selected_year_Oceania=st.slider('Select a year:', min_value=int(df.query("state=='Oceania'")['year'].min()),max_value=int(df.query("state=='Oceania'")['year'].max()))
#to add the checkbox featur
selected_countries_oceania = []
for country in df.query("state == 'Oceania'")['country'].unique():
    checkbox = st.checkbox(country)
    if checkbox:
        selected_countries_oceania.append(country)
df_filtered_oceania=df[(df['year'] == selected_year_Oceania) & df['country'].isin(selected_countries_oceania) & (df['state']=='Oceania')]

fig_oceania=px.histogram(df_filtered_oceania,x="country",y="gdp",title=f'GDP in Oceania in {selected_year_Oceania}')
st.plotly_chart(fig_oceania)
