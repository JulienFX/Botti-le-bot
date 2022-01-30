# Import package
import tweepy 
import time
import datetime

#Store credentials 
apiKey = "PUT_YOUR_OWN_KEY"
apiKeySecret = "PUT_YOUR_OWN_KEY"
accessToken = "PUT_YOUR_OWN_KEY"
accessTokenSecret = "PUT_YOUR_OWN_KEY"
bearerToken = "PUT_YOUR_OWN_KEY"

# Create auth client and set authentication and create API object
auth = tweepy.OAuthHandler(apiKey,apiKeySecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

# Try to verify if the connexion is well done
try :
    api.verify_credentials()
    print("ok")
except:
    print("erreur de connexion")


# Searching tweets with specific word
# for tweets in api.search_tweets(q="neymar", lang="fr"):
#     print(tweets.user.screen_name+" a tweeté "+tweets.text)

# information on user twitter
# user = api.get_user(screen_name = 'jokerGDL')
# print("@"+user.screen_name+" possede "+str(user.followers_count)+" followers")
# for friend in user.friends() :
#     print("il a récemment follow "+friend.screen_name)

# Tweet with my bot 

# Retweet a tweet by passing in argument the id of a tweet
# api.retweet(1487235515132825606)
# tweet = api.get_status(1487235515132825606)
# print(tweet.user.screen_name)

# Send a DM toward an account 
# user = api.get_user(screen_name = '')
# api.send_direct_message(user.id,"Salutatiton mon 2e compte")


# for tweet in api.search_tweets(q="quoi", lang="fr"):
#     if(tweet.text.endswith('quoi')) :
#         print(tweet.id)
#         print(tweet.text)
#         reponse = "chi"
#         id = tweet.id_str
#         api.update_status(reponse, id )


bot_id = api.get_user(screen_name="bot_ventePrive").id
mention_id = 1
message = "ratio"

dateLancement = datetime.date.today()
# now = datetime.date.fromtimestamp(time.time())
mentions = api.mentions_timeline(since_id = mention_id)

while True :
    for mention in mentions :
        print(mention.user.screen_name+" said "+mention.text)
        if mention.created_at.date() < dateLancement :
            print("pas de  réponse")
            print(dateLancement)
            # print(now)
        else :
            try :
                api.update_status(message.format(mention.user.screen_name),in_reply_to_status_id=mention.id_str)
            except Exception as exc :
                print(exc)
    time.sleep(15)
    

