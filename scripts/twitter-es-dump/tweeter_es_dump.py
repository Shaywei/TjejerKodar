import time

import tweepy
import elasticsearch

# Twitter API credentials
consumer_key = "" # NOQA
consumer_secret = "" # NOQA

access_token = "" # NOQA
access_token_secret = "" # NOQA

# ES URL and credential
es_url = ""  # NOQA Must start with http[s]
es_user = ""
es_pass = ""


'''
Make sure you PUT the following to init the index 'tweeter_dump'
with mapping for the 'tweet' doc type to your cluster first.

Otherwise the @timestamp will be a float and not an epoch_millis.

PUT /tweeter_dump/
{
  "mappings": {
    "tweet": {
      "properties": {
        "@timestamp" : {
            "format" : "epoch_millis",
            "type" : "date"
        },
        "user" : { "type": "string" },
        "text" : { "type": "string" },
        "word_count": { "type": "integer" }
      }
    }
  }
}
'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


es = elasticsearch.Elasticsearch([
    "{}//{}:{}@{}".format(
        es_url.split('//', 1)[0],
        es_user,
        es_pass,
        es_url.split('//', 1)[1])])


class StreamListener(tweepy.StreamListener):
    # override tweepy.StreamListener to add logic to on_status

    def on_status(self, status):
        status = status._json

        doc = {
            'text': status['text'],
            'user': status['user']['screen_name'],
            '@timestamp': int(time.mktime(time.strptime(
                status['created_at'], "%a %b %d %H:%M:%S +0000 %Y"))) * 1000,
            'word_count': len(status['text'].split())
        }
        print doc
        es.create(
            index='tweeter_dump',
            doc_type='tweet',
            body=doc)

        print "successfully put to ES!"

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

streamer = tweepy.Stream(
    auth=auth, listener=StreamListener())

# Fill with your own Keywords bellow
track_terms = ['sweden', 'feminism']

streamer.filter(track=track_terms)
# streamer.userstream(None)
