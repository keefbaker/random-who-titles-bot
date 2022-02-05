"""
handles all twitter functions
"""

import tweepy


def tweet_it(text, config):
    """ """
    client = create_client(config, "w")
    response = client.create_tweet(text=text)
    print(response)


def create_client(config, request_type="r"):
    """
    creates a twitter client, by default it will create a
    read only client using a bearer_token, but if fed a
    request_type of 'w', it will create a client capable
    of making tweets
    """
    if request_type == "w":
        client = tweepy.Client(
            consumer_key=config["consumer_key"],
            consumer_secret=config["consumer_secret"],
            access_token=config["access_token"],
            access_token_secret=config["access_token_secret"],
        )
    else:
        client = tweepy.Client(
            bearer_token=config["bearer_token"], wait_on_rate_limit=True
        )
    return client
