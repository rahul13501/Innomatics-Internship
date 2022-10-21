# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:39:30 2022

@author: ACER
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns
import datetime
from collections import Counter
import plotly.express as px

month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
               'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def writer(data, t):
    if t != 1:
        st.write(data)
        return
    st.title(data)


def display(fig_data):
    st.pyplot(fig_data)


def get_month(x):
    try:
        return month_order[int(str(x).split('-')[1]) - 1]
    except:
        return np.nan


def get_day(x):
    try:
        year, month, day = (int(i) for i in x.split('-'))
        answer = datetime.date(year, month, day).weekday()
        return day_order[answer]
    except:
        return np.nan

### ------------------ Univariate Analysis -------------------###


def gerns(df):
    """ For gerns """

    writer("1. Gernes", 1)

    count = Counter(df["genres"])
    count = count.most_common()[:20]

    x, y = map(list, zip(*count))

    fig_1 = plt.figure(figsize=(15, 7))
    g = sns.barplot(y, x, data=df)
    g.set_ylabel("genres")

    plt.title("TV series genres ", fontsize=20)

    plt.ylabel("Genre", fontsize=20)

    plt.xlabel("Count", fontsize=20)

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=17)

    display(fig_1)
    writer("Obsevation - As per the above count plot it seems there is highest no.of TV series gener are Drama as compared to the other TV series.", 0)


def lang_of_series(df):
    """ Language of Tv series """

    writer(" ", 0)
    writer("2. Languages of the TV series", 1)

    count = Counter(df["original_language"])
    count = count.most_common()[:20]
    x, y = map(list, zip(*count))

    fig_4 = plt.figure(figsize=(15, 7))

    g = sns.barplot(y, x)
    g.set_ylabel("Languages")

    plt.title("TV series languages ", fontsize=20)

    plt.ylabel("languages", fontsize=20)
    plt.xlabel("Count", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=17)

    display(fig_4)
    writer("Obsevation - As per the above count plot of languages it seems there is highest no.of TV series are in English", 0)


def series_cast(df):
    """Used for TV series cast count"""

    writer(" ", 0)
    writer("3. TV series Cast", 1)

    count = Counter(df["cast"])
    count = count.most_common()[:20]
    x, y = map(list, zip(*count))

    fig_5 = plt.figure(figsize=(15, 16))

    g = sns.barplot(y, x)
    g.set_ylabel("Language")

    plt.title("TV series cast ", fontsize=20)

    plt.ylabel("cast", fontsize=20)
    plt.xlabel("Count", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=17)

    display(fig_5)
    writer("Obsevation - As per the above count plot of cast it seems GeorgesMeeleis has acted in many TV series", 0)


def tv_crew(df):
    """Used for TV crew count"""

    writer(" ", 0)
    writer("4. TV series Crew", 1)

    count = Counter(df["crew"])
    count = count.most_common()[:20]
    x, y = map(list, zip(*count))

    fig_6 = plt.figure(figsize=(15, 10))

    g = sns.barplot(y, x)
    g.set_ylabel("Crew")

    plt.title("TV series crew ", fontsize=20)
    plt.ylabel("cast", fontsize=20)
    plt.xlabel("Count", fontsize=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=17)

    display(fig_6)
    writer("Obsevation - As per the above count plot of crew it seems JohnFord has directed many TV series", 0)


def num_movies(df):
    """ No. of movies per month """

    df['day'] = df['release_date'].apply(get_day)
    df['month'] = df['release_date'].apply(get_month)
    fig = plt.figure(figsize=(12, 6))
    writer("# Number of Movies released in a particular month.", 1)
    sns.countplot(x='month', data=df, order=month_order)
    display(fig)
    writer("Obseravtion - As per the above count plot of released date here it seems number of movies has released in month of January", 0)


def prod_per_countries(df):
    """TV series production per country"""
    writer(" ", 0)
    writer("# No. of TV series produced per Country", 1)
    fig_2 = plt.figure(figsize=(5, 5))
    df['production_countries'].value_counts().head(
        10).plot(kind='pie', autopct='%1.1f%%')
    display(fig_2)
    writer("Obseravation - As per the pie plot it seems USA has high production rate of making TV series", 0)


def word_cloud_gerns(df):
    """Word cloud for gerns in dataset"""

    writer(" ", 0)
    writer("# Word Cloud for Gerns", 1)

    df['genres'] = df['genres'].astype('str')
    genres_corpus = ' '.join(df['genres'])

    title_wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white',
                                height=2000, width=4000).generate(genres_corpus)

    fig_3 = plt.figure(figsize=(16, 8))
    plt.imshow(title_wordcloud)
    plt.axis('off')
    display(fig_3)


def numerics(df):
    """Numerical Data"""
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    return numerical_cols


def hist(df, nms):
    """Histogram from dataset"""

    writer(" ", 0)
    writer("1. Histogram", 1)

    fig_7 = plt.figure(figsize=(20, 20))

    for i, col in enumerate(nms[:-1]):
        plt.subplot(10, 3, i+1)
        plt.hist(df[col])
        plt.xlabel(col)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    display(fig_7)


def dist(df, nms):
    """distribution plot from dataset"""

    writer(" ", 0)
    writer("2. Distribution plot", 1)

    fig_8 = plt.figure(figsize=(20, 20))

    for i, col in enumerate(nms[:-1]):
        plt.subplot(10, 3, i+1)
        sns.distplot(df[col], bins=20, kde=True, rug=True)
        plt.xlabel(col)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    display(fig_8)


