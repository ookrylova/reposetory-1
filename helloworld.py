import plotly as plotly
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt

with st.echo(code_location='below'):
    """
    ## мой dataset movies
    """

    @st.cache
    def get_data():
        data_url = (
        "https://raw.githubusercontent.com/ookrylova/reposetory-1/"
        "master/movies.csv"
        )
        return (
        pd.read_csv(data_url))

    df = get_data()
    new_order =df.groupby(by=["genre"])["runtime"].median().iloc[::-1].index
    """
    # fig.1 зависимость длинны фильма отжанра
    """
    fig, ax = plt.subplots()
    sns.violinplot(x='genre', y='runtime', data=df, order=new_order)
    plt.xticks(rotation=90)
    plt.title("длины фильмов разных жанров")
    st.pyplot(fig)

    """
    ## столбики показывают связь бюджета и разрешенности детям
    """
    fig, ax = plt.subplots()
    sns.barplot(x="budget", y="mpaa_rating", data=df)
    st.pyplot(fig)

    """
        ## альтаир
    """

    fig1 = alt.Chart(df).mark_point().encode(x='budget', y='runtime', color='genre',
                                        tooltip=['release_date', 'budget']).interactive()

    st.altair_chart(
        (
            fig1
        ).interactive()
    )