import streamlit as st
import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import seaborn as sns
import eda_integration_support as eis

df = pd.read_csv(r'.\movies.csv')
df1 = pd.read_csv(r'.\ratings2.csv')

st.title('      INTERNSHIP FINAL PROJECT')
st.header(' 🎥 MOVIE RECOMMENDATION SYSTEMS  🎥')
st.write('Select datainfo for all the basic information regarding the dataset')
st.write('Select eda to get the visualizations')
st.write('Select get recommendations to get the top 10 movies recommended for you')

x = st.radio(label="", options=('DATA INFO', 'EDA', 'GET RECOMMENDATIONS'))

if x == 'DATA INFO':
    st.write('Here is First 5 rows of dataset')
    st.dataframe(df.head())

    st.write('Here is Last 5 rows of dataset')
    st.dataframe(df.tail())

    st.write('Here is description of dataset')
    st.dataframe(df.describe())

    st.write('Here is shape of our dataset')
    st.write('The number of rows in the dataset are')
    st.write(df.shape[0])
    st.write('The number of columns in the dataset are')
    st.write(df.shape[1])

    st.write('Here we see the columns of dataset')
    st.write(df.columns)

    st.write('Here we see the info of dataset')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()

    st.text(s)

    st.write('You can find the link for the dataset  https://www.kaggle.com/rounakbanik/movie-recommender-systems/data')

if x == 'EDA':
    st.title('Budget')
    fig = plt.figure(figsize=(10, 10))
    df['budget'].plot(logy=True, kind='hist')
    plt.xlabel('budget')
    st.pyplot(fig)
    st.write("The distribution of movie budgets shows an exponential decay.")

    st.title('Genres-Wordcloud')
    # image = Image.open(r'C:\Users\Admin\Desktop\Images\genres.png')
    # st.image(image)
    st.write('As we inferentiate that most common word is Drama,Romantic,Comedy')

    st.title("Language vs count")
    lang_df = pd.DataFrame(df['original_language'].value_counts())
    lang_df['language'] = lang_df.index
    lang_df.columns = ['number', 'language']
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x='language', y='number', data=lang_df.iloc[1:13])
    st.pyplot(fig)
    st.write(
        "Maximum number of language used is English as count 22299 followed by French,Italian")

    st.title('Overview-Wordcloud')
    # image = Image.open(r'C:\Users\Admin\Desktop\Images\Overview.png')
    # st.image(image)
    st.write("Life is the most commonly used word in Overview,followed by 'one' and 'find' are the most Movie Blurgs.Together with Love, Man and Girl, these wordclouds give us a pretty good idea of the most popular themes present in movies.")

    st.title('Popularity')
    fig = plt.figure(figsize=(10, 10))
    df['popularity'].plot(logy=True, kind='hist')
    plt.xlabel('popularity')
    st.pyplot(fig)
    st.write("As the popularity score it seems to be extremely right skewed data with the mean of 2.7 and maximum reaching upto 294 and the 75% percentile is at 3.493 and almost all the data below 75%")

    fig = plt.figure(figsize=(10, 10))
    axis1 = sns.barplot(x=df['vote_average'].head(10),
                        y=df['title'].head(10), data=df)
    plt.xlim(4, 10)
    plt.title('Best Movies by average votes', weight='bold')
    plt.xlabel('Weighted Average Score', weight='bold')
    plt.ylabel('Movie Title', weight='bold')
    st.pyplot(fig)
    st.write(
        "By the vote average we inferetiate that 'Toy Story'occupied the 1st position")

    st.title('Title-Wordcloud')
    # image = Image.open(r'C:\Users\Admin\Desktop\Images\Title.png')
    # st.image(image)
    st.write("As we can see 'LOVE' the title is common in most of the Movie title followed by 'LIFE','GIRL','MAN' and 'NIGHT'")

    plt.title('Released_year vs movies', weight='bold')
    year_df = pd.DataFrame(df['release_year'].value_counts())
    year_df['year'] = year_df.index
    year_df.columns = ['number', 'year']
    fig = plt.figure(figsize=(12, 5))
    sns.barplot(x='year', y='number', data=year_df.iloc[1:20])
    st.pyplot(fig)
    st.write(
        "By the Relaesed_year we inferetiate that Most number of movies released in 2006")

    scored_df = df1.sort_values('rating', ascending=False)
    fig = plt.figure(figsize=(10, 10))
    ax = sns.barplot(x=scored_df['rating'].head(
        10), y=scored_df['title'].head(10), data=scored_df, palette='deep')
    plt.title('Best Rated & Most Popular Blend', weight='bold')
    plt.xlabel('Score', weight='bold')
    plt.ylabel('Movie Title', weight='bold')
    st.pyplot(fig)
    st.write("This are the top 10 movie title recieved 5 ratings")

    fig = plt.figure(figsize=(10, 10))
    ax = sns.distplot(df['vote_average'])
    plt.title('Vote Average', weight='bold')
    plt.xlabel('Vote_Average', weight='bold')
    plt.ylabel('Density', weight='bold')
    st.pyplot(fig)
    st.write("There is a very small correlation between Vote Count and Vote Average. A large number of votes on a particular movie does not necessarily imply that the movie is good.")

    # popularity=df.sort_values('popularity',ascending=False)
    fig = plt.figure(figsize=(10, 10))
    ax = sns.barplot(x=df['popularity'].head(
        10), y=df['title'].head(10), data=df)
    plt.title('Most Popular by votes', weight='bold')
    plt.xlabel('Score of popularity', weight='bold')
    plt.ylabel('Movie Title', weight='bold')
    st.pyplot(fig)
    st.write("From the popularity based ,we inferentiate that 'Toy story'  occupied the 1st position followed by 'Heat' and 'Jumaji' respectively.")

    fig = plt.figure(figsize=(10, 10))
    ax = sns.distplot(
        df[(df['runtime'] < 300) & (df['runtime'] > 0)]['runtime'])
    plt.title('Runtime', weight='bold')
    plt.xlabel('Runtime', weight='bold')
    plt.ylabel('Density', weight='bold')
    st.pyplot(fig)
    st.write("Here we count that runtime is less than 300 but greater than 0 ")

    fig = plt.figure(figsize=(10, 10))
    year_runtime = df[df['release_year'] != 'NaT'].groupby('release_year')[
        'runtime'].mean()
    plt.plot(year_runtime.index, year_runtime)
    plt.xticks(np.arange(1900, 2024, 10.0))
    plt.title('Runtime vs Year_trend', weight='bold')
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Runtime in min', weight='bold')
    st.pyplot(fig)
    st.write("As we can inference that trends go down on 1917 till 50 min and gain it increse upto 110 almost the ranges lies 90 to 110")

    fig = plt.figure(figsize=(10, 10))
    sns.distplot(df['budget'])
    plt.title('Budget', weight='bold')

    st.pyplot(fig)
    st.write("The distribution of movie budgets shows an exponential decay.")

    # for EDA based on Uni, Bi and MultiVariate, refer to eda_integration_support.py for more info.
    eis.controller(df)