def box_plot(df, nms):
    """Box plot from dataset"""

    writer(" ", 0)
    writer("3. Box plot", 1)

    fig_9 = plt.figure(figsize=(20, 20))

    for i, col in enumerate(nms[:-1]):
        plt.subplot(10, 3, i+1)
        sns.boxplot(df[col])
        plt.xlabel(col)
        plt.subplots_adjust(left=0.1,
                            bottom=0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    display(fig_9)


def Univariate(df):
    """Controls the univariate block"""

    writer("Univariate Analysis", 1)
    writer(" ", 0)
    writer("# Categorical Columns", 1)

    gerns(df)
    lang_of_series(df)
    series_cast(df)
    tv_crew(df)
    num_movies(df)
    prod_per_countries(df)
    word_cloud_gerns(df)
    writer(" ", 0)
    writer("# All Nemericals Columns", 1)
    nms = numerics(df)
    hist(df, nms)
    dist(df, nms)
    box_plot(df, nms)

    writer("Conlusion: ", 1)
    data = ["1. Very few TV series has generated the higher revenue as shown in the histogram.",
            "2. The Vote average of the TV series between range 3 to 9 as shown in the bar plot.", "3. The Vote average column is normally distrubuted as shown in the distribution plot",
            "4. The runtime column has right tail which means it is right skewed as per the distribution plot."]
    for i in data:
        writer(i, 0)

### ------------------ Bivariate Analysis -------------------###


def rev_vs_month(df):
    """finds the month in which max revenue was generated"""

    writer(" ", 0)
    writer("# Month with Max Revenue", 1)

    fig_10 = plt.figure(figsize=(17, 5))
    plt.subplot(1, 2, 1)
    sns.barplot(x='month', y='revenue', data=df)
    display(fig_10)
    writer("Observation - As per the above sub plot we see highest revenue has generated in month of July", 0)


def rev_per_country(df):
    """finds the country with max. generated revenue"""

    writer(" ", 0)
    writer("# Country with Max. generated Revenue", 1)

    fig_10 = plt.figure(figsize=(17, 5))
    plt.subplot(1, 2, 1)
    sns.barplot(data=df.head(20), x='revenue', y='production_countries')
    display(fig_10)
    writer("Observation - As per the above sub plot we see highest revenue has generated by United Kingdom USA", 0)


def ten_pop_series(df):
    """finds the top ten popular series"""

    writer(" ", 0)
    writer("# Country with Max. generated Revenue", 1)

    popular = df.sort_values('popularity', ascending=False).reset_index()[:10]

    fig1 = px.bar(popular, popular['popularity'], popular['title'],
                  title='Popular Movies', color='vote_average')
    st.plotly_chart(fig1)
    writer("Observation - As per the above bar plot we can see Wonder Woman is very polpular TV series as popularity is at 7.2", 0)


def profit_vs_budget(df):
    """finds profit vs budget"""

    writer(" ", 0)
    writer("# Profit vs Budget", 1)

    df['profit'] = df['revenue'] - df['budget']

    fig = px.scatter(df, df['budget'], df['profit'], title='Profit vs Budget',
                     color='vote_average', size='revenue',  hover_data=['title'])

    st.plotly_chart(fig)
    writer("Observation - As per the above scatter plot between profit and budget we can see the TV series which has generated highest profit is range between 200M to 250M", 0)


def profit_vs_revenue(df):
    """finds profit vs revenue"""

    writer(" ", 0)
    writer("# Profit vs Revenue", 1)

    df['profit'] = df['revenue'] - df['budget']

    fig = px.scatter(df, df['revenue'], df['profit'], title='Profit vs revenue',
                     color='vote_average', size='revenue',  hover_data=['title'])

    st.plotly_chart(fig)
    writer("Observation - As per the scatter plot between profit and revenue we can see the higher revenue the higher profit which is directly propotional to ecah other", 0)


def bivariate(df):
    "Controls the bivariate block"

    writer(" ", 0)
    writer("Bivariate Analysis", 1)

    rev_vs_month(df)
    rev_per_country(df)
    ten_pop_series(df)
    profit_vs_budget(df)
    profit_vs_revenue(df)

### ------------------ Multivariate Analysis -------------------###


def plot1(df):
    """ Budget vs profit for production countries """

    fig_11 = plt.figure(figsize=(25, 8))
    sns.scatterplot(df["budget"], df["profit"],
                    hue=df["production_countries"].head(100))

    display(fig_11)


def plot2(df):
    """ revenue vs profit for production countries """

    fig_12 = plt.figure(figsize=(25, 8))
    sns.scatterplot(df["revenue"], df["profit"],
                    hue=df["production_countries"].head(100))

    display(fig_12)


def multivariate(df):
    "Controls the Multivariate block"

    writer(" ", 0)
    writer("Multivariate Analysis", 1)

    plot1(df)
    plot2(df)

    writer("Conclusion: ", 1)

    data = ["1. United state of America has generated highest profit with low budget.",
            "2. United state of America has highest revenue with highest profit.",
            "3. United state of America has genreated highest profit of 2.5B."]
    for d in data:
        writer(d, 0)


def controller(df):
    """ Calls all the varaite blocks """
    Univariate(df)
    bivariate(df)
    multivariate(df)


if __name__ == "__main__":
    print("Use the main file plaese!!")
    print("To use just do: ")
    print(" import eda_integration_support as eis ")
    print(" eis.controller(df) ")
    print("We belive in organized and easy to use systems, if any doubt please contact!")
