import twitter,json,csv

CONSUMER_KEY = 'aibHxBEBQfJXhOwiG40jzvtxb'
CONSUMER_SECRET = '8G6407wF5hswYM9XhIYlkDIypTLxiMcZr6uYRvwnlo3im3jMZd'
OAUTH_TOKEN = '249321562-xAo2RLI2iSzcPMgw4QFmUy55AIQSqyEwI1q9SyQ3'
OAUTH_TOKEN_SECRET = 'vGBbeDtZQCJjUT11AwCGtS6xy4KYsMTl8w4oNScdNXmfj'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth, retry=True)

# setup a file to write to
csvfile = open('streamed_tweets_delimiter.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

#  heres a function that takes out characters that can break
#  our import into Excel and replaces them with spaces
#  it also does the unicode bit
def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val
    return clean


q = "#covid19, Boris" # Comma-separated list of terms can go here
print ('Filtering the public timeline for track="%s"' % (q,))

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:
    if tweet['truncated']:
        tweet_text = tweet['extended_tweet']['full_text']
    else:
        tweet_text = tweet['text']
    # write the values to file
    csvwriter.writerow([
        tweet['id_str'],
        tweet['created_at'],
        getVal(tweet['user']['screen_name']),
        getVal(tweet_text),
        getVal(tweet['user']['location']),
        tweet['user']['statuses_count'],
        tweet['user']['followers_count'],
        tweet['user']['friends_count'],
        tweet['user']['created_at']
        ])
    # print something to the screen, mostly so we can see what is going on...
    print (tweet['user']['screen_name'], tweet['text'])
