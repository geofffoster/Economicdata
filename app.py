import pandas as pd
from datetime import date

import yfinance as yf
import numpy as np
import cufflinks as cf
from cufflinks import tools

cf.go_offline()

import wbgapi as wb

import streamlit as st

st.title('Trading Economics Data ')


tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(["Renewable Energy", "Inflation Rates", "Interest Rates", "Renewables", "Commodity Forecasts", "Commodites"])


with tab1:
    st.header("Renewable Energy")
    ren=wb.data.DataFrame('EG.ELC.RNEW.ZS',
                      ['DEU','FRA','ESP','GBR','USA'],
                      time=range(2000,2021,5))

    fig = ren.iplot(asFigure=True, kind='bar', title='Renewable Energy')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header("Inflation Rates")
    data1 = pd.read_html('https://tradingeconomics.com/country-list/inflation-rate')
    g20_interest_rates = data1[0].set_index('Country')
    data1b = pd.read_html('https://tradingeconomics.com/country-list/consumer-price-index-cpi?continent=g20')
    g20_CPI = data1b[0].set_index('Country')

    data2 = pd.read_html('https://tradingeconomics.com/country-list/inflation-rate?continent=australia')
    aus_interest_rates = data2[0].set_index('Country')
    data2b = pd.read_html('https://tradingeconomics.com/country-list/inflation-rate?continent=australia')
    aus_CPI = data2b[0].set_index('Country')


    fig2 = g20_interest_rates.iplot(asFigure=True, kind='bar', title='G20 Inflation Rates')
    st.plotly_chart(fig2, use_container_width=True)    
    # fig3 = g20_CPI.iplot(asFigure=True, kind='bar', title='G20 Consumer Price Index')
    # st.plotly_chart(fig3, use_container_width=True)
    # fig4 = aus_interest_rates.iplot(asFigure=True,kind='bar', title='Australasia Interest Rates')
    # st.plotly_chart(fig4, use_container_width=True)
    # fig5 = aus_CPI.iplot(asFigure=True,kind='bar', title='Australasia Consumer Price Index')
    # st.plotly_chart(fig5, use_container_width=True)

with tab3:
    st.header("Renewable Energy")
    data1 = pd.read_html('https://tradingeconomics.com/country-list/interest-rate')
    InterestRates = data1[0].set_index('Country')
    fig6 = InterestRates[['Last', 'Previous']].iplot(asFigure=True, kind='bar', title='InterestRates')
    st.plotly_chart(fig6, use_container_width=True)

with tab4:
    st.header("Renewable Energy")
    data1 = pd.read_html('https://tradingeconomics.com/country-list/co2-emissions?continent=g20')
    g20_CO2emissions = data1[0].set_index('Country')
    fig7 = g20_CO2emissions.iplot(asFigure=True, kind='bar', title='G20 CO2 Emissions')
    st.plotly_chart(fig7, use_container_width=True)

with tab5:
    st.header("Commodity Forecasts")
    data1 = pd.read_html('https://tradingeconomics.com/forecast/commodity')
    commodity_forecasts = data1[0].set_index('Energy')
    fig8 = commodity_forecasts[['Q3/22','Q4/22','Q1/23','Q2/23']].iplot(asFigure=True, kind='bar', title='Commodity Forecasts')
    st.plotly_chart(fig8, use_container_width=True)

with tab6:
    st.header("Commodities")
    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    energy = data1[0].set_index('Energy')
    energy['YoY'] = energy['YoY'].str.rstrip("%").astype(float)
    fig9 = energy[['YoY']].iplot(asFigure=True, kind='bar', title='Energy Commodities YoY')
    st.plotly_chart(fig9, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    metals = data1[1].set_index('Metals')
    metals['YoY'] = metals['YoY'].str.rstrip("%").astype(float)
    fig10 = metals[['YoY']].iplot(asFigure=True, kind='bar', title='metals Commodities YoY')
    st.plotly_chart(fig10, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    Agricultural = data1[2].set_index('Agricultural')
    Agricultural['YoY'] = Agricultural['YoY'].str.rstrip("%").astype(float)
    fig11 = Agricultural[['YoY']].iplot(asFigure=True, kind='bar', title='Agricultural Commodities YoY')
    st.plotly_chart(fig11, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    Industrial = data1[3].set_index('Industrial')
    Industrial['YoY'] = Industrial['YoY'].str.rstrip("%").astype(float)
    fig12 = Industrial[['YoY']].iplot(asFigure=True, kind='bar', title='Industrial Commodities YoY')
    st.plotly_chart(fig12, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    Livestock = data1[4].set_index('Livestock')
    Livestock['YoY'] = Livestock['YoY'].str.rstrip("%").astype(float)
    fig13 = Livestock[['YoY']].iplot(asFigure=True, kind='bar', title='Livestock Commodities YoY')
    st.plotly_chart(fig13, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    Index = data1[5].set_index('Index')
    Index['YoY'] = Index['YoY'].str.rstrip("%").astype(float)
    fig14 = Index[['YoY']].iplot(asFigure=True, kind='bar', title='Index Commodities YoY')
    st.plotly_chart(fig14, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/commodities')
    Electricity = data1[6].set_index('Electricity')
    Electricity['YoY'] = Electricity['YoY'].str.rstrip("%").astype(float)
    fig15 = Electricity[['YoY']].iplot(asFigure=True, kind='bar', title='Electricity Commodities YoY')
    st.plotly_chart(fig15, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/bonds')
    Major10Y = data1[0].set_index('Major10Y')
    Major10Y['YoY'] = Major10Y['YoY'].str.rstrip("%").astype(float)
    fig16 =  Major10Y[['YoY']].iplot(asFigure=True, kind='bar', title='Major10Y Bonds YoY')
    st.plotly_chart(fig16, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/bonds')
    Bonds = data1[0].set_index('Major10Y')
    Bonds['Yield'] = Bonds['Yield']#.str.rstrip("%").astype(float)
    fig17 =  Bonds[['Yield']].iplot(asFigure=True, kind='bar', title='Major10Y Bonds Yield')
    st.plotly_chart(fig17, use_container_width=True)

    data1 = pd.read_html('https://tradingeconomics.com/currencies')
    Currency = data1[0].set_index('Major')
    Currency['YoY'] = Currency['YoY'].str.rstrip("%").astype(float)
    Currency['Monthly'] = Currency['Monthly'].str.rstrip("%").astype(float)
    fig20 = Currency[['YoY', 'Monthly']].iplot(asFigure=True, dimensions= (800,250),
        subplots=True, kind='bar', title='Currencies YoY and Monthly')
    st.plotly_chart(fig20, use_container_width=True)

