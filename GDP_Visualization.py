import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.read_csv('https://github.com/Manouella-helou/GDP_Visualization/blob/main/gdp_1960_2020.csv')
st.title('GDP Visualizations')
#plot the GDP in Asia line chart with a selecting country feature
# to add a subheader and information about the chart 
st.subheader('GDP in Asia')
st.markdown("The chart below depicts the GDP of Asian countries from 1960 to 2020. Please use the dropdown menu to choose a specific country.")
#to add the selecting country feature
selected_countries_asia=st.multiselect('Select Country:',df.query("state=='Asia'")['country'].unique())
df_filtered_asia=df[df['country'].isin(selected_countries_asia)&(df['state']=='Asia')]

fig_asia=px.line(df_filtered_asia,x="year",y="gdp",color="country", title="GDP in Asia")
st.plotly_chart(fig_asia)
if st.checkbox("Analysis of GDP in Asia"):
    st.write("""
    China has the highest GDP in Asia, positioning it as a dominant economic force in the region. This economic supremacy places it in direct competition with major Asian economies like Japan, India, South Korea, and others. These countries vie for market share and influence in diverse sectors, including technology, manufacturing, trade, and finance. The competition in Asia reflects the complex and dynamic economic landscape, where China's economic strength and growth trajectory contribute to its influential role in regional and global affairs. Additionally, when comparing China's GDP growth with Japan's, China's impressive economic growth, from 59.72 billion in 1960 to 14.73 trillion in 2020, underscores its emergence as a powerful regional and global player. Japan, with a more modest growth from 59.22 billion in 1961 to 5.05 trillion in 2019, reflects its advanced industrial base and demographic challenges. The comparison highlights China's rapid ascent in the Asian region, driven by factors such as a large population, export-oriented policies, and market reforms, while Japan's growth is influenced by its technological innovation and skilled workforce. Both nations play pivotal roles in Asian and global trade, shaping the economic dynamics of the region.

    On the other hand, Timor-Leste, one of the youngest nations in Asia, has one of the lowest GDPs in the region. Several factors contribute to this situation, including a small population, heavy reliance on oil and gas exports, infrastructure challenges, institutional capacity issues, geopolitical factors, and limited economic diversification. These challenges underline the nation's need for investment in infrastructure, diversification, and improvements in governance to foster economic stability and growth.
    """)
#plot the GDP in Oceania with a country check box feature and a year slider feature
st.subheader('GDP in Oceania')
st.markdown("The chart below illustrates the GDP data for Oceania countries spanning from 1960 to 2020. You can select a specific country from the dropdown menu and utilize the year slider to examine the GDP for a particular year.")
#to add the slider feature
selected_year_Oceania=st.slider('Select a year:', min_value=int(df.query("state=='Oceania'")['year'].min()),max_value=int(df.query("state=='Oceania'")['year'].max()))
#to add the checkbox feature
selected_countries_oceania = []
for country in df.query("state == 'Oceania'")['country'].unique():
    checkbox = st.checkbox(country)
    if checkbox:
        selected_countries_oceania.append(country)
df_filtered_oceania=df[(df['year'] == selected_year_Oceania) & df['country'].isin(selected_countries_oceania) & (df['state']=='Oceania')]
fig_oceania=px.histogram(df_filtered_oceania,x="country",y="gdp",title=f'GDP in Oceania in {selected_year_Oceania}')
st.plotly_chart(fig_oceania)
if st.checkbox("Analysis of GDP in Oceania"):
    st.write("""
    Australia has a significantly larger and more diversified economy compared to New Zealand. Australia's GDP increased from 18.58 billion in 1960 to a substantial 1.33 trillion in 2020, demonstrating remarkable economic growth. This growth can be attributed to its diverse industries and abundant natural resources. In contrast, New Zealand's GDP, while still significant, grew from 5.49 billion in 1960 to 212.48 billion in 2020. New Zealand's economy is more reliant on agriculture and tourism, and it is known for its high quality of life.

    It's important to note that within the Oceania region, there are many countries with relatively smaller GDPs. These smaller nations often face unique economic challenges due to their size, limited resources, and geographical isolation. The economic landscape in Oceania is diverse, with a few larger economies, such as Australia and New Zealand, surrounded by numerous smaller economies with varying levels of economic development and GDP.
    """)

