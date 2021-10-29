import streamlit as st
from utils.tweet_scraping import *
from utils.tweet_analysis import *
from utils.figures import *

# Configuration of Streamlit page
st.set_page_config(
    page_title="Feeling of Twitter on ...",
    layout='centered',
    initial_sidebar_state="collapsed")

#TODO: Sidebar information

# Title
st.markdown(f"<h1 style='text-align: center;'>Feeling of Twitter on ...</h1>", unsafe_allow_html=True)

# Getting user's hashtags
hashtags_to_scrape = ''
hashtag = st.text_input('Wich # would you like to analyse ?', value="SquidGame")
if hashtag:
    hashtag_clean = clean_input(hashtag)
    if len(hashtag_clean) != 0:
        hashtags_to_scrape += hashtag_clean

if len(hashtags_to_scrape) == 0:
    hashtags_to_scrape = 'empty'

st.write(f'Current hashtags: __{hashtags_to_scrape}__')

number_tweets = st.slider('How many tweets do you want to analyze? (The more, the longer the processing time)', 0, 1000, 100)


# Selecting a language
selected_language = st.selectbox('Which language are you interested in?',
                                 ('English', 'French', 'German', 'Dutch', 'Spanish'))
if selected_language == 'English':
    language = 'en'
elif selected_language == 'French':
    language = 'fr'
elif selected_language == 'German':
    language = 'de'
elif selected_language == 'Dutch':
    language = 'nl'
elif selected_language == 'Spanish':
    language = 'es'