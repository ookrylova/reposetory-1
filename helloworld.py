import plotly as plotly
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt

with st.echo(code_location='below'):
    """
    # поработаю с тем же датасетом, который использовался в питоновском файле в другой части моего проекта. датасет про количество смерти ей заболевших по counties (областям внутри штатов США). в юпитере я избавилась от столбца counties, но сейчас нарисую про него график. 
    оставлю из этой огромной таблицы данные только за 11 июня 2022, но даже после этого в таблице 3 тысяч строк, так что на стримлете запустится не сразу. столбец FIPS – это номер county, т.е. области внутри штата.  
    """

    @st.cache
    def get_data():
        data_url = (
        "https://raw.githubusercontent.com/nytimes/covid-19-data/"
        "master/us-counties-recent.csv"
        )
        return (
        pd.read_csv(data_url))

    df_covid = get_data()
    df_cov_11 = df_covid[df_covid['date'] == '2022-06-11']
    """
    ##  библиотека seaborn. 
    ### рис. 1 зависимость кол-ва кейсов от county
    """
    fig, ax = plt.subplots()
    sns.violinplot(x='county', y='cases', data=df_cov_11)
    plt.xticks(rotation=90)
    plt.title("заболеваемость по counties")
    st.pyplot(fig)

    """
    ###  рисунок 2
    """
    sns.set(rc={'axes.facecolor': 'lightblue', 'figure.facecolor': 'lightgreen'})
    fig, ax = plt.subplots()
    sns.barplot(x="deaths", y="state", data=df_cov_11)
    plt.title("смертность по counties")
    st.pyplot(fig)

    """
    рисунок 3
    """

    fig, ax = plt.subplots()
    sns.histplot(data=df_cov_11, x='cases', y='deaths', cbar=True)
    plt.title("смертность в зависимости от заболеваемости")
    st.pyplot(fig)

    """
        ## библиотека альтаир
    """

    fig1 = alt.Chart(df_cov_11).mark_point().encode(x='deaths', y='cases', color=alt.Color('state', legend=alt.Legend(title="state by color")),
                                        tooltip=['county', 'deaths']).interactive()

    st.altair_chart(
        (
            fig1
        ).interactive()
    )