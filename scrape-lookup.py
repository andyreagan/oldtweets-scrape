#!/usr/bin/python
#
# scrape.py
#
# hammer the twitter API!

from twython import Twython, TwythonError
import json
import codecs
import time

if __name__ == '__main__':
    # the full rate limit is 180
    # with either app or user auth
    # numToGrab = 180
    # now with the loopup it is 60 for app auth
    numToGrab = 30
    
    # read current number
    f = open('completed-2.txt','r')
    numCompleted = int(f.readline().rstrip())
    f.close()
    
    print('getting tweets ' + str(numCompleted) + ' to ' + str(numCompleted+100*numToGrab-1))
    
    f = open('keys','r')
    APP_KEY = f.readline().rstrip()
    f.close()
    f = open('oauth2-key','r')
    ACCESS_TOKEN = f.readline().rstrip()
    f.close()
    
    twitter = Twython(APP_KEY,access_token=ACCESS_TOKEN)
    
    tweetIDs = [[",".join(["{0:.0f}".format(numCompleted+x*100+i) for i in range(100)])] for x in range(numToGrab)]
    
    outfile = '/users/a/r/areagan/fun/twitter/scraping/data-2/{0:019d}-{1:019d}.json'.format(numCompleted,numCompleted+numToGrab*100-1)
    outlog = '/users/a/r/areagan/fun/twitter/scraping/log-2/{0:019d}-{1:019d}.log'.format(numCompleted,numCompleted+numToGrab*100-1)
  
    f = codecs.open(outfile,'w','utf8')
    # f = codecs.open("test-output.json",'a','utf8')
    g = open(outlog,'w')
    
    # f.write('test\n')
    # f.close()
    # print(tweetIDs)
    for i,tweetIDlist in enumerate(tweetIDs):
        # time.sleep(1)
        g.write('getting tweet ID ' + str(tweetIDlist[0]) + ' to ' + str(tweetIDlist[-1]) + '\n')
        try:
            tweets = twitter.lookup_status(id=tweetIDlist,map="false",trim_user="false",entities="true")
            for tweet in tweets:
                # print(tweet["id"])
                json.dump(tweet,f,ensure_ascii=False)
                f.write('\n')
            # ujson.dump(tweet,f,ensure_ascii=False)
            # print(tweets)
            # print(len(tweets))
            # f.write('\n')
            g.write(",".join([tweet["id_str"] for tweet in tweets]))
            g.write('\n')
        except TwythonError as e:
            g.write(str(e))
            g.write('\n')
            # raise(e)
            # print(e)
            i = i-1
            break
            
    f.close()
    g.close()

    print(numCompleted+100*(i+1))
    # write new number
    f = open('completed-2.txt','w')
    f.write(str(numCompleted+100*(i+1))+'\n')
    f.close()









