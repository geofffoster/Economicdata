import pandas as pd
from datetime import date

import yfinance as yf
import numpy as np
import plotly.offline as pyo
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff

import cufflinks as cf
from cufflinks import tools
cf.go_offline()

import wbgapi as wb

import streamlit as st

st.title('Trading Economics Data ')


tab1, tab2,   = st.tabs(["Renewable Energy", "Commodities"])


with tab1:
    st.header("Renewable Energy")
    ren=wb.data.DataFrame('EG.ELC.RNEW.ZS',
                      ['DEU','FRA','ESP','GBR','USA'],
                      time=range(2000,2021,5))

    fig = ren.iplot(asFigure=True, kind='bar', title='Renewable Energy')
    st.plotly_chart(fig, use_container_width=True)


with tab2:
    st.header("Commodities")


    data1 = pd.read_html('https://tradingeconomics.com/currencies')
    Currency = data1[0].set_index('Major')
    Currency['YoY'] = Currency['YoY'].str.rstrip("%").astype(float)
    Currency['Monthly'] = Currency['Monthly'].str.rstrip("%").astype(float)
#, dimensions= (800,300)

    fig10 = Currency[['YoY', 'Monthly']].iplot(asFigure=True, dimensions= (800,250),
        subplots=True, kind='bar', title='Currencies YoY and Monthly')
    st.plotly_chart(fig10, use_container_width=True)

