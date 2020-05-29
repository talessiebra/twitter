import tweepy
import json

# access_token = 
# access_token_secret =
# API_key = 
# API_secret_key = 

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        y = json.loads(data)
          
        try:
            print('------------------------')
            #RT           
            tweet = y['retweeted_status']['extended_tweet']['full_text']
            print( tweet)
        except KeyError:
            try:
                #tweets longos
                tweet = y['extended_tweet']['full_text']
                print(tweet)
            except KeyError:
                try:
                    #tweets curtos
                    tweet = y['text']
                    print(tweet)
                except BaseException as e:
                    print("Error on_data %s" % str(e))
                return True           

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

print('Iniciando')

myStream = tweepy.Stream(auth, MyStreamListener())
myStream.filter(track=['netflix'], languages=['pt'])