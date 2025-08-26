
import praw
import pync
import logging
import sys
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
    password = "AkmZubi18018*",
    user_agent = "script:CommentIdentifier:v1.0 (by u/Little_Ad791)",
    username = "Little_Ad791"

)

reddit.read_only = False

all_subreddits = reddit.subreddit("all")
trolley_subreddit = reddit.subreddit("funny")
keyword = 'trolley problem'

def monitor_trolley_comments():
    try: 

        logger.info("Adding a notifier for trolley comments.")
        for comment in all_subreddits.stream.comments(skip_existing=False):
            logger.debug(f"Reddit comment: {comment.body.lower()}")
            if keyword.lower() in comment.body.lower():
                pync.Notifier.notify(
                    f"New comment about {keyword}: {comment.body}",
                    title="Reddit Alert",
                    open=f"https://www.reddit.com{comment.permalink}"
                )
                logger.info("Successfully added the notifier for the trolley comment.")
    except KeyboardInterrupt:
        print("Script interrupted by me. Exiting...")


def monitor_trolley_posts():
    try:
        logger.info("Adding a notifier for trolley posts.")
        for submission in all_subreddits.stream.submissions(skip_existing=True):
            if keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower():
                pync.Notifier.notify(
                    f"New submission about {keyword}: {submission.title}",
                    title="Reddit Alert",
                    open=submission.url
            )
    except KeyboardInterrupt:
        print("Script interrupted by me. Exiting...")

def monitor_trolley_subreddit():
    try: 
        logger.info("Adding a notifier for trolley subreddit posts.")
        for submission in trolley_subreddit.stream.submissions(skip_existing=True):
            pync.Notifier.notify(
                    f"New Trolley problem post: {submission.title}",
                    title="Reddit Alert",
                    open=submission.url
                )

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