from flask import Flask
import tweepy
#import streamlit as st
import sqlite3
import os
import random # for generating IDs

app = Flask(__name__)
app.secret_key = os.urandom(24)

'''Gather relevant tweets and store in SQL Database'''

'''The route will be for the direct home page --> can later change to /tweets when testing finishes'''

@app.route("/")
def main():

    '''Connect to SQLite database'''
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    '''Create table (if its not already there)'''
    cursor.execute("""CREATE TABLE IF NOT EXISTS tweets_database (
        tweetid INT PRIMARY KEY,
        Date TEXT,      
        tweetContent TEXT,
        tweetSentiment INT
        );""")

    '''Establish a connection with Twitter API'''
    bearer_token=os.getenv("TWITTER_KEY")
    client = tweepy.Client(bearer_token)
    #st.title("Social media aggregator and sentiment analysis project ")
    #st.write("Twitter tweets about topic")

    #hardcoded values for testing
    query = "Eminem" #hardcoded for testing needs
    tweets = ["Her new single is out!", "ughhhhh hate her", 
          "her hair looks so cute tho.. love that color on her lolz"]

def get_tweets(query):
    ''''Get all relevant tweets about a query from Twitter (using API call)'''
    '''Then add to the database'''
    '''write unit test for this'''
    
    #st.write(result.text)
    results = client.search_recent_tweets(query)
    result_list = []
    for result in results:
        result_list.append(result)
    
    add_tweets(result_list)



def add_tweets(tweets_list):
    '''add the tweets about a specific query to database'''
    '''write unit test for this'''
    for tweet in tweets_list:
        #fix the random id generation + sentiment
        cursor.execute(""" 
        INSERT INTO tweets_database VALUES (
            {random.random(0.00, 1.00)},
            {CURRENT_DATE()},
            {str({tweet})},
            {getSentiment(str({tweet}))} 
        ); """)

''' Function to get sentiment (as an int range) for a tweet'''

def getSentiment(tweet):
    #st.write(tweet)
    pass

if __name__ == "__main__":
    main()

'''There's errors with the structure --> Need to fix. And where is app.py?'''