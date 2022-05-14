import plotly as plotly
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt

with st.echo(code_location='below'):
    """
    # датасет movies (с ресурса data.world, загружен пользователем jamesgaskin)
    """

    @st.cache
    def get_data():
        data_url = (
        "https://raw.githubusercontent.com/studenteconomist/reposetory-1/"
        "master/movies.csv"
        )
        return (
        pd.read_csv(data_url))

    df = get_data()
    new_order =df.groupby(by=["genre"])["runtime"].median().iloc[::-1].index
    """
    ##  библиотека seaborn. 
    ### рис. 1 зависимость длинны фильма отжанра
    """
    fig, ax = plt.subplots()
    sns.violinplot(x='genre', y='runtime', data=df, order=new_order)
    plt.xticks(rotation=90)
    plt.title("длины фильмов разных жанров")
    st.pyplot(fig)

    """
    ### mpaa_rating - это степень запрещенности фильмадетям  

привожу     расшифровку названий  степеней запрета: G – General Audiences
All ages admitted. Nothing that would offend parents for viewing by children.
PG – Parental Guidance Suggested
Some material may not be suitable for children. Parents urged to give "parental guidance". May contain some material parents might not like for their young children.
PG-13 – Parents Strongly Cautioned
Some material may be inappropriate for children under 13. Parents are urged to be cautious. Some material may be inappropriate for pre-teenagers.
R – Restricted
Under 17 requires accompanying parent or adult guardian. Contains some adult material. Parents are urged to learn more about the film before taking their young children with them.
NC-17 – Adults Only.  
рисунок 2
    """
    sns.set(rc={'axes.facecolor': 'lightblue', 'figure.facecolor': 'lightgreen'})
    fig, ax = plt.subplots()
    sns.barplot(x="budget", y="mpaa_rating", data=df)
    plt.title("связь бюджета с категорией запрещен детям")
    st.pyplot(fig)

    """
    рисунок 3
    """

    fig, ax = plt.subplots()
    sns.histplot(data=df, x='mpaa_rating', y='rating', cbar=True)
    plt.title("успешность фильма в зависимости от категории запрещен детям")
    st.pyplot(fig)

    """
        ## библиотека альтаир
    """

    fig1 = alt.Chart(df).mark_point().encode(x='budget', y='runtime', color=alt.Color('genre', legend=alt.Legend(title="genre by color")),
                                        tooltip=['release_date', 'budget']).interactive()

    st.altair_chart(
        (
            fig1
        ).interactive()
    )