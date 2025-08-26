import tweepy
import streamlit as st

bearer_token="AAAAAAAAAAAAAAAAAAAAAIWWvQEAAAAAkhvDTlw6l2JrxWl7s83Gk%2FzZN%2BA%3DQKVCjTubYgGYEnBQv8yQglFMa6JcMdStVFkmJZxiTOVaKwNIqa"
client = tweepy.Client(bearer_token)
st.title("Social media aggregator and sentiment analysis project ")
st.write("Twitter tweets about topic")
query = "Eminem"
results = client.search_recent_tweets(query)

for result in results.data:
    st.write(result.text)

