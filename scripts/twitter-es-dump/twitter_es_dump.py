import time
import argparse


import tweepy
import elasticsearch

# NOQA Load the secrets from file so some scrublord like me doesn't accidentally commit them to git.

SEND_TO_ES = False

secrets = argparse.Namespace()
with open("SECRETS.txt") as f:
    for line in f:
        vals = line.strip().split('=', 1)
        setattr(secrets, vals[0].lower(), vals[1])

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

auth = tweepy.OAuthHandler(
    secrets.twitter_consumer_key, secrets.twitter_consumer_secret)
auth.set_access_token(
    secrets.twitter_access_token, secrets.twitter_access_token_secret)


if SEND_TO_ES:
    es = elasticsearch.Elasticsearch([
        "{}//{}:{}@{}".format(
            secrets.es_url.split('//', 1)[0],
            secrets.es_user,
            secrets.es_pass,
            secrets.es_url.split('//', 1)[1])])
    print 'sending tweets to ', secrets.es_url


class StreamListener(tweepy.StreamListener):
    # override tweepy.StreamListener to add logic to on_status

    def on_status(self, status):
        print "new status!"
        status = status._json

        doc = {
            'text': status['text'],
            'user': status['user']['screen_name'],
            '@timestamp': int(time.mktime(time.strptime(
                status['created_at'], "%a %b %d %H:%M:%S +0000 %Y"))) * 1000,
            'word_count': len(status['text'].split())
        }
        print doc

        if SEND_TO_ES:
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
track_terms = ['sex', 'sweden', 'Israel', 'feminism', 'cthulhu']

print "Tracking tweets with terms {}".format(track_terms)

streamer.filter(track=track_terms)
# streamer.userstream(None)
