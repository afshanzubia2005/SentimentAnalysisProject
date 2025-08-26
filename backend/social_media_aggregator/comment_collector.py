'''first step: import all threads and reddit comments'''

import praw
import pync
import logging
import sys
import os
import threading
#file_handler = logging.FileHandler(filename='tmp.log')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
#handlers = [file_handler, stdout_handler]


handlers = [stdout_handler]
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)
logger = logging.getLogger('LOGGER_NAME')


reddit = praw.Reddit(
    client_id = "GigJG-CSCi1v_g9z5Mdndg",
    client_secret = os.getenv("REDDIT_API_KEY"),
    password = os.getenv("PASSWORD"),
    user_agent = "script:CommentIdentifier:v1.0 (by u/Little_Ad791)",
    username = "Little_Ad791"

)


reddit.read_only = False

all_subreddits = reddit.subreddit("all")
trolley_subreddit = reddit.subreddit("funny")
keyword = 'trolley problem'


list_of_reddit_comments_and_posts = []


def monitor_trolley_comments():
    try: 
        logger.info("Collecting relevant comments and appending to list")
        for comment in all_subreddits.stream.comments(skip_existing=True):
            '''By putting skip_existing as false, I am collecting 
            information on people's attitudes to the topic that are most recent
            (ignoring past comments)'''
            logger.debug(f"Reddit comment: {comment.body.lower()}")
            if keyword.lower() in comment.body.lower():
                list_of_reddit_comments_and_posts.append(comment.body)
                logger.info("Successfully added a relevant comment to list ")
    except KeyboardInterrupt:
        print("Script interrupted by me. Exiting...")

def monitor_trolley_posts():
    try:
        logger.info("Collecting relevant posts and appending to list ")
        for submission in all_subreddits.stream.submissions(skip_existing=True):
            if keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower():
                list_of_reddit_comments_and_posts.append(submission.title)
                list_of_reddit_comments_and_posts.append(submission.selftext)
                logger.info("Successfully added a relevant post to list ")
    except KeyboardInterrupt:
        print("Script interrupted by me. Exiting...")

try:
    threads = []

    t1 = threading.Thread(target=monitor_trolley_comments)
    t2 = threading.Thread(target=monitor_trolley_posts)
    t3 = threading.Thread(target=monitor_trolley_subreddit)

    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for t in threads:
        t.join()

except Keyboardinterrupt:
    print("Script interrupted by me. Exiting...")